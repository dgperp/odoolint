import xml.etree.ElementTree as ET
from collections import defaultdict
from .module_finder import find_files_in_module


def check_xml_id_duplication(modules, config):
    errors = []
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
                errors.append(f"Error parsing {xml_file}: {e}")

        for xml_id, occurrences in xml_ids.items():
            if len(occurrences) > 1:
                error_msg = f"Duplicate XML ID '{xml_id}' in module '{module_name}':"
                for file, tag in occurrences:
                    error_msg += f"\n  {file}: <{tag}>"
                errors.append(error_msg)

    return errors
