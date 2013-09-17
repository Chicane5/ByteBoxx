'''
Created on 17 Sep 2013

@author: ByteBoxx
'''

#===============================================================================
# 
#===============================================================================
class Session(object):
    '''
    classdocs
    '''
    def __init__(self, pType, pRootFolder):
        self.mType = pType
        self.mRootFolder = pRootFolder
        self.mShootFolder = ''
        