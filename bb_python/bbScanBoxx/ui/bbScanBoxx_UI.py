# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbScanBoxx_UI.ui'
#
# Created: Tue Sep 10 01:20:52 2013
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

class Ui_MainWindow_bbScanBoxx(object):
    def setupUi(self, MainWindow_bbScanBoxx):
        MainWindow_bbScanBoxx.setObjectName(_fromUtf8("MainWindow_bbScanBoxx"))
        MainWindow_bbScanBoxx.resize(616, 348)
        self.centralwidget = QtGui.QWidget(MainWindow_bbScanBoxx)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 581, 291))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_project = QtGui.QWidget()
        self.tab_project.setObjectName(_fromUtf8("tab_project"))
        self.label = QtGui.QLabel(self.tab_project)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.tab_project)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(140, 20, 391, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.radioButton = QtGui.QRadioButton(self.tab_project)
        self.radioButton.setEnabled(False)
        self.radioButton.setGeometry(QtCore.QRect(70, 50, 61, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.tab_project)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 50, 51, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_project)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 50, 391, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.treeWidget = QtGui.QTreeWidget(self.tab_project)
        self.treeWidget.setEnabled(False)
        self.treeWidget.setGeometry(QtCore.QRect(10, 110, 531, 141))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.line = QtGui.QFrame(self.tab_project)
        self.line.setGeometry(QtCore.QRect(10, 90, 531, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.tabWidget.addTab(self.tab_project, _fromUtf8(""))
        self.tab_control = QtGui.QWidget()
        self.tab_control.setObjectName(_fromUtf8("tab_control"))
        self.tabWidget.addTab(self.tab_control, _fromUtf8(""))
        self.tab_post = QtGui.QWidget()
        self.tab_post.setObjectName(_fromUtf8("tab_post"))
        self.tabWidget.addTab(self.tab_post, _fromUtf8(""))
        MainWindow_bbScanBoxx.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow_bbScanBoxx)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 616, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuNew_Project = QtGui.QMenu(self.menuFile)
        self.menuNew_Project.setObjectName(_fromUtf8("menuNew_Project"))
        self.menuSmartShooter = QtGui.QMenu(self.menuFile)
        self.menuSmartShooter.setObjectName(_fromUtf8("menuSmartShooter"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuOpenComms = QtGui.QMenu(self.menubar)
        self.menuOpenComms.setObjectName(_fromUtf8("menuOpenComms"))
        MainWindow_bbScanBoxx.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow_bbScanBoxx)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow_bbScanBoxx.setStatusBar(self.statusbar)
        self.actionMesh = QtGui.QAction(MainWindow_bbScanBoxx)
        self.actionMesh.setObjectName(_fromUtf8("actionMesh"))
        self.actionTexture = QtGui.QAction(MainWindow_bbScanBoxx)
        self.actionTexture.setObjectName(_fromUtf8("actionTexture"))
        self.actionConfigure = QtGui.QAction(MainWindow_bbScanBoxx)
        self.actionConfigure.setObjectName(_fromUtf8("actionConfigure"))
        self.actionCOM1 = QtGui.QAction(MainWindow_bbScanBoxx)
        self.actionCOM1.setObjectName(_fromUtf8("actionCOM1"))
        self.menuNew_Project.addAction(self.actionMesh)
        self.menuNew_Project.addAction(self.actionTexture)
        self.menuSmartShooter.addAction(self.actionConfigure)
        self.menuFile.addAction(self.menuNew_Project.menuAction())
        self.menuFile.addAction(self.menuSmartShooter.menuAction())
        self.menuOpenComms.addAction(self.actionCOM1)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOpenComms.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow_bbScanBoxx)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_bbScanBoxx)

    def retranslateUi(self, MainWindow_bbScanBoxx):
        MainWindow_bbScanBoxx.setWindowTitle(_translate("MainWindow_bbScanBoxx", "ByteBoxx::SCANBOXX v1.01", None))
        self.label.setText(_translate("MainWindow_bbScanBoxx", "SmartShooter Download:", None))
        self.radioButton.setText(_translate("MainWindow_bbScanBoxx", "Texture", None))
        self.radioButton_2.setText(_translate("MainWindow_bbScanBoxx", "Mesh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_project), _translate("MainWindow_bbScanBoxx", "Project Setup", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_control), _translate("MainWindow_bbScanBoxx", "Rig Control", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_post), _translate("MainWindow_bbScanBoxx", "Post Process", None))
        self.menuFile.setTitle(_translate("MainWindow_bbScanBoxx", "File", None))
        self.menuNew_Project.setTitle(_translate("MainWindow_bbScanBoxx", "New Project", None))
        self.menuSmartShooter.setTitle(_translate("MainWindow_bbScanBoxx", "SmartShooter", None))
        self.menuAbout.setTitle(_translate("MainWindow_bbScanBoxx", "About", None))
        self.menuOpenComms.setTitle(_translate("MainWindow_bbScanBoxx", "OpenComms", None))
        self.actionMesh.setText(_translate("MainWindow_bbScanBoxx", "Mesh", None))
        self.actionTexture.setText(_translate("MainWindow_bbScanBoxx", "Texture", None))
        self.actionConfigure.setText(_translate("MainWindow_bbScanBoxx", "Configure", None))
        self.actionCOM1.setText(_translate("MainWindow_bbScanBoxx", "COM1", None))

