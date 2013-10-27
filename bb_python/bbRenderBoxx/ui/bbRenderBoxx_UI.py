# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbRenderBoxx_UI.ui'
#
# Created: Sun Oct 27 00:39:14 2013
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

class Ui_MainWindow_bbRenderBoxx(object):
    def setupUi(self, MainWindow_bbRenderBoxx):
        MainWindow_bbRenderBoxx.setObjectName(_fromUtf8("MainWindow_bbRenderBoxx"))
        MainWindow_bbRenderBoxx.resize(498, 381)
        self.centralwidget = QtGui.QWidget(MainWindow_bbRenderBoxx)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_session = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_session.setObjectName(_fromUtf8("lineEdit_session"))
        self.horizontalLayout_2.addWidget(self.lineEdit_session)
        self.pushButton_browse = QtGui.QPushButton(self.centralwidget)
        self.pushButton_browse.setObjectName(_fromUtf8("pushButton_browse"))
        self.horizontalLayout_2.addWidget(self.pushButton_browse)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeView_dataSets = QtGui.QTreeView(self.groupBox)
        self.treeView_dataSets.setObjectName(_fromUtf8("treeView_dataSets"))
        self.verticalLayout.addWidget(self.treeView_dataSets)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_genBatch = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_genBatch.setFont(font)
        self.pushButton_genBatch.setObjectName(_fromUtf8("pushButton_genBatch"))
        self.horizontalLayout.addWidget(self.pushButton_genBatch)
        spacerItem = QtGui.QSpacerItem(408, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow_bbRenderBoxx.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow_bbRenderBoxx)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow_bbRenderBoxx.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow_bbRenderBoxx)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow_bbRenderBoxx.setStatusBar(self.statusbar)
        self.label.setBuddy(self.lineEdit_session)

        self.retranslateUi(MainWindow_bbRenderBoxx)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_bbRenderBoxx)

    def retranslateUi(self, MainWindow_bbRenderBoxx):
        MainWindow_bbRenderBoxx.setWindowTitle(_translate("MainWindow_bbRenderBoxx", "ByteBoxx::RENDERBOXX v1.01", None))
        self.label.setText(_translate("MainWindow_bbRenderBoxx", "Root Session:", None))
        self.pushButton_browse.setText(_translate("MainWindow_bbRenderBoxx", "browse", None))
        self.groupBox.setTitle(_translate("MainWindow_bbRenderBoxx", "Session Data", None))
        self.pushButton_genBatch.setText(_translate("MainWindow_bbRenderBoxx", "Generate Batch...", None))

