import yaml

config_file = r'config-sample.yaml'

with open(config_file) as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    config = yaml.safe_load(file)

print(yaml.dump(config))
