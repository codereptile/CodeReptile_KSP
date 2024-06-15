import re


def read_file(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()


def write_file(filename: str, content: str) -> None:
    with open(filename, 'w') as file:
        file.write(content)


def add_and_sort_depends(content: str, new_mod: dict) -> str:
    # Regex to find the depends array
    depends_pattern = re.compile(r'("depends": \[\n(?:\s*{\s*"name": "[^"]*"\s*},?\n)+\s*\])')
    match = depends_pattern.search(content)

    if match:
        depends_content = match.group(1)
        # Find all mod names
        mods = re.findall(r'"name": "([^"]*)"', depends_content)
        # Add the new mod's name
        if new_mod['name'] != "":
            mods.append(new_mod['name'])
        # Sort alphabetically
        mods_sorted = sorted(mods)

        # Build the new depends string with adjusted formatting
        new_depends_content = ',\n'.join([f'        {{\n            "name": "{mod}"\n        }}' for mod in mods_sorted])
        new_depends_block = f'"depends": [\n{new_depends_content}\n    ]'

        # Replace the old depends block with the new one
        return depends_pattern.sub(new_depends_block, content)

    return content


if __name__ == '__main__':
    target_filename = input("Please enter the mod file (v/r/g): ")
    if target_filename == 'v':
        target_filename = 'codereptile-vanilla-plus-plus.ckan'
    elif target_filename == 'r':
        target_filename = 'codereptile-realism.ckan'
    elif target_filename == 'g':
        target_filename = 'codereptile-graphics-enhanced.ckan'
    new_mod_name = input("Please enter the name of the new mod (leave null to just sort): ").strip()
    new_content = add_and_sort_depends(read_file(target_filename), {"name": new_mod_name})
    write_file(target_filename, new_content)
