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

    b1.clicked.connect(lambda: show_text('quotes'))
    b2.clicked.connect(lambda: show_text('mems'))
    b3.clicked.connect(lambda: show_text('anecdotes'))
    b4.clicked.connect(input_note)

    win.setWindowTitle("Случайное сообщение")
    win.show()
    sys.exit(app.exec_())

def input_note(): # окно для внесения новой информации 
    dlg = QDialog()

    # создание переменных для кнопки, строчки внесения текста и радиокнопок 
    txt = QTextEdit()   
    b1 = QPushButton("Внести")
    r1 = QRadioButton("Цитаты")
    r2 = QRadioButton("Мемы")
    r3 = QRadioButton("Анекдоты")
    r1.setChecked(True) # Установить по умолчанию выбор на r1
    
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

    b1.clicked.connect(lambda: new_text(txt, r1, r2)) # увязка нажатия кнопки и вызова ф-ции внесения текста в файл

    dlg.setWindowTitle("Внести новый контент")
    dlg.setWindowModality(Qt.ApplicationModal)
    dlg.exec_()    

def new_text(b, r1, r2): # функция внесения текста, внесение происходит в зависимости от выбранной радиокнопки
    if r1.isChecked():
        with open('quotes.txt', 'a') as file:
            print(b.toPlainText()+'\n', file=file)
    elif r2.isChecked():
        with open('mems.txt', 'a') as file:
            print(b.toPlainText()+'\n', file=file)
    else:
        with open('anecdotes.txt', 'a') as file:
            print(b.toPlainText()+'\n', file=file)

def show_text(text): # функция вывода случайного текста (цитаты, мема или анекдота), на вход подается строка с началом названия файла
    dlg = QDialog()
         
    with open(f'{text}.txt') as file: # открывается тот файл, начало которого подаётся на вход ф-ции, для формирования имени используется f-строка
        txt = [c.strip('\n') for c in file.read().split('\n\n') if c] # списочное выражение используется для устранения пустых строк и символов '\n'
    
    l = QLabel() 
    l.setText(ch(txt))

    vbox = QVBoxLayout()
    vbox.addWidget(l)
    dlg.setLayout(vbox)

    dlg.setWindowTitle("Text")
    dlg.setWindowModality(Qt.ApplicationModal)
    dlg.exec_()

if __name__ == '__main__':
    main_window()
