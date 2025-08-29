from utils.data_ingestion import get_country_specific_info
from utils.nlp_processing import generate_guide

class RelocationGuideAgent:
    def __init__(self, user_data):
        self.user_data = user_data

    def generate_guide(self):
        country_info = get_country_specific_info(self.user_data['new_location'])
        guide = generate_guide(self.user_data, country_info)
        return guide