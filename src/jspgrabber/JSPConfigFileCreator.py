import yaml


def create_config_file(config_file, config=None):
    if config is None:
        config = get_default_config()

    with open(config_file, 'w') as file:
        documents = yaml.dump(config, file)


def get_default_config():
    return {'job_queries': [{'job_name': 'Software Engineer'},
                            {'job_name': 'Backend Developer'}],
            'job_services': [{'class_name': 'jspgrabber.MuseDataGrabber',
                            'Authorization-Key': 'YourAPIKey', 
                            'User-Agent': 'your@email.address',
                            'method': 'GET', 'name': 'The Muse', 
                            'url': 'https://www.themuse.com/api/public/jobs',
                            'params': [{'category': 'Software Engineer',
                                        'level': 'Senior Level',
                                        'location': 'United States'}]}]}


if __name__ == '__main__':
    config_file = r'config-sample.yaml'
    create_config_file(config_file)
    print("Config file created: ", config_file)
