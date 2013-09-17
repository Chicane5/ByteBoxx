'''
Created on 17 Sep 2013

@author: ByteBoxx
'''

from PyQt4 import QtCore, QtGui

class Warning():
    '''
    BB wrapper for QtMessageBox.warning
    '''
    @staticmethod
    def show(pParent, pText):
        QtGui.QMessageBox.warning(pParent, "ByteBoxx Warning", QtCore.QString(pText))
        
#------------------------------------------------------------------------------ 

class Critical(QtGui.QMessageBox):
    '''
    BB wrapper for QtMessageBox.critical
    '''
    @staticmethod
    def show(pParent, pText):
        QtGui.QMessageBox.critical(pParent, "ByteBoxx Critical", QtCore.QString(pText))
        
#------------------------------------------------------------------------------ 

class Info(QtGui.QMessageBox):
    '''
    BB wrapper for QtMessageBox.information
    '''
    @staticmethod
    def show(pParent, pText):
        QtGui.QMessageBox.information(pParent, "ByteBoxx Info", QtCore.QString(pText))
        
#------------------------------------------------------------------------------ 

class Question(QtGui.QMessageBox):
    '''
    BB wrapper for QtMessageBox.question
    '''
    @staticmethod
    def show(pParent, pText):
        QtGui.QMessageBox.question(pParent, "ByteBoxx Question", QtCore.QString(pText))
