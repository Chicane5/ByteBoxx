'''
Created on 11 Mar 2014

@author: ByteBoxx
'''

from __future__ import absolute_import

from celery import Celery

app = Celery('cascelery',
             broker='amqp://',
             backend='amqp://',
             include=['cascelery.tasks','app.pscan.psbatchjobs'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()
