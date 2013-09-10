'''
Created on 10 Sep 2013

@author: ByteBoxx
'''
#builtins
import sys, os
#3rd
from PyQt4 import QtCore, QtGui
#user
from ui import bbScanBoxx_UI as uifile

#globals


class MW_bbScanBoxx(QtGui.QMainWindow, uifile.Ui_MainWindow_bbScanBoxx):
    def __init__(self, parent=None):
        super(MW_bbScanBoxx, self).__init__(parent)
        self.setupUi(self)
        
        styleFile=os.path.join(os.path.dirname(os.path.split(__file__)[0]),"common//qt", "DarkOrangeQStyleTemplate.txt")
        with open(styleFile,"r") as fh:
            self.setStyleSheet(fh.read())
            
        
        
    def _main(self):
        self.show()
        
    def loadConfig(self):
        '''
        try and load a smartshooter config from disk
        '''
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = MW_bbScanBoxx()
    win._main()
    app.exec_()

