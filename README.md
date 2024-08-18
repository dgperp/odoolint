# Odoolint

Odoolint is a comprehensive linting tool designed specifically for Odoo modules. It helps developers maintain code quality and consistency across their Odoo projects by performing various checks on Python files, XML files, and other web assets.

## Features

- Python code style checking using Flake8
- XML ID duplication detection within Odoo modules
- End-of-file newline validation for various file types
- Configurable rules and file exclusions

## Installation

You can install Odoolint using pip:

```
pip install odoolint
```

## Usage

### Command Line

Run Odoolint from the command line:

```
odoolint --config path/to/config.yaml
```

If no config file is specified, default settings will be used.

### Python Script

Use Odoolint in your Python scripts:

```python
from odoolint import find_odoo_modules, check_python_code, check_xml_id_duplication, check_files_end_of_file_newline, load_config

config = load_config("path/to/config.yaml")
modules = find_odoo_modules("/path/to/odoo/addons")
check_python_code("/path/to/python/file.py", config)
check_xml_id_duplication(modules, config)
check_files_end_of_file_newline(modules, config)
```

## Configuration

Create a YAML configuration file to customize Odoolint's behavior:

```yaml
flake8_select: "C,E,F,W,B,B9,N801,N803"
flake8_ignore: "E203,E501,W503,C901,W605,E722,E731"
flake8_exclude:
  - "**unported**"
  - "**__init__.py"
  - "tests"
  - "toa_account_report"
  - "toa_server_wide_multi_addons_path"
check_file_types:
  - ".xml"
  - ".js"
  - ".css"
  - ".scss"
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
