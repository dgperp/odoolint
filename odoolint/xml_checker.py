import xml.etree.ElementTree as ET
from collections import defaultdict
from .module_finder import find_files_in_module

def check_xml_id_duplication(modules, config):
    duplicates = []
    target_tags = {'record', 'template', 'menuitem'}

    for module_name, module_path in modules.items():
        xml_files = find_files_in_module(module_path, ['.xml'], config)
        xml_ids = defaultdict(list)

        for xml_file in xml_files:
            try:
                tree = ET.parse(xml_file)
                root = tree.getroot()

                for elem in root.iter():
                    if elem.tag in target_tags and 'id' in elem.attrib:
                        xml_id = elem.attrib['id']
                        xml_ids[xml_id].append((xml_file, elem.tag))

            except ET.ParseError as e:
                print(f"Error parsing {xml_file}: {e}")

        module_duplicates = [(xml_id, files) for xml_id, files in xml_ids.items() if len(files) > 1]
        if module_duplicates:
            duplicates.append((module_name, module_duplicates))

    if duplicates:
        print("\nFound duplicate XML IDs within modules:")
        for module, module_duplicates in duplicates:
            print(f"Module: {module}")
            for xml_id, files in module_duplicates:
                print(f"  XML ID: {xml_id}")
                for file, tag in files:
                    print(f"    - File: {file}, Tag: <{tag}>")
            print()
        return True
    return False
