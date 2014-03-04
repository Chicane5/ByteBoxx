'''
Created on 17 Sep 2013

@author: ByteBoxx
'''
#builtins
import shutil, os
import xml.etree.ElementTree
import xml.etree.cElementTree as ET
#3rd
#user
from image.meta import Meta
from qt.popup import Popup
from batch import batchtypes
#globals


#===============================================================================
# 
#===============================================================================
class DataTake(object):
    '''
    describes a 'post' Session object to be passed into the render queue
    '''
    cMESH_DATA = 'meshdata'
    cTEX_DATA = 'texdata'
    
    def __init__(self, pPath):
        self.mPath = pPath
        self.mBatchJobs = []
        self.mBatchVersions = {}
        
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
        if not self.mXML:
            twat = Popup.question(None, "create XML?")
            print twat
            
    def popBatchJobs(self):
        '''
        populate default batch job to appear in queue window
        '''
        self.mBatchJobs.append('tk')
        
    def updateBatchVersions(self):
        '''
        update dict to dynamically keep latest batch versions and their file path up to date
        '''
        if not self.mXML:
            Popup.warning(self, "No bound XML! Cannot update batch versions for this take")
            return
        
        lTree = ET.parse(self.mXML)
        root = lTree.getroot()
        
        lBatchElem = None
        for child in root:
            if child.tag == 'batch':
                lBatchElem = child
                break
                          
        for lChildElem in lBatchElem:
            self.mBatchVersions[lChildElem.tag] = [lChildElem.text, lChildElem.attrib['file']] if 'file' in lChildElem.attrib.keys() else [lChildElem.text]  
            
            
            
#=======================================================================
# 
#=======================================================================
class MeshTake(DataTake):
    '''
    mesh take object, specific to data being passed into photoscan
    '''
    def __init__(self, pPath):
        super(MeshTake, self).__init__(pPath)
        self.mType = DataTake.cMESH_DATA
        
    def popBatchJobs(self):
        '''
        populate batch jobs specific to mesh processing
        '''
        super(MeshTake, self).popBatchJobs()
        self.mBatchJobs.extend(batchtypes.gMESH_TASKS)
             
        
#=======================================================================
# 
#=======================================================================
class TextureTake(DataTake):
    '''
    texture ref take object, specific to data intended for a post texture pipe
    '''
    def __init__(self, pPath):
        super(TextureTake, self).__init__(pPath)
        self.mType = DataTake.cTEX_DATA
        
    def popBatchJobs(self):
        '''
        populate batch jobs specific to texture processing
        '''
        super(TextureTake, self).popBatchJobs()
        self.mBatchJobs.extend(batchtypes.gTEX_TASKS)
        
        
#===============================================================================
# 
#===============================================================================
class Session(object):
    '''
    describes a session - a container of an entire shootday of data.
    Sessions are created under the root folder and have a discreet type.
    Only one session 'type' can be created for a shootday. Dynamic member attributes
    set current subject/character/definition/pose
    '''
    def __init__(self, pType, pRootFolder):
        self.mType = pType
        self.mRootFolder = pRootFolder #i.e Z:\\
        self.mShootFolder = '' #the user defined shoot directory "*_mesh", "*_texture"
        self.mActivePath = ''
        self.mActiveTakePath = ''
        
    def newSession(self):
        pass

    def updateActivePath(self, basePath):
        '''
        builds the whole path to the POSE
        '''
        self.mActivePath = os.path.join(self.mShootFolder, basePath)
        
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
                
        #assuming jpgs are alwasy shot after this point
        if not lJpgList:
            return False
        
        lJpgList.sort()
        lTakeRootEl = ET.Element("take")
        lImagesEl = ET.SubElement(lTakeRootEl, "images")
        lJpgEl = ET.SubElement(lImagesEl, "jpeg")
        lCr2El = ET.SubElement(lImagesEl, "cr2")
        lJpgEl.text = "1"
        
        #are there cr2s in addition to the jpegs
        if lCr2List:
            lCr2El.text = "1"
        else:
            lCr2El.text = "0"
            
        #exif stuff
        lMeta = Meta(os.path.join(self.mActiveTakePath,'jpg', lJpgList[0]), ['Exif.Photo.ExposureTime','Exif.Photo.FNumber','Exif.Photo.ColorSpace'])
        lMeta.GetAllMeta()
        lExifEl = ET.SubElement(lTakeRootEl, "exif")
        lColourSpaceEl = ET.SubElement(lExifEl, "colourspace")
        if lMeta.mValDict['Exif.Photo.ColorSpace'] == '1':
            lColourSpaceEl.text = 'sRGB'
        else:
            lColourSpaceEl.text = lMeta.mValDict['Exif.Photo.ColorSpace']
        
        lFNumberEl = ET.SubElement(lExifEl, "fnumber")
        lFNumberEl.text = lMeta.mValDict['Exif.Photo.FNumber']
        
        lShutterEl = ET.SubElement(lExifEl, "exposuretime")
        lShutterEl.text = lMeta.mValDict['Exif.Photo.ExposureTime']
        
        #extra
        lExtraEl = ET.SubElement(lTakeRootEl, "extra")
        lCommentEl = ET.SubElement(lExtraEl, "comment")
        if pCommentStr == "":
            lCommentEl.text = "empty"
        else:
            lCommentEl.text = pCommentStr
        
        #batch stuff - will differ for session types
        lBatchEl = ET.SubElement(lTakeRootEl, "batch")
        
        if self.mType == 'Mesh':
            for task in batchtypes.gMESH_TASKS:
                lTaskEl = ET.SubElement(lBatchEl, task)
                lTaskEl.text = "v0"
          
        elif self.mType == 'Texture':
            for task in batchtypes.gTEX_TASKS:
                lTaskEl = ET.SubElement(lBatchEl, task)
                lTaskEl.text = "v0"
        
        tree = ET.ElementTree(lTakeRootEl)
        tree.write(os.path.join(self.mActiveTakePath, 'bb_takeInfo.xml'))
        
        return True
    
#===============================================================================
# 
#===============================================================================
class SetSession(Session):
    
    def __init__(self, *args):
        super(SetSession, self).__init__(*args)
        self.mSubjectName = ''
        self.mCharacterName = ''
        self.mDefinition = ''
        self.mPose = ''
    
    def newSession(self):
        '''
        sets all the relevant parameters for a new session
        or when a pickled session is loaded from disk
        '''
        self.newSubject()
        self.updateCharacter()
        self.updateDefinition()
        self.updatePose()
        super(SetSession, self).updateActivePath(os.path.join(self.mSubjectName, self.mCharacterName, self.mDefinition, self.mPose))

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
        super(SetSession, self).updateActivePath(os.path.join(self.mSubjectName, self.mCharacterName, self.mDefinition, self.mPose))

#===============================================================================
# 
#===============================================================================
class FlexSession(Session):
    
    def __init__(self, *args):
        super(FlexSession, self).__init__(*args)
        self.mBucket = ''

    def newSession(self):
        self.updateBucket()
        super(FlexSession, self).updateActivePath(self.mBucket)
    
    def updateBucket(self, name='bucket01'):
        '''
        update the bucket
        '''
        self.mBucket = name
        
    def updateActivePath(self):
        super(FlexSession, self).updateActivePath(self.mBucket)
    