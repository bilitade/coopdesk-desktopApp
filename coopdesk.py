from PySide6.QtCore import Qt
import webbrowser
from PySide6.QtWidgets  import QWidget, QMainWindow,QHeaderView,QSizePolicy,QTableWidget,QTableWidgetItem
from coopdesk_ui import Ui_MainWindow

class CoopDeskWidget (QMainWindow,Ui_MainWindow):
     def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Coop Desk")
        self.icon_only_widget.setHidden(True)
        
        self.home_1_button.clicked.connect(self.redirectHome)
        self.app_1_button.clicked.connect(self.redirectApp)
        self.about_1_button.clicked.connect(self.redirectAbout)
        self.update_1_button.clicked.connect(self.redirectUpdate)

        self.home_2_button.clicked.connect(self.redirectHome)
        self.app_2_button.clicked.connect(self.redirectApp)
        self.about_2_button.clicked.connect(self.redirectAbout)
        self.update_2_button.clicked.connect(self.redirectUpdate)
        self.pcinfo_button.clicked.connect(self.redirectPCinfo)
        self.coopurl_table.horizontalHeader().setStyleSheet("QHeaderView::section {"
                                                            "background-color: #02C1FE;"
                                                            "color:white;"
                                                            "border: 1px solid white;"
                                                            "font-size: 14pt;"
                                                            "}"
                                                            )
        self.coopurl_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.coopurl_table.verticalScrollBar().setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.coopurl_table.verticalScrollBar().setStyleSheet("QScrollBar:vertical { background: #d3d3d3; width: 10px; }"
                                                            "QScrollBar::handle:vertical { background: #02C1FE; }"
                                                            "QScrollBar::add-line:vertical { background: #d3d3d3; }"
                                                            "QScrollBar::sub-line:vertical { background: #d3d3d3; }")
        self.coopurl_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.coopurl_Search_button.clicked.connect(self.filterResults)
        self.coopurl_table.cellDoubleClicked.connect(self.openWebsite)
        self.loadDummyData()
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

         # url data 
     def loadDummyData(self):
        websites =[
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
     def filterResults(self):
          searchText = self.coopurl_search_lineedit.text().lower()
          for row in range(self.coopurl_table.rowCount()):
               site_name = self.coopurl_table.item(row, 0).text().lower()
               url = self.coopurl_table.item(row, 1).text().lower()

               if searchText in site_name or searchText in url:
                    self.coopurl_table.setRowHidden(row, False)
               else:
                    self.coopurl_table.setRowHidden(row, True)

     def openWebsite(self, row, column):
         url = self.coopurl_table.item(row, 1).text()
         webbrowser.open(url)

