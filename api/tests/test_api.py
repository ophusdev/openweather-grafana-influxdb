import unittest

from api import app


class BasicTestCase(unittest.TestCase):
    def setUp(self):

        self.app = app.app.test_client()

    # executed after each test
    def tearDown(self):
        pass

    def test_home(self):
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_current_weather(self):
        response = self.app.get("/current-weather", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_forecast_weather(self):
        response = self.app.get("/forecast-weather", follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
