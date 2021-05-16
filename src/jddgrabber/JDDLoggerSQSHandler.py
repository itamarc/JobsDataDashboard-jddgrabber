import logging
import logging.handlers
from datetime import datetime, timezone
import JDDConfig as cnf

import boto3
from retrying import retry


class JDDLoggerSQSHandler(logging.Handler):
    """
    A Python logging handler which sends messages to Amazon SQS.
    Code based on Zyllow's SQS-Logging-Handler https://github.com/zillow/python-sqs-logging-handler/
    """

    def __init__(self,
                 queue,
                 aws_key_id=None,
                 secret_key=None,
                 aws_region=None,
                 global_extra=None):
        """
        Sends log messages to SQS so downstream processors can consume
        (e.g. push the log messages to Splunk).
        :param queue: SQS queue name.
        :param aws_key_id: aws key id. Explicit credential parameters is
        not needed when running with EC2 role-based authentication.
        :param secret_key: secret key associated with the key id.
        """

        logging.Handler.__init__(self)
        client = boto3.resource('sqs',
                                aws_access_key_id=aws_key_id,
                                aws_secret_access_key=secret_key,
                                region_name=aws_region)
        self.queue = client.get_queue_by_name(QueueName=queue)
        self._global_extra = global_extra

        # When self.emit is called, the emit function will call boto3 code,
        # which in-turn will generate logs, leading to infinitely nested
        # call to the log handler (when the log handler is attached to the
        # root logger). We use this flag to guard against nested calling.
        self._entrance_flag = False


    @retry(stop_max_attempt_number=7)
    def logMessage(self, message, level="INFO", origin="jddgrabber"):
        # "body": 
        # "{ \"time\": {\"$date\": \"2021-05-14T11:11:33.289-03:00\"}, \"origin\": \"LambdaAWSControlPanelWeb\",
        #  \"message\": \"Testing the lambda function\", \"level\": \"INFO\" }"
        date = datetime.now(tz=timezone.utc).isoformat()
        body = '{ "time": {"$date": "%(date)s"}, "origin": "%(origin)s", "message": "%(message)s", "level": "%(level)s" }' % {"date": date, "origin": origin, "message": message, "level": level}
        if not self._entrance_flag:
            # When the handler is attached to root logger, the call on SQS
            # below could generate more logging, and trigger nested emit
            # calls. Use the flag to prevent stack overflow.
            self._entrance_flag = True
            try:
                msgdedid = str(round(datetime.now().replace(tzinfo=timezone.utc).timestamp()))
                self.queue.send_message(MessageBody=body, MessageGroupId="jddlog", MessageDeduplicationId=msgdedid)
            finally:
                self._entrance_flag = False


if __name__ == '__main__':
    config_file = r'config.yaml'
    # Load configuration and job listings APIs
    config = cnf.load_config(config_file)
    print(config)
    sqslogconf = config['sqslog']
    logh = JDDLoggerSQSHandler(sqslogconf['queue'], sqslogconf['aws_key_id'], sqslogconf['secret_key'], sqslogconf['aws_region'])
    logh.logMessage("Execution of JDDLoggerSQSHandler for testing purposes")
    print("Message sent.")
