'''
Created on 17 Sep 2013

@author: ByteBoxx
'''
#builtins
import shutil, os
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
        #
        self.mSubjectName = ''
        self.mCharacterName = ''
        self.mDefinition = ''
        self.mPose = ''
        #
        self.mActivePath = ''
        self.mActiveTakePath = ''
        
    def newSession(self):
        self.newSubject()
        self.updateCharacter()
        self.updateDefinition()
        self.updatePose()
        self.updateActivePath()
    
    def newSubject(self, name='testSubject'):
        self.mSubjectName = name
    
    def updateCharacter(self, name='testCharacter'):
        self.mCharacterName = name
    
    def updateDefinition(self, name='default'):
        self.mDefinition = name
    
    def updatePose(self, name='pose01'):
        self.mPose = name
    
    def updateActivePath(self):
        self.mActivePath = os.path.join(self.mShootFolder,
                                        self.mSubjectName,
                                        self.mCharacterName,
                                        self.mDefinition,
                                        self.mPose)
        
    def moveImages(self):
        lFinished = 0
        count = 0
        while not lFinished:
            for newImage in os.listdir(self.mRootFolder):
                root, ext = os.path.splitext(newImage)
                if ext in ('.jpg', '.JPG', '.jpeg', '.JPEG', '.cr2', '.CR2'):
                    shutil.move(os.path.join(self.mRootFolder, newImage), self.mActiveTakePath)
                    count = count + 1
            lFinished = 1
        return count