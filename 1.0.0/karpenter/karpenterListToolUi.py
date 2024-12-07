# -*- encoding: utf-8 -*-
"""
Module with searchbar functions
"""


from PyQt5.QtWidgets import QWidget, QLineEdit, QTableView, QHeaderView, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QRegExp, pyqtSlot, pyqtSignal, QSize
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
import karpenterCore
import karpenterOptionWindow
import CONSTANTS



class ToolBoxUi(QWidget):
    displayedElementCountChanged = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.checked_instances = {}
        self.init_ui()

    def init_ui(self):
        mainLayout = QVBoxLayout(self)

        icon_button = QPushButton()
        icon_button.setIcon(QIcon(f"{CONSTANTS.rootProject}/icons/gear.png"))
        icon_button.setIconSize(QSize(14, 14))
        icon_button.setFixedSize(14, 14)
        icon_button.setStyleSheet("background-color: transparent; border: none;")
        icon_button.clicked.connect(self.open_side_list_ui)

        mainLayout.addWidget(icon_button)

        scripts = karpenterCore.getToolsConfigData()
        self.model = QStandardItemModel(len(scripts), 1)
        for row, script in enumerate(scripts):
            item = QStandardItem(script)
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.setTextAlignment(Qt.AlignCenter)
            self.model.setItem(row, 0, item)

        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(self.model)
        self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filter_proxy_model.setFilterKeyColumn(0)
        self.filter_proxy_model.setFilterRegExp(QRegExp('^$'))

        search_layout = QHBoxLayout()
        search_field = QLineEdit()
        search_field.setStyleSheet('font-size: 16px; height: 32px;')
        search_field.textChanged.connect(self.update_filter)
        search_layout.addWidget(search_field)

        mainLayout.addLayout(search_layout)

        self.table = QTableView()
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setModel(self.filter_proxy_model)
        self.table.setEditTriggers(QTableView.NoEditTriggers)
        self.table.setSelectionMode(QTableView.SingleSelection)
        self.table.clicked.connect(self.execute_selected_element)

        self.table.setStyleSheet("""
            QTableView::item:hover {
                background-color: #5da6ff;
                border: 0px solid #5da6ff;
            }
        """)

        mainLayout.addWidget(self.table)

    def update_filter(self, text):
            regexp = QRegExp(text) if text else QRegExp('^$')
            self.filter_proxy_model.setFilterRegExp(regexp)
            if text:
                displayed_count = self.filter_proxy_model.rowCount()
            else:
                displayed_count = 0
            self.displayedElementCountChanged.emit(displayed_count)

    def execute_selected_element(self, index):
        selected_indexes = self.table.selectionModel().selectedIndexes()
        jsonData = karpenterCore.getToolsConfigData()
        for sel_index in selected_indexes:
            test_button = self.filter_proxy_model.mapToSource(sel_index).data(Qt.DisplayRole)
            if jsonData[test_button]["type"] == "rez":
                karpenterCore.executeCommandScript(test_button, None)
            if jsonData[test_button]["type"] == "python":
                for instance_name, is_checked in self.checked_instances.items():
                    if is_checked:
                        karpenterCore.executeCommandScript(test_button, instance_name)

    @pyqtSlot(dict)
    def update_checked_instances(self, checked_instances):
        self.checked_instances = checked_instances

    @pyqtSlot()
    def open_side_list_ui(self):
        self.side_list_ui = karpenterOptionWindow.SideListUi()
        self.side_list_ui.show()
        self.side_list_ui.closed.connect(self.handle_side_list_closed)

    @pyqtSlot(dict)
    def handle_side_list_closed(self, modified_data):
        data = karpenterCore.remove_untitled_keys(modified_data)
        karpenterCore.updateToolsConfigData(data)
        if self.side_list_ui:
            scripts = karpenterCore.getToolsConfigData()
            self.model.clear()
            for row, script in enumerate(scripts):
                item = QStandardItem(script)
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                item.setTextAlignment(Qt.AlignCenter)
                self.model.setItem(row, 0, item)


