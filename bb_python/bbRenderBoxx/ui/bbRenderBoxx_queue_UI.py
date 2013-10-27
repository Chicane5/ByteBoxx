# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbRenderBoxx_queue_UI.ui'
#
# Created: Sun Oct 27 00:22:04 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog_bbRenderBoxx_queue(object):
    def setupUi(self, Dialog_bbRenderBoxx_queue):
        Dialog_bbRenderBoxx_queue.setObjectName(_fromUtf8("Dialog_bbRenderBoxx_queue"))
        Dialog_bbRenderBoxx_queue.resize(606, 528)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog_bbRenderBoxx_queue)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_queue = QtGui.QGroupBox(Dialog_bbRenderBoxx_queue)
        self.groupBox_queue.setObjectName(_fromUtf8("groupBox_queue"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_queue)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget_queue = QtGui.QTableWidget(self.groupBox_queue)
        self.tableWidget_queue.setObjectName(_fromUtf8("tableWidget_queue"))
        self.tableWidget_queue.setColumnCount(0)
        self.tableWidget_queue.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget_queue)
        self.verticalLayout_3.addWidget(self.groupBox_queue)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_moveUp = QtGui.QPushButton(Dialog_bbRenderBoxx_queue)
        self.pushButton_moveUp.setObjectName(_fromUtf8("pushButton_moveUp"))
        self.horizontalLayout.addWidget(self.pushButton_moveUp)
        self.pushButton_moveDown = QtGui.QPushButton(Dialog_bbRenderBoxx_queue)
        self.pushButton_moveDown.setObjectName(_fromUtf8("pushButton_moveDown"))
        self.horizontalLayout.addWidget(self.pushButton_moveDown)
        self.pushButton = QtGui.QPushButton(Dialog_bbRenderBoxx_queue)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(228, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.groupBox_logging = QtGui.QGroupBox(Dialog_bbRenderBoxx_queue)
        self.groupBox_logging.setObjectName(_fromUtf8("groupBox_logging"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_logging)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textEdit_logging = QtGui.QTextEdit(self.groupBox_logging)
        self.textEdit_logging.setObjectName(_fromUtf8("textEdit_logging"))
        self.verticalLayout_2.addWidget(self.textEdit_logging)
        self.verticalLayout_3.addWidget(self.groupBox_logging)

        self.retranslateUi(Dialog_bbRenderBoxx_queue)
        QtCore.QMetaObject.connectSlotsByName(Dialog_bbRenderBoxx_queue)

    def retranslateUi(self, Dialog_bbRenderBoxx_queue):
        Dialog_bbRenderBoxx_queue.setWindowTitle(_translate("Dialog_bbRenderBoxx_queue", "ByteBoxx:RENDERBOXX::queue v1.01", None))
        self.groupBox_queue.setTitle(_translate("Dialog_bbRenderBoxx_queue", "Active Queue", None))
        self.pushButton_moveUp.setText(_translate("Dialog_bbRenderBoxx_queue", "Move Up", None))
        self.pushButton_moveDown.setText(_translate("Dialog_bbRenderBoxx_queue", "Move Down", None))
        self.pushButton.setText(_translate("Dialog_bbRenderBoxx_queue", "Render Queue", None))
        self.groupBox_logging.setTitle(_translate("Dialog_bbRenderBoxx_queue", "GroupBox", None))

