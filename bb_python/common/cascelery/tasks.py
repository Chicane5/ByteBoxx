'''
Created on 11 Mar 2014

@author: ByteBoxx
'''

from __future__ import absolute_import

import os

from cascelery.celery import app
from app.pscan import psbatchjobs
#from app.maya import mybatchjobs


@app.task
def align(label, photodir, accuracy):
    psb = psbatchjobs.PSBatchJobs()
    lfile = psb.align(label, photodir, accuracy)
    return lfile
    
    
@app.task
def runInPhotoScan(script):
    os.system("C:\\Users\\ByteBoxx\\Desktop\\cockit.bat " + script)
    
@app.task
def mayatest():
    os.system("mayapy E:\\codebase\\ByteBoxx\\bb_python\\common\\app\\maya\\mybatchjobs.py 'test'")