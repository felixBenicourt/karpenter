


from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QHBoxLayout, QListWidgetItem, QCheckBox, QPushButton, QLabel
from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtGui import QIcon
import karpenterWorker
import CONSTANTS



class InstanceWindowUi(QWidget):
    checkedItemsChanged = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.checked_items = {}
        self.worker = None
        self.worker_running = False
        self.init_ui()

    def init_ui(self):
        instance_layout = QVBoxLayout(self)
        button_layout = QHBoxLayout()
        button_layout.addSpacing(-6)

        self.checkButton = QPushButton()
        self.update_button_icon()
        self.checkButton.setIconSize(QSize(24, 24))
        self.checkButton.setFixedSize(24, 24)
        self.checkButton.setStyleSheet("QPushButton {background-color: transparent; border: none;}")
        self.checkButton.clicked.connect(self.check_button_clicked)
        button_layout.addWidget(self.checkButton)
        self.label = QLabel("Check DCC instances")
        self.label.setStyleSheet("font-size: 13px; margin-top: 0;")
        button_layout.addWidget(self.label)
        instance_layout.addLayout(button_layout)
        list_layout = QVBoxLayout()
        list_layout.addSpacing(10)
        self.instanceList = QListWidget()
        list_layout.addWidget(self.instanceList)
        instance_layout.addLayout(list_layout)

    def check_button_clicked(self):
        if self.worker_running:
            self.stop_worker()
        else:
            self.start_worker()
        self.update_button_icon()

    def start_worker(self):
        if not self.worker_running:
            self.worker = karpenterWorker.Worker()
            self.worker.update_signal.connect(self.update_status)
            self.worker.start()
            self.worker_running = True

    def stop_worker(self):
        if self.worker_running:
            self.worker.terminate()
            self.worker_running = False

    def update_button_icon(self):
        if self.worker_running:
            self.checkButton.setIcon(QIcon(f"{CONSTANTS.rootProject}/icons/stop_icon.png"))
        else:
            self.checkButton.setIcon(QIcon(f"{CONSTANTS.rootProject}/icons/start_icon.png"))

    def update_status(self, all_instances):
        self.instanceList.clear()
        for key, value in all_instances.items():
            item = QListWidgetItem()
            checkbox = QCheckBox()
            checkbox.setText(key)
            checkbox.setCheckable(True)
            if key in self.checked_items:
                checkbox.setChecked(self.checked_items[key])
            checkbox.stateChanged.connect(lambda state, key=key: self.checkbox_state_changed(state, key))
            self.instanceList.addItem(item)
            self.instanceList.setItemWidget(item, checkbox)
            self.checked_items[key] = checkbox.isChecked()
        self.instanceList.setMaximumHeight(self.instanceList.sizeHint().height())

    def checkbox_state_changed(self, state, key):
        self.checked_items[key] = state
        self.checkedItemsChanged.emit(self.checked_items)
