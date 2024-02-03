import os
from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
app = QApplication([])

win=QWidget()
win.resize(700,500)
win.setWindowTitle('English')
#win.setWindowIcon(QtGui.QIcon('english.ico'))

label_caption=QLabel("Вивчення англійської")
label_caption.setStyleSheet("font-size:20px;color:red")

label_t=QLabel('')
label_t.setFixedSize(500,400)
label_t.setStyleSheet("font-size:40px;padding:125px")
label_p=QLabel('')
label_p.setFixedSize(500,400)

left=QPushButton("<<")
right=QPushButton(">>")

button=QHBoxLayout()
button.addWidget(left)
button.addWidget(right)

row_label=QHBoxLayout()

row_label.addWidget(label_t)
row_label.addWidget(label_p)
h=QVBoxLayout()

h.addWidget(label_caption, alignment=Qt.AlignCenter)
h.addLayout(row_label)
h.addLayout(button)
button.addWidget(left)
button.addWidget(right)

win.setLayout(h)

m=os.path.abspath('1.txt')
t=open(m, encoding='utf-8')
label_t.setText(t.read())
label_p.hide()
pixmapimage = QPixmap('1.jpg')
w, h = label_p.width(), label_p.height()
pixmapimage = pixmapimage.scaled(500, 700, Qt.KeepAspectRatio)
label_p.setPixmap(pixmapimage)
label_p.show()

i=1
def button_right():
    global i
    i=i+1
    if i==6:
        i=1
    t=open(str(i)+'.txt', encoding='utf-8')
    label_t.setText(t.read())

    label_p.hide()
    pixmapimage = QPixmap(str(i)+'.jpg')
    w,h = label_p.width(), label_p.height()
    pixmapimage = pixmapimage.scaled(500, 700, Qt.KeepAspectRatio)
    label_p.setPixmap(pixmapimage)
    label_p.show()

right.clicked.connect(button_right)

i=1
def button_left():
    global i
    i=i-1
    if i==0:
        i=5
    t=open(str(i)+'.txt', encoding='utf-8')
    label_t.setText(t.read())

    label_p.hide()
    pixmapimage = QPixmap(str(i)+'.jpg')
    w,h = label_p.width(), label_p.height()
    pixmapimage = pixmapimage.scaled(500, 700, Qt.KeepAspectRatio)
    label_p.setPixmap(pixmapimage)
    label_p.show()

left.clicked.connect(button_left)


win.show()
app.exec_()