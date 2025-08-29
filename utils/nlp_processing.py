from utils.api_calls import call_openai_api

def generate_guide(user_data, country_info):
    prompt = (
        f"Generate a detailed, step-by-step relocation guide for {user_data['name']} moving from {user_data['current_location']} to {user_data['new_location']}. "
        f"Include sections on Housing, Transportation, Employment, Culture, and Education. "
        f"Provide specific tasks and actions that {user_data['name']} needs to complete, including deadlines and relevant documents. "
        f"Ensure the guide is tailored to {user_data['name']}'s personal details and specific needs. "
        f"For example, if {user_data['name']} has children, include tasks related to enrolling them in school. "
        f"For each task, provide a brief description, any relevant links or resources, and specific deadlines. "
        f"Additionally, include some local tips for settling into {user_data['new_location']}. "
        f"Ensure the guide is comprehensive and covers all essential aspects of the relocation process. "
        f"User Details: {user_data['name']} is a {user_data['personal_details']['age']}-year-old {user_data['personal_details']['occupation']} who is {user_data['personal_details']['marital_status']} and has {user_data['personal_details']['children']} children. "
        f"Additional Info: {user_data['personal_details']['additional_info']}. "
        f"Specific Needs: {', '.join(user_data['specific_needs'])}."
    )
    response = call_openai_api(prompt)

    # Check if the response contains the expected keys
    if 'choices' in response and len(response['choices']) > 0 and 'text' in response['choices'][0]:
        guide = response['choices'][0]['text']
    else:
        guide = "Failed to generate the guide. Please try again later."

    return guide