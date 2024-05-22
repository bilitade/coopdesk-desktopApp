from PySide6.QtCore import QThread, Signal



class CpuInfoThread(QThread):
    cpu_info_ready = Signal(dict)

    def __init__(self, performance):
        super().__init__()
        self.performance = performance
        self.running = True

    def run(self):
        while self.running:
            cpu_percent = self.performance.get_cpu_percent()
            cpu_freq_current = self.performance.get_cpu_frequency()
            memory_percent, memory_total_gb, memory_used_gb = self.performance.get_memory_info()

            info = {
                'cpu_percent': cpu_percent,
                'cpu_freq_current': cpu_freq_current,
                'memory_percent': memory_percent,
                'memory_total_gb': memory_total_gb,
                'memory_used_gb': memory_used_gb
            }
            self.cpu_info_ready.emit(info)
            self.sleep(1)  # Update every second

    def stop(self):
        self.running = False
