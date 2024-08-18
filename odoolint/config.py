import os
import yaml

DEFAULT_CONFIG = {
    "flake8_select": "C,E,F,W,B,B9,N801,N803",
    "flake8_ignore": "E203,E501,W503,C901,W605,E722,E731",
    "flake8_exclude": ["**unported**", "**__init__.py", "tests"],
    "check_file_types": [".xml", ".js", ".css", ".scss", "csv"]
}


def load_config():
    config_file = '.odoolint'
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)
    return DEFAULT_CONFIG.copy()
