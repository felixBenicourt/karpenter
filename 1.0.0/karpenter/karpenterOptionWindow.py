# -*- encoding: utf-8 -*-
"""
Module with commandes ui functions
"""



from PyQt5.QtWidgets import QWidget, QListWidget, QTextEdit, QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal
import karpenterCore
import CONSTANTS



class SideListUi(QWidget):
    closed = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.scripts = karpenterCore.getToolsConfigData()
        self.init_ui()
        self.modified_data = {}
        self.all_data_edited = {}
        self.fields_changed = False

    def init_ui(self):
        main_layout = QVBoxLayout()

        layout = QGridLayout()
        self.width = 660

        self.list_widget = QListWidget()
        self.list_widget.addItems(self.scripts.keys())
        self.list_widget.itemClicked.connect(self.on_item_clicked)
        layout.addWidget(self.list_widget, 0, 0, 6, 1)

        self.title_edit = QTextEdit()
        self.title_edit.setPlaceholderText('Title')
        self.title_edit.setStyleSheet("background-color: #181a1c; color: white;")
        self.title_edit.setFixedWidth(self.width)
        self.title_edit.setFixedHeight(24)
        self.title_edit.textChanged.connect(self.field_changed)
        layout.addWidget(self.title_edit, 0, 1, 1, 1)

        self.type_edit = QTextEdit()
        self.type_edit.setPlaceholderText('Type')
        self.type_edit.setStyleSheet("background-color: #181a1c; color: white;")
        self.type_edit.setFixedWidth(self.width)
        self.type_edit.setFixedHeight(24)
        self.type_edit.textChanged.connect(self.field_changed)
        layout.addWidget(self.type_edit, 1, 1, 1, 1)

        self.tag_edit = QTextEdit()
        self.tag_edit.setPlaceholderText('Tags')
        self.tag_edit.setStyleSheet("background-color: #181a1c; color: white;")
        self.tag_edit.setFixedWidth(self.width)
        self.tag_edit.setFixedHeight(24)
        self.tag_edit.textChanged.connect(self.field_changed)
        layout.addWidget(self.tag_edit, 2, 1, 1, 1)

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText('Code')
        self.text_edit.setStyleSheet("background-color: #181a1c; color: white;")
        self.text_edit.setFixedWidth(self.width)
        self.text_edit.textChanged.connect(self.field_changed)
        layout.addWidget(self.text_edit, 3, 1, 1, 1)

        main_layout.addLayout(layout)

        buttons_layout = QHBoxLayout()

        self.add_button = QPushButton()
        self.add_button.setFixedSize(24, 24)
        self.add_button.setStyleSheet("background-color: transparent;")
        self.add_button.setIcon(QIcon(f"{CONSTANTS.rootProject}/icons/plus.png"))
        self.add_button.clicked.connect(self.add_item)
        buttons_layout.addWidget(self.add_button)

        self.delete_button = QPushButton()
        self.delete_button.setFixedSize(24, 24)
        self.delete_button.setStyleSheet("background-color: transparent;")
        self.delete_button.setIcon(QIcon(f"{CONSTANTS.rootProject}/icons/minus.png"))
        self.delete_button.clicked.connect(self.delete_item)
        buttons_layout.addWidget(self.delete_button)

        buttons_layout.addStretch(1)

        self.save_button = QPushButton()
        self.save_button.setFixedSize(24, 24)
        self.save_button.setStyleSheet("background-color: transparent;")
        self.save_button.setIcon(QIcon(f"{CONSTANTS.rootProject}/icons/noSave.png"))
        self.save_button.clicked.connect(self.save_changes)
        self.save_button.setEnabled(False)
        buttons_layout.addWidget(self.save_button)

        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)

        self.setWindowIcon(QIcon(f'{CONSTANTS.rootProject}/icons/karpenter_icone.png'))
        self.setWindowTitle("Edit Commands")

    def field_changed(self):
        self.fields_changed = True
        self.save_button.setIcon(QIcon(f"{CONSTANTS.rootProject}/icons/save.png"))
        self.save_button.setEnabled(True) 

    def reset_save_button(self):
        self.fields_changed = False
        self.save_button.setIcon(QIcon(f"{CONSTANTS.rootProject}/icons/noSave.png"))
        self.save_button.setEnabled(False)

    def closeEvent(self, event):
        self.handle_close_event()
        super().closeEvent(event)

    def handle_close_event(self):
        self.all_data_edited = {**self.scripts, **self.modified_data}
        self.closed.emit(self.all_data_edited)

    def on_item_clicked(self, item):
        self.current_item_key = item.text()
        item_data = self.scripts[item.text()]
        self.text_edit.setText(item_data['cmd'])
        self.type_edit.setText(item_data['type'])
        self.tag_edit.setText(", ".join(item_data['tags']))
        self.title_edit.setText(item.text())
        self.reset_save_button()

    def add_item(self):
        new_title = "Untitled"
        index = 1
        while new_title in self.scripts:
            new_title = f"Untitled_{index}"
            index += 1
        self.list_widget.addItem(new_title)
        self.list_widget.setCurrentRow(self.list_widget.count() - 1)
        self.text_edit.clear()
        self.type_edit.clear()
        self.tag_edit.clear()
        self.title_edit.setText(new_title)
        self.reset_save_button()
        
        if self.list_widget.count() > 0:
            self.save_changes()

    def save_changes(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            old_title = selected_item.text()
            new_title = self.title_edit.toPlainText()
            edited_data = {
                'cmd': self.text_edit.toPlainText(),
                'type': self.type_edit.toPlainText(),
                'tags': self.tag_edit.toPlainText().split(",")
            }
            self.scripts[new_title] = edited_data
            self.modified_data[new_title] = edited_data
            if old_title != new_title:
                del self.scripts[old_title]
                selected_item.setText(new_title)
            self.reset_save_button()

    def delete_item(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            confirm_dialog = QMessageBox()
            confirm_dialog.setWindowIcon(QIcon())
            confirm_dialog.setWindowTitle("Confirm Deletion")
            confirm_dialog.setText("Are you sure you want to delete this item?")
            confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirm_dialog.setDefaultButton(QMessageBox.No)
            confirm_dialog.setStyleSheet("background-color: #181a1c; color: white;")

            result = confirm_dialog.exec_()
            if result == QMessageBox.Yes:
                title = selected_item.text()
                del self.scripts[title]
                row = self.list_widget.row(selected_item)
                self.list_widget.takeItem(row)
                self.text_edit.clear()
                self.type_edit.clear()
                self.tag_edit.clear()
                self.title_edit.clear()
                self.reset_save_button()

    def switch_element(self, new_item_key):
        if hasattr(self, 'current_item_key'):
            if self.current_item_key in self.scripts:
                edited_data = {
                    'cmd': self.text_edit.toPlainText(),
                    'type': self.type_edit.toPlainText(),
                    'tags': self.tag_edit.toPlainText().split(",")
                }
                self.modified_data[self.current_item_key] = edited_data

        if new_item_key in self.scripts:
            item_data = self.scripts[new_item_key]
            self.text_edit.setText(item_data['cmd'])
            self.type_edit.setText(item_data['type'])
            self.tag_edit.setText(", ".join(item_data['tags']))
            self.title_edit.setText(new_item_key)
            self.current_item_key = new_item_key
            self.reset_save_button()

    def switch_to_previous_item(self):
        if hasattr(self, 'previous_item_key'):
            self.switch_element(self.previous_item_key)

    def switch_to_next_item(self):
        if hasattr(self, 'next_item_key'):
            self.switch_element(self.next_item_key)


