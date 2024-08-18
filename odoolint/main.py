import sys
import os
from .python_checker import check_python_code
from .xml_checker import check_xml_id_duplication
from .file_checker import check_files_end_of_file_newline
from .module_finder import find_odoo_modules, find_files_in_module
from .config import load_config


def main():
    config = load_config()

    current_directory = os.getcwd()
    modules = find_odoo_modules(current_directory)

    if not modules:
        print(f"No Odoo modules found in {current_directory} and its subdirectories.")
        return 0

    print(f"Found {len(modules)} Odoo modules. Checking Python files, XML IDs, and end-of-file newlines...")

    total_errors = 0

    for module_name, module_path in modules.items():
        python_files = find_files_in_module(module_path, ['.py'], config)
        for file_path in python_files:
            errors = check_python_code(file_path, config)
            total_errors += len(errors)
            for error in errors:
                print(error)

    xml_errors = check_xml_id_duplication(modules, config)
    total_errors += len(xml_errors)
    for error in xml_errors:
        print(error)

    eol_errors = check_files_end_of_file_newline(modules, config)
    total_errors += len(eol_errors)
    for error in eol_errors:
        print(error)

    if total_errors == 0:
        print("All files passed the checks.")
        return 0
    else:
        print(f"\nFound {total_errors} issue(s).")
        return 1


if __name__ == "__main__":
    sys.exit(main())
