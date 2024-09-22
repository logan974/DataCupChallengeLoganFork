# test_api.py
import unittest

# Variables globales à tester
status_code = None
api_response = None

class TestApiResponse(unittest.TestCase):
    def test_status_code(self):
        self.assertEqual(status_code, 200, "Le code de statut doit être 200")

    def test_api_response(self):
        self.assertEqual(api_response, "Accés à l\'api ok ", "La réponse API n'est pas correcte")
