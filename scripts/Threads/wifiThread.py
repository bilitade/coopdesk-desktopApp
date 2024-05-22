from PySide6.QtCore import QObject, QThread, Signal
from scripts.wifi import get_wifi_info
class WifiThread (QThread):
    wifi_info_ready=Signal(dict)
    def __init__(self):
        super().__init__()
    def run(self):
        info=get_wifi_info()
        self.wifi_info_ready.emit(info)
