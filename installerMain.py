import os
import shutil
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class InstallerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('InstallerUI.ui', self)
        QMainWindow.setGeometry(self, 600, 400, 520, 110)
        QMainWindow.setFixedSize(self, 520, 110)
        self.ok.clicked.connect(self.next)
        self.cancel.clicked.connect(self.kill)

    def next(self):
        self.way = self.wayinstall.text()
        self.hide
        os.startfile('installerP.bat')
        try:
            shutil.copytree('SDPES', self.way + '\\SDPES')
        except BaseException:
            print('ERROR')
        self.l = open('C:/Users/' + os.environ.get("USERNAME") + '/Desktop/SDPES_Launcher.txt', 'w')
        self.l.write('@echo off\ncd ' + self.way + '\\SDPES' + '\nstart pythonw ' + self.way + '\\SDPES\\MainWindow.py')
        self.l.close()
        os.rename('C:/Users/' + os.environ.get("USERNAME") + '/Desktop/SDPES_Launcher.txt', 'C:/Users/' + os.environ.get("USERNAME") + '/Desktop/SDPES_Launcher.bat')

    def kill(self):
        self.hide()


def main():
    app = QApplication(sys.argv)
    ex = InstallerWindow()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()                                          # ММММ ОАОАОАОАОАОАОАО
