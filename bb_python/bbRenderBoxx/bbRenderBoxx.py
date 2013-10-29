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
from ui import bbRenderBoxx_info_UI as infouifile
from qt import popup
from smartshooter.session import MeshTake

#globals

#===============================================================================
# 
#===============================================================================
class DL_bbRenderBoxxQueue(QtGui.QDialog, queueuifile.Ui_Dialog_bbRenderBoxx_queue):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        super(DL_bbRenderBoxxQueue, self).__init__(parent)
        self.setupUi(self)
        
        #connections
        
        
    def _main(self):
        self.show()


#===============================================================================
# 
#===============================================================================
class DL_bbRenderBoxxInfo(QtGui.QDialog, infouifile.Ui_Dialog_bbRenderBoxx_info):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        super(DL_bbRenderBoxxInfo, self).__init__(parent)
        self.setupUi(self)
        
    def _main(self):
        self.show()
        



#===============================================================================
# 
#===============================================================================
class MW_bbRenderBoxx(QtGui.QMainWindow, uifile.Ui_MainWindow_bbRenderBoxx):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        super(MW_bbRenderBoxx, self).__init__(parent)
        self.setupUi(self)
        
        styleFile=os.path.join(os.path.dirname(os.path.split(__file__)[0]),"common//qt", "DarkOrangeQStyleTemplate.txt")
        with open(styleFile,"r") as fh:
            self.setStyleSheet(fh.read())
                       
        #connections
        self.connect(self.pushButton_browse, QtCore.SIGNAL("clicked()"), self.GetSessionRoot)
        self.connect(self.pushButton_genBatch, QtCore.SIGNAL("clicked()"), self.GenerateBatch)
        self.connect(self.pushButton_addQueue, QtCore.SIGNAL("clicked()"), self.AddQueue)
        self.connect(self.pushButton_remQueue, QtCore.SIGNAL("clicked()"), self.RemQueue)
        self.connect(self.pushButton_info, QtCore.SIGNAL("clicked()"), self.MoreInfo)
        
        #attrs
        self.mRootPath = ""
        self.mQueueDialog = DL_bbRenderBoxxQueue(self)
        self.mProcessQueue = {}
        
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
        
    def AddQueue(self):
        #have they even populated the treeview at this point?
        try:
            assert 'model' in self.__dict__
        except AssertionError:
            popup.Popup.warning(self, "Pick a session root directory first!")
            return
        
        #get the path from the tree view and ensure they are only trying to add take objects
        lPath = self.ResolveTreeIndex()
        if not os.path.basename(str(lPath)).startswith('tk'):
            popup.Popup.warning(self, "Only take objects can be added to the process queue!")
            return
            
        lProcTake = MeshTake(lPath)
        lProcTake.BindXML() #check for XML and bind it
        #save the take in the dict, reference it by path name
        if not lPath in self.mProcessQueue.keys():
            self.mProcessQueue[lPath] = lProcTake
            self.listWidget_queue.addItem(lPath)
        else:
            popup.Popup.info(self, "This take is already in your queue!")
            del(lProcTake)
            
    def RemQueue(self):
        #grab the text of the current selection in the queue list and pop it from the dict
        lPath = self.listWidget_queue.currentItem().text()
        self.mProcessQueue.pop(lPath)
        self.listWidget_queue.takeItem(self.listWidget_queue.currentRow())

    def ResolveTreeIndex(self):
        indexItem = self.treeView_dataSets.currentIndex()
        return self.model.filePath(indexItem)
    
    def MoreInfo(self):
        #parse the associated take XML to glean more info about the take
        lPath = self.listWidget_queue.currentItem().text()
        lXML = self.mProcessQueue[lPath].mXML
        if not lXML:
            popup.Popup.info(self, "This take has no bound XML info!")
            return
        
        lInfoDlg = DL_bbRenderBoxxInfo(self)
        lInfoDlg._main()
        
        
        
    def GenerateBatch(self):
        if not self.mProcessQueue:
            popup.Popup.warning(self, "There's nothing in your queue to process!")
            return
        self.mQueueDialog._main()
        
#------------------------------------------------------------------------------ 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = MW_bbRenderBoxx()
    win._main()
    app.exec_()