'''
Created on 10 Sep 2013

@author: ByteBoxx
'''
#builtins
import sys, os, shutil
import datetime as date
import serial
import time
import pickle
import Queue

#3rd
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot
import win32file
import win32con
#user
from ui import bbTriggerBoxx_UI as uifile
from ui import bbTriggerBoxx_config_UI as configuifile
from qt import popup
from smartshooter.session import SetSession, FlexSession
from util import makepy2exe

#globals
gCONFIG_VAR = 'TRIGGERBOXX_CONFIG'
gCONFIG_FILE = 'triggerboxx_defaults.txt'
gSESSION_FILE = 'session.tbs'
gTAKEDIR_PREFIX = 'tk'
gJPGXTNS = ['jpg', 'JPG', 'jpeg', 'JPEG']
gCR2XTNS = ['cr2', 'CR2']
gCOMBINED_FILES = ['jpg', 'JPG', 'jpeg', 'JPEG', 'cr2', 'CR2']

gDEBUG = True

#===============================================================================
# 
#===============================================================================
class DirectoryPeriodCheck(QtCore.QObject):
    '''
    '''
    def __init__(self, dir):
        super(DirectoryPeriodCheck, self).__init__()
        self.dirToWatch = dir
        self.filesDictJPG = {} #holds all the new jpg files in dumpster 
        self.filesDictCR2 = {} #holds all the new cr2 files in dumpster
        
        self.FILE_LIST_DIRECTORY = 0x0001


        self.hDir = win32file.CreateFile (
                                          self.dirToWatch,
                                          self.FILE_LIST_DIRECTORY,
                                          win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
                                          None,
                                          win32con.OPEN_EXISTING,
                                          win32con.FILE_FLAG_BACKUP_SEMANTICS,
                                          None
                                          )
        
    @pyqtSlot()
    def process(self):
        thistrigger = None
        while 1:
            results = win32file.ReadDirectoryChangesW (
                self.hDir,
                1024,
                True,
                win32con.FILE_NOTIFY_CHANGE_FILE_NAME,
                None,
                None
              )
            
            
            if results:
                for res in results:
                    if res[0] == 1:
                        root, ext = os.path.splitext(res[1])
                        if any(imagefile in ext for imagefile in gCOMBINED_FILES):
                            
                            thistrigger = int(root.split('_')[2])

                                    
                            #triggers past the first        
                            if any(jp in ext for jp in gJPGXTNS):
                                if thistrigger not in self.filesDictJPG.keys():
                                    self.filesDictJPG[thistrigger] = []
                                self.filesDictJPG[thistrigger].append(os.path.join(self.dirToWatch, res[1]))
                            elif any(cr in ext for cr in gCR2XTNS):
                                if thistrigger not in self.filesDictCR2.keys():
                                    self.filesDictCR2[thistrigger] = []
                                self.filesDictCR2[thistrigger].append(os.path.join(self.dirToWatch, res[1]))
                            
            #print len(self.filesDictJPG[thistrigger])
            self.updateDictionaries()
            time.sleep(0.5)
            
    def updateDictionaries(self):
        self.emit(QtCore.SIGNAL("updatingJPGs(PyQt_PyObject)"), self.filesDictJPG)
        self.emit(QtCore.SIGNAL("updatingCR2s(PyQt_PyObject)"), self.filesDictCR2)

#===============================================================================
# 
#===============================================================================
class DL_bbTriggerBoxxConfig(QtGui.QDialog, configuifile.Ui_Dialog_bbTriggerBoxx_config):
    '''
    popup to write default values to disk for
    PHOTODIR
    JPG INCLUDE
    CR2 INCLUDE
    FOCUS TIME
    FLASH TIME
    '''
    def __init__(self, parent=None):
        super(DL_bbTriggerBoxxConfig, self).__init__(parent)
        self.setupUi(self)
        
        #connections
        self.connect(self.pushButton_browse, QtCore.SIGNAL("clicked()"), self.getPhotoDir)
        self.connect(self.pushButton_save, QtCore.SIGNAL("clicked()"), self.writeToFile)
        self.connect(self.pushButton_cancel, QtCore.SIGNAL("clicked()"), self.close)
        
    def _main(self):
        self.show()
        
    def getPhotoDir(self):
        lDir = popup.FileDialog.getDirectory(self, "Pick SmartShooter photo dir")
        if lDir:
            self.lineEdit_photoDownload.setText(lDir)
            
    def writeToFile(self):
        try:
            with open(os.path.join(os.environ.get(gCONFIG_VAR), gCONFIG_FILE), "w") as fh:
                fh.writelines("photodir " + str(self.lineEdit_photoDownload.text()) + '\n')
                fh.writelines("jpg " + str(self.checkBox_jpg.checkState()) + '\n')
                fh.writelines("cr2 " + str(self.checkBox_cr2.checkState()) + '\n')
                fh.writelines("focus " + str(self.doubleSpinBox_focus.value()) + '\n')
                fh.writelines("flash " + str(self.doubleSpinBox_flash.value()) + '\n')
            
            #success
            popup.Popup.info(self, "Successfully written config file to disk")
            self.close()
            
        except IOError:
            print "Error writing to file, check permissions"
            
            
