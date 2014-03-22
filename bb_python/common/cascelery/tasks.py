'''
Created on 11 Mar 2014

@author: ByteBoxx
'''

from __future__ import absolute_import
from celery.contrib.methods import task_method

import os

from cascelery.celery import app
from app.pscan import psbatchjobs
#from app.maya import mybatchjobs


class Align(object):
    
    @app.task(filter=task_method)
    def align(self, label, photodir, accuracy):
        psb = psbatchjobs.PSBatchJobs()
        lfile = psb.align(label, photodir, accuracy)
        return lfile
    
    
@app.task
def runInPhotoScan(script):
    psb = psbatchjobs.PSBatchJobs()
    cmd = psb.runInPhotoScan(script)
    os.system(cmd)
    
@app.task
def mayatest():
    os.system("mayapy E:\\codebase\\ByteBoxx\\bb_python\\common\\app\\maya\\mybatchjobs.py 'test'")