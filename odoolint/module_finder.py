import os
import fnmatch
import subprocess


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

def find_modified_modules(directory, branch):
    # Get the list of modified files
    cmd = ['git', 'diff', '--name-only', f'origin/{branch}...HEAD']
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=directory)

    modified_files = result.stdout.splitlines()
    modules = {}
    for file_path in modified_files:

        parts = file_path.split(os.sep)
        if len(parts) > 1:
            module_name = f'{parts[0]}/{parts[1]}'
            if module_name not in modules:
                modules[module_name] = os.path.join(directory, module_name)
    return modules