#===============================================================================
# 
#===============================================================================
class MW_bbTriggerBoxx(QtGui.QMainWindow, uifile.Ui_MainWindow_bbTriggerBoxx):
    '''
    TriggerBoxx main window class
    '''
    def __init__(self, watcher, parent=None):
        super(MW_bbTriggerBoxx, self).__init__(parent)
        self.setupUi(self)
        
        #load the global ByteBoxx stylesheet - check if we are frozen
        lCurrentDir = makepy2exe.get_main_dir()
        if lCurrentDir:
            styleFile=os.path.join(lCurrentDir, "DarkOrangeQStyleTemplate.txt")
            with open(styleFile,"r") as fh:
                self.setStyleSheet(fh.read())
                       
        #action connections
        self.connect(self.actionMesh, QtCore.SIGNAL("triggered()"), self.newSession)
        self.connect(self.actionTexture, QtCore.SIGNAL("triggered()"), self.newSession)
        self.connect(self.actionNew_Subject, QtCore.SIGNAL("triggered()"), self.newSubject)
        self.connect(self.actionNew_Character, QtCore.SIGNAL("triggered()"), self.newCharacter)
        self.connect(self.actionNew_Definition, QtCore.SIGNAL("triggered()"), self.newDefinition)
        self.connect(self.actionEdit_Prefs, QtCore.SIGNAL("triggered()"), self.editPrefs)
        
        for x in ['COM1', 'COM3', 'COM4']:
            lAction = self.__dict__['actionOpen_{0}'.format(x)]
            self.connect(lAction, QtCore.SIGNAL("triggered()"), self.openComms)
            
        self.connect(self.actionCopyNow, QtCore.SIGNAL("triggered()"), self.copyFromDumpster)
                     
        #edits/spinners/checks
        self.connect(self.lineEdit_pose, QtCore.SIGNAL("returnPressed()"), self.updatePose)
        self.connect(self.lineEdit_bucket, QtCore.SIGNAL("returnPressed()"), self.updateBucket)
        
        
        #main buttons
        self.connect(self.pushButton_fire, QtCore.SIGNAL("clicked()"), self.fireArray)
        self.connect(self.pushButton_prime, QtCore.SIGNAL("clicked()"), self.primeArray)
        
        #attrs
        self.filesDictJPG = {}
        self.filesDictCR2 = {}
        self.activeTakeNames = []

        self.watcher = watcher
        self.connect(watcher, QtCore.SIGNAL("updatingJPGs(PyQt_PyObject)"), self.updatefilesDictJPG)
        self.connect(watcher, QtCore.SIGNAL("updatingCR2s(PyQt_PyObject)"), self.updatefilesDictCR2)

        
    def _main(self):
        self.show()
        
        #load/create a config file
        self.checkConfig()
        

    def checkConfig(self):
        if not os.environ.get(gCONFIG_VAR):
            popup.Popup.critical(self, "No $TRIGGERBOXX_CONFIG variable set\nPlease set and retry")
            self.close()
        else:
            #try to load a preset
            try:
                with open(os.path.join(os.environ.get(gCONFIG_VAR),gCONFIG_FILE), "r") as lFile:
                    lLines = lFile.readlines()
                    self.populateDefaults(lLines)                            
            except IOError:
                popup.Popup.warning(self, "Couldn't find a default config file\nOK to create one now")
                lConfigurator = DL_bbTriggerBoxxConfig(self)
                lConfigurator._main()
                
    def editPrefs(self):
        lConfigurator = DL_bbTriggerBoxxConfig(self)
        lConfigurator._main()
                
    def openComms(self):
        try:
            self.mSerial = serial.Serial(str(self.sender().objectName()).lstrip('actionOpen_'), 9600)   # open serial port that Arduino is using
            popup.Popup.info(self, "Successfully opened COM port")
        except:
            popup.Popup.critical(self, "Fatal! Could not open COM port")
            
   
    def populateDefaults(self, pLines):
        for line in pLines:
            if line.startswith('photodir'):
                lSplit = line.split(' ')
                self.lineEdit_photoDownload.setText(lSplit[1].rstrip())
                self.lineEdit_photoDownload.setReadOnly(True)
            elif line.startswith('jpg'):
                lSplit = line.split(' ')
                #self.checkBox_jpg.setCheckState(QtCore.Qt.CheckState(lSplit[1].rstrip())) DEPR
            elif line.startswith('cr2'):
                lSplit = line.split(' ')
                #self.checkBox_cr2.setCheckState(QtCore.Qt.CheckState(lSplit[1].rstrip())) DEPR
            elif line.startswith('focus'):
                lSplit = line.split(' ')
                self.doubleSpinBox_focus.setValue(float(lSplit[1].rstrip()))
            elif line.startswith('flash'):
                lSplit = line.split(' ')
                self.doubleSpinBox_flash.setValue(float(lSplit[1].rstrip()))
                
            

    def populateFields(self):
        if self.mSession.__class__ == FlexSession:
            self.lineEdit_bucket.setText(self.mSession.mBucket)
        elif self.mSession.__class__ == SetSession:
            self.lineEdit_subject.setText(self.mSession.mSubjectName)
            self.lineEdit_character.setText(self.mSession.mCharacterName)
            self.lineEdit_definition.setText(self.mSession.mDefinition)
            self.lineEdit_pose.setText(self.mSession.mPose)
            
    def newSession(self):
        #create a smartShooter session instance, either mesh or texture, flex or Set
        if self.groupBox_setcap.isChecked() and self.groupBox_flexcap.isChecked():
            popup.Popup.warning(self, "Cant run a 'Set' and 'Flex' Session at once!")
            return
        elif self.groupBox_setcap.isChecked():
            self.mSession = SetSession(str(self.sender().objectName()).lstrip('action'), str(self.lineEdit_photoDownload.text()))
        elif self.groupBox_flexcap.isChecked():
            self.mSession = FlexSession(str(self.sender().objectName()).lstrip('action'), str(self.lineEdit_photoDownload.text()))
            
        if self.mSession.mType == 'Mesh':
            self.radioButton_mesh.setChecked(True)
        elif self.mSession.mType == 'Texture':
            self.radioButton_texture.setChecked(True)
            
        #create the shoot folder dir
        lFolderName = str(popup.Input.getText(self, "Enter Root Shoot Folder Name")[0])
        lShootFolder = os.path.join(os.path.dirname(self.mSession.mRootFolder), lFolderName + '_' + self.mSession.mType)
        
        
        #check for a previous pickled session on disk and try to load
        lSessionFile = os.path.join(lShootFolder, gSESSION_FILE)
        if os.path.isfile(lSessionFile):
            with open(lSessionFile, 'r') as fh:
                lPrevSession = pickle.load(fh)
            self.mSession = lPrevSession
            
            #---CHANGE---
            self.populateFields() #write them to the GUI
            #work out the take
            lTakeFolder = os.path.basename(self.mSession.mActiveTakePath)
            self.spinBox_take.setValue(int(lTakeFolder.lstrip('tk')) + 1)
        else:

            if not os.path.exists(os.path.abspath(lShootFolder)):
                os.makedirs(lShootFolder)
            self.mSession.mShootFolder = lShootFolder
            
            #create the default session if we didnt find a pickle - CHANGE?
            self.mSession.newSession()
            self.populateFields()
            
            if not os.path.exists(os.path.abspath(self.mSession.mActivePath)):
                os.makedirs(self.mSession.mActivePath)
        
        #switch off
        self.radioButton_mesh.setEnabled(False)
        self.radioButton_texture.setEnabled(False)    
        
        self.populateTreeView()
        
    def newSubject(self):
        lNewSubjName = popup.Input.getText(self, "Enter new Subject name")
        if lNewSubjName:
            self.mSession.newSubject(name=str(lNewSubjName[0]))
            self.lineEdit_subject.setText(lNewSubjName[0])
            self.newCharacter()
            self.newDefinition()
            
    def newCharacter(self):
        lNewCharName = popup.Input.getText(self, "Enter new Character name")
        if lNewCharName:
            self.mSession.updateCharacter(name=str(lNewCharName[0]))
            self.mSession.updateActivePath()
            self.lineEdit_character.setText(lNewCharName[0])
            #reset takes
            self.spinBox_take.setValue(1)
    
    def newDefinition(self):
        lNewDefName = popup.Input.getText(self, "Enter new Definition name")
        if lNewDefName:
            self.mSession.updateDefinition(name=str(lNewDefName[0]))
            self.mSession.updateActivePath()
            self.lineEdit_definition.setText(lNewDefName[0])
            #reset takes
            self.spinBox_take.setValue(1)
            
    def updatePose(self):
        self.mSession.updatePose(name=str(self.lineEdit_pose.text()))
        self.mSession.updateActivePath()
        #reset the takes
        self.spinBox_take.setValue(1)
        self.plainTextEdit_logging.setPlainText("Set new pose name to {0}".format(self.mSession.mPose))
        
    def updateBucket(self):
        self.mSession.updateBucket(name=str(self.lineEdit_bucket.text()))
        self.mSession.updateActivePath()
        #reset the takes
        self.spinBox_take.setValue(1)
        self.plainTextEdit_logging.setPlainText("Set new bucket name to {0}".format(self.mSession.mBucket))
        
    def populateTreeView(self):
        model = QtGui.QFileSystemModel(self.treeView_diskMap)
        model.setReadOnly(True)
        root = model.setRootPath(self.mSession.mShootFolder)
        self.treeView_diskMap.setModel(model)
        self.treeView_diskMap.setRootIndex(root)
        
    def updatefilesDictJPG(self, adict):
        self.filesDictJPG = adict
        
    def updatefilesDictCR2(self, adict):
        self.filesDictCR2 = adict
        
    def CheckSerialComms(self):
        try:
            assert 'mSerial' in self.__dict__
        except AssertionError:
            popup.Popup.critical(self, "no serial port defined!")
            return False
    
        return True
        
    def primeArray(self):
        if self.CheckSerialComms():
            #create the take folders
            lTakeFolder = gTAKEDIR_PREFIX + str(self.spinBox_take.value()) if self.spinBox_take.value() > 9 else gTAKEDIR_PREFIX + '0' + str(self.spinBox_take.value())
            lActiveTakePath = os.path.join(self.mSession.mActivePath, lTakeFolder)
            self.mSession.setActiveTakePath(lActiveTakePath)
            #create on disk
            try:
                if not os.path.exists(os.path.abspath(self.mSession.mActiveTakePath)):
                    os.makedirs(self.mSession.mActiveTakePath)
                    
                #make jpg and cr2 directories
                if self.checkBox_jpg.isChecked():
                    os.makedirs(os.path.join(self.mSession.mActiveTakePath, 'jpg'))
                if self.checkBox_cr2.isChecked():
                    os.makedirs(os.path.join(self.mSession.mActiveTakePath, 'cr2'))
            except:
                popup.Popup.warning(self, "Error creating take directory, check permission")
                
            #write to the arduino
            self.plainTextEdit_logging.setPlainText('take directories created, priming cams...\n')
            self.mSerial.write('b')
    
    def fireArray(self):
        if self.CheckSerialComms():
            self.plainTextEdit_logging.clear()
            #write to the arduino
            self.mSerial.write('a')
            
            #update our active take names
            self.activeTakeNames.append((self.mSession.mActiveTakePath, self.lineEdit_comment.text()))          
            #increment take?
            if self.checkBox_inc.isChecked():
                self.spinBox_take.setValue(self.spinBox_take.value() + 1)
                
            self.lineEdit_comment.clear()
            
    def copyFromDumpster(self):
        '''
        we need to flush everything from Dumpster and create XML info for each take
        '''
        for i, v in enumerate(self.activeTakeNames):

            if self.filesDictJPG != {}:
                for jfile in self.filesDictJPG[i+1]: #we have to assume SmartShooter batch started at 0001
                    lsplit = os.path.basename(jfile).split('_')
                    shutil.move(jfile, os.path.join(v[0], 'jpg', lsplit[0]+'_'+lsplit[1]+'.jpg'))
            if self.filesDictCR2 != {}:
                for cfile in self.filesDictCR2[i+1]: #we have to assume SmartShooter batch started at 0001
                    lsplit = os.path.basename(cfile).split('_')
                    shutil.move(cfile, os.path.join(v[0], 'cr2', lsplit[0]+'_'+lsplit[1]+'.cr2'))
                        
            lNewXML = self.mSession.GenerateXML(v)
            
        self.activeTakeNames = []
        self.filesDictJPG = {}
        self.filesDictCR2 = {}
        
    def closeEvent(self, event):
        #try and pickle the session for later
        with open(os.path.join(self.mSession.mShootFolder, gSESSION_FILE), 'w') as fh:
            pickle.dump(self.mSession, fh)
            
            
#------------------------------------------------------------------------------ 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    objThread = QtCore.QThread()
    if gDEBUG:
        d = DirectoryPeriodCheck("Z:\\dumpster\\SS")
    else:
        d = DirectoryPeriodCheck(sys.argv[1])
    d.moveToThread(objThread)
    objThread.started.connect(d.process)
    objThread.start()
    win = MW_bbTriggerBoxx(d)
    win._main()
    app.exec_()
