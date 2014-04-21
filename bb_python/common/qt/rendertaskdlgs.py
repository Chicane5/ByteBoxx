'''
Created on 21 Apr 2014

@author: ByteBoxx
'''

from PyQt4 import QtCore, QtGui
import bbRenderBox_paramsMask_UI as automaskUI
import bbRenderBox_paramsAlign_UI as alignUI

#===============================================================================
# 
#===============================================================================
class DL_AutoMask_Params(QtGui.QDialog, automaskUI.Ui_Dialog_bbRenderBox_Params_Mask):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        super(DL_AutoMask_Params, self).__init__(parent)
        self.setupUi(self)
        
    def _main(self):
        self.show()
        
#===============================================================================
# 
#===============================================================================
class DL_Align_Params(QtGui.QDialog, alignUI.Ui_Dialog_bbRenderBox_Params_Align):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        super(DL_Align_Params, self).__init__(parent)
        self.setupUi(self)
        
    def _main(self):
        self.show()