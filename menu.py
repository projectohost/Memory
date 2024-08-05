from PyQt5.QtWidgets import *

import database

def menu(edit_index=None):
    window = QDialog()
    main_line = QVBoxLayout()

    add_btn = QPushButton("Зберегти")
    quest_lbl = QLabel("Запитання")
    quest_ledt = QLineEdit()

    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_ledt)
    main_line.addLayout(h1)

    right_lbl = QLabel("Правильна відповідь")
    right_ledt = QLineEdit()

    h2 = QHBoxLayout()
    h2.addWidget(right_lbl)
    h2.addWidget(right_ledt)
    main_line.addLayout(h2)

    wrong1_lbl = QLabel("Не правильна відповідь 1")
    wrong1_ledt = QLineEdit()

    h3 = QHBoxLayout()
    h3.addWidget(wrong1_lbl)
    h3.addWidget(wrong1_ledt)
    main_line.addLayout(h3)

    wrong2_lbl = QLabel("Не правильна відповідь 2")
    wrong2_ledt = QLineEdit()

    h4 = QHBoxLayout()
    h4.addWidget(wrong2_lbl)
    h4.addWidget(wrong2_ledt)
    main_line.addLayout(h4)

    wrong3_lbl = QLabel("Не правильна відповідь 3")
    wrong3_ledt = QLineEdit()

    h5 = QHBoxLayout()
    h5.addWidget(wrong3_lbl)
    h5.addWidget(wrong3_ledt)
    main_line.addLayout(h5)

    if edit_index is not None:
        question = database.questions[edit_index]
        quest_ledt.setText(question["запитання"])
        right_ledt.setText(question["Правильна відповідь"])
        wrong1_ledt.setText(question["Не правильна відповідь1"])
        wrong2_ledt.setText(question["Не правильна відповідь2"])
        wrong3_ledt.setText(question["Не правильна відповідь3"])

    def save_func():
        new_quest = {
            "запитання": quest_ledt.text(),
            "Правильна відповідь": right_ledt.text(),
            "Не правильна відповідь1": wrong1_ledt.text(),
            "Не правильна відповідь2": wrong2_ledt.text(),
            "Не правильна відповідь3": wrong3_ledt.text(),
        }
        if edit_index is None:
            database.questions.append(new_quest)
        else:
            database.questions[edit_index] = new_quest

    add_btn.clicked.connect(save_func)
    main_line.addWidget(add_btn)

    window.setLayout(main_line)
    window.exec()
