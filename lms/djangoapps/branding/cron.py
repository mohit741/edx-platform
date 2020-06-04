'''
    Cron Job to delete expired notifications so that they
    don't pile up.
    -mohit741
'''
import logging
from messages_extends.models import Message
from datetime import datetime

log = logging.getLogger('Cron Task')

def delete_task():
    now = datetime.now()
    to_delete = Message.objects.filter(expires__lte=now)
    log.info('+++++++++++++++++++++ Cron Job Started +++++++++++++++++++')
    for msg in to_delete:
        msg.delete()
    log.info('+++++++++++++++++++++ Cron Job Completed +++++++++++++++++')


