import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from random import choice as ch

def main_window():
    app = QApplication(sys.argv)
    win = QWidget()
    win.setGeometry(900, 400, 300, 200)
    
    b1 = QPushButton("Цитаты")
    b2 = QPushButton("Мемы")
    b3 = QPushButton("Анекдоты")
    b4 = QPushButton("Внести заметку")

    vbox = QVBoxLayout()
    vbox.addWidget(b4)
    vbox.addStretch()
    vbox.addWidget(b1)
    vbox.addWidget(b2)
    vbox.addWidget(b3)
    win.setLayout(vbox)

    b1.clicked.connect(show_quotes)
    b2.clicked.connect(show_mems)
    b3.clicked.connect(show_anecdotes)
    b4.clicked.connect(input_note)

    win.setWindowTitle("PyQt Dialog demo")
    win.show()
    sys.exit(app.exec_())

def input_note(): # окно для внесения новой информации 
    dlg = QDialog()

    # создание переменных для кнопки, строчки внесения текста и радиокнопок 
    txt = QLineEdit()   
    b1 = QPushButton("Внести")
    r1 = QRadioButton("Цитаты")
    r2 = QRadioButton("Анекдоты")
    r3 = QRadioButton("Внести заметку")
    
    # создание вертикального и горизонтального слоя
    vbox = QVBoxLayout()
    hbox = QHBoxLayout()

    # добавление в вертикальный слой попорядку: строчки для текста, горизонтального слоя с радиокнопками (они добавлены предварительно), кнопки 
    vbox.addWidget(txt) 
    hbox.addWidget(r1)
    hbox.addWidget(r2)
    hbox.addWidget(r3)
    vbox.addLayout(hbox)
    vbox.addWidget(b1)
   
    dlg.setLayout(vbox) # добавление в окно вертикального слоя

    b1.clicked.connect(lambda: clicked(txt)) # увязка нажатия кнопки и вызова ф-ции внесения текста в файл

    dlg.setWindowTitle("Внести новый контент")
    dlg.setWindowModality(Qt.ApplicationModal)
    dlg.exec_()    

def clicked(b):
    print(b.text())

def show_quotes():
    dlg = QDialog()

    l = QLabel()    
    l.setText(ch(quotes))

    vbox = QVBoxLayout()
    vbox.addWidget(l)
    dlg.setLayout(vbox)

    dlg.setWindowTitle("Dialog")
    dlg.setWindowModality(Qt.ApplicationModal)
    dlg.exec_()

def show_mems():
    dlg = QDialog()

    l = QLabel()    
    l.setText(ch(mems))

    vbox = QVBoxLayout()
    vbox.addWidget(l)
    dlg.setLayout(vbox)

    dlg.setWindowTitle("Dialog")
    dlg.setWindowModality(Qt.ApplicationModal)
    dlg.exec_()

def show_anecdotes():
    dlg = QDialog()

    l = QLabel()    
    l.setText(ch(anecdotes))

    vbox = QVBoxLayout()
    vbox.addWidget(l)
    dlg.setLayout(vbox)

    dlg.setWindowTitle("Dialog")
    dlg.setWindowModality(Qt.ApplicationModal)
    dlg.exec_()    


with open('quotes.txt') as file:
    quotes = file.read().split('\n\n')
#просто коммент
with open('mems.txt') as file:
    mems = file.read().split('\n\n')

with open('anecdotes.txt') as file:
    anecdotes = file.read().split('\n\n')

if __name__ == '__main__':
    main_window()


