def write_to_markdown_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)