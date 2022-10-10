#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, builtins

from kombu                 import Queue, Exchange
from celery.schedules      import crontab
from librerias.datos.base  import globales

from . import crea_celery_app

programadas_app = crea_celery_app.simple_celery('programadas_app')
programadas_app.conf.task_queues = (
   Queue('conversion_pdf',        exchange=Exchange('conversion_pdf'),        routing_key='conversion_pdf'),
)


programadas_app.conf.beat_schedule = {      
   "conversion_pdf": {
      "task"    : "conversion_pdf",
      "schedule": crontab(minute='*/5'),
      "options" : {'queue': 'conversion_pdf'}
   }
}