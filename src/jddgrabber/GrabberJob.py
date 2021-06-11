'''
GrabberJob.py
by Itamar Carvalho
This file is part of the Jobs Data Dashboard Project stored in:
https://github.com/users/itamarc/projects/1

- This job will run periodically (initially can be once a day).
- This job will connect to public job listings APIs
(using REST or other method) and save the data loaded in an "inbox" database
for further processing.
- After saving the data, this job will trigger the JobsAnalyzer.
'''
import logging
import logging.handlers
import jddgrabber.JDDConfig as cnf
from jddgrabber.DataGrabber import DataGrabber
from jddgrabber.JDDLoggerSQSHandler import JDDLoggerSQSHandler

def runJob(config_file=r'config.yaml'):
    """
    Run the job, loading the config file received as parameter
    (default: config.yaml).
    The config file must be in the "conf" directory under the working dir.

    This job will grab the data from the configured online job services, save
    it to the database and then run the JDDAnalyzer to consolidate the data.
    """
    # Load configuration and job listings APIs
    config = cnf.load_config(config_file)
    logger = initLogging(config)
    logger.debug("Logging started using config in file: " + config_file)
    logger.info("Starting GrabberJob.")
    # For each API
    for service in config['job_services']:
        # Grab data
        grabber = DataGrabber.get_grabber(service["class_name"], service)
        logger.info("Grabbing data with " + service["class_name"])
        grabber.fetch_data()


def initLogging(config):
    logger = logging.getLogger('jddgrabberlog')
    handler = None
    try:
        sqslogconf = config['sqslog']
        handler = JDDLoggerSQSHandler(
            sqslogconf['queue'],
            sqslogconf['aws_key_id'],
            sqslogconf['secret_key'],
            sqslogconf['aws_region'])
    except:
        handler = logging.FileHandler(config['logfile'])
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(config['loglevel'])
    return logger


if __name__ == '__main__':
    runJob(r'config-sample.yaml')
