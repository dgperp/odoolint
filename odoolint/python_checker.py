from flake8.api import legacy as flake8


def check_python_code(file_path, config):
    style_guide = flake8.get_style_guide(
        select=config['flake8_select'].split(','),
        ignore=config['flake8_ignore'].split(',')
    )
    report = style_guide.check_files([file_path])

    errors = []
    for line_number, column, message, check in report._application.formatter.found_errors:
        errors.append(f"{file_path}:{line_number}:{column}: {message}")
    return errors
