import sys
import webbrowser
from PySide6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton, QWidget, QHeaderView, QSizePolicy

class WebsiteCatalog(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Main layout
        mainLayout = QVBoxLayout()

        # Search bar layout
        searchLayout = QHBoxLayout()
        self.searchLineEdit = QLineEdit(self)
        self.searchLineEdit.setPlaceholderText("Search...")
        searchButton = QPushButton("Clean Search", self)
        searchButton.clicked.connect(self.filterResults)
        searchLayout.addWidget(self.searchLineEdit)
        searchLayout.addWidget(searchButton)

        # Table widget
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Site Name", "URL"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalScrollBar().setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # Make cells non-editable
        self.tableWidget.cellDoubleClicked.connect(self.openWebsite)

        # Add search layout and table widget to main layout
        mainLayout.addLayout(searchLayout)
        mainLayout.addWidget(self.tableWidget)

        # Set main layout
        self.setLayout(mainLayout)

        # Populate table with dummy data
        self.loadDummyData()

    def loadDummyData(self):
        websites = []
        for i in range(100):
            websites.append({"name": f"Website {i+1}", "url": f"https://www.website{i+1}.com"})

        self.tableWidget.setRowCount(len(websites))

        for row, website in enumerate(websites):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(website["name"]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(website["url"]))

    def filterResults(self):
        searchText = self.searchLineEdit.text().lower()
        for row in range(self.tableWidget.rowCount()):
            site_name = self.tableWidget.item(row, 0).text().lower()
            url = self.tableWidget.item(row, 1).text().lower()

            if searchText in site_name or searchText in url:
                self.tableWidget.setRowHidden(row, False)
            else:
                self.tableWidget.setRowHidden(row, True)

    def openWebsite(self, row, column):
        url = self.tableWidget.item(row, 1).text()
        webbrowser.open(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WebsiteCatalog()
    ex.resize(600, 400)
    ex.show()
    sys.exit(app.exec())
