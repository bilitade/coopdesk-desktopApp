from PySide6.QtCore import QObject, QThread, Signal
from scripts.disks import get_primary_disk_info
class DiskThread(QThread):
    disk_info_ready=Signal(dict)

    def __init__(self ):
        super().__init__()

    def run(self):
        info=get_primary_disk_info()
        self.disk_info_ready.emit(info)

        