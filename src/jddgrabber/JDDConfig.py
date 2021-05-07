import yaml
import os


def load_config(config_file):
    config_dir = os.path.join(os.getcwd(), "conf")
    with open(os.path.join(config_dir, config_file)) as file:
        config = yaml.safe_load(file)
    return config


if __name__ == '__main__':
    config_file = r'config-sample.yaml'
    config = load_config(config_file)
    print("YAML config:\n", yaml.dump(config))
    print("Loaded config:\n", config)
