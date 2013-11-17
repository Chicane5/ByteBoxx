#ifndef BBSCANBOXX_PROTO_H
#define BBSCANBOXX_PROTO_H

#include <QtGui/QMainWindow>
#include "ui_bbscanboxx_proto.h"

class bbScanBoxx_proto : public QMainWindow
{
	Q_OBJECT

public:
	bbScanBoxx_proto(QWidget *parent = 0, Qt::WFlags flags = 0);
	~bbScanBoxx_proto();

private:
	Ui::bbScanBoxx_protoClass ui;
};

#endif // BBSCANBOXX_PROTO_H
