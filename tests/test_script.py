import unittest
import requests



class TestAPi(unittest.TestCase):
    """
    @desc Test the status code after successfully json file cration with the help of API created
    """
    API_BASE_URL = 'http://127.0.0.1:8000/'
    ENDPOINT = 'candidate/candidate-details'

    def test_status(self):
        #--Test the api.
        responce = requests.get("{}".format(TestAPi.API_BASE_URL + TestAPi.ENDPOINT))
        self.assertEqual(responce.status_code, 200)


if __name__ == '__main__':
    unittest.main()
