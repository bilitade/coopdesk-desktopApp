
from PySide6.QtCore import QThread, Signal


from scripts.networkInfo  import get_ethernet_adapter_info
class NetworkInfoThread(QThread):
    network_info_ready = Signal(dict)

    def __init__(self):
        super().__init__()

    def run(self):
        info = get_ethernet_adapter_info()
        self.network_info_ready.emit(info)