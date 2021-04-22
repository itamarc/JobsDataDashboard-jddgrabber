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
import JSPConfig as cnf

# Load configuration
config = cnf.load_config(r'config-sample.yaml')
    # Load job listings APIs
# For each API
    # Grab data
    # Save data

