'''
Created on 17 Sep 2013

@author: ByteBoxx
'''
#builtins
import shutil, os
import xml.etree.cElementTree as cetree
#3rd
#user
from image.meta import Meta
from qt.popup import Popup


#===============================================================================
# 
#===============================================================================
class DataTake(object):
    '''
    describes a 'post' Session object to be passed into the render queue
    '''
    def __init__(self, pPath):
        self.mPath = pPath
        
    def BindXML(self):
        '''
        look for the existence of XML info
        '''
        self.mXML = None
        for lContent in os.listdir(self.mPath):
            root, ext = os.path.splitext(lContent)
            if ext == '.xml':
                self.mXML = os.path.join(str(self.mPath), lContent)
                break
            
              
#=======================================================================
# 
#=======================================================================
class MeshTake(DataTake):
    '''
    mesh take object
    '''
    def __init__(self, pPath):
        super(MeshTake, self).__init__(pPath)
        
        
#===============================================================================
# 
#===============================================================================
class Session(object):
    '''
    describes a session - a container of an entire shootday of data.
    Sessions are created under the root folder and have a discreet type.
    Only one session 'type' can be created for a shootday, with dynamic values
    for active definition/poses etc.
    '''
    def __init__(self, pType, pRootFolder):
        self.mType = pType
        self.mRootFolder = pRootFolder
        self.mShootFolder = ''
        self.mSubjectName = ''
        self.mCharacterName = ''
        self.mDefinition = ''
        self.mPose = ''
        self.mActivePath = ''
        self.mActiveTakePath = ''
        
    def newSession(self):
        '''
        sets all the relevant parameters for a new session
        or when a pickled session is loaded from disk
        '''
        self.newSubject()
        self.updateCharacter()
        self.updateDefinition()
        self.updatePose()
        self.updateActivePath()
    
    def newSubject(self, name='testSubject'):
        '''
        create a new subject under this session
        '''
        self.mSubjectName = name
    
    def updateCharacter(self, name='testCharacter'):
        '''
        update the 'character' this subject is performing
        '''
        self.mCharacterName = name
    
    def updateDefinition(self, name='default'):
        '''
        update the definition
        '''
        self.mDefinition = name
    
    def updatePose(self, name='pose01'):
        '''
        update the pose
        '''
        self.mPose = name
    
    def updateActivePath(self):
        '''
        builds the whole path to the POSE
        '''
        self.mActivePath = os.path.join(self.mShootFolder,
                                        self.mSubjectName,
                                        self.mCharacterName,
                                        self.mDefinition,
                                        self.mPose)
        
    def setActiveTakePath(self, pPath):
        self.mActiveTakePath = pPath
        
    def moveImages(self):
        '''
        after images land in the global shot directory bucket
        we move them into the active take path. Sanity checks how many images we expect to copy
        '''
        lFinished = 0
        count = 0
        while not lFinished:
            for newImage in os.listdir(self.mRootFolder):
                root, ext = os.path.splitext(newImage)
                if ext in ('.jpg', '.JPG', '.jpeg', '.JPEG', ):
                    shutil.move(os.path.join(self.mRootFolder, newImage), os.path.join(self.mActiveTakePath, 'jpg'))
                    count = count + 1
                elif ext in ('.cr2', '.CR2'):
                    shutil.move(os.path.join(self.mRootFolder, newImage), os.path.join(self.mActiveTakePath, 'cr2'))
                    count = count + 1
            lFinished = 1
        return count
    
    def GenerateXML(self, pCommentStr):
        '''
        once we have copied all the images over to the proper take directory, we need to generate some
        meta data about this trigger
        '''
        #check for jpg and cr2?
        lJpgList, lCr2List = [], []
        if os.path.exists(os.path.abspath(os.path.join(self.mActiveTakePath, 'jpg'))):
            lJpgList = [j for j in os.listdir(os.path.join(self.mActiveTakePath, 'jpg'))]
        if os.path.exists(os.path.abspath(os.path.join(self.mActiveTakePath, 'cr2'))):
            lCr2List = [c for c in os.listdir(os.path.join(self.mActiveTakePath, 'cr2'))]
                
        #assuming jpgs after this point
        if not lJpgList:
            return False
        
        lJpgList.sort()
        lTakeRootEl = cetree.Element("take")
        lImagesEl = cetree.SubElement(lTakeRootEl, "images")
        lJpgEl = cetree.SubElement(lImagesEl, "jpeg")
        lCr2El = cetree.SubElement(lImagesEl, "cr2")
        lJpgEl.text = "1"
        if lCr2List:
            lCr2El.text = "1"
        else:
            lCr2El.text = "0"
            
        #exif stuff
        lMeta = Meta(os.path.join(self.mActiveTakePath,'jpg', lJpgList[0]), ['Exif.Photo.ExposureTime','Exif.Photo.FNumber','Exif.Photo.ColorSpace'])
        lMeta.GetAllMeta()
        lExifEl = cetree.SubElement(lTakeRootEl, "exif")
        lColourSpaceEl = cetree.SubElement(lExifEl, "colourspace")
        lColourSpaceEl.text = lMeta.mValDict['Exif.Photo.ColorSpace']
        
        lFNumberEl = cetree.SubElement(lExifEl, "fnumber")
        lFNumberEl.text = lMeta.mValDict['Exif.Photo.FNumber']
        
        lShutterEl = cetree.SubElement(lExifEl, "exposuretime")
        lShutterEl.text = lMeta.mValDict['Exif.Photo.ExposureTime']
        
        lCommentEl = cetree.SubElement(lTakeRootEl, "comment")
        if pCommentStr == "":
            lCommentEl.text = "empty"
        else:
            lCommentEl.text = pCommentStr
        
        #batch stuff
        lBatchEl = cetree.SubElement(lTakeRootEl, "batch")
        lMaskEl = cetree.SubElement(lBatchEl, "automask")
        lAlignEl = cetree.SubElement(lBatchEl, "align")
        lGeoEl = cetree.SubElement(lBatchEl, "geobuild")
        lDecEl = cetree.SubElement(lBatchEl, "decimate")
        lTexEl = cetree.SubElement(lBatchEl, "texturebake")
        lMdlExpEl = cetree.SubElement(lBatchEl, "modelexport")
        lClientEl = cetree.SubElement(lBatchEl, "clientpackage")
        lRenderEl = cetree.SubElement(lBatchEl, "render")
        
        for element in [lMaskEl, lAlignEl, lGeoEl, lDecEl, lTexEl, lMdlExpEl, lClientEl, lRenderEl]:
            element.text = "0" 
        
        tree = cetree.ElementTree(lTakeRootEl)
        tree.write(os.path.join(self.mActiveTakePath, 'bb_takeInfo.xml'))
        
        return True
    