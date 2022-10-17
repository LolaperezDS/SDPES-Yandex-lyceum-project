import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QFileDialog, QLabel
import os
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon


class Ui_Error(object):
    def setupUi(self, eror):
        eror.setObjectName("eror")
        eror.resize(370, 158)
        eror.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.ok = QtWidgets.QPushButton(eror)
        self.ok.setGeometry(QtCore.QRect(160, 130, 51, 21))
        self.ok.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ok.setObjectName("ok")
        self.errtext = QtWidgets.QLabel(eror)
        self.errtext.setGeometry(QtCore.QRect(10, 10, 351, 111))
        self.errtext.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.errtext.setObjectName("errtext")

        self.retranslateUi(eror)
        QtCore.QMetaObject.connectSlotsByName(eror)

    def retranslateUi(self, eror):
        _translate = QtCore.QCoreApplication.translate
        eror.setWindowTitle(_translate("eror", "Error"))
        self.ok.setText(_translate("eror", "ok"))
        self.errtext.setText(_translate("eror", "<html><head/><body><p><br/></p></body></html>"))


class Ui_Choose_Picture(object):
    def setupUi(self, Choose_Picture):
        Choose_Picture.setObjectName("Choose_Picture")
        Choose_Picture.resize(229, 78)
        Choose_Picture.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.choose = QtWidgets.QPushButton(Choose_Picture)
        self.choose.setGeometry(QtCore.QRect(120, 30, 93, 28))
        self.choose.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.choose.setObjectName("choose")
        self.cancel = QtWidgets.QPushButton(Choose_Picture)
        self.cancel.setGeometry(QtCore.QRect(10, 30, 93, 28))
        self.cancel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cancel.setObjectName("cancel")

        self.retranslateUi(Choose_Picture)
        QtCore.QMetaObject.connectSlotsByName(Choose_Picture)

    def retranslateUi(self, Choose_Picture):
        _translate = QtCore.QCoreApplication.translate
        Choose_Picture.setWindowTitle(_translate("Choose_Picture", "Form"))
        self.choose.setText(_translate("Choose_Picture", "choose file"))
        self.cancel.setText(_translate("Choose_Picture", "cancel"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 300)
        # MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.AddButton.setStyleSheet("border-color: rgb(0, 255, 255);\n"
                                     "background-color: rgb(255, 255, 255);")
        self.AddButton.setObjectName("AddButton")
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(10, 50, 71, 31))
        self.DeleteButton.setStyleSheet("border-color: rgb(0, 255, 255);\n"
                                        "background-color: rgb(255, 255, 255);")
        self.DeleteButton.setObjectName("DeleteButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 0, 3, 61))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(90, 60, 3, 61))
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(90, 120, 3, 61))
        self.line_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(90, 180, 3, 61))
        self.line_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(90, 360, 3, 61))
        self.line_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(90, 240, 3, 61))
        self.line_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(90, 300, 3, 61))
        self.line_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(90, 420, 3, 61))
        self.line_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 435, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AddButton.setText(_translate("MainWindow", "add"))
        self.DeleteButton.setText(_translate("MainWindow", "delete"))


