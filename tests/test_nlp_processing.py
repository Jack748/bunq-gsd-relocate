import unittest
from utils.nlp_processing import generate_guide
from data.mock_data import mock_user_data

class TestNlpProcessing(unittest.TestCase):
    def test_generate_guide(self):
        guide = generate_guide(mock_user_data, {"health_insurance": "https://example.com/health-insurance", "bank_account": "https://example.com/bank-account"})
        self.assertIsNotNone(guide)

if __name__ == "__main__":
    unittest.main()