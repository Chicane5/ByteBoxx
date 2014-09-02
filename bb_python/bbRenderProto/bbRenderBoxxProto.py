import sys, os

from PyQt4 import QtCore, QtGui
from ui import bbRenderBoxx_Proto_UI as Proto_UI
from qt import popup


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
        self.connect(self.pushButton_browseIn, QtCore.SIGNAL("clicked()"), self._browseIn)
        #self.connect(self.comboBox_preset, QtCore.SIGNAL("clicked()"), self._browse)
        self.connect(self.pushButton_browseOut, QtCore.SIGNAL("clicked()"), self._browseOut)
        self.connect(self.pushButton_doit, QtCore.SIGNAL("clicked()"), self._render)
        
        
    def _main(self):
        self.show()
        
    def _browseIn(self):
        lFile = popup.FileDialog.getFileFilter(self, "pick a file to render", '*.fbx')
        if lFile:
            print lFile
            self.mInFile = str(lFile[0])
            self.lineEdit_file.setText(lFile[0])
            
    def _browseOut(self):
        lDir = popup.FileDialog.getDirectory(self, "pick output directory")
        if lDir:
            self.mOutDir = lDir

    def _render(self):
        os.system("mayapy {0} {1} {2}".format(MW_bbRenderBoxxProto.cMAYA_BATCHRENDER_FILE, self.mInFile, self.mOutDir))
    
        
        
#------------------------------------------------------------------------------ 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = MW_bbRenderBoxxProto()
    win._main()
    app.exec_()
    