class Ui_Add_Button(object):
    def setupUi(self, Browser):
        Browser.setObjectName("Browser")
        Browser.resize(329, 279)
        Browser.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Browser)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 311, 181))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.further = QtWidgets.QPushButton(self.centralwidget)
        self.further.setGeometry(QtCore.QRect(210, 200, 111, 31))
        self.further.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.further.setObjectName("further")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(10, 200, 51, 31))
        self.cancel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cancel.setObjectName("cancel")
        Browser.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Browser)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 329, 21))
        self.menubar.setObjectName("menubar")
        Browser.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Browser)
        self.statusbar.setObjectName("statusbar")
        Browser.setStatusBar(self.statusbar)

        self.retranslateUi(Browser)
        QtCore.QMetaObject.connectSlotsByName(Browser)

    def retranslateUi(self, Browser):
        _translate = QtCore.QCoreApplication.translate
        Browser.setWindowTitle(_translate("Browser", "Browser"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Browser", "выберите папку для просмотра"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.further.setText(_translate("Browser", "change dir"))
        self.cancel.setText(_translate("Browser", "cancel"))


class Ui_Delete_Button(object):
    def setupUi(self, Delete_Button):
        Delete_Button.setObjectName("Delete_Button")
        Delete_Button.resize(400, 300)
        Delete_Button.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.retranslateUi(Delete_Button)
        QtCore.QMetaObject.connectSlotsByName(Delete_Button)

    def retranslateUi(self, Delete_Button):
        _translate = QtCore.QCoreApplication.translate
        Delete_Button.setWindowTitle(_translate("Delete_Button", "Deleting"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.set_background()
        self.setupUi(self)
        self.AddButton.clicked.connect(self.addbutton)
        self.DeleteButton.clicked.connect(self.delbutton)
        QMainWindow.setGeometry(self, 600, 400, 500, 300)
        QMainWindow.setFixedSize(self, 500, 300)  # запрет изменения размера виджета
        self.x_btns, self.y_btns = 100, 10  # начало рабочих кнопок(координаты)
        self.x_btns_end = 400  # 'y' будет до бесконечности
        self.t = False
        self.setWindowTitle('SDPES')

    def delbutton(self):
        self.diDel = DelBtnWidget()  # открываю диалоговое окно с удалением
        self.diDel.setbtndel()
        self.hide()
        self.diDel.show()

    def set_background(self):
        try:  # если картинки нет, ставит чёрный экран
            file = open('pic.jpg')
            file.close()
        except IOError as e:
            self.setStyleSheet('background-color: rgb(0,0,0);')
        else:
            oImage = QImage("pic.jpg")
            sImage = oImage.scaled(500, 300)
            palette = QPalette()
            palette.setBrush(QPalette.Window, QBrush(sImage))
            self.setPalette(palette)

    def addbutton(self):
        self.diAdd = AddBtnWidget()  # открываю диалоговое окно с вводом пути
        self.diAdd.show()

    def addBackground(self):
        self.diAddB = Background()
        self.diAddB.show()

    def setbtn(self):        # код установки кнопок
        if self.t:
            os.execl(sys.executable, sys.executable, *sys.argv)     # перезапуск программы для обновления кнопок
        else:                                                                                 # .    ^^^
            self.t = True                        # триггер для закрывания окна(чтоб в 1 запуск кода это не срабатывало)
        self.listbtn = open('btns.txt')
        k = 0
        self.b = []
        for c in self.listbtn:
            s = c.split("/")[-1].split('.')[0]  # неразбитая строка
            ret = ''  # разбитая строка ( в будущем )
            for j in range(len(s) // 12):
                ret += s[j * 12:(j + 1) * 12] + '\n'
            ret += s[len(s) // 12 * 12:]
            self.b.append(c.split("/")[-1].split('.')[0])  # выделяю имя кнопки из пути
            self.b[k] = QPushButton(ret, self)
            self.b[k].resize(90, 90)
            self.b[k].move(100 + (k % 4) * 100, 10 + (k // 4) * 100)
            self.b[k].setStyleSheet('QPushButton {background-color: #ffffff;}')
            self.b[k].clicked.connect(self.run)
            self.b[k].setObjectName(c)
            k += 1
        self.listbtn.close()

    def run(self):
        try:
            file = open(self.sender().objectName()[:-1])
        except IOError as e:
            self.err = Error()
            self.err.show()
            self.err.errortext('  введите действительный путь\n  (файл не найден)')
        else:
            os.startfile(self.sender().objectName()[:-1])

    def keyPressEvent(self, event):
        if int(event.modifiers()) == Qt.ControlModifier:
            if event.key() == Qt.Key_N:
                self.addbutton()
            elif event.key() == Qt.Key_D:
                self.delbutton()
            elif event.key() == Qt.Key_S:
                self.addBackground()


class AddBtnWidget(QMainWindow, Ui_Add_Button):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cancel.clicked.connect(self.kill)
        self.further.clicked.connect(self.browse_folder)
        self.string = None
        self.setWindowTitle('Добавить кнопку')

    def browse_folder(self):
        self.listWidget.clear()  # На случай, если в списке уже есть элементы
        self.directory = QFileDialog.getExistingDirectory(self, "Выберите папку с исполняемым файлом")
        self.listWidget.itemSelectionChanged.connect(self.prntfile)

        if self.directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            for file_name in os.listdir(self.directory):  # для каждого файла в директории
                if len(file_name[1:].split('.')) == 1:
                    file_name = file_name + '.dir'
                self.listWidget.addItem(file_name)
        # print(self.string)
        return self.string

    def prntfile(self):
        for i in self.listWidget.selectedItems():
            item = i
            self.hide()
            if item.text().split('.')[-1] != 'dir':
                self.string = self.directory + '/' + item.text()
                self.listbtn = open('btns.txt', 'a')
                self.listbtn.write(self.string + '\n')  # записываю путь в текст
                self.listbtn.close()
                ex.setbtn()  # после добавления обновить расположение
                self.hide()
            else:
                pass

    def kill(self):
        self.hide()


class DelBtnWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('deletebtn.ui', self)
        QMainWindow.setGeometry(self, 600, 400, 410, 300)
        QMainWindow.setFixedSize(self, 410, 300)

    def delbtn(self, number):
        self.listbtn = open('btns.txt')
        btn_list = []
        for c in self.listbtn:
            btn_list.append(c)  # получил список всех путей кнопок
        del btn_list[number - 1]  # удаление элемента
        self.listbtn.close()
        self.listbtn = open('btns.txt', 'w')
        for c in btn_list:
            self.listbtn.write(c)  # записываю данные обратно без удалённого элемента
        self.listbtn.close()
        ex.setbtn()  # после удаления обновить расположение кнопок
        self.hide()

    def setbtndel(self):
        self.listbtn = open('btns.txt')
        k = 0
        self.b = []
        for c in self.listbtn:
            s = c.split("/")[-1].split('.')[0]   # неразбитая строка
            ret = ''                             # разбитая строка ( в будущем )
            for j in range(len(s) // 12):
                ret += s[j * 12:(j + 1) * 12] + '\n'
            ret += s[len(s) // 12 * 12:]
            self.b.append(c.split("/")[-1].split('.')[0])       # выделяю имя кнопки из пути
            self.b[k] = QPushButton(ret, self)
            self.b[k].resize(90, 90)
            self.b[k].move(10 + (k % 4) * 100, 10 + (k // 4) * 100)
            self.b[k].setStyleSheet('QPushButton {background-color: #ff0000;}')
            self.b[k].clicked.connect(self.run)
            self.b[k].setObjectName(c)
            k += 1
        self.listbtn.close()

    def run(self):
        k = 0
        self.listbtn = open('btns.txt')
        for c in self.listbtn:
            k += 1
            if c == self.sender().objectName():
                self.delbtn(k)
        self.listbtn.close()


class Background(QMainWindow, Ui_Choose_Picture):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cancel.clicked.connect(self.kill)
        self.choose.clicked.connect(self.browse_folder)
        self.setWindowTitle('Добавить background')

    def browse_folder(self):
        self.directory, _ = QFileDialog.getOpenFileName(self, "Выберите фото")
        try:
            file = open('pic.jpg')
            file.close()
        except IOError as e:
            pass
        else:
            os.remove('pic.jpg')
        image = Image.open(self.directory)
        resized_image = image.resize((500, 300))
        resized_image.save('pic.jpg')
        ex.set_background()
        ex.setbtn()
        self.hide()

    def kill(self):
        self.hide()




    def run(self):
        k = 0
        self.listbtn = open('btns.txt')
        for c in self.listbtn:
            k += 1
            if c == self.sender().objectName():
                self.delbtn(k)
        self.listbtn.close()


class Error(QMainWindow, Ui_Error):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ok.clicked.connect(self.kill)

    def errortext(self, s):
        self.errtext.setText('  ERROR!!!\n' + s)

    def kill(self):
        self.hide()


if __name__ == '__main__':
    try:                             # если текстового файла с путями нет, создаёт этот файл
        file = open('btns.txt')
    except IOError as e:
        f = open('btns.txt', 'w')
        f.close()
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.setbtn()
    ex.show()
    sys.exit(app.exec())
