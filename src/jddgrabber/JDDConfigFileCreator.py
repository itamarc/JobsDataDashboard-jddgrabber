import yaml
import os


def create_config_file(config_file, config=None):
    if config is None:
        config = get_default_config()

    config_dir = os.path.join(os.getcwd(), "conf")
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    with open(os.path.join(config_dir, config_file), 'w') as file:
        yaml.dump(config, file)


def remove_config_file(config_file):
    config_dir = os.path.join(os.getcwd(), "conf")
    if os.path.exists(os.path.join(config_dir, config_file)):
        os.remove(os.path.join(config_dir, config_file))


def get_default_config():
    return {'job_queries': [{'job_name': 'Software Engineer'},
                            {'job_name': 'Backend Developer'}],
            'job_services': [{'class_name': 'MuseDataGrabber',
                              'Authorization-Key': 'YourAPIKey',
                              'User-Agent': 'your@email.address',
                              'method': 'GET', 'name': 'The Muse',
                              'url': 'https://www.themuse.com/api/public/jobs',
                              'params': [{'category': ['Software Engineer', 'Data Science', 'IT'],
                                          'level': ['Senior Level', 'Mid Level'],
                                          'location': 'United States'}]}],
            'mongodb': [{'connection': 'mongodb+srv://<user>:<password>@cluster0.abcd.mongodb.net/<default_database>?retryWrites=true&w=majority'}]
            }


if __name__ == '__main__':
    config_file = r'config-sample.yaml'
    create_config_file(config_file)
    print("Config file created: ", os.path.join(os.getcwd(), "conf", config_file))
