#include "bbscanboxx_proto.h"
#include <QtGui/QApplication>

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	bbScanBoxx_proto w;
	w.show();
	return a.exec();
}
