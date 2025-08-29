import unittest
from utils.api_calls import call_openai_api

class TestApiCalls(unittest.TestCase):
    def test_call_openai_api(self):
        response = call_openai_api("Hello, world!")
        self.assertIn('choices', response)

if __name__ == "__main__":
    unittest.main()