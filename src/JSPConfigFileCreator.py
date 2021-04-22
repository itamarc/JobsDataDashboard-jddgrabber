import yaml

config_file = r'config-sample.yaml'

config = {'job_sites': [{'name': 'USAJOBS',
			 'url': 'https://data.usajobs.gov/api/search',
			 'host': 'data.usajobs.gov',
			 'method': 'GET',
			 'User-Agent': 'your@email.address',
			 'Authorization-Key': 'YourAPIKey' }],
	  'job_queries' : [{'job_name': 'Software Engineer'},
			 {'job_name': 'Backend Developer'}]}

with open(config_file, 'w') as file:
    documents = yaml.dump(config, file)
