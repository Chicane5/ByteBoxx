# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbRenderBox_paramsAlign_UI.ui'
#
# Created: Tue Apr 22 00:09:57 2014
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

class Ui_Dialog_bbRenderBox_Params_Align(object):
    def setupUi(self, Dialog_bbRenderBox_Params_Align):
        Dialog_bbRenderBox_Params_Align.setObjectName(_fromUtf8("Dialog_bbRenderBox_Params_Align"))
        Dialog_bbRenderBox_Params_Align.resize(400, 175)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_bbRenderBox_Params_Align.sizePolicy().hasHeightForWidth())
        Dialog_bbRenderBox_Params_Align.setSizePolicy(sizePolicy)
        Dialog_bbRenderBox_Params_Align.setMaximumSize(QtCore.QSize(16777215, 175))
        self.verticalLayout = QtGui.QVBoxLayout(Dialog_bbRenderBox_Params_Align)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog_bbRenderBox_Params_Align)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_accuracy = QtGui.QComboBox(self.groupBox)
        self.comboBox_accuracy.setObjectName(_fromUtf8("comboBox_accuracy"))
        self.comboBox_accuracy.addItem(_fromUtf8(""))
        self.comboBox_accuracy.addItem(_fromUtf8(""))
        self.comboBox_accuracy.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_accuracy, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_pairps = QtGui.QComboBox(self.groupBox)
        self.comboBox_pairps.setObjectName(_fromUtf8("comboBox_pairps"))
        self.comboBox_pairps.addItem(_fromUtf8(""))
        self.comboBox_pairps.addItem(_fromUtf8(""))
        self.comboBox_pairps.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_pairps, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.spinBox_pointlimit = QtGui.QSpinBox(self.groupBox)
        self.spinBox_pointlimit.setMinimum(50)
        self.spinBox_pointlimit.setMaximum(10000000)
        self.spinBox_pointlimit.setProperty("value", 40000)
        self.spinBox_pointlimit.setObjectName(_fromUtf8("spinBox_pointlimit"))
        self.gridLayout.addWidget(self.spinBox_pointlimit, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.comboBox_consbymask = QtGui.QComboBox(self.groupBox)
        self.comboBox_consbymask.setObjectName(_fromUtf8("comboBox_consbymask"))
        self.comboBox_consbymask.addItem(_fromUtf8(""))
        self.comboBox_consbymask.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_consbymask, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Dialog_bbRenderBox_Params_Align)
        QtCore.QMetaObject.connectSlotsByName(Dialog_bbRenderBox_Params_Align)

    def retranslateUi(self, Dialog_bbRenderBox_Params_Align):
        Dialog_bbRenderBox_Params_Align.setWindowTitle(_translate("Dialog_bbRenderBox_Params_Align", "Align Parameters", None))
        self.groupBox.setTitle(_translate("Dialog_bbRenderBox_Params_Align", "parameters", None))
        self.label.setText(_translate("Dialog_bbRenderBox_Params_Align", "Accuracy:", None))
        self.comboBox_accuracy.setItemText(0, _translate("Dialog_bbRenderBox_Params_Align", "low", None))
        self.comboBox_accuracy.setItemText(1, _translate("Dialog_bbRenderBox_Params_Align", "medium", None))
        self.comboBox_accuracy.setItemText(2, _translate("Dialog_bbRenderBox_Params_Align", "high", None))
        self.label_2.setText(_translate("Dialog_bbRenderBox_Params_Align", "PairPreselect:", None))
        self.comboBox_pairps.setItemText(0, _translate("Dialog_bbRenderBox_Params_Align", "disabled", None))
        self.comboBox_pairps.setItemText(1, _translate("Dialog_bbRenderBox_Params_Align", "generic", None))
        self.comboBox_pairps.setItemText(2, _translate("Dialog_bbRenderBox_Params_Align", "ground control", None))
        self.label_3.setText(_translate("Dialog_bbRenderBox_Params_Align", "Point Limit:", None))
        self.label_4.setText(_translate("Dialog_bbRenderBox_Params_Align", "Constrint Features By Mask:", None))
        self.comboBox_consbymask.setItemText(0, _translate("Dialog_bbRenderBox_Params_Align", "no", None))
        self.comboBox_consbymask.setItemText(1, _translate("Dialog_bbRenderBox_Params_Align", "yes", None))

