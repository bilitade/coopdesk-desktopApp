from PySide6.QtCore import QObject, Qt, QThread, Signal, QTimer
import webbrowser
from PySide6.QtWidgets import QWidget, QMainWindow, QHeaderView, QSizePolicy, QTableWidget, QTableWidgetItem
from coopdesk_ui import Ui_MainWindow  
from scripts.performance import Performance 
from scripts.networkInfo import get_ethernet_adapter_info 
from scripts.Threads.networkThread import NetworkInfoThread;
from scripts.Threads.cpuThread import CpuInfoThread
from scripts.Threads.systemInfoTread import SystemTread
from scripts.Threads.diskThread import DiskThread
from scripts.Threads.displayThread import DisplayThread
from scripts.Threads.wifiThread import WifiThread


class CoopDeskWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Coop Desk")
        self.performance = Performance()
        self.icon_only_widget.setHidden(True)
        
        self.setup_connections()
        self.setup_cpu_thread()
        self.setup_network_thread()
        self.setup_url_table()
        self.setup_system_thread()
        self.load_website_data()
        self.setup_disk_thread()
        self.setup_display_thread()
        self.setup_wifi_thread()
        self.michu_Next.clicked.connect(self.show_michu_next)
        self.michu_Previous.clicked.connect(self.show_michu_previous)


    def setup_connections(self):
        self.home_1_button.clicked.connect(self.redirectHome)
        self.app_1_button.clicked.connect(self.redirectApp)
        self.about_1_button.clicked.connect(self.redirectAbout)
        self.update_1_button.clicked.connect(self.redirectUpdate)

        self.home_2_button.clicked.connect(self.redirectHome)
        self.app_2_button.clicked.connect(self.redirectApp)
        self.about_2_button.clicked.connect(self.redirectAbout)
        self.update_2_button.clicked.connect(self.redirectUpdate)
        self.pcinfo_button.clicked.connect(self.redirectPCinfo)
        self.coopurl_Search_button.clicked.connect(self.coopUrlFilterResults)
        self.coopurl_table.cellDoubleClicked.connect(self.coopUrlopenWebsite)

    def setup_cpu_thread(self):
        self.cpu_info_thread = CpuInfoThread(self.performance)
        self.cpu_info_thread.cpu_info_ready.connect(self.update_metrics)
        self.cpu_info_thread.start()

    def setup_network_thread(self):
        self.network_info_thread = NetworkInfoThread()
        self.network_info_thread.network_info_ready.connect(self.update_network_info)
        self.network_info_thread.start()
    def setup_system_thread(self):
        self.system_info_thread=SystemTread()
        self.system_info_thread.system_info_ready.connect(self.update_system_info)
        self.system_info_thread.start()
    def setup_disk_thread(self):
        self.disk_info_thread=DiskThread();
        self.disk_info_thread.disk_info_ready.connect(self.update_disk_info)
        self.disk_info_thread.start()

    def setup_display_thread(self):
        self.display_info_thread=DisplayThread()
        self.display_info_thread.display_info_ready.connect(self.update_display_info)
        self.display_info_thread.start()

    def setup_wifi_thread(self):
        self.wifi_info_thread=WifiThread()
        self.wifi_info_thread.wifi_info_ready.connect(self.update_wifi_info)
        self.wifi_info_thread.start()

    def setup_url_table(self):
        self.coopurl_table.horizontalHeader().setStyleSheet(
            "QHeaderView::section {"
            "background-color: #02C1FE;"
            "color:white;"
            "border: 1px solid white;"
            "font-size: 14pt;"
            "}"
        )
        self.coopurl_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.coopurl_table.verticalScrollBar().setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.coopurl_table.verticalScrollBar().setStyleSheet(
            "QScrollBar:vertical { background: #d3d3d3; width: 10px; }"
            "QScrollBar::handle:vertical { background: #02C1FE; }"
            "QScrollBar::add-line:vertical { background: #d3d3d3; }"
            "QScrollBar::sub-line:vertical { background: #d3d3d3; }"
        )
        self.coopurl_table.setEditTriggers(QTableWidget.NoEditTriggers)

    def redirectHome(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def redirectApp(self):
        self.stackedWidget.setCurrentIndex(3)
    
    def redirectAbout(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def redirectUpdate(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def redirectPCinfo(self):
        self.stackedWidget.setCurrentIndex(2)

    def load_website_data(self):
        websites = [
            {"name": "Temenos T24", "url": "http://10.1.126.11:8080/CBS"},
            {"name": "Coop Outlook", "url": "https://mail.coopbankoromiasc.com/owa/auth/logon.aspx"},
            {"name": "Coop Ambition", "url": "http://learn.coopbank.local/"},
            {"name": "Coop FTP", "url": "http://10.1.125.11:8181/ftp"},
            {"name": "Coop Card Banking", "url": "http://10.1.125.11:8181/cardbanking"},
            {"name": "Deboo Fund", "url": "https://debo.coopbankoromiasc.com/"},
            {"name": "Coopay-Ebirr agent", "url": "https://agent.ebirr.com"},
            {"name": "Coopay-Ebirr Dealer", "url": "https://dealer.ebirr.com/"},
            {"name": "Coopay-Ebirr Distributor", "url": "https://distributor.ebirr.com/"},
            {"name": "Coopay-Ebirr Reporting", "url": "https://reporting.ebirr.com/"},
            {"name": "CHEQUEPOINTV6", "url": "http://10.1.130.100/login.aspx"},
            {"name": "IT Service Managment ", "url": "https://itservicemanagement.coopbank.local:8080/"},
            {"name": "EESW- CBRA ", "url": "https://esw.et/esw-cbra/"},
            {"name": "Federal Document Authentication And Registration Service ", "url": "http://10.100.3.9/Account/Login"},
            {"name": "Open KM ", "url": "http://10.1.125.7:8080/OpenKM/login.jsp"},
            {"name": "Coopbank Webiste", "url": "https://coopbankoromia.com.et/"}
        ]
      
        self.coopurl_table.setRowCount(len(websites))
        for row, website in enumerate(websites):
            self.coopurl_table.setItem(row, 0, QTableWidgetItem(website["name"]))
            self.coopurl_table.setItem(row, 1, QTableWidgetItem(website["url"]))

    def coopUrlFilterResults(self):
        searchText = self.coopurl_search_lineedit.text().lower()
        for row in range(self.coopurl_table.rowCount()):
            site_name = self.coopurl_table.item(row, 0).text().lower()
            url = self.coopurl_table.item(row, 1).text().lower()

            if searchText in site_name or searchText in url:
                self.coopurl_table.setRowHidden(row, False)
            else:
                self.coopurl_table.setRowHidden(row, True)

    def coopUrlopenWebsite(self, row, column):
        url = self.coopurl_table.item(row, 1).text()
        webbrowser.open(url)

    def update_metrics(self, info):
        cpu_percent = info['cpu_percent']
        cpu_freq_current = info['cpu_freq_current'] / 1000.0
        memory_percent = info['memory_percent']
        memory_total_gb = info['memory_total_gb']
        memory_used_gb = info['memory_used_gb']

        self.cpu_frequency_label.setText(f"{cpu_freq_current:.2f} GHz")
        self.cpu_progress_bar.setValue(cpu_percent)
        self.cpu_ram_free_used_ratio.setText(f"{memory_used_gb:.2f} GB / {memory_total_gb:.2f} GB")
        self.ram_progressbar.setValue(memory_percent)

    def update_network_info(self, info):
        self.ethernet_adapter_label.setText(info.get('model', 'N/A'))
        self.ethernet_ip_label.setText(info.get('ip_address', 'N/A'))
        self.ethernet_subnet_label.setText(info.get('netmask', 'N/A'))
        self.ethernet_defaultGateway_label.setText(info.get('default_gateway', 'N/A'))
        self.ethernet_Deafult_DNS.setText(info.get('default_dns', 'N/A'))
        self.ethernet_alternative_DNS_label.setText(info.get('alternative_dns', 'N/A'))
        self.ethernet_status.setText(info.get( 'connection_status', 'Disconnected'))
        self.ethernet_mac_label.setText(info.get('mac_address', 'N/A'))
        self.ethernet_speed_label.setText(info.get('speed', 'N/A'))
    def update_system_info(self, info):
        self.sys_processor_name.setText(info.get('Processor Name'))
        self.sysprocessor_manu.setText(info.get('Processor Manufacturer'))
        self.sys_processor_max_clock.setText(info.get('Processor Max Clock Speed', 'N/A'))
        self.sys_processor_num_core.setText(info.get('Number of Cores','N/A'))
        self.sys_processor_logical_num_core.setText(info.get('Number of Logical Processors'))
        self.sys_system_name.setText(info.get('System Name'))
        self.sys_system_manu.setText(info.get('System Manufacturer'))
        self.sys_system_model.setText(info.get('System Model'))
        self.sys_system_type.setText(info.get('System Type'))
        self.sys_os_name.setText(info.get('Version'))
        self.sys_os_version.setText(info.get('OS Name'))
        self.sys_os_manu.setText(info.get('OS Manufacturer'))
        self.sys_ram.setText(info.get('Installed RAM'))
        
    def update_disk_info(self,info):
      
        self.disk_desc.setText(info.get('Description','N/A'))
        self.disk_model.setText(info.get('Model','N/A'))
        self.disk_size.setText(info.get('Size','N/A'))
        self.disk_part.setText(info.get('Partitions','N/A'))
        self.disk_type.setText(info.get('Media Type','N/A'))
        self.disk_byte_sector.setText(info.get('Bytes/Sector','N/A'))
        self.disk_manu.setText(info.get('Manufacturer','N/A'))
        
    def update_display_info(self,info):
 
         self.display_name.setText(info.get('Name','N/A'))
         self.display_type.setText(info.get('Adapter Type','N/A'))
         self.display_desc.setText(info.get('Adapter Description','N/A'))
         self.display_ram.setText(info.get('Adapter RAM','N/A'))
         self.display_driver_version.setText(info.get('Driver Version','N/A'))
         self.display_resolution.setText(info.get('Resolution','N/A'))
         self.display_bit_pixel.setText(info.get('Bits/Pixel','N/A'))
    def update_wifi_info(self, info):
        self.wifi_adapter_label.setText(info.get('model'))
        self.wifi_MAC_label.setText(info.get('mac_address'))
        self.wifi_subnet_label.setText(info.get('netmask'))
        self.wifi_default_dns_label.setText(info.get('default_dns'))
        self.wifi_alternat_DNS_label.setText(info.get('alternative_dns','N/A'))
        self.wifi_ip_label.setText(info.get('ip_address'))
        self.wifi_speed_label.setText(info.get('speed'))
        self.wifi_status_label.setText(info.get('is_up','Disconnected'))


        
    def closeEvent(self, event):
        
        self.network_info_thread.quit()
        self.system_info_thread.quit()
        self.display_info_thread.quit()
        self.wifi_info_thread.quit()
        self.cpu_info_thread.stop()
        self.cpu_info_thread.wait()
        super().closeEvent(event)


    def show_michu_previous(self):
        current_index = self.michu_slider.currentIndex()

        if current_index > 0:
            self.michu_slider.setCurrentIndex(current_index - 1)

    def show_michu_next(self):
        current_index = self.michu_slider.currentIndex()
        if current_index < self.michu_slider.count() - 1:
            self.michu_slider.setCurrentIndex(current_index + 1)

