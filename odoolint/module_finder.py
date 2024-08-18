import os
import fnmatch


def should_exclude(path, exclude_patterns):
    for pattern in exclude_patterns:
        if fnmatch.fnmatch(path, pattern) or any(fnmatch.fnmatch(part, pattern) for part in path.split(os.sep)):
            return True
    return False


def find_odoo_modules(directory):
    modules = {}
    for root, dirs, files in os.walk(directory):
        if '__manifest__.py' in files:
            module_name = os.path.basename(root)
            modules[module_name] = root
    return modules


def find_files_in_module(module_path, extensions, config):
    files = []
    for root, dirs, filenames in os.walk(module_path):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, filename)
                if not should_exclude(file_path, config['flake8_exclude']):
                    files.append(file_path)
    return files
