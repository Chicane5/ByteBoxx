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
import logging
import itertools

#3rd
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot
import win32file
import win32con
import _winreg as winreg

#user
from ui import bbTriggerBoxx_UI as uifile
from ui import bbTriggerBoxx_config_UI as configuifile
from qt import popup
from smartshooter.session import  FlexSession
from util import makepy2exe

#globals
gSESSION_FILE = 'session.tbs'
gTAKEDIR_PREFIX = 'tk'
gJPGXTNS = ['jpg', 'JPG', 'jpeg', 'JPEG']
gCR2XTNS = ['cr2', 'CR2']
gCOMBINED_FILES = ['jpg', 'JPG', 'jpeg', 'JPEG', 'cr2', 'CR2']

gDEBUG = True

"""
Use for log window
"""
def write(self, string):
    if string.lower().find("info") >= 0:
        #green
        self.setTextColor (QtGui.QColor.fromRgb(23, 122, 58))
    elif string.lower().find("warning") >= 0:
        #yellow
        self.setTextColor (QtGui.QColor.fromRgb(204, 201, 2))
    elif string.lower().find("error") >= 0:
        #red
        self.setTextColor (QtGui.QColor.fromRgb(173, 2, 25))
    else:
        self.setTextColor (QtGui.QColor.fromRgb(0, 0, 0))
    self.append(string)

"""
loop thru serial ports
"""
def enumerate_serial_ports():
    """
    Uses the Win32 registry to return a iterator of serial
        (COM) ports existing on this computer.
    """
    path = 'HARDWARE\\DEVICEMAP\\SERIALCOMM'
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
    except WindowsError:
        raise Exception

    for i in itertools.count():
        try:
            val = winreg.EnumValue(key, i)
            yield (str(val[1]))
        except EnvironmentError:
            break

#===============================================================================
# 
#===============================================================================
class DirectoryPeriodCheck(QtCore.QObject):
    '''
    This object constantly monitors our chosen photodownload directory for changes, and communicates
    to image mover when there is something new to move
    '''
    def __init__(self):
        super(DirectoryPeriodCheck, self).__init__()
        self.dirToWatch = None
        self.filesDictJPG = {} #holds all the new jpg files in dumpster 
        self.filesDictCR2 = {} #holds all the new cr2 files in dumpster
        self.mErrors = []
        
        self.FILE_LIST_DIRECTORY = 0x0001
        self.hDir = None
        
    def updateDirToWatch(self, pDir):
        
        self.dirToWatch = pDir
        
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
                #files have dropped into the bucket, iterate through to file into dicts
                for res in results:
                    if res[0] == 1:
                        root, ext = os.path.splitext(res[1])
                        if any(imagefile in ext for imagefile in gCOMBINED_FILES): #are these JPGs or CR2s?
                            
                            #make sure we are dealing with the following convention from SmartCrap:
                            #CAMERANAME_DATE_BATCHNUMBER eg AL01_20140101_0001
                            rsplit = root.split('_')
                            if len(rsplit) != 3:
                                if res[1] not in self.mErrors:
                                    self.mErrors.append(res[1])
                                continue
                            
                            #what is this batchnumber?
                            thistrigger = int(root.split('_')[2])
                            
                            if any(jp in ext for jp in gJPGXTNS):
                                if thistrigger not in self.filesDictJPG.keys():
                                    self.filesDictJPG[thistrigger] = []
                                #self.filesDictJPG[thistrigger].append(os.path.join(self.dirToWatch, res[1]))
                                self.emit(QtCore.SIGNAL("updatingJPGs(PyQt_PyObject)"), (thistrigger, os.path.join(self.dirToWatch, res[1])))
                            elif any(cr in ext for cr in gCR2XTNS):
                                if thistrigger not in self.filesDictCR2.keys():
                                    self.filesDictCR2[thistrigger] = []
                                #self.filesDictCR2[thistrigger].append(os.path.join(self.dirToWatch, res[1]))
                                self.emit(QtCore.SIGNAL("updatingCR2s(PyQt_PyObject)"), (thistrigger, os.path.join(self.dirToWatch, res[1])))
                            
                    #if self.mErrors:
                        #self.emit(QtCore.SIGNAL("errorFiles()"))
            

