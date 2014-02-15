# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbRenderBoxx_queue_UI.ui'
#
# Created: Thu Jan 02 03:27:29 2014
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
        Dialog_bbRenderBoxx_queue.resize(652, 549)
        self.verticalLayout_6 = QtGui.QVBoxLayout(Dialog_bbRenderBoxx_queue)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.tabWidget = QtGui.QTabWidget(Dialog_bbRenderBoxx_queue)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_queue = QtGui.QWidget()
        self.tab_queue.setObjectName(_fromUtf8("tab_queue"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_queue)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.tab_queue)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget_queue = QtGui.QTableWidget(self.groupBox)
        self.tableWidget_queue.setObjectName(_fromUtf8("tableWidget_queue"))
        self.tableWidget_queue.setColumnCount(0)
        self.tableWidget_queue.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget_queue)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_queue, _fromUtf8(""))
        self.tab_res = QtGui.QWidget()
        self.tab_res.setObjectName(_fromUtf8("tab_res"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_res)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_res)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tableWidget_res = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidget_res.setObjectName(_fromUtf8("tableWidget_res"))
        self.tableWidget_res.setColumnCount(0)
        self.tableWidget_res.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget_res)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab_res, _fromUtf8(""))
        self.verticalLayout_6.addWidget(self.tabWidget)
        self.frame = QtGui.QFrame(Dialog_bbRenderBoxx_queue)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_moveUp = QtGui.QPushButton(self.frame)
        self.pushButton_moveUp.setObjectName(_fromUtf8("pushButton_moveUp"))
        self.horizontalLayout.addWidget(self.pushButton_moveUp)
        self.pushButton_moveDown = QtGui.QPushButton(self.frame)
        self.pushButton_moveDown.setObjectName(_fromUtf8("pushButton_moveDown"))
        self.horizontalLayout.addWidget(self.pushButton_moveDown)
        self.pushButton_addCmd = QtGui.QPushButton(self.frame)
        self.pushButton_addCmd.setObjectName(_fromUtf8("pushButton_addCmd"))
        self.horizontalLayout.addWidget(self.pushButton_addCmd)
        self.pushButton = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.checkBox_notifyTask = QtGui.QCheckBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_notifyTask.sizePolicy().hasHeightForWidth())
        self.checkBox_notifyTask.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.checkBox_notifyTask.setFont(font)
        self.checkBox_notifyTask.setObjectName(_fromUtf8("checkBox_notifyTask"))
        self.horizontalLayout.addWidget(self.checkBox_notifyTask)
        self.checkBox_notifyJob = QtGui.QCheckBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_notifyJob.sizePolicy().hasHeightForWidth())
        self.checkBox_notifyJob.setSizePolicy(sizePolicy)
        self.checkBox_notifyJob.setChecked(True)
        self.checkBox_notifyJob.setTristate(False)
        self.checkBox_notifyJob.setObjectName(_fromUtf8("checkBox_notifyJob"))
        self.horizontalLayout.addWidget(self.checkBox_notifyJob)
        self.verticalLayout_6.addWidget(self.frame)
        self.groupBox_logging = QtGui.QGroupBox(Dialog_bbRenderBoxx_queue)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_logging.sizePolicy().hasHeightForWidth())
        self.groupBox_logging.setSizePolicy(sizePolicy)
        self.groupBox_logging.setMinimumSize(QtCore.QSize(0, 136))
        self.groupBox_logging.setMaximumSize(QtCore.QSize(16777215, 136))
        self.groupBox_logging.setObjectName(_fromUtf8("groupBox_logging"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_logging)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textEdit_logging = QtGui.QTextEdit(self.groupBox_logging)
        self.textEdit_logging.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit_logging.setReadOnly(True)
        self.textEdit_logging.setObjectName(_fromUtf8("textEdit_logging"))
        self.verticalLayout_2.addWidget(self.textEdit_logging)
        self.verticalLayout_6.addWidget(self.groupBox_logging)

        self.retranslateUi(Dialog_bbRenderBoxx_queue)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_bbRenderBoxx_queue)

    def retranslateUi(self, Dialog_bbRenderBoxx_queue):
        Dialog_bbRenderBoxx_queue.setWindowTitle(_translate("Dialog_bbRenderBoxx_queue", "ByteBoxx:RENDERBOXX::queue v1.01", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_queue), _translate("Dialog_bbRenderBoxx_queue", "Queue", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_res), _translate("Dialog_bbRenderBoxx_queue", "Resources", None))
        self.pushButton_moveUp.setText(_translate("Dialog_bbRenderBoxx_queue", "Move Up", None))
        self.pushButton_moveDown.setText(_translate("Dialog_bbRenderBoxx_queue", "Move Down", None))
        self.pushButton_addCmd.setText(_translate("Dialog_bbRenderBoxx_queue", "Add Cmd Task", None))
        self.pushButton.setText(_translate("Dialog_bbRenderBoxx_queue", "Render Queue", None))
        self.checkBox_notifyTask.setText(_translate("Dialog_bbRenderBoxx_queue", "Notify on Task", None))
        self.checkBox_notifyJob.setText(_translate("Dialog_bbRenderBoxx_queue", "Notify on Job", None))
        self.groupBox_logging.setTitle(_translate("Dialog_bbRenderBoxx_queue", "Logging", None))

