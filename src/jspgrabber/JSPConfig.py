import yaml


def load_config(config_file):
    with open(config_file) as file:
        config = yaml.safe_load(file)
    return config


if __name__ == '__main__':
    config_file = r'config-sample.yaml'
    print(yaml.dump(load_config(config_file)))
