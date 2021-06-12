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
    return {
            'sqslog': {'queue': 'JDDLogQueue.fifo',
                        'aws_key_id': '<your AWS SQS key id>',
                        'secret_key': '<your AWS SQS secret key>',
                        'aws_region': 'us-xxxx-N'},
            'loglevel': 'DEBUG',
            'logfile': 'jdd-log.txt', # file used only if SQS connection fails
            'job_services': [
                {
                'name': 'The Muse',
                'class_name': 'MuseDataGrabber',
                'User-Agent': 'your@email.address',
                'method': 'GET',
                'url': 'https://www.themuse.com/api/public/jobs',
                'api_key': '<get your key by registering your app in themuse.com>',
                'category': ['Data Science', 'IT', 'Software Engineer'],
                'level': ['Mid Level', 'Senior Level'],
                'location': [
                    'Amsterdam, Netherlands',
                    'Rotterdam, Netherlands',
                    'The Hague, Netherlands',
                    'Lisbon, Portugal',
                    'Porto, Portugal',
                    'Barcelona, Spain',
                    'Madrid, Spain',
                    'Murcia, Spain',
                    'Seville, Spain',
                    'Valencia, Spain',
                    'Paris, France',
                    'London, United Kingdom',
                    'Dublin, Ireland',
                    'Rome, Italy',
                    'Milan, Italy',
                    'Berkeley, CA',
                    'Mountain View, CA',
                    'San Francisco, CA',
                    'San Jose, CA',
                    'Raleigh, NC',
                    'Redmond, WA',
                    'Seattle, WA',
                    'New York, NY'
                    ]
                }
            ],
            'mongodb': {'connection': 'mongodb+srv://<user>:<password>@cluster0.abcd.mongodb.net/<default_database>?retryWrites=true&w=majority'}
        }

if __name__ == '__main__':
    config_file = r'config-sample.yaml'
    create_config_file(config_file)
    print("Config file created: ", os.path.join(os.getcwd(), "conf", config_file))
