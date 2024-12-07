# -*- encoding: utf-8 -*-
"""
Module with worker detection functions
"""


import time
from PyQt5.QtCore import QThread, pyqtSignal
import hal_server.InstanceDetector


class Worker(QThread):
    update_signal = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.dcc_detector = hal_server.InstanceDetector.DCCInstanceDetector()
        self.is_detecting = True

    def run(self):
        while self.is_detecting:
            self.dcc_detector.detect_maya_instances()
            self.dcc_detector.detect_houdini_instances()
            self.dcc_detector.detect_unreal_instances()
            self.dcc_detector.detect_blender_instances()

            all_instances = {}

            for i, (process_id, process_name) in enumerate(self.dcc_detector.maya_instances, start=1):
                all_instances["{}-maya-PID: {}".format(i, process_id)] = [process_name, process_id]

            for i, (process_id, process_name) in enumerate(self.dcc_detector.houdini_instances, start=1):
                all_instances["{}-houdini-PID: {}".format(i, process_id)] = [process_name, process_id]

            for i, (process_id, process_name) in enumerate(self.dcc_detector.unreal_instances, start=1):
                all_instances["{}-unreal-PID: {}".format(i, process_id)] = [process_name, process_id]

            for i, (process_id, process_name) in enumerate(self.dcc_detector.blender_instances, start=1):
                all_instances["{}-blender-PID: {}".format(i, process_id)] = [process_name, process_id]

            self.update_signal.emit(all_instances)
            time.sleep(1)



