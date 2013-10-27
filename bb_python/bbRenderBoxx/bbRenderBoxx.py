'''
Created on 26 Oct 2013

@author: ByteBoxx
'''
#builtins
import sys, os
#3rd
from PyQt4 import QtCore, QtGui
#user
from ui import bbRenderBoxx_UI as uifile
from ui import bbRenderBoxx_queue_UI as queueuifile
from qt import popup
from smartshooter.session import Session

#globals

#===============================================================================
# 
#===============================================================================
class DL_bbRenderBoxxQueue(QtGui.QDialog, queueuifile.Ui_Dialog_bbRenderBoxx_queue):
    def __init__(self, parent=None):
        super(DL_bbRenderBoxxQueue, self).__init__(parent)
        self.setupUi(self)
        
        #connections
        
        
    def _main(self):
        self.show()






#===============================================================================
# 
#===============================================================================
class MW_bbRenderBoxx(QtGui.QMainWindow, uifile.Ui_MainWindow_bbRenderBoxx):
    def __init__(self, parent=None):
        super(MW_bbRenderBoxx, self).__init__(parent)
        self.setupUi(self)
        
        styleFile=os.path.join(os.path.dirname(os.path.split(__file__)[0]),"common//qt", "DarkOrangeQStyleTemplate.txt")
        with open(styleFile,"r") as fh:
            self.setStyleSheet(fh.read())
                       
        #connections
        self.connect(self.pushButton_browse, QtCore.SIGNAL("clicked()"), self.GetSessionRoot)
        self.connect(self.pushButton_genBatch, QtCore.SIGNAL("clicked()"), self.GenerateBatch)
        
        #attrs
        self.mRootPath = ""
        self.mQueueDialog = DL_bbRenderBoxxQueue(self)
        
    def _main(self):
        self.show()
        
    def GetSessionRoot(self):
        lSessionFolder = popup.FileDialog.getDirectory(self, "Pick Dataset Session Root")
        if lSessionFolder:
            self.mRootPath = os.path.abspath(str(lSessionFolder))
            self.lineEdit_session.setText(lSessionFolder)
            
        self.PopulateTreeView()
        
    def PopulateTreeView(self):
        self.model = QtGui.QFileSystemModel(self.treeView_dataSets)
        self.model.setReadOnly(True)
        
        root = self.model.setRootPath(self.mRootPath)
        self.treeView_dataSets.setModel(self.model)
        self.treeView_dataSets.setRootIndex(root)
        
    def GenerateBatch(self):
        indexItem = self.treeView_dataSets.currentIndex()

        fileName = self.model.fileName(indexItem)
        print fileName
        #self.mQueueDialog._main()
        
#------------------------------------------------------------------------------ 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = MW_bbRenderBoxx()
    win._main()
    app.exec_()