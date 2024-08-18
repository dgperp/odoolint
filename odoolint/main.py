import os
import argparse
from .python_checker import check_python_code
from .xml_checker import check_xml_id_duplication
from .file_checker import check_files_end_of_file_newline
from .module_finder import find_odoo_modules, find_files_in_module
from .config import load_config


def main():
    parser = argparse.ArgumentParser(description="Odoolint: Odoo Code Checker")
    parser.add_argument("--config", help="Path to configuration file")
    args = parser.parse_args()

    config = load_config(args.config)

    current_directory = os.getcwd()
    modules = find_odoo_modules(current_directory)

    if not modules:
        print(f"No Odoo modules found in {current_directory} and its subdirectories.")
        return

    files_with_errors = 0
    for module_name, module_path in modules.items():
        python_files = find_files_in_module(module_path, ['.py'], config)
        for file_path in python_files:
            if check_python_code(file_path, config):
                files_with_errors += 1

    if check_xml_id_duplication(modules, config):
        files_with_errors += 1

    if check_files_end_of_file_newline(modules, config):
        files_with_errors += 1

    if files_with_errors:
        print(f"\nFound issues in {files_with_errors} file(s) or modules.")


if __name__ == "__main__":
    main()
