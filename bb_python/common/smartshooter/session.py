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
from app.maya import mybatchjobs
from app.pscan import psbatchjobs
from util import utilbatchjobs
#globals


#===============================================================================
# 
#===============================================================================
class DataTake(object):
    '''
    describes a 'post' Project object to be passed into the render queue
    '''
    cMESH_DATA = 'meshdata'
    cTEX_DATA = 'texdata'
    
    def __init__(self, pPath):
        self.mPath = pPath
        self.mBatchJobs = []
        #self.mBatchJobsParams = {}
        self.mBatchVersions = {}
        self.mPriority = 1
        
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
            return False
            
        return True
    
    def popBatchJobs(self):
        '''
        populate default batch job to appear in queue window
        '''
        #self.mBatchJobs.append('tk')
        
    def updateBatchVersions(self):
        '''
        update dict to dynamically keep latest batch versions and their file path up to date
        '''
        if not self.mXML:
            return False
        
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
    mesh take object, specific to data being passed into photoscan post pipe
    '''
    def __init__(self, pPath):
        super(MeshTake, self).__init__(pPath)
        self.mType = DataTake.cMESH_DATA
        
    def popBatchJobs(self):
        '''
        populate batch jobs specific to mesh processing
        '''
        #super(MeshTake, self).popBatchJobs()
        #self.mBatchJobs.extend(psbatchjobs.PSBatchJobs.cBATCH_TASKS) 
        #self.mBatchJobs.extend(mybatchjobs.MYBatchJobs.cBATCH_TASKS)
        #paramters
        
        #add an instance of each task to the list of tasks for this take
        self.mBatchJobs.append(psbatchjobs.JobMask())
        self.mBatchJobs.append(psbatchjobs.JobAlign())
        
        
        #for d in (psbatchjobs.PSBatchJobs.cBATCH_PARAMS, mybatchjobs.MYBatchJobs.cBATCH_PARAMS):
            #self.mBatchJobsParams.update(d)
        
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
        #super(TextureTake, self).popBatchJobs()
        #self.mBatchJobs.extend(batchtypes.gTEX_TASKS)
        
        
#===============================================================================
# 
#===============================================================================
class Project(object):
    '''
    describes a project - a container of multiple shootdays of data.
    Sessions are created under the root folder and have a discreet type.
    '''
    def __init__(self, pType, pRootFolder):
        self.mType = pType
        self.mRootFolder = pRootFolder #i.e Z:\\DUMPSTER
        self.mShootFolder = '' #the top level project directory
        self.mActivePath = ''
        self.mActiveTakePath = ''
        

    def updateActivePath(self, basePath):
        '''
        builds the whole path to the POSE
        '''
        self.mActivePath = os.path.join(self.mShootFolder, basePath)
        
    def setActiveTakePath(self, pPath):
        self.mActiveTakePath = pPath
        

    def GenerateXML(self, pTakePath_and_Comment):
        '''
        creates post session XML files when flushing to dumpster - batch steps, comments and META info
        '''
        #check for jpg and cr2
        lJpgs, lCr2s = False, False
        if os.path.exists(os.path.abspath(os.path.join(pTakePath_and_Comment[0], 'jpg'))):
            lJpgs = True
        if os.path.exists(os.path.abspath(os.path.join(pTakePath_and_Comment[0], 'cr2'))):
            lCr2s = True
                
        jpglist = []
        while jpglist == []:
            jpglist = [x for x in os.listdir(os.path.abspath(os.path.join(pTakePath_and_Comment[0], 'jpg')))]
        
        lTakeRootEl = ET.Element("take")
        lImagesEl = ET.SubElement(lTakeRootEl, "images")
        lJpgEl = ET.SubElement(lImagesEl, "jpeg")
        lCr2El = ET.SubElement(lImagesEl, "cr2")
        
        lJpgEl.text = "1" #assuming there are jpegs
        
        #are there cr2s in addition to the jpegs
        if lCr2s:
            lCr2El.text = "1"
        else:
            lCr2El.text = "0"
            
        #exif stuff
        lMeta = Meta(os.path.join(pTakePath_and_Comment[0], 'jpg', jpglist[0]), ['Exif.Photo.ExposureTime','Exif.Photo.FNumber','Exif.Photo.ColorSpace'])
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
        if str(pTakePath_and_Comment[1]) == "":
            lCommentEl.text = "empty"
        else:
            lCommentEl.text = str(pTakePath_and_Comment[1])
        
        #batch stuff - will differ for session types
        lBatchEl = ET.SubElement(lTakeRootEl, "batch")
        
        lTasks = []
        if self.mType == 'Mesh':
            lTasks.extend(psbatchjobs.PSBatchJobs.cBATCH_TASKS)
            lTasks.extend(mybatchjobs.MYBatchJobs.cBATCH_TASKS)
            lTasks.extend(utilbatchjobs.UTILBatchJobs.cBATCH_TASKS)
            for task in lTasks:
                lTaskEl = ET.SubElement(lBatchEl, task)
                lTaskEl.text = "v0"
          
        '''
        elif self.mType == 'Texture':
            for task in batchtypes.gTEX_TASKS:
                lTaskEl = ET.SubElement(lBatchEl, task)
                lTaskEl.text = "v0"
        '''
                
        tree = ET.ElementTree(lTakeRootEl)
        lfiletoXML = os.path.join(pTakePath_and_Comment[0], 'bb_takeInfo.xml') 
        tree.write(lfiletoXML)
        
        return True
    
""" > DEPR
#===============================================================================
# 
#===============================================================================
class SetSession(Project):
    
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

"""
#===============================================================================
# 
#===============================================================================
class FlexSession(Project):
    '''
    flexible data container, for testing or fast iteration shoots
    structure = PROJECT > shootday > bucket > take
    '''
    def __init__(self, *args):
        super(FlexSession, self).__init__(*args)
        self.mShootDay = ''
        self.mBucket = ''

    def newSession(self):
        self.newShootDay()
        self.updateBucket()
        self.updateActivePath()
    
    def newShootDay(self, name='shootDay01'):
        self.mShootDay = name
        
    def updateBucket(self, name='bucket01'):
        '''
        update the bucket
        '''
        self.mBucket = name
        
    def updateActivePath(self):
        super(FlexSession, self).updateActivePath(os.path.join(self.mShootDay, self.mBucket))