#===============================================================================
# 
#===============================================================================
class ImageMovers(QtCore.QObject):
    '''
    This object waits for notification of additions to the watchers directory structures and starts to pull data from them
    '''
    def __init__(self, watcher):
        super(ImageMovers, self).__init__()
        
        self.watcher = watcher
        self.takes = [] #take list gets updated by MainGui whenever we fire off a new take
        self.takesToJpgs = {}
        self.takesToCR2s = {}
        
        self.timerJ = QtCore.QTimer() # jpg timer
        self.timerC = QtCore.QTimer() #cr2 timer
        self.timerJ.timeout.connect(self.moveJPG)
        self.timerC.timeout.connect(self.moveCR2) 
        
        self.connect(self.watcher, QtCore.SIGNAL("updatingJPGs(PyQt_PyObject)"), self.updatefilesDictJPG)
        self.connect(self.watcher, QtCore.SIGNAL("updatingCR2s(PyQt_PyObject)"), self.updatefilesDictCR2)
        #self.connect(self.watcher, QtCore.SIGNAL("errorFiles()"), self.cacheErrors)
        
        
        self.timerJ.start(3000)
        self.timerC.start(3000)
    
    def addToTakes(self, take):
        print "got new take ", take
        self.takes.append(take)
        
    def updatefilesDictJPG(self, batchNo_filePath):
        '''
        when this signal is received, we get tuple of index and path
        '''
        if batchNo_filePath[0] not in self.takesToJpgs.keys():
            self.takesToJpgs[batchNo_filePath[0]] = []
        if batchNo_filePath[1] not in self.takesToJpgs[batchNo_filePath[0]]:
            self.takesToJpgs[batchNo_filePath[0]].append(os.path.abspath(batchNo_filePath[1]))
            
    def updatefilesDictCR2(self, batchNo_filePath):
        '''
        when this signal is received, we get tuple of index and path
        '''
        if batchNo_filePath[0] not in self.takesToCR2s.keys():
            self.takesToCR2s[batchNo_filePath[0]] = []
        if batchNo_filePath[1] not in self.takesToCR2s[batchNo_filePath[0]]:
            self.takesToCR2s[batchNo_filePath[0]].append(os.path.abspath(batchNo_filePath[1]))
        
        
    def moveJPG(self):
        
        
        for k in self.takesToJpgs.keys():
            print "key is ", k
            index = int(k-1)
            takePath = str(self.takes[index])
            print "takePath is ", takePath
            for j in self.takesToJpgs[k]:
                print "jpg is ", j
                lsplit = os.path.basename(j).split('_')
                print "lsplit is ", lsplit
                shutil.move(j, os.path.join(takePath, 'jpg', lsplit[0]+'_'+lsplit[1]+ '_'+lsplit[2] ))
                if os.path.isfile(os.path.join(takePath, 'jpg', lsplit[0]+'_'+lsplit[1]+ '_'+lsplit[2] )):
                    print "yes its a file, removing"
                    self.takesToJpgs[k].remove(j)
                    
    def moveCR2(self):
        
        
        for k in self.takesToCR2s.keys():
            print "key is ", k
            index = int(k-1)
            takePath = str(self.takes[index])
            print "takePath is ", takePath
            for c in self.takesToCR2s[k]:
                print "cr2 is ", c
                lsplit = os.path.basename(c).split('_')
                print "lsplit is ", lsplit
                shutil.move(c, os.path.join(takePath, 'cr2', lsplit[0]+'_'+lsplit[1]+ '_'+lsplit[2]))
                if os.path.isfile(os.path.join(takePath, 'cr2', lsplit[0]+'_'+lsplit[1]+ '_'+lsplit[2])):
                    print "yes its a file, removing"
                    self.takesToCR2s[k].remove(c)

        """
        for i, v in enumerate(self.takes):
            print i
            if i+1 in self.watcher.filesDictJPG.keys():
                print "key here" #make sure there is a valid key
                if self.watcher.filesDictJPG[i+1] == []:
                    print "empty"
                    break
                else:
                    while self.watcher.filesDictJPG[i+1] != []:
                        for jpg in self.watcher.filesDictJPG[i+1]:
                            try:
                                print jpg
                                lsplit = os.path.basename(jpg).split('_')
                                shutil.move(jpg, os.path.join(str(v[0]), 'jpg', lsplit[0]+'_'+lsplit[1]+'.jpg'))
                                if os.path.isfile(os.path.join(str(v[0]), 'jpg', lsplit[0]+'_'+lsplit[1]+'.jpg')):
                                    self.watcher.filesDictJPG[i+1].remove(jpg)
                            except (IOError, WindowsError):
                                print "fucking error"
                                continue
        
                            
    def updatefilesDictCR2(self):
        '''
        when this signal is received, we know that watcher has added more images to its interal CR2 structure
        '''
        print "got update CR2 signal"
        for i, v in enumerate(self.takes):
            if i+1 in self.watcher.filesDictCR2.keys(): #make sure there is a valid key
                if self.watcher.filesDictCR2[i+1] != []:
                    while self.watcher.filesDictCR2[i+1] != []:
                        for cr2 in self.watcher.filesDictCR2[i+1]:
                            try:
                                lsplit = os.path.basename(cr2).split('_')
                                shutil.move(cr2, os.path.join(str(v[0]), 'cr2', lsplit[0]+'_'+lsplit[1]+'.cr2'))
                                if os.path.isfile(os.path.join(str(v[0]), 'cr2', lsplit[0]+'_'+lsplit[1]+'.cr2')):
                                    self.watcher.filesDictCR2[i+1].remove(cr2)
                            except (IOError, WindowsError):
                                continue
    
    def cacheErrors(self):
        '''
        when this signal is received we know there have been error files that dont match our convention,
        we will attempt to move them to an intermediary directory to deal with later
        '''
        
        if self.mErrorList:
            sortmedir = os.path.join(os.path.dirname(str(self.lineEdit_photoDownload.text())), 'tosort')
            if not os.path.exists(sortmedir):
                os.makedirs(sortmedir)
                popup.Popup.warning(self, "{0} appears to have bad naming, check SmartShooter. Ignoring".format(','.join(self.mErrorList)))
                for errorFile in self.mErrorList:
        shutil.move(os.path.join(str(self.lineEdit_photoDownload.text()), errorFile), sortmedir)
        
        pass
        """
     
