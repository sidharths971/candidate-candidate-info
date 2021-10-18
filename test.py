try:
    from app import app
    import unittest

except Exception as e:
    print(f"module not found {e}")


class ApiTest(unittest.TestCase):
    
    def test_status(self):
        tester = app.test_client(self)
        responce = tester.get('/get/data/')
        self.assertEqual(responce.status_code, 200)
