from PySide6.QtCore import QThread, Signal
from scripts.systeminfo import get_important_system_info;

class SystemTread(QThread):
    system_info_ready=Signal(dict)

    def __init__(self):
        super().__init__()


    def run(self):
      info= get_important_system_info()
      self.system_info_ready.emit(info)
       
