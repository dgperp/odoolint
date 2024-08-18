import subprocess
import sys


def check_python_code(file_path, config):
    select = config['flake8_select']
    ignore = config['flake8_ignore']

    cmd = [sys.executable, '-m', 'flake8', file_path, f'--select={select}', f'--ignore={ignore}',
           '--format=%(path)s:%(row)d:%(col)d: %(code)s %(text)s']

    result = subprocess.run(cmd, capture_output=True, text=True)

    errors = []
    for line in result.stdout.splitlines():
        if line.strip():
            errors.append(line)

    return errors
