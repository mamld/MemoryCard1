from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, \
    QRadioButton, QSpinBox, QGroupBox, QButtonGroup

card_width, card_height = 600, 500 
win_card = QWidget() 
win_card.resize(card_width, card_height) 
win_card.move(300, 300) 
win_card.setWindowTitle("Memory card") 

btn_Menu = QPushButton('Меню') 
btn_Sleep = QPushButton('Відпочити')
btn_OK = QPushButton('Відповісти')
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
lb_Question = QLabel('Запитання')

RadioGroupBox = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup()

rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

AnsGroupBox = QGroupBox('Результат тесту')
lb_Result = QLabel('Правильно')
lb_Corect = QLabel('Відповідь')
########### Матвій

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Corect, alignment = Qt.AlignHCenter, stretch = 2 )
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('хвилини'))

layout_line2.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))

layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch = 2)
layout_line4.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

win_card.setLayout(layout_card)
win_card.show()