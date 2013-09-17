'''
Created on 10 Sep 2013

@author: ByteBoxx
'''
#builtins
import sys, os
import datetime as date
#3rd
from PyQt4 import QtCore, QtGui
#user
from ui import bbScanBoxx_UI as uifile
from ui import bbScanBoxx_config_UI as configuifile
from qt import popup
from smartshooter.session import Session

#globals
gCONFIG_VAR = 'SCANBOXX_CONFIG'
gCONFIG_FILE = 'scanboxx_defaults.txt'

#===============================================================================
# 
#===============================================================================
class DL_bbScanBoxxConfig(QtGui.QDialog, configuifile.Ui_Dialog_bbScanBoxx_config):
    def __init__(self, parent=None):
        super(DL_bbScanBoxxConfig, self).__init__(parent)
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
                fh.writelines("mirror " + str(self.checkBox_mirror.checkState()) + '\n')
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
class MW_bbScanBoxx(QtGui.QMainWindow, uifile.Ui_MainWindow_bbScanBoxx):
    def __init__(self, parent=None):
        super(MW_bbScanBoxx, self).__init__(parent)
        self.setupUi(self)
        
        styleFile=os.path.join(os.path.dirname(os.path.split(__file__)[0]),"common//qt", "DarkOrangeQStyleTemplate.txt")
        with open(styleFile,"r") as fh:
            self.setStyleSheet(fh.read())
            
        #connections
        self.connect(self.actionMesh, QtCore.SIGNAL("triggered()"), self.newSession)
        self.connect(self.actionTexture, QtCore.SIGNAL("triggered()"), self.newSession)
        
    def _main(self):
        self.show()
        
        #load a config file
        self.checkConfig()

    def checkConfig(self):
        if not os.environ.get(gCONFIG_VAR):
            popup.Popup.critical(self, "No $SCANBOXX_CONFIG variable set\nPlease set and retry")
            self.close()
        else:
            #try to load a preset
            try:
                with open(os.path.join(os.environ.get(gCONFIG_VAR),gCONFIG_FILE), "r") as lFile:
                    lLines = lFile.readlines()
                    self.populateDefaults(lLines)                            
            except IOError:
                popup.Popup.warning(self, "Couldn't find a default config file\nOK to create one now")
                lConfigurator = DL_bbScanBoxxConfig(self)
                lConfigurator._main()
                
    def populateDefaults(self, pLines):
        for line in pLines:
            if line.startswith('photodir'):
                lSplit = line.split(' ')
                self.lineEdit_photoDownload.setText(lSplit[1].rstrip())
                self.lineEdit_photoDownload.setReadOnly(True)
            elif line.startswith('mirror'):
                lSplit = line.split(' ')
                self.checkBox_mirror.setCheckState(QtCore.Qt.CheckState(lSplit[1].rstrip()))
            elif line.startswith('focus'):
                lSplit = line.split(' ')
                self.doubleSpinBox_focus.setValue(float(lSplit[1].rstrip()))
            elif line.startswith('flash'):
                lSplit = line.split(' ')
                self.doubleSpinBox_flash.setValue(float(lSplit[1].rstrip()))
            
    def newSession(self):
        self.mSession = Session(str(self.sender().objectName()).lstrip('action'), str(self.lineEdit_photoDownload.text()))
        if self.mSession.mType == 'Mesh':
            self.radioButton_mesh.setChecked(True)
        elif self.mSession.mType == 'Texture':
            self.radioButton_texture.setChecked(True)
            
        #switch off
        self.radioButton_mesh.setEnabled(False)
        self.radioButton_texture.setEnabled(False)
        
        #create the root dir
        lToday = date.datetime.today()
        lShootFolder = os.path.join(self.mSession.mRootFolder, lToday.strftime('%Y%m%d') + '_' + self.mSession.mType)
        try:
            os.makedirs(lShootFolder)
        except:
            popup.Popup.warning(self, "Error creating shootday directory, check permission")
        
#------------------------------------------------------------------------------ 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = MW_bbScanBoxx()
    win._main()
    app.exec_()

