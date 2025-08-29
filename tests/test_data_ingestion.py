import unittest
from utils.data_ingestion import get_country_specific_info

class TestDataIngestion(unittest.TestCase):
    def test_get_country_specific_info(self):
        info = get_country_specific_info("Berlin")
        self.assertIn('health_insurance', info)
        self.assertIn('bank_account', info)

if __name__ == "__main__":
    unittest.main()