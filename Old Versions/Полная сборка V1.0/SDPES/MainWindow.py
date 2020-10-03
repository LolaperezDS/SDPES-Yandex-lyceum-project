import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QFileDialog
import os


class MainWindow(QMainWindow):  # банально... нет смысла объяснять, думаю
    def __init__(self):
        super().__init__()
        uic.loadUi('Main.ui', self)  # в проэкте используем относительные пути файлов ВСЕГДА
        self.AddButton.clicked.connect(self.addbutton)
        self.DeleteButton.clicked.connect(self.delbutton)
        QMainWindow.setGeometry(self, 600, 400, 500, 300)
        QMainWindow.setFixedSize(self, 500, 300)     # запрет изменения размера виджета
        self.x_btns, self.y_btns = 100, 10  # начало рабочих кнопок(координаты)
        self.x_btns_end = 400   # 'y' будет до бесконечности
        self.t = False

    def delbutton(self):
        self.diDel = DelBtnWidget()  # открываю диалоговое окно с удалением
        self.diDel.setbtndel()
        self.hide()
        self.diDel.show()

    def addbutton(self):
        self.diAdd = AddBtnWidget()           # открываю диалоговое окно с вводом пути
        self.diAdd.show()

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


class AddBtnWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('browser.ui', self)
        self.cancel.clicked.connect(self.kill)
        self.further.clicked.connect(self.browse_folder)
        self.string = None

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


class DelBtnWidget(QMainWindow):  # банально... нет смысла объяснять, думаю
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


class Error(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('error.ui', self)
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
