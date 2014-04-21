# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbRenderBox_paramsMask_UI.ui'
#
# Created: Mon Apr 21 23:15:51 2014
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

class Ui_Dialog_bbRenderBox_Params_Mask(object):
    def setupUi(self, Dialog_bbRenderBox_Params_Mask):
        Dialog_bbRenderBox_Params_Mask.setObjectName(_fromUtf8("Dialog_bbRenderBox_Params_Mask"))
        Dialog_bbRenderBox_Params_Mask.resize(400, 175)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_bbRenderBox_Params_Mask.sizePolicy().hasHeightForWidth())
        Dialog_bbRenderBox_Params_Mask.setSizePolicy(sizePolicy)
        Dialog_bbRenderBox_Params_Mask.setMaximumSize(QtCore.QSize(16777215, 175))
        self.verticalLayout = QtGui.QVBoxLayout(Dialog_bbRenderBox_Params_Mask)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog_bbRenderBox_Params_Mask)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_maskPath = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_maskPath.setObjectName(_fromUtf8("lineEdit_maskPath"))
        self.gridLayout.addWidget(self.lineEdit_maskPath, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBox_blur = QtGui.QSpinBox(self.groupBox)
        self.spinBox_blur.setMaximum(10000)
        self.spinBox_blur.setProperty("value", 10)
        self.spinBox_blur.setObjectName(_fromUtf8("spinBox_blur"))
        self.gridLayout.addWidget(self.spinBox_blur, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(243, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.spinBox_threshold = QtGui.QSpinBox(self.groupBox)
        self.spinBox_threshold.setMaximum(10000)
        self.spinBox_threshold.setProperty("value", 75)
        self.spinBox_threshold.setObjectName(_fromUtf8("spinBox_threshold"))
        self.gridLayout.addWidget(self.spinBox_threshold, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(243, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.spinBox_gapfill = QtGui.QSpinBox(self.groupBox)
        self.spinBox_gapfill.setMaximum(10000)
        self.spinBox_gapfill.setProperty("value", 25)
        self.spinBox_gapfill.setObjectName(_fromUtf8("spinBox_gapfill"))
        self.gridLayout.addWidget(self.spinBox_gapfill, 3, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(243, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Dialog_bbRenderBox_Params_Mask)
        QtCore.QMetaObject.connectSlotsByName(Dialog_bbRenderBox_Params_Mask)

    def retranslateUi(self, Dialog_bbRenderBox_Params_Mask):
        Dialog_bbRenderBox_Params_Mask.setWindowTitle(_translate("Dialog_bbRenderBox_Params_Mask", "Automask Parameters", None))
        self.groupBox.setTitle(_translate("Dialog_bbRenderBox_Params_Mask", "parameters", None))
        self.label.setText(_translate("Dialog_bbRenderBox_Params_Mask", "Mask Path:", None))
        self.label_2.setText(_translate("Dialog_bbRenderBox_Params_Mask", "Blur:", None))
        self.label_3.setText(_translate("Dialog_bbRenderBox_Params_Mask", "Threshold:", None))
        self.label_4.setText(_translate("Dialog_bbRenderBox_Params_Mask", "Gapfill:", None))

