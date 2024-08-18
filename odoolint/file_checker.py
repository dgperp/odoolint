import os
from .module_finder import find_files_in_module


def check_end_of_file_newline(file_path):
    with open(file_path, 'rb') as file:
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        if file_size == 0:
            return True  # Empty file, consider it as having a newline at the end

        file.seek(-1, os.SEEK_END)
        last_char = file.read(1)
        if last_char != b'\n':
            return False  # No newline at the end of the file

        if file_size >= 2:
            file.seek(-2, os.SEEK_END)
            second_last_char = file.read(1)
            if second_last_char == b'\n':
                return False  # More than one newline at the end of the file

        return True  # Exactly one newline at the end of the file


def check_files_end_of_file_newline(modules, config):
    errors = []

    for module_name, module_path in modules.items():
        files = find_files_in_module(module_path, config['check_file_types'], config)
        for file_path in files:
            if not check_end_of_file_newline(file_path):
                errors.append(f"{file_path}: Missing or extra newline at the end of the file")

    return errors
