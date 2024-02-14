import http.client
import os
import unittest
from urllib.request import urlopen
import requests
import json

import pytest

BASE_URL = os.environ.get("BASE_URL")
#BASE_URL = "https://m0qwfec693.execute-api.us-east-1.amazonaws.com/Prod"
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_listtodos(self):
        print('---------------------------------------')
        print('Starting - integration test List TODO')
        #List
        url = BASE_URL+"/todos"
        response = requests.get(url)
        print('Response List Todo:' + str(response.json()))
        self.assertEqual(
            response.status_code, 200, "Error en la petición API a {url}"
        )
        self.assertTrue(response.json())
        
        print('End - integration test List TODO')
    def test_api_gettodo(self):
        print('---------------------------------------')
        print('Starting - integration test Get TODO')
        # Seria necesaroi un ID del entorno de produccion, para no escribir en la base de datos
        # Por ello se va a crear un registro a mano y usarlo para este Test o eso o un error al no tener el ID
        #Test GET TODO
        url = BASE_URL+"/todos/"+'ID_FALSO'
        response = requests.get(url)
        self.assertEqual(
            response.status_code, 404, "Error en la petición API a {url}"
        )
        print('End - integration test Get TODO')
    