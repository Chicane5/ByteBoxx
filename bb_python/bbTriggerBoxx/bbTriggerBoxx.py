'''
Created on 10 Sep 2013

@author: ByteBoxx
'''
#builtins
import sys, os
import datetime as date
import serial
import time
import pickle
#3rd
from PyQt4 import QtCore, QtGui
#user
from ui import bbTriggerBoxx_UI as uifile
from ui import bbTriggerBoxx_config_UI as configuifile
from qt import popup
from smartshooter.session import Session

#globals
gCONFIG_VAR = 'TRIGGERBOXX_CONFIG'
gCONFIG_FILE = 'triggerboxx_defaults.txt'
gSESSION_FILE = 'session.tbs'

#===============================================================================
# 
#===============================================================================
class DL_bbTriggerBoxxConfig(QtGui.QDialog, configuifile.Ui_Dialog_bbTriggerBoxx_config):
    '''
    classdocs
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
    classdocs
    '''
    def __init__(self, parent=None):
        super(MW_bbTriggerBoxx, self).__init__(parent)
        self.setupUi(self)
        
        styleFile=os.path.join(os.path.dirname(os.path.split(__file__)[0]),"common//qt", "DarkOrangeQStyleTemplate.txt")
        with open(styleFile,"r") as fh:
            self.setStyleSheet(fh.read())
                       
        #action connections
        self.connect(self.actionMesh, QtCore.SIGNAL("triggered()"), self.newSession)
        self.connect(self.actionTexture, QtCore.SIGNAL("triggered()"), self.newSession)
        self.connect(self.actionNew_Subject, QtCore.SIGNAL("triggered()"), self.newSubject)
        self.connect(self.actionNew_Character, QtCore.SIGNAL("triggered()"), self.newCharacter)
        self.connect(self.actionNew_Definition, QtCore.SIGNAL("triggered()"), self.newDefinition)
        
        for x in ['COM1', 'COM3', 'COM4']:
            lAction = self.__dict__['actionOpen_{0}'.format(x)]
            self.connect(lAction, QtCore.SIGNAL("triggered()"), self.openComms)
        
        #edits/spinners/checks
        self.connect(self.lineEdit_pose, QtCore.SIGNAL("returnPressed()"), self.updatePose)
        self.connect(self.spinBox_imgWait, QtCore.SIGNAL("valueChanged(int)"), self.updateInternalSleep)
        self.connect(self.checkBox_jpg, QtCore.SIGNAL("stateChanged(int)"), self.calculateSleepDelay)
        self.connect(self.checkBox_cr2, QtCore.SIGNAL("stateChanged(int)"), self.calculateSleepDelay)
        
        #main buttons
        self.connect(self.pushButton_fire, QtCore.SIGNAL("clicked()"), self.fireArray)
        self.connect(self.pushButton_prime, QtCore.SIGNAL("clicked()"), self.primeArray)
        
        #attrs
        self.sleepDelay = 0
        
    def _main(self):
        self.show()
        
        #load a config file
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
                self.checkBox_jpg.setCheckState(QtCore.Qt.CheckState(lSplit[1].rstrip()))
            elif line.startswith('cr2'):
                lSplit = line.split(' ')
                self.checkBox_cr2.setCheckState(QtCore.Qt.CheckState(lSplit[1].rstrip()))
            elif line.startswith('focus'):
                lSplit = line.split(' ')
                self.doubleSpinBox_focus.setValue(float(lSplit[1].rstrip()))
            elif line.startswith('flash'):
                lSplit = line.split(' ')
                self.doubleSpinBox_flash.setValue(float(lSplit[1].rstrip()))
                
            self.calculateSleepDelay()
            
    def calculateSleepDelay(self):
        if self.checkBox_jpg.isChecked() and self.checkBox_cr2.isChecked():
            self.spinBox_imgWait.setValue(85)
        elif self.checkBox_jpg.isChecked() and not self.checkBox_cr2.isChecked():
            self.spinBox_imgWait.setValue(25)
            
    def updateInternalSleep(self, pValue):
        self.sleepDelay = pValue
                
    def populateSubjectFields(self):
        self.lineEdit_subject.setText(self.mSession.mSubjectName)
        self.lineEdit_character.setText(self.mSession.mCharacterName)
        self.lineEdit_definition.setText(self.mSession.mDefinition)
        self.lineEdit_pose.setText(self.mSession.mPose)
            
    def newSession(self):
        #create a smartShooter session instance
        self.mSession = Session(str(self.sender().objectName()).lstrip('action'), str(self.lineEdit_photoDownload.text()))
        if self.mSession.mType == 'Mesh':
            self.radioButton_mesh.setChecked(True)
        elif self.mSession.mType == 'Texture':
            self.radioButton_texture.setChecked(True)
            
        #create the root dir
        lToday = date.datetime.today()
        lShootFolder = os.path.join(self.mSession.mRootFolder, lToday.strftime('%Y%m%d') + '_' + self.mSession.mType)
        
        #check for a previous session and try to load
        lSessionFile = os.path.join(lShootFolder, gSESSION_FILE)
        if os.path.isfile(lSessionFile):
            with open(lSessionFile, 'r') as fh:
                lPrevSession = pickle.load(fh)
            self.mSession = lPrevSession
            self.populateSubjectFields()
        else:
            try:
                if not os.path.exists(os.path.abspath(lShootFolder)):
                    os.makedirs(lShootFolder)
                self.mSession.mShootFolder = lShootFolder
                
                #create default session
                self.mSession.newSession()
                self.populateSubjectFields()
                
                if not os.path.exists(os.path.abspath(self.mSession.mActivePath)):
                    os.makedirs(self.mSession.mActivePath)
            except:
                popup.Popup.warning(self, "Error creating shootday directory, check permission")
                
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
        
    def populateTreeView(self):
        model = QtGui.QFileSystemModel(self.treeView_diskMap)
        model.setReadOnly(True)
        root = model.setRootPath(self.mSession.mShootFolder)
        self.treeView_diskMap.setModel(model)
        self.treeView_diskMap.setRootIndex(root)
        
    def primeArray(self):
        try:
            assert(hasattr(self, 'mSerial'))
        except AssertionError:
            popup.Popup.critical(self, "no serial port defined!")
            return
        
        #write to the arduino and prime the cams
        self.plainTextEdit_logging.setPlainText('priming cams...\n')
        self.mSerial.write('b')
    
    def fireArray(self):
        try:
            assert(hasattr(self, 'mSerial'))
        except AssertionError:
            popup.Popup.critical(self, "no serial port defined!")
            return
        
        #write to the arduino and trigger the cams
        self.plainTextEdit_logging.setPlainText('firing cams...\n')
        self.mSerial.write('a')
        
        #create the take folder
        lTakeFolder = str(self.spinBox_take.value()) if self.spinBox_take.value() > 9 else '0' + str(self.spinBox_take.value())
        self.mSession.mActiveTakePath = os.path.join(self.mSession.mActivePath, lTakeFolder)
        try:
            if not os.path.exists(os.path.abspath(self.mSession.mActiveTakePath)):
                os.makedirs(self.mSession.mActiveTakePath)
        except:
            popup.Popup.warning(self, "Error creating take directory, check permission")
        
        #todo -- thread this
        #sleep to allow images to drop in?
        time.sleep(self.sleepDelay)
        #todo --
        
        #cleanup the images
        lCount = self.mSession.moveImages()
        self.plainTextEdit_logging.appendPlainText('moved {0} images to {1}'.format(lCount, self.mSession.mActiveTakePath))
        
        #increment take?
        if self.checkBox_inc.isChecked():
            self.spinBox_take.setValue(self.spinBox_take.value() + 1)
            
    def closeEvent(self, event):
        #try and pickle the session for later
        with open(os.path.join(self.mSession.mShootFolder, gSESSION_FILE), 'w') as fh:
            pickle.dump(self.mSession, fh)
            
        
#------------------------------------------------------------------------------ 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = MW_bbTriggerBoxx()
    win._main()
    app.exec_()
