import sys, os

from PyQt4 import QtCore, QtGui
from ui import bbRenderBoxx_Proto_UI as Proto_UI
from qt import popup

#===============================================================================
# 
#===============================================================================
class RenderTake(object):
    
    cFILE_FORMAT = '.fbx'
    
    def __init__(self, pInFile, pOutDir):
        self.mInFile = pInFile
        self.mOutDir = str(pOutDir)
        self.mOutPath = None
        self._buildOutPutPath()
        
    def _buildOutPutPath(self):
        self.mOutPath = os.path.join(self.mOutDir, os.path.basename(self.mInFile.split(RenderTake.cFILE_FORMAT)[0]))
        
        
    
#===============================================================================
# 
#===============================================================================
class MW_bbRenderBoxxProto(QtGui.QMainWindow, Proto_UI.Ui_MainWindow_RenderBoxx):
    '''
    classdocs
    '''
    cROW_HEIGHT = 38
    cLINE_EDIT_MIN_WIDTH = 35
    
    #are we frozen?
    if hasattr(sys, "frozen") or hasattr(sys, "importers"):
        cMAYA_BATCHRENDER_FILE = os.path.join(os.path.dirname(sys.executable), 'scripts', 'batchrender.py')
    else:
        cMAYA_BATCHRENDER_FILE = os.path.join(os.path.dirname(__file__), 'scripts', 'batchrender.py')
    
    def __init__(self,parent=None):
        super(MW_bbRenderBoxxProto, self).__init__(parent)
        self.setupUi(self)
        
        #connections
        #self.connect(self.pushButton_browseIn, QtCore.SIGNAL("clicked()"), self._browseIn)
        #self.connect(self.comboBox_preset, QtCore.SIGNAL("clicked()"), self._browse)
        self.connect(self.pushButton_add, QtCore.SIGNAL("clicked()"), self._add)
        self.connect(self.pushButton_remove, QtCore.SIGNAL("clicked()"), self._remove)
        self.connect(self.pushButton_browseLight, QtCore.SIGNAL("clicked()"), self._browseLight)
        self.connect(self.pushButton_browseOut, QtCore.SIGNAL("clicked()"), self._browseOut)
        self.connect(self.pushButton_doit, QtCore.SIGNAL("clicked()"), self._render)
        
        self.mLightFile = None
        self.mOutDir = None
        self.mRootPath = "C:\\Users"
        self.mQueue = {}
        
        
    def _main(self):
        self.show()
        self.model = QtGui.QFileSystemModel(self.treeView_diskmap)
        self.model.setReadOnly(True)
        root = self.model.setRootPath(self.mRootPath)
        self.treeView_diskmap.setModel(self.model)
        self.treeView_diskmap.setRootIndex(root)
        
    def _add(self):
        if not self.mOutDir:
            popup.Popup.critical(self, "set an output directory first!")
            return
        
        lItem = str(self.model.filePath(self.treeView_diskmap.currentIndex()))
        root, ext = os.path.splitext(lItem)
        if not ext == RenderTake.cFILE_FORMAT:
            popup.Popup.warning(self, "Format Incompatible!")
        else:
            t = RenderTake(lItem, self.mOutDir)
            self.listWidget_queue.addItem(lItem)
            self.mQueue[lItem] = t
    
    def _remove(self):
        pass
        
    def _browseLight(self):
        lFile = popup.FileDialog.getFileFilter(self, "pick a file to render", '*.mb')
        if lFile:
            self.mLightFile = str(lFile[0])
            self.lineEdit_fileLighting.setText(lFile[0])
            
    def _browseOut(self):
        lDir = popup.FileDialog.getDirectory(self, "pick output directory")
        if lDir:
            self.mOutDir = lDir
            self.lineEdit_outputdir.setText(lDir)

    def _render(self):
        for lProcessFile in self.mQueue.values():
            if os.path.isfile(lProcessFile.mInFile) and os.path.splitext(os.path.basename(lProcessFile.mInFile))[1] == '.fbx':
                if not self.mLightFile or not self.checkBox_useMaya.isChecked():
                    #script, in, out, base?
                    os.system("mayapy {0} {1} {2}".format(MW_bbRenderBoxxProto.cMAYA_BATCHRENDER_FILE, lProcessFile.mInFile, lProcessFile.mOutPath))
                elif self.mLightFile and self.checkBox_useMaya.isChecked():
                    os.system("mayapy {0} {1} {2} {3}".format(MW_bbRenderBoxxProto.cMAYA_BATCHRENDER_FILE, lProcessFile.mInFile, lProcessFile.mOutPath, self.mLightFile))
    
        
        
#------------------------------------------------------------------------------ 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = MW_bbRenderBoxxProto()
    win._main()
    app.exec_()
    