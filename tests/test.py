try:

    import unittest
    import requests

except Exception as e:
    print(f"module not found {e}")


class TestAPi(unittest.TestCase):
    API_BASE_URL = 'http://127.0.0.1:8000/'
    ENDPOINT = 'candidate/candidate-details'

    def test_status(self):
        responce = requests.get("{}".format(TestAPi.API_BASE_URL + TestAPi.ENDPOINT))
        self.assertEqual(responce.status_code, 200)


if __name__ == '__main__':
    unittest.main()
