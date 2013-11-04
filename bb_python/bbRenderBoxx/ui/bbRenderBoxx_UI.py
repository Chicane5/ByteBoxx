# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbRenderBoxx_UI.ui'
#
# Created: Sun Nov 03 18:17:32 2013
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
        MainWindow_bbRenderBoxx.resize(637, 548)
        self.centralwidget = QtGui.QWidget(MainWindow_bbRenderBoxx)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
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
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeView_dataSets = QtGui.QTreeView(self.groupBox)
        self.treeView_dataSets.setMinimumSize(QtCore.QSize(0, 0))
        self.treeView_dataSets.setObjectName(_fromUtf8("treeView_dataSets"))
        self.verticalLayout.addWidget(self.treeView_dataSets)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_queue = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_queue.sizePolicy().hasHeightForWidth())
        self.groupBox_queue.setSizePolicy(sizePolicy)
        self.groupBox_queue.setMaximumSize(QtCore.QSize(16777215, 160))
        self.groupBox_queue.setObjectName(_fromUtf8("groupBox_queue"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_queue)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.listWidget_queue = QtGui.QListWidget(self.groupBox_queue)
        self.listWidget_queue.setObjectName(_fromUtf8("listWidget_queue"))
        self.verticalLayout_2.addWidget(self.listWidget_queue)
        self.verticalLayout_3.addWidget(self.groupBox_queue)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_addQueue = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_addQueue.setFont(font)
        self.pushButton_addQueue.setObjectName(_fromUtf8("pushButton_addQueue"))
        self.horizontalLayout.addWidget(self.pushButton_addQueue)
        self.pushButton_remQueue = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_remQueue.setFont(font)
        self.pushButton_remQueue.setObjectName(_fromUtf8("pushButton_remQueue"))
        self.horizontalLayout.addWidget(self.pushButton_remQueue)
        self.pushButton_info = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_info.setFont(font)
        self.pushButton_info.setObjectName(_fromUtf8("pushButton_info"))
        self.horizontalLayout.addWidget(self.pushButton_info)
        self.pushButton_genBatch = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_genBatch.setFont(font)
        self.pushButton_genBatch.setObjectName(_fromUtf8("pushButton_genBatch"))
        self.horizontalLayout.addWidget(self.pushButton_genBatch)
        self.label_logo = QtGui.QLabel(self.centralwidget)
        self.label_logo.setText(_fromUtf8(""))
        self.label_logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/bbRenderBoxx_logo.jpg")))
        self.label_logo.setScaledContents(False)
        self.label_logo.setObjectName(_fromUtf8("label_logo"))
        self.horizontalLayout.addWidget(self.label_logo)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow_bbRenderBoxx.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow_bbRenderBoxx)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuResource = QtGui.QMenu(self.menubar)
        self.menuResource.setObjectName(_fromUtf8("menuResource"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow_bbRenderBoxx.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow_bbRenderBoxx)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow_bbRenderBoxx.setStatusBar(self.statusbar)
        self.actionNew_Resource_File = QtGui.QAction(MainWindow_bbRenderBoxx)
        self.actionNew_Resource_File.setObjectName(_fromUtf8("actionNew_Resource_File"))
        self.actionLoad_Resource_File = QtGui.QAction(MainWindow_bbRenderBoxx)
        self.actionLoad_Resource_File.setObjectName(_fromUtf8("actionLoad_Resource_File"))
        self.actionRenderBoxx = QtGui.QAction(MainWindow_bbRenderBoxx)
        self.actionRenderBoxx.setObjectName(_fromUtf8("actionRenderBoxx"))
        self.menuResource.addAction(self.actionNew_Resource_File)
        self.menuResource.addAction(self.actionLoad_Resource_File)
        self.menuAbout.addAction(self.actionRenderBoxx)
        self.menubar.addAction(self.menuResource.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.label.setBuddy(self.lineEdit_session)

        self.retranslateUi(MainWindow_bbRenderBoxx)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_bbRenderBoxx)

    def retranslateUi(self, MainWindow_bbRenderBoxx):
        MainWindow_bbRenderBoxx.setWindowTitle(_translate("MainWindow_bbRenderBoxx", "ByteBoxx::RENDERBOXX v1.01", None))
        self.label.setText(_translate("MainWindow_bbRenderBoxx", "Root Session:", None))
        self.pushButton_browse.setText(_translate("MainWindow_bbRenderBoxx", "browse", None))
        self.groupBox.setTitle(_translate("MainWindow_bbRenderBoxx", "Session Data", None))
        self.groupBox_queue.setTitle(_translate("MainWindow_bbRenderBoxx", "Active Queue", None))
        self.pushButton_addQueue.setText(_translate("MainWindow_bbRenderBoxx", "-> Queue", None))
        self.pushButton_remQueue.setText(_translate("MainWindow_bbRenderBoxx", "<- Queue", None))
        self.pushButton_info.setText(_translate("MainWindow_bbRenderBoxx", "More Info", None))
        self.pushButton_genBatch.setText(_translate("MainWindow_bbRenderBoxx", "Generate Batch...", None))
        self.menuResource.setTitle(_translate("MainWindow_bbRenderBoxx", "Resource", None))
        self.menuHelp.setTitle(_translate("MainWindow_bbRenderBoxx", "Help", None))
        self.menuAbout.setTitle(_translate("MainWindow_bbRenderBoxx", "About", None))
        self.actionNew_Resource_File.setText(_translate("MainWindow_bbRenderBoxx", "New Resource File", None))
        self.actionLoad_Resource_File.setText(_translate("MainWindow_bbRenderBoxx", "Load Resource File", None))
        self.actionRenderBoxx.setText(_translate("MainWindow_bbRenderBoxx", "RenderBoxx", None))

import bbRenderBoxx_QRC_rc
