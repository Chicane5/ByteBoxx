# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbTriggerBoxx_config_UI.ui'
#
# Created: Fri Sep 20 17:00:10 2013
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog_bbTriggerBoxx_config(object):
    def setupUi(self, Dialog_bbTriggerBoxx_config):
        Dialog_bbTriggerBoxx_config.setObjectName(_fromUtf8("Dialog_bbTriggerBoxx_config"))
        Dialog_bbTriggerBoxx_config.resize(464, 113)
        Dialog_bbTriggerBoxx_config.setWindowTitle(QtGui.QApplication.translate("Dialog_bbTriggerBoxx_config", "ByteBoxx::TRIGGERBOXX::config v1.01", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(Dialog_bbTriggerBoxx_config)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Dialog_bbTriggerBoxx_config)
        self.label.setText(QtGui.QApplication.translate("Dialog_bbTriggerBoxx_config", "Photo Download:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_photoDownload = QtGui.QLineEdit(Dialog_bbTriggerBoxx_config)
        self.lineEdit_photoDownload.setObjectName(_fromUtf8("lineEdit_photoDownload"))
        self.horizontalLayout.addWidget(self.lineEdit_photoDownload)
        self.pushButton_browse = QtGui.QPushButton(Dialog_bbTriggerBoxx_config)
        self.pushButton_browse.setText(QtGui.QApplication.translate("Dialog_bbTriggerBoxx_config", "browse", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_browse.setObjectName(_fromUtf8("pushButton_browse"))
        self.horizontalLayout.addWidget(self.pushButton_browse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkBox_jpg = QtGui.QCheckBox(Dialog_bbTriggerBoxx_config)
        self.checkBox_jpg.setText(QtGui.QApplication.translate("Dialog_bbTriggerBoxx_config", "jpg", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_jpg.setObjectName(_fromUtf8("checkBox_jpg"))
        self.horizontalLayout_2.addWidget(self.checkBox_jpg)
        self.checkBox_cr2 = QtGui.QCheckBox(Dialog_bbTriggerBoxx_config)
        self.checkBox_cr2.setText(QtGui.QApplication.translate("Dialog_bbTriggerBoxx_config", "cr2", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_cr2.setObjectName(_fromUtf8("checkBox_cr2"))
        self.horizontalLayout_2.addWidget(self.checkBox_cr2)
        spacerItem = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_7 = QtGui.QLabel(Dialog_bbTriggerBoxx_config)
        self.label_7.setText(QtGui.QApplication.translate("Dialog_bbTriggerBoxx_config", "Focus (s):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.doubleSpinBox_focus = QtGui.QDoubleSpinBox(Dialog_bbTriggerBoxx_config)
        self.doubleSpinBox_focus.setFrame(True)
        self.doubleSpinBox_focus.setSingleStep(0.25)
        self.doubleSpinBox_focus.setObjectName(_fromUtf8("doubleSpinBox_focus"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_focus)
        spacerItem1 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_8 = QtGui.QLabel(Dialog_bbTriggerBoxx_config)
        self.label_8.setText(QtGui.QApplication.translate("Dialog_bbTriggerBoxx_config", "Flash (ms):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_2.addWidget(self.label_8)
        self.doubleSpinBox_flash = QtGui.QDoubleSpinBox(Dialog_bbTriggerBoxx_config)
        self.doubleSpinBox_flash.setFrame(True)
        self.doubleSpinBox_flash.setSingleStep(0.5)
        self.doubleSpinBox_flash.setObjectName(_fromUtf8("doubleSpinBox_flash"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_flash)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_save = QtGui.QPushButton(Dialog_bbTriggerBoxx_config)
        self.pushButton_save.setMinimumSize(QtCore.QSize(0, 32))
        self.pushButton_save.setText(QtGui.QApplication.translate("Dialog_bbTriggerBoxx_config", "Save to File", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.horizontalLayout_3.addWidget(self.pushButton_save)
        self.pushButton_cancel = QtGui.QPushButton(Dialog_bbTriggerBoxx_config)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(0, 32))
        self.pushButton_cancel.setText(QtGui.QApplication.translate("Dialog_bbTriggerBoxx_config", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label.setBuddy(self.lineEdit_photoDownload)
        self.label_7.setBuddy(self.doubleSpinBox_focus)
        self.label_8.setBuddy(self.doubleSpinBox_flash)

        self.retranslateUi(Dialog_bbTriggerBoxx_config)
        QtCore.QMetaObject.connectSlotsByName(Dialog_bbTriggerBoxx_config)

    def retranslateUi(self, Dialog_bbTriggerBoxx_config):
        pass

