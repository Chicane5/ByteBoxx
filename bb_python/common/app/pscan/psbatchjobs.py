'''
Created on 11 Mar 2014

@author: ByteBoxx
'''
#builtins
import getpass
import os
#3rd
#user
from PyQt4.QtCore import QObject, SIGNAL
from qt import rendertaskdlgs

gDEBUG = True

#===============================================================================
# 
#===============================================================================
class PSBatchJobs(object):
    '''
    cunting photoscan wont accept command line py scripts so we have to
    generate them dynamically at runtime you Russian bastards
    '''
    cSINGLE_SPACE = '    '
    cDOUBLE_SPACE = cSINGLE_SPACE+cSINGLE_SPACE
    cBAT_DIR = 'C:\\Program Files\\ByteBoxx\\RenderBoxx\\bin'
    #standard tasks for processing a photoscan mesh job
    cBATCH_TASKS = ['automask',
                    'align',
                    'builddensecloud',
                    'geotexbuild',
                    'modelexport']
    
    cBATCH_PARAMS = {'automask':[('mask directory:',''), ('blur:',10), ('threshold:',75), ('gapfill:',25)],
                    'align':[('accuracy:','low')],
                    'builddensecloud':[],
                    'geotexbuild':[],
                    'modelexport':[]}
    
    def __init__(self):
        self.mBatchParamsDlg = None
        self.mJobName = None

    def showParams(self):
        self.mBatchParamsDlg._main()
        
    #@app.task(filter=task_method)
    def align(self, label, photodir, accuracy):
        tempfile = os.path.abspath(os.path.join(os.path.dirname(photodir), "align.py"))
        with open(tempfile, 'w') as fh:
            fh.write("####AUTO GENERATED PHOTOSCAN SCRIPT...POWERED BY BYTEBOXX LTD###\n\n\n")
            fh.write("import PhotoScan\n")
            fh.write("import os\n\n")
            fh.write("def main():\n")
            fh.write(self.cSINGLE_SPACE+"app = PhotoScan.Application()\n")
            fh.write(self.cSINGLE_SPACE+"doc = app.document\n")
            
            fh.write(self.cSINGLE_SPACE+"chunk = PhotoScan.Chunk()\n")
            fh.write(self.cSINGLE_SPACE+"chunk.label = '"+label+"'\n")
            fh.write(self.cSINGLE_SPACE+"doc.chunks.add(chunk)\n")
            fh.write(self.cSINGLE_SPACE+"photos_list = os.listdir('"+photodir+"')\n")
            
            fh.write(self.cSINGLE_SPACE+"for photo_name in photos_list:\n")
            fh.write(self.cDOUBLE_SPACE+"chunk.photos.add(os.path.join('"+photodir+"', photo_name))\n")
            
            fh.write(self.cSINGLE_SPACE+"doc.activeChunk.matchPhotos(accuracy='"+accuracy+"', preselection='disabled', filter_mask=False)\n")
            fh.write(self.cSINGLE_SPACE+"doc.activeChunk.alignPhotos()\n")
            
            
            fh.write("PhotoScan.app.addMenuItem('ByteBoxx/Align_"+tempfile+"', main)\n")
            #fh.write("doc.save('C:\\Users\\ByteBoxx\\Desktop\\align_celery.psz')\n")
            #fh.write("app.quit()")
            
            
            fh.close()
        return tempfile
    
    def runInPhotoScan(self, script):
        return '"' + os.path.join(self.cBAT_DIR, 'copyToPSScripts.bat') +'" ' + script
    
    
#===============================================================================
# 
#===============================================================================
class JobMask(PSBatchJobs):
    def __init__(self):
        super(JobMask, self).__init__()
        self.mBatchParamsDlg  = rendertaskdlgs.DL_AutoMask_Params()
        self.mJobName = 'automask'
        #parameters
        self.maskDirectory = ''
        self.blur = 10
        self.threshold = 75
        self.gapfill = 25
        
        #parameter connections
        QObject.connect(self.mBatchParamsDlg.lineEdit_maskPath, SIGNAL("textEdited (QString)"), self.updatePath)
        QObject.connect(self.mBatchParamsDlg.spinBox_blur, SIGNAL("valueChanged (int)"), self.updateBlur)
        QObject.connect(self.mBatchParamsDlg.spinBox_threshold, SIGNAL("valueChanged (int)"), self.updateThreshold)
        QObject.connect(self.mBatchParamsDlg.spinBox_gapfill, SIGNAL("valueChanged (int)"), self.updateGapfill)
        

    def updatePath(self, pQString):
        self.maskDirectory = str(pQString)
        if gDEBUG:
            print self.maskDirectory
        
    
    def updateBlur(self, pValue):
        self.blur = pValue
        if gDEBUG:
            print self.blur
            
    def updateThreshold(self, pValue):
        self.threshold = pValue
        if gDEBUG:
            print self.threshold
            
    def updateGapfill(self, pValue):
        self.gapfill = pValue
        if gDEBUG:
            print self.gapfill
        
        
#==========================================================================
# 
#==========================================================================
class JobAlign(PSBatchJobs):
    def __init__(self):
        super(JobAlign, self).__init__()
        self.mBatchParamsDlg  = rendertaskdlgs.DL_Align_Params()
        self.mJobName = 'align'
        #parameters
        self.accuracy = 'low'
        self.pairPreselect = 'disabled'
        self.pointLimit = 40000
        self.constrainByMask = False
        
        #parameter connections
        QObject.connect(self.mBatchParamsDlg.comboBox_accuracy, SIGNAL("currentIndexChanged (QString)"), self.updateAccuracy)
        QObject.connect(self.mBatchParamsDlg.comboBox_consbymask, SIGNAL("currentIndexChanged (QString)"), self.updateConstrainMask)

    def updateAccuracy(self, pQString):
        self.accuracy = str(pQString)
        if gDEBUG:
            print self.accuracy
    
    def updateConstrainMask(self, pQString):
        if pQString == 'no':
            self.constrainByMask = False
        elif pQString == 'yes':
            self.constrainByMask = True
        if gDEBUG:
            print self.constrainByMask

        
if __name__ == "__main__":
    psb = PSBatchJobs()
    psb.align('twat', "C:\\sometwatdir\\init", "low")
