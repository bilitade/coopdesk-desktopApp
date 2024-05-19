import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame, QGridLayout
from PySide6.QtCore import QTimer
from scripts.performance import SystemMonitor

class SystemMonitorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.monitor = SystemMonitor()
        self.initUI()
        self.start_timer()

    def initUI(self):
        self.setWindowTitle("System Monitor")
        layout = QVBoxLayout()

        # Create a grid layout for displaying the stats
        grid_layout = QGridLayout()

        self.cpu_label = QLabel("CPU Usage: Calculating...")
        self.cpu_color_box = QFrame()
        self.cpu_color_box.setFixedSize(20, 20)

        self.ram_label = QLabel("RAM Usage: Calculating...")
        self.ram_color_box = QFrame()
        self.ram_color_box.setFixedSize(20, 20)

        self.disk_label = QLabel("Disk Activity: Calculating...")
        self.disk_color_box = QFrame()
        self.disk_color_box.setFixedSize(20, 20)

        grid_layout.addWidget(self.cpu_label, 0, 0)
        grid_layout.addWidget(self.cpu_color_box, 0, 1)
        grid_layout.addWidget(self.ram_label, 1, 0)
        grid_layout.addWidget(self.ram_color_box, 1, 1)
        grid_layout.addWidget(self.disk_label, 2, 0)
        grid_layout.addWidget(self.disk_color_box, 2, 1)

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def start_timer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.update_stats)
        timer.start(1000)  # Update every second

    def update_stats(self):
        cpu_freq, cpu_percent = self.monitor.get_cpu_usage()
        ram_used, ram_total, ram_percent = self.monitor.get_ram_usage()
        disk_activity_percentage = self.monitor.get_disk_activity()

        self.cpu_label.setText(f"CPU Usage: {cpu_freq:.2f} GHz ({cpu_percent:.2f}%)")
        self.set_color_box(self.cpu_color_box, cpu_percent)

        self.ram_label.setText(f"RAM Usage: {ram_used:.2f}/{ram_total:.2f} GB ({ram_percent:.2f}%)")
        self.set_color_box(self.ram_color_box, ram_percent)

        self.disk_label.setText(f"Disk Activity: {disk_activity_percentage:.2f}%")
        self.set_color_box(self.disk_color_box, disk_activity_percentage)

    def set_color_box(self, color_box, percent):
        if percent <= 20:
            color_box.setStyleSheet("background-color: green;")
        elif percent <= 40:
            color_box.setStyleSheet("background-color: yellow;")
        elif percent <= 80:
            color_box.setStyleSheet("background-color: red;")
        else:
            color_box.setStyleSheet("background-color: darkred;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    monitor_gui = SystemMonitorGUI()
    monitor_gui.show()
    sys.exit(app.exec())