#==============================================================================
# 
#===============================================================================
class SerialMonitor(QtCore.QObject):
    '''
    The serial monitor spins in another seperate thread and listens for the Arduino writing back to the PC -
    in this case we want to emit the signal we have been triggered from cable and fire off a take as usal
    '''
    def __init__(self):
        super(SerialMonitor, self).__init__()
        self.mSerial = None
        
    def updateSerialPort(self, serial):
        '''
        shared reference to the serial.Serial class from the MainGUI
        '''
        self.mSerial = serial
    
    @pyqtSlot()  
    def monitor(self):
        while True:
            val = self.mSerial.read(1) #read a byte from the serial port
            if val == 'c':
                self.emit(QtCore.SIGNAL("cableTrigger()"))
            time.sleep(1.5)
 
     
#===============================================================================
# 
#===============================================================================
class MW_bbTriggerBoxx(QtGui.QMainWindow, uifile.Ui_MainWindow_bbTriggerBoxx):
    '''
    TriggerBoxx main window class
    '''
    cBAUD_RATE = 9600
    cPHOTO_DLOAD_DIR = "Z:\\dumpster\\SS"
    
    def __init__(self, watcher, serialmonitor, imageMover, parent=None):
        super(MW_bbTriggerBoxx, self).__init__(parent)
        self.setupUi(self)
        
        #load the global ByteBoxx stylesheet - check if we are frozen
        styleFile = ''
        lCurrentDir = makepy2exe.get_main_dir()
        if lCurrentDir:
            styleFile=os.path.join(lCurrentDir, "DarkOrangeQStyleTemplate.txt")

        else:
            styleFile=os.path.join(os.path.dirname(__file__), "DarkOrangeQStyleTemplate.txt")
            
        try:
            with open(styleFile,"r") as fh:
                self.setStyleSheet(fh.read())
        except:
            pass
        
        #action connections
        self.connect(self.actionMesh, QtCore.SIGNAL("triggered()"), self.newProject)
        self.connect(self.actionTexture, QtCore.SIGNAL("triggered()"), self.newProject)
        self.connect(self.actionLoad_Project, QtCore.SIGNAL("triggered()"), self.loadProject)
        self.connect(self.actionSave_Project, QtCore.SIGNAL("triggered()"), self.saveProject)
        self.connect(self.actionNewShootday, QtCore.SIGNAL("triggered()"), self.updateShootDay)
        
        self.connect(self.lineEdit_bucket, QtCore.SIGNAL("returnPressed()"), self.updateBucket)
        
        #main buttons
        self.connect(self.pushButton_fire, QtCore.SIGNAL("clicked()"), self.fireArray)
        self.connect(self.pushButton_prime, QtCore.SIGNAL("clicked()"), self.primeArray)
        
        #attrs
        self.batchCounter = 1
        self.mSession = None #the main session for this run __smartshooter.session.FlexSession__

        #directory watcher & serial port stuffz
        self.watcher = watcher
        self.watcher_thread = self.watcher.thread()

        
        self.srmonitor = serialmonitor
        self.srmonitor_thread = self.srmonitor.thread()
        self.connect(self.srmonitor, QtCore.SIGNAL("cableTrigger()"), self.triggeredFromCable)
        
        self.imageMover = imageMover
        self.imageMover_thread = self.imageMover.thread()
        self.connect(self, QtCore.SIGNAL("updatingTakes(PyQt_PyObject)"), self.imageMover.addToTakes)
        
        logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', \
                            level=logging.INFO, stream=self.textEdit_logging)
        
        self.logger = logging.getLogger(__name__)   
        
        QtGui.QTextEdit.write = write #enable logging to TextBox 
        self.lcdNumber_countdown.display(self.batchCounter) 
        
    def _main(self):
        self.show()
        
        #get the COM port we are on
        sr = self.findPort(MW_bbTriggerBoxx.cBAUD_RATE)
        if sr:
            print 
            self.logger.info("found TriggerBoxx Hardware on {0}".format(sr.port))
            sr.flush()
            self.mSerial = sr
        
        #pass the serial port instance to monitor & init the thread
        self.srmonitor.updateSerialPort(self.mSerial)
        
        #set our SmartShooter dir
        self.lineEdit_photoDownload.setText(MW_bbTriggerBoxx.cPHOTO_DLOAD_DIR)
        self.lineEdit_photoDownload.setReadOnly(True)
        
        self.watcher.updateDirToWatch(os.path.abspath(MW_bbTriggerBoxx.cPHOTO_DLOAD_DIR))
        
        #start our threads
        self.srmonitor_thread.start()
        self.watcher_thread.start()
        self.imageMover_thread.start()
        
        #remind to reset smart shooter shit
        popup.Popup.critical(self, "REMEMBER TO RESET SMART SHOOTER BATCH TO 0001, CONVENTION: $CAM_$DATE_$BATCH")
            
        
    def findPort(self, baud):
        ports = enumerate_serial_ports()
        for p in ports:
            try:
                sr = serial.Serial(p, baud, timeout=2)
            except (serial.serialutil.SerialException, OSError) as e:
                print(str(e))
                continue
        return sr
        
    def populateFields(self):
        self.lineEdit_shootday.setText(self.mSession.mShootDay)
        self.lineEdit_bucket.setText(self.mSession.mBucket)
    
    def newProject(self):
        #create a smartShooter project instance, either mesh or texture - paremeters type and root folder

        self.mSession = FlexSession(str(self.sender().objectName()).lstrip('action'), os.path.dirname(str(self.lineEdit_photoDownload.text())))
            
        if self.mSession.mType == 'Mesh':
            self.radioButton_mesh.setChecked(True)
        elif self.mSession.mType == 'Texture':
            self.radioButton_texture.setChecked(True)
            
        #get a name from the user for a new project
        lFolderName = str(popup.Input.getText(self, "Enter Project Root Name")[0])
        lProjectFolder = os.path.join(os.path.dirname(self.mSession.mRootFolder), lFolderName + '_' + self.mSession.mType)
        
        if not os.path.exists(os.path.abspath(lProjectFolder)):
            os.makedirs(lProjectFolder)
        self.mSession.mShootFolder = lProjectFolder
        self.lineEdit_projectRoot.setText(lProjectFolder)

        self.mSession.newSession()
        self.populateFields()
        
        #create this path if it doenst exist
        if not os.path.exists(os.path.abspath(self.mSession.mActivePath)):
            os.makedirs(self.mSession.mActivePath)
        
        #switch off
        self.radioButton_mesh.setEnabled(False)
        self.radioButton_texture.setEnabled(False)    
        
        self.populateTreeView()
        self.logger.info("created new project at {0}".format(lProjectFolder))
    
    def loadProject(self):
        #directory popup to pick a TBS file
        lTBSFile = popup.FileDialog.getFileFilter(self, "pick an existing .TBS project file", '*.tbs')
        if lTBSFile[0] != '':
            with open(os.path.abspath(str(lTBSFile[0])), 'r') as fh:
                lPrevSession = pickle.load(fh)
            
            self.mSession = lPrevSession
            self.populateFields() #write them to the GUI
            
            if self.mSession.mType == 'Mesh':
                self.radioButton_mesh.setChecked(True)
            elif self.mSession.mType == 'Texture':
                self.radioButton_texture.setChecked(True)
                
            #switch off
            self.radioButton_mesh.setEnabled(False)
            self.radioButton_texture.setEnabled(False)  
            
            #work out the previous take and increment by 1
            lTakeFolder = os.path.basename(self.mSession.mActiveTakePath)
            if lTakeFolder:
                self.spinBox_take.setValue(int(lTakeFolder.lstrip('tk')) + 1)
            else:
                self.spinBox_take.setValue(1)
                
            self.lineEdit_projectRoot.setText(self.mSession.mShootFolder)
            self.populateTreeView()
            self.logger.info("loaded project from {0}".format(self.mSession.mShootFolder))
    
    def saveProject(self):
        if self.mSession:
            with open(os.path.join(self.mSession.mShootFolder, gSESSION_FILE), 'w') as fh:
                pickle.dump(self.mSession, fh)
        
    def _checkForSession(self):
        if not self.mSession:
            popup.Popup.critical(self, "No Root Project! Create or Open to start shooting")
            return False
        return True
    
    def updateShootDay(self):
        if not self._checkForSession():
            return
        lNewShootDayName = popup.Input.getText(self, "Enter new Shootday name")
        if lNewShootDayName:
            self.mSession.newShootDay(name=str(lNewShootDayName[0]))
            self.mSession.updateBucket() # update with the default name
            self.mSession.updateActivePath()
            self.spinBox_take.setValue(1)
            self.populateFields()
            self.logger.info("Set new shootday name to {0}".format(self.mSession.mShootDay))
    
    def updateBucket(self):
        if not self._checkForSession():
            return
        self.mSession.updateBucket(name=str(self.lineEdit_bucket.text()))
        self.mSession.updateActivePath()
        #reset the takes
        self.spinBox_take.setValue(1)
        self.logger.info("Set new bucket name to {0}".format(self.mSession.mBucket))
        
    def populateTreeView(self):
        model = QtGui.QFileSystemModel(self.treeView_diskMap)
        model.setReadOnly(True)
        root = model.setRootPath(self.mSession.mShootFolder)
        self.treeView_diskMap.setModel(model)
        self.treeView_diskMap.setRootIndex(root)
                
    def CheckSerialComms(self):
        try:
            assert 'mSerial' in self.__dict__
        except AssertionError:
            popup.Popup.critical(self, "no serial port defined!")
            return False
    
        return True
    
    def primeArray(self):
        if not self._checkForSession():
            return
        if self.CheckSerialComms():
            #write to the arduino
            self.mSerial.write('b')
    
    def triggeredFromCable(self):
        self.logger.warning("got fire from cable trigger!")
        self.fireArray()
        
    def fireArray(self):
        if not self._checkForSession():
            return
        if self.CheckSerialComms():
            #check for camera count
            if self.spinBox_cams.value() == 100:
                q = popup.Popup.question(self, "current connected cameras is default 100 - correct?")
                if q:
                    return
            
            #create the take folders
            lTakeFolder = gTAKEDIR_PREFIX + str(self.spinBox_take.value()) if self.spinBox_take.value() > 9 else gTAKEDIR_PREFIX + '0' + str(self.spinBox_take.value())
            lActiveTakePath = os.path.join(self.mSession.mActivePath, lTakeFolder)
            self.mSession.setActiveTakePath(lActiveTakePath)
            #create on disk
            try:
                if not os.path.exists(os.path.abspath(self.mSession.mActiveTakePath)):
                    os.makedirs(self.mSession.mActiveTakePath)
                #make jpg and cr2 directories
                os.makedirs(os.path.join(self.mSession.mActiveTakePath, 'jpg'))
                os.makedirs(os.path.join(self.mSession.mActiveTakePath, 'cr2'))
                
                #create a text document for comment
                with open(os.path.join(self.mSession.mActiveTakePath, 'comment.txt'), 'w') as fh:
                    fh.write(str(self.lineEdit_comment.text()))
                
                self.logger.info("created take directory {0}".format(self.mSession.mActiveTakePath))
            except:
                popup.Popup.warning(self, "Error creating take directory, check permission")
            
            #write to the arduino
            self.mSerial.write('a')
            
            #update our active take names
            self.emit(QtCore.SIGNAL("updatingTakes(PyQt_PyObject)"), self.mSession.mActiveTakePath)
            #increment take?
            if self.checkBox_inc.isChecked():
                self.spinBox_take.setValue(self.spinBox_take.value() + 1)
                
            self.lineEdit_comment.clear()
            self.batchCounter+=1
            self.lcdNumber_countdown.display(self.batchCounter)
            
    def closeEvent(self, event):
        #try and pickle the session for later
        self.saveProject()
        #close our two threads
        self.srmonitor_thread.terminate()
        self.watcher_thread.terminate()
        self.imageMover_thread.terminate()
        
#------------------------------------------------------------------------------ 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #create our 3 child threads
    objThread = QtCore.QThread()
    serialThread = QtCore.QThread()
    imThread = QtCore.QThread()

    d = DirectoryPeriodCheck()
    d.moveToThread(objThread)
    objThread.started.connect(d.process)

    #----
    srmonitor = SerialMonitor()
    srmonitor.moveToThread(serialThread)
    serialThread.started.connect(srmonitor.monitor)
    
    im = ImageMovers(d)
    im.moveToThread(imThread)
    win = MW_bbTriggerBoxx(d, srmonitor, im)
    win._main()
    app.exec_()
