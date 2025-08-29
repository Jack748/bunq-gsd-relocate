from data.mock_data import mock_user_data
from models.ai_agent import RelocationGuideAgent
from utils.file_operations import write_to_markdown_file
from utils.data_ingestion import get_country_specific_info

def main():
    country_info = get_country_specific_info(mock_user_data['new_location'])
    agent = RelocationGuideAgent(mock_user_data)
    guide = agent.generate_guide(country_info)

    # Write the guide to a Markdown file
    filename = "relocation_guide.md"
    write_to_markdown_file(filename, guide)

    print(f"Relocation guide has been saved to {filename}")

if __name__ == "__main__":
    main()