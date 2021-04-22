import yaml

def create_config_file(config_file, config=None):
    if config == None:
        config = get_default_config()

    with open(config_file, 'w') as file:
        documents = yaml.dump(config, file)

def get_default_config():
    return {'job_sites': [{'name': 'USAJOBS',
                           'url': 'https://data.usajobs.gov/api/search',
                           'host': 'data.usajobs.gov',
                           'method': 'GET',
                           'User-Agent': 'your@email.address',
                           'Authorization-Key': 'YourAPIKey' }],
            'job_queries' : [{'job_name': 'Software Engineer'},
                             {'job_name': 'Backend Developer'}]}

if __name__ == '__main__':
    config_file = r'config-sample.yaml'
    create_config_file(config_file)
    print("Config file created: ", config_file)
