from PyQt5.QtWidgets import *

import database
import menu

def edit_menu():
    window = QDialog()
    main_line = QVBoxLayout()
    
    list_widget = QListWidget()
    for i, question in enumerate(database.questions):
        item = QListWidgetItem(f"{i+1}. {question['запитання']}")
        list_widget.addItem(item)
    
    edit_btn = QPushButton("Редагувати")
    
    def edit_func():
        selected_items = list_widget.selectedItems()  # список
        if selected_items:
            selected_item = selected_items[0] 
            index = list_widget.row(selected_item)
            menu.menu(edit_index=index)
            window.close()
    
    edit_btn.clicked.connect(edit_func)
    main_line.addWidget(list_widget)
    main_line.addWidget(edit_btn)
    
    window.setLayout(main_line)
    window.exec()
