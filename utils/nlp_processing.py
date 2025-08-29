from utils.api_calls import call_openai_api
import json

def generate_guide(user_data, country_info):
    prompt = (
        f"Generate a detailed, step-by-step relocation guide for {user_data['name']} moving from {user_data['current_location']} to {user_data['new_location']}. "
        f"Include sections on Housing, Transportation, Employment, Culture, and Education. "
        f"Provide specific tasks and actions that {user_data['name']} needs to complete, including deadlines, descriptions, and relevant documents or links. "
        f"Ensure the guide is tailored to {user_data['name']}'s personal details and specific needs. "
        f"For example, if {user_data['name']} has children, include tasks related to enrolling them in school. "
        f"Additionally, include some local tips for settling into {user_data['new_location']}. "
        f"Finally, generate a checklist of tasks at the end. "
        f"**Important:** The checklist must always follow this exact structure for each item:\n\n"
        f"- Task: [task name]\n"
        f"  Deadline: [deadline]\n"
        f"  Description: [short description of the task]\n"
        f"  Links: [optional links, if applicable]\n\n"
        f"Ensure the checklist is clearly marked with 'Checklist of Tasks to Do' at the beginning and '---' at the end."
    )
    response = call_openai_api(prompt)

    # Check if the response contains the expected keys
    if 'choices' in response and len(response['choices']) > 0 and 'text' in response['choices'][0]:
        guide = response['choices'][0]['text']
    else:
        guide = "Failed to generate the guide. Please try again later."

    # Parse the checklist from the response
    checklist = parse_checklist(guide)

    print("Checklist of Tasks to Do:")
    for item in checklist:
        print(f"- {item['task']} (Deadline: {item['deadline']})")

    return guide, checklist

def parse_checklist(guide):
    checklist_start = "Checklist of Tasks to Do"
    checklist_end = "---"
    try:
        checklist_text = guide.split(checklist_start)[1].split(checklist_end)[0].strip()
        lines = checklist_text.split("\n")
        checklist = []
        current_item = {}
        for line in lines:
            line = line.strip()
            if line.startswith("- Task:"):
                if current_item:
                    checklist.append(current_item)
                current_item = {"task": line.replace("- Task:", "").strip()}
            elif line.startswith("Deadline:"):
                current_item["deadline"] = line.replace("Deadline:", "").strip()
            elif line.startswith("Description:"):
                current_item["description"] = line.replace("Description:", "").strip()
            elif line.startswith("Links:"):
                current_item["links"] = line.replace("Links:", "").strip()
        if current_item:
            checklist.append(current_item)
        return checklist
    except IndexError:
        return "Failed to parse the checklist."