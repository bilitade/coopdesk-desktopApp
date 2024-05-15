
import sys
from PySide6.QtWidgets  import QApplication;
from coopdesk import CoopDeskWidget
app=QApplication(sys.argv)
window=CoopDeskWidget()
window.show()
app.exec()