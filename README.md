# Odoolint

Odoolint is a comprehensive linting tool designed specifically for Odoo modules. It helps developers maintain code quality and consistency across their Odoo projects by performing various checks on Python files, XML files, and other web assets.

## Features

- Python code style checking using Flake8
- XML ID duplication detection within Odoo modules
- End-of-file newline validation for various file types

## Installation

You can install Odoolint using pip:

```
pip install odoolint
```

## Usage

Run Odoolint from the command line in your Odoo project directory:

```
odoolint
```

Odoolint will automatically look for a `.odoolint` configuration file in the current directory. If no configuration file is found, default settings will be used.

## Configuration

Create a `.odoolint` file in YAML format in your project's root directory to customize Odoolint's behavior. Here's an example configuration:

```yaml
flake8_select: "C,E,F,W,B,B9,N801,N803"
flake8_ignore: "E203,E501,W503,C901,W605,E722,E731"
flake8_exclude:
  - "**unported**"
  - "**__init__.py"
  - "tests"
check_file_types:
  - ".xml"
  - ".js"
  - ".css"
  - ".scss"
  - ".csv"
```

### Configuration Options

- `flake8_select`: Comma-separated list of error codes to check for in Python files.
- `flake8_ignore`: Comma-separated list of error codes to ignore in Python files.
- `flake8_exclude`: List of file or directory patterns to exclude from checks.
- `check_file_types`: List of file extensions to check for end-of-file newlines.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
