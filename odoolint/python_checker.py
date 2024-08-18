from flake8.api import legacy as flake8

def check_python_code(file_path, config):
    style_guide = flake8.get_style_guide(
        select=config['flake8_select'].split(','),
        ignore=config['flake8_ignore'].split(',')
    )
    report = style_guide.check_files([file_path])

    if report.total_errors > 0:
        print(f"\nFound {report.total_errors} style errors in {file_path}:")
        for error in report.get_statistics(''):
            print(f"  {error}")
        return True
    return False