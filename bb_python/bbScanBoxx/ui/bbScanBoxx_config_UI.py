# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbScanBoxx_config_UI.ui'
#
# Created: Wed Sep 18 00:32:34 2013
#      by: PyQt4 UI code generator 4.10
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

class Ui_Dialog_bbScanBoxx_config(object):
    def setupUi(self, Dialog_bbScanBoxx_config):
        Dialog_bbScanBoxx_config.setObjectName(_fromUtf8("Dialog_bbScanBoxx_config"))
        Dialog_bbScanBoxx_config.resize(464, 123)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog_bbScanBoxx_config)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Dialog_bbScanBoxx_config)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_photoDownload = QtGui.QLineEdit(Dialog_bbScanBoxx_config)
        self.lineEdit_photoDownload.setObjectName(_fromUtf8("lineEdit_photoDownload"))
        self.horizontalLayout.addWidget(self.lineEdit_photoDownload)
        self.pushButton_browse = QtGui.QPushButton(Dialog_bbScanBoxx_config)
        self.pushButton_browse.setObjectName(_fromUtf8("pushButton_browse"))
        self.horizontalLayout.addWidget(self.pushButton_browse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBox_mirror = QtGui.QCheckBox(Dialog_bbScanBoxx_config)
        self.checkBox_mirror.setObjectName(_fromUtf8("checkBox_mirror"))
        self.gridLayout.addWidget(self.checkBox_mirror, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(Dialog_bbScanBoxx_config)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.doubleSpinBox_focus = QtGui.QDoubleSpinBox(Dialog_bbScanBoxx_config)
        self.doubleSpinBox_focus.setFrame(True)
        self.doubleSpinBox_focus.setSingleStep(0.25)
        self.doubleSpinBox_focus.setObjectName(_fromUtf8("doubleSpinBox_focus"))
        self.gridLayout.addWidget(self.doubleSpinBox_focus, 0, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.label_8 = QtGui.QLabel(Dialog_bbScanBoxx_config)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 0, 5, 1, 1)
        self.doubleSpinBox_flash = QtGui.QDoubleSpinBox(Dialog_bbScanBoxx_config)
        self.doubleSpinBox_flash.setFrame(True)
        self.doubleSpinBox_flash.setSingleStep(0.5)
        self.doubleSpinBox_flash.setObjectName(_fromUtf8("doubleSpinBox_flash"))
        self.gridLayout.addWidget(self.doubleSpinBox_flash, 0, 6, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 7, 1, 1)
        self.pushButton_save = QtGui.QPushButton(Dialog_bbScanBoxx_config)
        self.pushButton_save.setMinimumSize(QtCore.QSize(0, 32))
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.gridLayout.addWidget(self.pushButton_save, 1, 0, 1, 4)
        self.pushButton_cancel = QtGui.QPushButton(Dialog_bbScanBoxx_config)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(0, 32))
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.gridLayout.addWidget(self.pushButton_cancel, 1, 4, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label.setBuddy(self.lineEdit_photoDownload)
        self.label_7.setBuddy(self.doubleSpinBox_focus)
        self.label_8.setBuddy(self.doubleSpinBox_flash)

        self.retranslateUi(Dialog_bbScanBoxx_config)
        QtCore.QMetaObject.connectSlotsByName(Dialog_bbScanBoxx_config)

    def retranslateUi(self, Dialog_bbScanBoxx_config):
        Dialog_bbScanBoxx_config.setWindowTitle(_translate("Dialog_bbScanBoxx_config", "ByteBoxx::SCANBOXX::config", None))
        self.label.setText(_translate("Dialog_bbScanBoxx_config", "Photo Download:", None))
        self.pushButton_browse.setText(_translate("Dialog_bbScanBoxx_config", "browse", None))
        self.checkBox_mirror.setText(_translate("Dialog_bbScanBoxx_config", "Mirror Lock?", None))
        self.label_7.setText(_translate("Dialog_bbScanBoxx_config", "Focus Comp (s):", None))
        self.label_8.setText(_translate("Dialog_bbScanBoxx_config", "Flash Delay (ms):", None))
        self.pushButton_save.setText(_translate("Dialog_bbScanBoxx_config", "Save to File", None))
        self.pushButton_cancel.setText(_translate("Dialog_bbScanBoxx_config", "Cancel", None))

