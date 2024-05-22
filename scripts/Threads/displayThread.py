from PySide6.QtCore import QObject, QThread, Signal

from scripts.graphics import get_graphics_info

class DisplayThread(QThread):
    display_info_ready=Signal(dict)
    def __init__(self):
        super().__init__()

    def run(self):
        info=get_graphics_info()
        self.display_info_ready.emit(info)