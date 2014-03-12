'''
Created on 11 Mar 2014

@author: ByteBoxx
'''

from __future__ import absolute_import

import os

from cascelery.celery import app
from app.pscan import psbatchjobs


@app.task
def align(label, photodir, accuracy):
    psb = psbatchjobs.PSBatchJobs()
    psb.align(label, photodir, accuracy)
    
    
@app.task
def runInPhotoScan(script):
    os.system("C:\\Users\\ByteBoxx\\Desktop\\cockit.bat " + script)
    
@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)