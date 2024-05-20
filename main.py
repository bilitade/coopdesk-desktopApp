import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon

from coopdesk import CoopDeskWidget
app=QApplication(sys.argv)
window=CoopDeskWidget()
app.setWindowIcon(QIcon(":/logo.png"))

window.show()
app.exec()