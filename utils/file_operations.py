import json

def write_to_markdown_file(filename, content):
    if isinstance(content, list):
        # Convert dicts to strings
        content = "\n".join(
            f"- {item['task']} (Deadline: {item['deadline']})"
            for item in content
        )
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def write_to_json_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(content, file, ensure_ascii=False, indent=4)