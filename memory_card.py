import random

from PyQt5.QtWidgets import *

import database
import menu
import edit_menu as edit_menu_module  # Import the new edit_menu module

app = QApplication([])
window = QWidget()
menu_btn = QPushButton("Меню")
relax_btn = QPushButton("Відпочити")
timer_sbx = QSpinBox()
min_lbl = QLabel("Хвилин")
quest_lbl = QLabel("2+2?")
var1_btn = QRadioButton("1")
var2_btn = QRadioButton("2")
var3_btn = QRadioButton("3")
var4_btn = QRadioButton("4")
answer_btn = QPushButton("Відповісти")
next_quest_btn = QPushButton("Наступне запитання")
res_lbl = QLabel("Результат")
edit_btn = QPushButton("Редагувати запитання")
group = QGroupBox("Варіанти відповідей")

main_line = QVBoxLayout()

horizontal_line1 = QHBoxLayout()
horizontal_line1.addWidget(menu_btn)
horizontal_line1.addStretch(1)
horizontal_line1.addWidget(relax_btn)
horizontal_line1.addWidget(timer_sbx)
horizontal_line1.addWidget(min_lbl)
main_line.addLayout(horizontal_line1)
main_line.addWidget(quest_lbl)

group_main_line = QVBoxLayout()
group_main_line.addWidget(var1_btn)
group_main_line.addWidget(var2_btn)
group_main_line.addWidget(var3_btn)
group_main_line.addWidget(var4_btn)
group_main_line.addWidget(res_lbl)
group.setLayout(group_main_line)
main_line.addWidget(group)
main_line.addWidget(answer_btn)
main_line.addWidget(next_quest_btn)
main_line.addWidget(edit_btn)

answers = [var1_btn, var2_btn, var3_btn, var4_btn]

def set_quest():
    if not database.questions:
        quest_lbl.setText("Немає запитань")
        for btn in answers:
            btn.setText("")
        return

    if database.nomer >= len(database.questions):
        database.nomer = len(database.questions) - 1

    random.shuffle(answers)
    current_question = database.questions[database.nomer]
    quest_lbl.setText(current_question["запитання"])
    answers[0].setText(current_question["Правильна відповідь"])
    answers[1].setText(current_question["Не правильна відповідь1"])
    answers[2].setText(current_question["Не правильна відповідь2"])
    answers[3].setText(current_question["Не правильна відповідь3"])


set_quest()
res_lbl.hide()
next_quest_btn.hide()

def ans_func():
    if answers[0].isChecked():
        res_lbl.setText("Правильно")
    else:
        res_lbl.setText("не правильно")
    answers[0].hide()
    answers[1].hide()
    answers[2].hide()
    answers[3].hide()
    res_lbl.show()
    next_quest_btn.show()
    answer_btn.hide()

def next_quest_func():
    if database.nomer + 1 >= len(database.questions):
        database.nomer = 0
    else:
        database.nomer += 1

    answers[0].show()
    answers[1].show()
    answers[2].show()
    answers[3].show()
    res_lbl.hide()
    next_quest_btn.hide()
    answer_btn.show()
    set_quest()


def edit_quest_func():
    edit_menu_module.edit_menu()  # Open the new edit menu
    set_quest()

next_quest_btn.clicked.connect(next_quest_func)
answer_btn.clicked.connect(ans_func)
menu_btn.clicked.connect(menu.menu)
edit_btn.clicked.connect(edit_quest_func)

window.setLayout(main_line)
window.show()
app.exec()
