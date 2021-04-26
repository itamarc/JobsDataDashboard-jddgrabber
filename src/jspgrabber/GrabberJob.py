'''
GrabberJob.py
by Itamar Carvalho
This file is part of the Job Seeker Project stored in:
https://github.com/itamarc/JobSeekerProject/

- This job will run periodically (initially can be once a day).
- This job will connect to public job listings APIs (using REST or other method)
and save the data loaded in an "inbox" database for further processing.
- After saving the data, this job will trigger the JobsAnalyzer.
'''
import jspgrabber.JSPConfig as cnf
from jspgrabber.DataGrabber import DataGrabber


def runJob(config_file):
    # Load configuration and job listings APIs
    config = cnf.load_config(r'config.yaml')
    # For each API
    for service in config['job_services']:
        # Grab data
        grabber = DataGrabber.get_grabber(service["class_name"], service)
        grabber.fetch_data()
        # Save data


if __name__ == '__main__':
    runJob(r'config-sample.yaml')
