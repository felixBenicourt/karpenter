# -*- encoding: utf-8 -*-
"""
Module with some main ui
"""


from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTabWidget
from PyQt5 import QtGui
import os
import CONSTANTS
from utils import loadStylesheets
from karpenterListToolUi import ToolBoxUi
import karpenterListInstancesUi



class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.default_size = self.size()


    def init_ui(self):
        self.setWindowTitle("Karpenter")
        self.setWindowIcon(QtGui.QIcon(f'{CONSTANTS.rootProject}/icons/karpenter_icone.png'))
        self.stylesheet_filename = os.path.join(os.path.dirname(__file__), "qss/karpenter-dark.qss")
        self.width = 400
        self.countNum = None
        self.height_map = {"ToolBox": 160, "Instance Window": 240}
        self.new_height = self.height_map["ToolBox"]
        self.setFixedSize(self.width, self.height_map["ToolBox"])

        loadStylesheets(self.stylesheet_filename)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        self.tab_widget = QTabWidget()
        self.tab_widget.currentChanged.connect(self.adjust_height)

        self.tab1 = QWidget()
        self.tool_box_layout = QVBoxLayout(self.tab1)
        self.tool_box_ui = ToolBoxUi()
        self.tool_box_ui.displayedElementCountChanged.connect(self.adjust_height_based_on_element_count)
        self.tool_box_layout.addWidget(self.tool_box_ui)
        self.tab_widget.addTab(self.tab1, "ToolBox")

        self.tab2 = QWidget()
        self.instance_layout = QVBoxLayout(self.tab2)
        self.instance_window_ui = karpenterListInstancesUi.InstanceWindowUi()
        self.instance_window_ui.checkedItemsChanged.connect(self.tool_box_ui.update_checked_instances)
        self.instance_layout.addWidget(self.instance_window_ui)
        self.tab_widget.addTab(self.tab2, "Instance Window")

        main_layout.addWidget(self.tab_widget)


    def adjust_height(self):
        current_tab_index = self.tab_widget.currentIndex()
        current_tab_text = self.tab_widget.tabText(current_tab_index)
        if current_tab_text == "ToolBox":
            if self.countNum:
                new_height = self.height_map["ToolBox"] + self.countNum * 32
                self.setFixedHeight(new_height)
            else:
                self.setFixedHeight(self.height_map[current_tab_text])
        elif current_tab_text == "Instance Window":
            self.setFixedHeight(self.height_map[current_tab_text])


    def adjust_height_based_on_element_count(self, count):
        self.countNum = count
        new_height = self.height_map["ToolBox"] + count * 32
        self.setFixedHeight(new_height)
