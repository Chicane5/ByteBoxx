# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbRenderBoxx_Proto_UI.ui'
#
# Created: Tue Sep 02 17:34:19 2014
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

class Ui_MainWindow_RenderBoxx(object):
    def setupUi(self, MainWindow_RenderBoxx):
        MainWindow_RenderBoxx.setObjectName(_fromUtf8("MainWindow_RenderBoxx"))
        MainWindow_RenderBoxx.resize(667, 200)
        self.centralwidget = QtGui.QWidget(MainWindow_RenderBoxx)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 621, 83))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(88, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.lineEdit_file = QtGui.QLineEdit(self.widget)
        self.lineEdit_file.setObjectName(_fromUtf8("lineEdit_file"))
        self.gridLayout.addWidget(self.lineEdit_file, 0, 2, 1, 2)
        self.pushButton_browseIn = QtGui.QPushButton(self.widget)
        self.pushButton_browseIn.setObjectName(_fromUtf8("pushButton_browseIn"))
        self.gridLayout.addWidget(self.pushButton_browseIn, 0, 4, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.checkBox_useMaya = QtGui.QCheckBox(self.widget)
        self.checkBox_useMaya.setChecked(True)
        self.checkBox_useMaya.setObjectName(_fromUtf8("checkBox_useMaya"))
        self.gridLayout.addWidget(self.checkBox_useMaya, 1, 1, 1, 2)
        self.lineEdit_fileLighting = QtGui.QLineEdit(self.widget)
        self.lineEdit_fileLighting.setObjectName(_fromUtf8("lineEdit_fileLighting"))
        self.gridLayout.addWidget(self.lineEdit_fileLighting, 1, 3, 1, 1)
        self.pushButton_browseLight = QtGui.QPushButton(self.widget)
        self.pushButton_browseLight.setObjectName(_fromUtf8("pushButton_browseLight"))
        self.gridLayout.addWidget(self.pushButton_browseLight, 1, 4, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(88, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.lineEdit_outputdir = QtGui.QLineEdit(self.widget)
        self.lineEdit_outputdir.setObjectName(_fromUtf8("lineEdit_outputdir"))
        self.gridLayout.addWidget(self.lineEdit_outputdir, 2, 3, 1, 1)
        self.pushButton_browseOut = QtGui.QPushButton(self.widget)
        self.pushButton_browseOut.setObjectName(_fromUtf8("pushButton_browseOut"))
        self.gridLayout.addWidget(self.pushButton_browseOut, 2, 4, 1, 1)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 104, 604, 51))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget1)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBox_preset = QtGui.QComboBox(self.widget1)
        self.comboBox_preset.setObjectName(_fromUtf8("comboBox_preset"))
        self.comboBox_preset.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_preset, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(378, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 2)
        self.label_3 = QtGui.QLabel(self.widget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_annotation = QtGui.QLineEdit(self.widget1)
        self.lineEdit_annotation.setObjectName(_fromUtf8("lineEdit_annotation"))
        self.gridLayout_2.addWidget(self.lineEdit_annotation, 1, 1, 1, 1)
        self.pushButton_doit = QtGui.QPushButton(self.widget1)
        self.pushButton_doit.setObjectName(_fromUtf8("pushButton_doit"))
        self.gridLayout_2.addWidget(self.pushButton_doit, 1, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(268, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 3, 1, 1)
        MainWindow_RenderBoxx.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow_RenderBoxx)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow_RenderBoxx.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow_RenderBoxx)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow_RenderBoxx.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_RenderBoxx)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_RenderBoxx)

    def retranslateUi(self, MainWindow_RenderBoxx):
        MainWindow_RenderBoxx.setWindowTitle(_translate("MainWindow_RenderBoxx", "RenderBoxx_Proto", None))
        self.label.setText(_translate("MainWindow_RenderBoxx", "File To Render", None))
        self.pushButton_browseIn.setText(_translate("MainWindow_RenderBoxx", ">> Browse", None))
        self.label_5.setText(_translate("MainWindow_RenderBoxx", "Template Lighting", None))
        self.checkBox_useMaya.setText(_translate("MainWindow_RenderBoxx", "Use as base Maya", None))
        self.pushButton_browseLight.setText(_translate("MainWindow_RenderBoxx", ">> Browse", None))
        self.label_4.setText(_translate("MainWindow_RenderBoxx", "Output Directory", None))
        self.pushButton_browseOut.setText(_translate("MainWindow_RenderBoxx", ">> Browse", None))
        self.label_2.setText(_translate("MainWindow_RenderBoxx", "Preset", None))
        self.comboBox_preset.setItemText(0, _translate("MainWindow_RenderBoxx", "BodyScan", None))
        self.label_3.setText(_translate("MainWindow_RenderBoxx", "PDF Annotation:", None))
        self.pushButton_doit.setText(_translate("MainWindow_RenderBoxx", "** D O  I T **", None))

