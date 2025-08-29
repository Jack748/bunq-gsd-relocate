from data.mock_data import mock_user_data
from models.ai_agent import RelocationGuideAgent
from utils.file_operations import write_to_markdown_file, write_to_json_file
from utils.data_ingestion import get_country_specific_info

def main():
    country_info = get_country_specific_info(mock_user_data['new_location'])
    agent = RelocationGuideAgent(mock_user_data)
    guide, checklist = agent.generate_guide(country_info)

    # Write the guide to a Markdown file
    guide_filename = "output/relocation_guide.md"
    write_to_markdown_file(guide_filename, guide)

    # Write the checklist to a Markdown file
    checklist_filename = "output/relocation_checklist.md"
    write_to_markdown_file(checklist_filename, checklist)

    # Write the checklist to a JSON file
    checklist_json_filename = "output/relocation_checklist.json"
    write_to_json_file(checklist_json_filename, checklist)

    print(f"Relocation guide has been saved to {guide_filename}")
    print(f"Relocation checklist has been saved to {checklist_filename}")
    print(f"Relocation checklist in JSON format has been saved to {checklist_json_filename}")

if __name__ == "__main__":
    main()