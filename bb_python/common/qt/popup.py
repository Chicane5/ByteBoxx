'''
Created on 17 Sep 2013

@author: ByteBoxx
'''

from PyQt4 import QtCore, QtGui

#===============================================================================
# 
#===============================================================================
class Popup(object):
    '''
    BB wrapper for QtMessageBox static methods
    '''
    @staticmethod
    def warning(pParent, pText):
        QtGui.QMessageBox.warning(pParent, "ByteBoxx Warning", QtCore.QString(pText))
        
    @staticmethod
    def critical(pParent, pText):
        QtGui.QMessageBox.critical(pParent, "ByteBoxx Critical", QtCore.QString(pText))

    @staticmethod
    def info(pParent, pText):
        QtGui.QMessageBox.information(pParent, "ByteBoxx Info", QtCore.QString(pText))
        
    @staticmethod
    def question(pParent, pText):
        QtGui.QMessageBox.question(pParent, "ByteBoxx Question", QtCore.QString(pText))
        
#===============================================================================
# 
#===============================================================================
class FileDialog(object):
    '''
    BB wrapper for QtMessageBox static methods
    '''
    @staticmethod
    def getDirectory(pParent, pText):
        return QtGui.QFileDialog.getExistingDirectory(pParent, QtCore.QString(pText))
    
    @staticmethod
    def getFile():
        pass
    
    @staticmethod
    def getFileFilter(self):
        pass
        
#===============================================================================
# 
#===============================================================================
class Input(object):
    '''
    BB wrapper for QtInputBox static methods
    '''
    @staticmethod
    def getText(pParent, pText):
        return QtGui.QInputDialog.getText(pParent, "ByteBoxx Input", QtCore.QString(pText))