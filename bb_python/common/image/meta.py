'''
Created on 4 Nov 2013

@author: ByteBoxx
'''

import pyexiv2


#===============================================================================
# 
#===============================================================================
class Meta(object):
    '''
    meta object gets exif data from an image file and stores.
    Pass in a list of tags we want to retrieve and their raw values are stored in
    a global dict
    '''
    def __init__(self, pFile, pMetaList):
        '''
        Constructor
        '''
        self.mFile = pFile
        self.mMetaList = pMetaList #a list of exif tags we want to return
        self.mValDict = {}
        
        #build the pyexiv meta obj
        self.mPyExMeta = pyexiv2.ImageMetadata(self.mFile)
        self.mPyExMeta.read()
        
    def GetAllMeta(self):
        for lTag in self.mMetaList:
            tag = self.mPyExMeta[lTag]
            self.mValDict[lTag] = tag.raw_value
            