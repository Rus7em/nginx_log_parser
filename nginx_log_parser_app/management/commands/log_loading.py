import ijson
from django.core.management.base import BaseCommand
from nginx_log_parser_app.models import Nginx_log
from datetime import datetime
from django.db import transaction

BATCH_SIZE = 2000

class Command(BaseCommand):
    help = 'Loading a log file (nginx)'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help="Path to the log file (nginx)")

    def handle(self, *args, **kwargs):
        file_path = kwargs['path']

        with open(file_path, 'r') as file:
            logs = []

            for line in file:
                if line.strip():
                    parser = ijson.items(line, '')
                    log_data = next(parser)

                    log = Nginx_log(
                        ip_address = log_data['remote_ip'],
                        time = datetime.strptime(log_data['time'],
                                                 '%d/%b/%Y:%H:%M:%S %z'),
                        http_method = log_data['request'].split(' ')[0],
                        uri = log_data['request'].split(' ')[1],
                        response_code = int(log_data['response']),
                        response_size = int(log_data['bytes'])
                    )
                    logs.append(log)

                    if len(logs) >= BATCH_SIZE:
                        self.process_data(logs)
                        logs.clear()
        # save remaining data
        if logs: 
            self.process_data(logs)


        self.stdout.write(self.style.SUCCESS('Loading log file completed'))

    def process_data(self, logs):
        with transaction.atomic():
            Nginx_log.objects.bulk_create(logs, BATCH_SIZE)

