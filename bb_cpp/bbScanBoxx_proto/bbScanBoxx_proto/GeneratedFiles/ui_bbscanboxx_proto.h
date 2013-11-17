/********************************************************************************
** Form generated from reading UI file 'bbscanboxx_proto.ui'
**
** Created: Sun 17. Nov 01:12:32 2013
**      by: Qt User Interface Compiler version 4.7.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_BBSCANBOXX_PROTO_H
#define UI_BBSCANBOXX_PROTO_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QHeaderView>
#include <QtGui/QMainWindow>
#include <QtGui/QMenuBar>
#include <QtGui/QStatusBar>
#include <QtGui/QToolBar>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_bbScanBoxx_protoClass
{
public:
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QWidget *centralWidget;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *bbScanBoxx_protoClass)
    {
        if (bbScanBoxx_protoClass->objectName().isEmpty())
            bbScanBoxx_protoClass->setObjectName(QString::fromUtf8("bbScanBoxx_protoClass"));
        bbScanBoxx_protoClass->resize(600, 400);
        menuBar = new QMenuBar(bbScanBoxx_protoClass);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        bbScanBoxx_protoClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(bbScanBoxx_protoClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        bbScanBoxx_protoClass->addToolBar(mainToolBar);
        centralWidget = new QWidget(bbScanBoxx_protoClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        bbScanBoxx_protoClass->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(bbScanBoxx_protoClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        bbScanBoxx_protoClass->setStatusBar(statusBar);

        retranslateUi(bbScanBoxx_protoClass);

        QMetaObject::connectSlotsByName(bbScanBoxx_protoClass);
    } // setupUi

    void retranslateUi(QMainWindow *bbScanBoxx_protoClass)
    {
        bbScanBoxx_protoClass->setWindowTitle(QApplication::translate("bbScanBoxx_protoClass", "bbScanBoxx_proto", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class bbScanBoxx_protoClass: public Ui_bbScanBoxx_protoClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_BBSCANBOXX_PROTO_H
