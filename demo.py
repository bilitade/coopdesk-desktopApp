import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nested Stacked Widgets Example")
        self.setGeometry(100, 100, 800, 600)

        # Main stacked widget
        self.main_stacked_widget = QStackedWidget()

        # Create parent pages
        self.coopurl_page = self.create_page("Coopurl Page Content")
        self.michu_page = self.create_michu_page()
        self.pc_page = self.create_page("PC Page Content")

        # Add parent pages to main stacked widget
        self.main_stacked_widget.addWidget(self.coopurl_page)
        self.main_stacked_widget.addWidget(self.michu_page)
        self.main_stacked_widget.addWidget(self.pc_page)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.main_stacked_widget)

        # Navigation buttons for main pages
        main_nav_layout = QHBoxLayout()
        self.main_prev_button = QPushButton("Previous Page")
        self.main_next_button = QPushButton("Next Page")
        self.main_prev_button.clicked.connect(self.show_main_previous)
        self.main_next_button.clicked.connect(self.show_main_next)

        main_nav_layout.addWidget(self.main_prev_button)
        main_nav_layout.addWidget(self.main_next_button)

        main_layout.addLayout(main_nav_layout)

        # Set main layout to central widget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def create_page(self, text):
        page = QWidget()
        layout = QVBoxLayout()
        label = QLabel(text)
        layout.addWidget(label)
        page.setLayout(layout)
        return page

    def create_michu_page(self):
        page = QWidget()
        layout = QVBoxLayout()

        self.michu_stacked_widget = QStackedWidget()

        # Add slides to the michu_stacked_widget
        for i in range(1, 6):
            slide = self.create_page(f"Slide {i}")
            self.michu_stacked_widget.addWidget(slide)

        layout.addWidget(self.michu_stacked_widget)

        # Navigation buttons for michu slides
        michu_nav_layout = QHBoxLayout()
        self.michu_prev_button = QPushButton("Previous Slide")
        self.michu_next_button = QPushButton("Next Slide")
        self.michu_prev_button.clicked.connect(self.show_michu_previous)
        self.michu_next_button.clicked.connect(self.show_michu_next)

        michu_nav_layout.addWidget(self.michu_prev_button)
        michu_nav_layout.addWidget(self.michu_next_button)

        layout.addLayout(michu_nav_layout)

        page.setLayout(layout)
        return page

    def show_main_previous(self):
        current_index = self.main_stacked_widget.currentIndex()
        if current_index > 0:
            self.main_stacked_widget.setCurrentIndex(current_index - 1)

    def show_main_next(self):
        current_index = self.main_stacked_widget.currentIndex()
        if current_index < self.main_stacked_widget.count() - 1:
            self.main_stacked_widget.setCurrentIndex(current_index + 1)

    def show_michu_previous(self):
        current_index = self.michu_stacked_widget.currentIndex()
        if current_index > 0:
            self.michu_stacked_widget.setCurrentIndex(current_index - 1)

    def show_michu_next(self):
        current_index = self.michu_stacked_widget.currentIndex()
        if current_index < self.michu_stacked_widget.count() - 1:
            self.michu_stacked_widget.setCurrentIndex(current_index + 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
