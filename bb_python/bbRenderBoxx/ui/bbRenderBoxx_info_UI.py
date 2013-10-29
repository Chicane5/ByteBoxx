# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbRenderBoxx_info_UI.ui'
#
# Created: Tue Oct 29 00:12:39 2013
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

class Ui_Dialog_bbRenderBoxx_info(object):
    def setupUi(self, Dialog_bbRenderBoxx_info):
        Dialog_bbRenderBoxx_info.setObjectName(_fromUtf8("Dialog_bbRenderBoxx_info"))
        Dialog_bbRenderBoxx_info.resize(431, 272)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog_bbRenderBoxx_info)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(Dialog_bbRenderBoxx_info)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget_info = QtGui.QTableWidget(self.groupBox)
        self.tableWidget_info.setObjectName(_fromUtf8("tableWidget_info"))
        self.tableWidget_info.setColumnCount(0)
        self.tableWidget_info.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget_info)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(358, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_ok = QtGui.QPushButton(Dialog_bbRenderBoxx_info)
        self.pushButton_ok.setObjectName(_fromUtf8("pushButton_ok"))
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog_bbRenderBoxx_info)
        QtCore.QObject.connect(self.pushButton_ok, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog_bbRenderBoxx_info.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog_bbRenderBoxx_info)

    def retranslateUi(self, Dialog_bbRenderBoxx_info):
        Dialog_bbRenderBoxx_info.setWindowTitle(_translate("Dialog_bbRenderBoxx_info", "ByteBoxx::RENDERBOXX::info v1.01", None))
        self.groupBox.setTitle(_translate("Dialog_bbRenderBoxx_info", "Take Info", None))
        self.pushButton_ok.setText(_translate("Dialog_bbRenderBoxx_info", "OK", None))

