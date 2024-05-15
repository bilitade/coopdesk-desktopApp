from PySide6.QtCore import Qt
from PySide6.QtWidgets  import QWidget, QMainWindow;
from coopdesk_ui import Ui_MainWindow

class CoopDeskWidget (QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Coop Desk")
        self.icon_name_widget.setHidden(True)
        
        self.home_1_button.clicked.connect(self.redirectHome)
        self.app_1_button.clicked.connect(self.redirectApp)
        self.about_1_button.clicked.connect(self.redirectAbout)
        self.update_1_button.clicked.connect(self.redirectUpdate)

        self.home_2_button.clicked.connect(self.redirectHome)
        self.app_2_button.clicked.connect(self.redirectApp)
        self.about_2_button.clicked.connect(self.redirectAbout)
        self.update_2_button.clicked.connect(self.redirectUpdate)


    def redirectHome(self):
        self.stackedWidget.setCurrentIndex(2)
    def redirectApp(self):
         self.stackedWidget.setCurrentIndex(1)
    def redirectAbout(self):
         self.stackedWidget.setCurrentIndex(0)
    def redirectUpdate(self):
         self.stackedWidget.setCurrentIndex(3)


