# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coopDesk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1033, 648)
        MainWindow.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy)
        self.icon_only_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align: center;\n"
"border-radius:10px;\n"
"text-alignment:center\n"
"\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_2_button = QPushButton(self.icon_only_widget)
        self.home_2_button.setObjectName(u"home_2_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.home_2_button.sizePolicy().hasHeightForWidth())
        self.home_2_button.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/images/home_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/home_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_2_button.setIcon(icon)
        self.home_2_button.setIconSize(QSize(32, 32))
        self.home_2_button.setCheckable(True)
        self.home_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2_button)

        self.app_2_button = QPushButton(self.icon_only_widget)
        self.app_2_button.setObjectName(u"app_2_button")
        icon1 = QIcon()
        icon1.addFile(u":/images/apps_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/apps_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.app_2_button.setIcon(icon1)
        self.app_2_button.setIconSize(QSize(32, 32))
        self.app_2_button.setCheckable(True)
        self.app_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.app_2_button)

        self.about_2_button = QPushButton(self.icon_only_widget)
        self.about_2_button.setObjectName(u"about_2_button")
        icon2 = QIcon()
        icon2.addFile(u":/images/about_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/images/about_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.about_2_button.setIcon(icon2)
        self.about_2_button.setIconSize(QSize(32, 32))
        self.about_2_button.setCheckable(True)
        self.about_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.about_2_button)

        self.update_2_button = QPushButton(self.icon_only_widget)
        self.update_2_button.setObjectName(u"update_2_button")
        icon3 = QIcon()
        icon3.addFile(u":/images/update_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/images/update_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.update_2_button.setIcon(icon3)
        self.update_2_button.setIconSize(QSize(32, 32))
        self.update_2_button.setCheckable(True)
        self.update_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_2_button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_2_button = QPushButton(self.icon_only_widget)
        self.exit_2_button.setObjectName(u"exit_2_button")
        icon4 = QIcon()
        icon4.addFile(u":/images/logout_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/images/logout_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.exit_2_button.setIcon(icon4)
        self.exit_2_button.setIconSize(QSize(32, 32))
        self.exit_2_button.setCheckable(True)
        self.exit_2_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.exit_2_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.icon_name_widget.sizePolicy().hasHeightForWidth())
        self.icon_name_widget.setSizePolicy(sizePolicy2)
        self.icon_name_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-top-left-radius:10px;\n"
"\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(48, 48))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 146, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.home_1_button = QPushButton(self.icon_name_widget)
        self.home_1_button.setObjectName(u"home_1_button")
        font1 = QFont()
        font1.setFamilies([u"Roboto Medium"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.home_1_button.setFont(font1)
        self.home_1_button.setIcon(icon)
        self.home_1_button.setIconSize(QSize(32, 32))
        self.home_1_button.setCheckable(True)
        self.home_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1_button)

        self.app_1_button = QPushButton(self.icon_name_widget)
        self.app_1_button.setObjectName(u"app_1_button")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.app_1_button.setFont(font2)
        self.app_1_button.setIcon(icon1)
        self.app_1_button.setIconSize(QSize(32, 32))
        self.app_1_button.setCheckable(True)
        self.app_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.app_1_button)

        self.about_1_button = QPushButton(self.icon_name_widget)
        self.about_1_button.setObjectName(u"about_1_button")
        self.about_1_button.setFont(font2)
        self.about_1_button.setIcon(icon2)
        self.about_1_button.setIconSize(QSize(32, 32))
        self.about_1_button.setCheckable(True)
        self.about_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.about_1_button)

        self.update_1_button = QPushButton(self.icon_name_widget)
        self.update_1_button.setObjectName(u"update_1_button")
        self.update_1_button.setFont(font2)
        self.update_1_button.setIcon(icon3)
        self.update_1_button.setIconSize(QSize(32, 32))
        self.update_1_button.setCheckable(True)
        self.update_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_1_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exit_1_button = QPushButton(self.icon_name_widget)
        self.exit_1_button.setObjectName(u"exit_1_button")
        self.exit_1_button.setFont(font2)
        self.exit_1_button.setIcon(icon4)
        self.exit_1_button.setIconSize(QSize(32, 32))
        self.exit_1_button.setCheckable(True)
        self.exit_1_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.exit_1_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(15)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy3)
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_19 = QPushButton(self.main_menu)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/images/menu_icon_blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/images/menu_icon_blue_inverted.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_19.setIcon(icon5)
        self.pushButton_19.setIconSize(QSize(24, 24))
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_19)

        self.horizontalSpacer = QSpacerItem(668, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.label_5 = QLabel(self.home_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 150, 181, 16))
        self.stackedWidget.addWidget(self.home_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_3 = QLabel(self.about_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 160, 171, 16))
        self.stackedWidget.addWidget(self.about_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.label_6 = QLabel(self.update_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 170, 221, 101))
        self.stackedWidget.addWidget(self.update_page)
        self.apps_page = QWidget()
        self.apps_page.setObjectName(u"apps_page")
        self.label_4 = QLabel(self.apps_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 110, 161, 111))
        self.stackedWidget.addWidget(self.apps_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_19.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_19.toggled.connect(self.icon_name_widget.setVisible)
        self.home_2_button.toggled.connect(self.home_1_button.setChecked)
        self.app_2_button.toggled.connect(self.app_1_button.setChecked)
        self.about_2_button.toggled.connect(self.about_1_button.setChecked)
        self.update_2_button.toggled.connect(self.update_1_button.setChecked)
        self.exit_2_button.toggled.connect(self.exit_1_button.setChecked)
        self.exit_1_button.toggled.connect(self.exit_2_button.setChecked)
        self.update_1_button.toggled.connect(self.update_2_button.setChecked)
        self.about_1_button.toggled.connect(self.about_2_button.setChecked)
        self.app_1_button.toggled.connect(self.app_2_button.setChecked)
        self.home_1_button.toggled.connect(self.home_2_button.setChecked)
        self.exit_2_button.toggled.connect(MainWindow.close)
        self.exit_1_button.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.home_2_button.setText("")
        self.app_2_button.setText("")
        self.about_2_button.setText("")
        self.update_2_button.setText("")
        self.exit_2_button.setText("")
        self.label_2.setText("")
        self.home_1_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.app_1_button.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.about_1_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.update_1_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.exit_1_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton_19.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Home_page", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About PAGE ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"update page ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apps Page", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coopDesk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1205, 748)
        MainWindow.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_19 = QPushButton(self.main_menu)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/menu_icon_blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/menu_icon_blue_inverted.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_19.setIcon(icon)
        self.pushButton_19.setIconSize(QSize(24, 24))
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_19)

        self.horizontalSpacer = QSpacerItem(668, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.gridLayout_2 = QGridLayout(self.home_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.pushButton = QPushButton(self.home_page)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.home_page)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.home_page)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.home_page)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.home_page)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.home_page)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.home_page)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.home_page)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_2.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.home_page)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_2.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_10 = QPushButton(self.home_page)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_2.addWidget(self.pushButton_10, 3, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.home_page)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_2.addWidget(self.pushButton_11, 3, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.home_page)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_2.addWidget(self.pushButton_12, 3, 2, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_3 = QLabel(self.about_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 65, 301, 111))
        self.stackedWidget.addWidget(self.about_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.label_6 = QLabel(self.update_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 170, 221, 101))
        self.stackedWidget.addWidget(self.update_page)
        self.apps_page = QWidget()
        self.apps_page.setObjectName(u"apps_page")
        self.label_4 = QLabel(self.apps_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 110, 161, 111))
        self.stackedWidget.addWidget(self.apps_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy1)
        self.icon_only_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align: center;\n"
"border-radius:10px;\n"
"text-alignment:center\n"
"\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_2_button = QPushButton(self.icon_only_widget)
        self.home_2_button.setObjectName(u"home_2_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_2_button.sizePolicy().hasHeightForWidth())
        self.home_2_button.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u":/images/home_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/home_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_2_button.setIcon(icon1)
        self.home_2_button.setIconSize(QSize(32, 32))
        self.home_2_button.setCheckable(True)
        self.home_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2_button)

        self.app_2_button = QPushButton(self.icon_only_widget)
        self.app_2_button.setObjectName(u"app_2_button")
        icon2 = QIcon()
        icon2.addFile(u":/images/apps_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/images/apps_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.app_2_button.setIcon(icon2)
        self.app_2_button.setIconSize(QSize(32, 32))
        self.app_2_button.setCheckable(True)
        self.app_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.app_2_button)

        self.about_2_button = QPushButton(self.icon_only_widget)
        self.about_2_button.setObjectName(u"about_2_button")
        icon3 = QIcon()
        icon3.addFile(u":/images/about_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/images/about_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.about_2_button.setIcon(icon3)
        self.about_2_button.setIconSize(QSize(32, 32))
        self.about_2_button.setCheckable(True)
        self.about_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.about_2_button)

        self.update_2_button = QPushButton(self.icon_only_widget)
        self.update_2_button.setObjectName(u"update_2_button")
        icon4 = QIcon()
        icon4.addFile(u":/images/update_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/images/update_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.update_2_button.setIcon(icon4)
        self.update_2_button.setIconSize(QSize(32, 32))
        self.update_2_button.setCheckable(True)
        self.update_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_2_button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_2_button = QPushButton(self.icon_only_widget)
        self.exit_2_button.setObjectName(u"exit_2_button")
        icon5 = QIcon()
        icon5.addFile(u":/images/logout_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/images/logout_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.exit_2_button.setIcon(icon5)
        self.exit_2_button.setIconSize(QSize(32, 32))
        self.exit_2_button.setCheckable(True)
        self.exit_2_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.exit_2_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.icon_name_widget.sizePolicy().hasHeightForWidth())
        self.icon_name_widget.setSizePolicy(sizePolicy3)
        self.icon_name_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-top-left-radius:10px;\n"
"\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(48, 48))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 146, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.home_1_button = QPushButton(self.icon_name_widget)
        self.home_1_button.setObjectName(u"home_1_button")
        font2 = QFont()
        font2.setFamilies([u"Roboto Medium"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.home_1_button.setFont(font2)
        self.home_1_button.setIcon(icon1)
        self.home_1_button.setIconSize(QSize(32, 32))
        self.home_1_button.setCheckable(True)
        self.home_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1_button)

        self.app_1_button = QPushButton(self.icon_name_widget)
        self.app_1_button.setObjectName(u"app_1_button")
        self.app_1_button.setFont(font1)
        self.app_1_button.setIcon(icon2)
        self.app_1_button.setIconSize(QSize(32, 32))
        self.app_1_button.setCheckable(True)
        self.app_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.app_1_button)

        self.about_1_button = QPushButton(self.icon_name_widget)
        self.about_1_button.setObjectName(u"about_1_button")
        self.about_1_button.setFont(font1)
        self.about_1_button.setIcon(icon3)
        self.about_1_button.setIconSize(QSize(32, 32))
        self.about_1_button.setCheckable(True)
        self.about_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.about_1_button)

        self.update_1_button = QPushButton(self.icon_name_widget)
        self.update_1_button.setObjectName(u"update_1_button")
        self.update_1_button.setFont(font1)
        self.update_1_button.setIcon(icon4)
        self.update_1_button.setIconSize(QSize(32, 32))
        self.update_1_button.setCheckable(True)
        self.update_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_1_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exit_1_button = QPushButton(self.icon_name_widget)
        self.exit_1_button.setObjectName(u"exit_1_button")
        self.exit_1_button.setFont(font1)
        self.exit_1_button.setIcon(icon5)
        self.exit_1_button.setIconSize(QSize(32, 32))
        self.exit_1_button.setCheckable(True)
        self.exit_1_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.exit_1_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_19.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_19.toggled.connect(self.icon_name_widget.setVisible)
        self.home_2_button.toggled.connect(self.home_1_button.setChecked)
        self.app_2_button.toggled.connect(self.app_1_button.setChecked)
        self.about_2_button.toggled.connect(self.about_1_button.setChecked)
        self.update_2_button.toggled.connect(self.update_1_button.setChecked)
        self.exit_2_button.toggled.connect(self.exit_1_button.setChecked)
        self.exit_1_button.toggled.connect(self.exit_2_button.setChecked)
        self.update_1_button.toggled.connect(self.update_2_button.setChecked)
        self.about_1_button.toggled.connect(self.about_2_button.setChecked)
        self.app_1_button.toggled.connect(self.app_2_button.setChecked)
        self.home_1_button.toggled.connect(self.home_2_button.setChecked)
        self.exit_2_button.toggled.connect(MainWindow.close)
        self.exit_1_button.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_19.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About PAGE ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"update page ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apps Page", None))
        self.label.setText("")
        self.home_2_button.setText("")
        self.app_2_button.setText("")
        self.about_2_button.setText("")
        self.update_2_button.setText("")
        self.exit_2_button.setText("")
        self.label_2.setText("")
        self.home_1_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.app_1_button.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.about_1_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.update_1_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.exit_1_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coopDesk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1205, 748)
        MainWindow.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_19 = QPushButton(self.main_menu)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/menu_icon_blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/menu_icon_blue_inverted.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_19.setIcon(icon)
        self.pushButton_19.setIconSize(QSize(24, 24))
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_19)

        self.horizontalSpacer = QSpacerItem(668, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"QPushButton{\n"
" border-radius: 40px;\n"
"  background: qlineargradient(\n"
"                    x1: 0, y1: 0, x2: 1, y2: 1,\n"
"                    stop: 0 #00AEEF, stop: 1 #08B0F0\n"
"                );\n"
"  border: none;\n"
"height :100px\n"
"\n"
"}")
        self.gridLayout_2 = QGridLayout(self.home_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.pushButton_11 = QPushButton(self.home_page)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_2.addWidget(self.pushButton_11, 3, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.home_page)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_2.addWidget(self.pushButton_12, 3, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.home_page)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_2.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.home_page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.home_page)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.home_page)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.home_page)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.home_page)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_2.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.home_page)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.home_page)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_2.addWidget(self.pushButton_10, 3, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.home_page)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.home_page)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_3 = QLabel(self.about_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 65, 301, 111))
        self.stackedWidget.addWidget(self.about_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.label_6 = QLabel(self.update_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 170, 221, 101))
        self.stackedWidget.addWidget(self.update_page)
        self.apps_page = QWidget()
        self.apps_page.setObjectName(u"apps_page")
        self.label_4 = QLabel(self.apps_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 110, 161, 111))
        self.stackedWidget.addWidget(self.apps_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy1)
        self.icon_only_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align: center;\n"
"border-radius:10px;\n"
"text-alignment:center\n"
"\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_2_button = QPushButton(self.icon_only_widget)
        self.home_2_button.setObjectName(u"home_2_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_2_button.sizePolicy().hasHeightForWidth())
        self.home_2_button.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u":/images/home_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/home_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_2_button.setIcon(icon1)
        self.home_2_button.setIconSize(QSize(32, 32))
        self.home_2_button.setCheckable(True)
        self.home_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2_button)

        self.app_2_button = QPushButton(self.icon_only_widget)
        self.app_2_button.setObjectName(u"app_2_button")
        icon2 = QIcon()
        icon2.addFile(u":/images/apps_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/images/apps_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.app_2_button.setIcon(icon2)
        self.app_2_button.setIconSize(QSize(32, 32))
        self.app_2_button.setCheckable(True)
        self.app_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.app_2_button)

        self.about_2_button = QPushButton(self.icon_only_widget)
        self.about_2_button.setObjectName(u"about_2_button")
        icon3 = QIcon()
        icon3.addFile(u":/images/about_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/images/about_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.about_2_button.setIcon(icon3)
        self.about_2_button.setIconSize(QSize(32, 32))
        self.about_2_button.setCheckable(True)
        self.about_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.about_2_button)

        self.update_2_button = QPushButton(self.icon_only_widget)
        self.update_2_button.setObjectName(u"update_2_button")
        icon4 = QIcon()
        icon4.addFile(u":/images/update_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/images/update_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.update_2_button.setIcon(icon4)
        self.update_2_button.setIconSize(QSize(32, 32))
        self.update_2_button.setCheckable(True)
        self.update_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_2_button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_2_button = QPushButton(self.icon_only_widget)
        self.exit_2_button.setObjectName(u"exit_2_button")
        icon5 = QIcon()
        icon5.addFile(u":/images/logout_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/images/logout_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.exit_2_button.setIcon(icon5)
        self.exit_2_button.setIconSize(QSize(32, 32))
        self.exit_2_button.setCheckable(True)
        self.exit_2_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.exit_2_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.icon_name_widget.sizePolicy().hasHeightForWidth())
        self.icon_name_widget.setSizePolicy(sizePolicy3)
        self.icon_name_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-top-left-radius:10px;\n"
"\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(48, 48))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 146, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.home_1_button = QPushButton(self.icon_name_widget)
        self.home_1_button.setObjectName(u"home_1_button")
        font2 = QFont()
        font2.setFamilies([u"Roboto Medium"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.home_1_button.setFont(font2)
        self.home_1_button.setIcon(icon1)
        self.home_1_button.setIconSize(QSize(32, 32))
        self.home_1_button.setCheckable(True)
        self.home_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1_button)

        self.app_1_button = QPushButton(self.icon_name_widget)
        self.app_1_button.setObjectName(u"app_1_button")
        self.app_1_button.setFont(font1)
        self.app_1_button.setIcon(icon2)
        self.app_1_button.setIconSize(QSize(32, 32))
        self.app_1_button.setCheckable(True)
        self.app_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.app_1_button)

        self.about_1_button = QPushButton(self.icon_name_widget)
        self.about_1_button.setObjectName(u"about_1_button")
        self.about_1_button.setFont(font1)
        self.about_1_button.setIcon(icon3)
        self.about_1_button.setIconSize(QSize(32, 32))
        self.about_1_button.setCheckable(True)
        self.about_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.about_1_button)

        self.update_1_button = QPushButton(self.icon_name_widget)
        self.update_1_button.setObjectName(u"update_1_button")
        self.update_1_button.setFont(font1)
        self.update_1_button.setIcon(icon4)
        self.update_1_button.setIconSize(QSize(32, 32))
        self.update_1_button.setCheckable(True)
        self.update_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_1_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exit_1_button = QPushButton(self.icon_name_widget)
        self.exit_1_button.setObjectName(u"exit_1_button")
        self.exit_1_button.setFont(font1)
        self.exit_1_button.setIcon(icon5)
        self.exit_1_button.setIconSize(QSize(32, 32))
        self.exit_1_button.setCheckable(True)
        self.exit_1_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.exit_1_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_19.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_19.toggled.connect(self.icon_name_widget.setVisible)
        self.home_2_button.toggled.connect(self.home_1_button.setChecked)
        self.app_2_button.toggled.connect(self.app_1_button.setChecked)
        self.about_2_button.toggled.connect(self.about_1_button.setChecked)
        self.update_2_button.toggled.connect(self.update_1_button.setChecked)
        self.exit_2_button.toggled.connect(self.exit_1_button.setChecked)
        self.exit_1_button.toggled.connect(self.exit_2_button.setChecked)
        self.update_1_button.toggled.connect(self.update_2_button.setChecked)
        self.about_1_button.toggled.connect(self.about_2_button.setChecked)
        self.app_1_button.toggled.connect(self.app_2_button.setChecked)
        self.home_1_button.toggled.connect(self.home_2_button.setChecked)
        self.exit_2_button.toggled.connect(MainWindow.close)
        self.exit_1_button.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_19.setText("")
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"CAO Cash Management ", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Coop History", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Coop Alhuda", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PC info", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PhoneBook", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"CoopURL", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Michu", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"CoopayEbirr", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Coop Conventional Product ", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"COOPAPP", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Remittance Guide", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"CRM Guide", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About PAGE ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"update page ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apps Page", None))
        self.label.setText("")
        self.home_2_button.setText("")
        self.app_2_button.setText("")
        self.about_2_button.setText("")
        self.update_2_button.setText("")
        self.exit_2_button.setText("")
        self.label_2.setText("")
        self.home_1_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.app_1_button.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.about_1_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.update_1_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.exit_1_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coopDesk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1199, 735)
        MainWindow.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_19 = QPushButton(self.main_menu)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/menu_icon_blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/menu_icon_blue_inverted.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_19.setIcon(icon)
        self.pushButton_19.setIconSize(QSize(24, 24))
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_19)

        self.horizontalSpacer = QSpacerItem(668, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"QPushButton{\n"
" border-radius: 40px;\n"
"  background: qlineargradient(\n"
"                    x1: 0, y1: 0, x2: 1, y2: 1,\n"
"                    stop: 0 #00AEEF, stop: 1 #08B0F0\n"
"                );\n"
"  border: none;\n"
"height :100px\n"
"\n"
"}")
        self.gridLayout_2 = QGridLayout(self.home_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.pushButton_11 = QPushButton(self.home_page)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_2.addWidget(self.pushButton_11, 3, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.home_page)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_2.addWidget(self.pushButton_12, 3, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.home_page)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_2.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pcinfo_button = QPushButton(self.home_page)
        self.pcinfo_button.setObjectName(u"pcinfo_button")
        self.pcinfo_button.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.pcinfo_button, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.home_page)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.home_page)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.home_page)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.home_page)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_2.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.home_page)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.home_page)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_2.addWidget(self.pushButton_10, 3, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.home_page)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.home_page)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_3 = QLabel(self.about_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 65, 301, 111))
        self.stackedWidget.addWidget(self.about_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.label_6 = QLabel(self.update_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 170, 221, 101))
        self.stackedWidget.addWidget(self.update_page)
        self.pc_info_page = QWidget()
        self.pc_info_page.setObjectName(u"pc_info_page")
        self.widget = QWidget(self.pc_info_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 291, 251))
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 30, 181, 21))
        self.widget_2 = QWidget(self.pc_info_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(330, 20, 301, 251))
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 30, 171, 21))
        self.widget_3 = QWidget(self.pc_info_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(650, 20, 301, 251))
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 30, 171, 21))
        self.widget_4 = QWidget(self.pc_info_page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(20, 260, 301, 251))
        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 30, 171, 21))
        self.stackedWidget.addWidget(self.pc_info_page)
        self.apps_page = QWidget()
        self.apps_page.setObjectName(u"apps_page")
        self.label_4 = QLabel(self.apps_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 110, 161, 111))
        self.stackedWidget.addWidget(self.apps_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy1)
        self.icon_only_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align: center;\n"
"border-radius:10px;\n"
"text-alignment:center\n"
"\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_2_button = QPushButton(self.icon_only_widget)
        self.home_2_button.setObjectName(u"home_2_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_2_button.sizePolicy().hasHeightForWidth())
        self.home_2_button.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u":/images/home_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/home_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_2_button.setIcon(icon1)
        self.home_2_button.setIconSize(QSize(32, 32))
        self.home_2_button.setCheckable(True)
        self.home_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2_button)

        self.app_2_button = QPushButton(self.icon_only_widget)
        self.app_2_button.setObjectName(u"app_2_button")
        icon2 = QIcon()
        icon2.addFile(u":/images/apps_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/images/apps_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.app_2_button.setIcon(icon2)
        self.app_2_button.setIconSize(QSize(32, 32))
        self.app_2_button.setCheckable(True)
        self.app_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.app_2_button)

        self.about_2_button = QPushButton(self.icon_only_widget)
        self.about_2_button.setObjectName(u"about_2_button")
        icon3 = QIcon()
        icon3.addFile(u":/images/about_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/images/about_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.about_2_button.setIcon(icon3)
        self.about_2_button.setIconSize(QSize(32, 32))
        self.about_2_button.setCheckable(True)
        self.about_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.about_2_button)

        self.update_2_button = QPushButton(self.icon_only_widget)
        self.update_2_button.setObjectName(u"update_2_button")
        icon4 = QIcon()
        icon4.addFile(u":/images/update_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/images/update_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.update_2_button.setIcon(icon4)
        self.update_2_button.setIconSize(QSize(32, 32))
        self.update_2_button.setCheckable(True)
        self.update_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_2_button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_2_button = QPushButton(self.icon_only_widget)
        self.exit_2_button.setObjectName(u"exit_2_button")
        icon5 = QIcon()
        icon5.addFile(u":/images/logout_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/images/logout_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.exit_2_button.setIcon(icon5)
        self.exit_2_button.setIconSize(QSize(32, 32))
        self.exit_2_button.setCheckable(True)
        self.exit_2_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.exit_2_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.icon_name_widget.sizePolicy().hasHeightForWidth())
        self.icon_name_widget.setSizePolicy(sizePolicy3)
        self.icon_name_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-top-left-radius:10px;\n"
"\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(48, 48))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 146, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.home_1_button = QPushButton(self.icon_name_widget)
        self.home_1_button.setObjectName(u"home_1_button")
        font2 = QFont()
        font2.setFamilies([u"Roboto Medium"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.home_1_button.setFont(font2)
        self.home_1_button.setIcon(icon1)
        self.home_1_button.setIconSize(QSize(32, 32))
        self.home_1_button.setCheckable(True)
        self.home_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1_button)

        self.app_1_button = QPushButton(self.icon_name_widget)
        self.app_1_button.setObjectName(u"app_1_button")
        self.app_1_button.setFont(font1)
        self.app_1_button.setIcon(icon2)
        self.app_1_button.setIconSize(QSize(32, 32))
        self.app_1_button.setCheckable(True)
        self.app_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.app_1_button)

        self.about_1_button = QPushButton(self.icon_name_widget)
        self.about_1_button.setObjectName(u"about_1_button")
        self.about_1_button.setFont(font1)
        self.about_1_button.setIcon(icon3)
        self.about_1_button.setIconSize(QSize(32, 32))
        self.about_1_button.setCheckable(True)
        self.about_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.about_1_button)

        self.update_1_button = QPushButton(self.icon_name_widget)
        self.update_1_button.setObjectName(u"update_1_button")
        self.update_1_button.setFont(font1)
        self.update_1_button.setIcon(icon4)
        self.update_1_button.setIconSize(QSize(32, 32))
        self.update_1_button.setCheckable(True)
        self.update_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_1_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exit_1_button = QPushButton(self.icon_name_widget)
        self.exit_1_button.setObjectName(u"exit_1_button")
        self.exit_1_button.setFont(font1)
        self.exit_1_button.setIcon(icon5)
        self.exit_1_button.setIconSize(QSize(32, 32))
        self.exit_1_button.setCheckable(True)
        self.exit_1_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.exit_1_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_19.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_19.toggled.connect(self.icon_name_widget.setVisible)
        self.home_2_button.toggled.connect(self.home_1_button.setChecked)
        self.app_2_button.toggled.connect(self.app_1_button.setChecked)
        self.about_2_button.toggled.connect(self.about_1_button.setChecked)
        self.update_2_button.toggled.connect(self.update_1_button.setChecked)
        self.exit_2_button.toggled.connect(self.exit_1_button.setChecked)
        self.exit_1_button.toggled.connect(self.exit_2_button.setChecked)
        self.update_1_button.toggled.connect(self.update_2_button.setChecked)
        self.about_1_button.toggled.connect(self.about_2_button.setChecked)
        self.app_1_button.toggled.connect(self.app_2_button.setChecked)
        self.home_1_button.toggled.connect(self.home_2_button.setChecked)
        self.exit_2_button.toggled.connect(MainWindow.close)
        self.exit_1_button.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_19.setText("")
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"CAO Cash Management ", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Coop History", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Coop Alhuda", None))
        self.pcinfo_button.setText(QCoreApplication.translate("MainWindow", u"PC info", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PhoneBook", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"CoopURL", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Michu", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"CoopayEbirr", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Coop Conventional Product ", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"COOPAPP", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Remittance Guide", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"CRM Guide", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About PAGE ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"update page ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Network Information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ram Usage", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Disk Usage", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apps Page", None))
        self.label.setText("")
        self.home_2_button.setText("")
        self.app_2_button.setText("")
        self.about_2_button.setText("")
        self.update_2_button.setText("")
        self.exit_2_button.setText("")
        self.label_2.setText("")
        self.home_1_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.app_1_button.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.about_1_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.update_1_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.exit_1_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coopDesk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1199, 735)
        MainWindow.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_19 = QPushButton(self.main_menu)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/menu_icon_blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/menu_icon_blue_inverted.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_19.setIcon(icon)
        self.pushButton_19.setIconSize(QSize(24, 24))
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_19)

        self.horizontalSpacer = QSpacerItem(668, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"QPushButton{\n"
" border-radius: 40px;\n"
"  background: qlineargradient(\n"
"                    x1: 0, y1: 0, x2: 1, y2: 1,\n"
"                    stop: 0 #00AEEF, stop: 1 #08B0F0\n"
"                );\n"
"  border: none;\n"
"height :100px\n"
"\n"
"}")
        self.gridLayout_2 = QGridLayout(self.home_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.pushButton_11 = QPushButton(self.home_page)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_2.addWidget(self.pushButton_11, 3, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.home_page)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_2.addWidget(self.pushButton_12, 3, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.home_page)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_2.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.home_page)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/images/netconfig.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.home_page)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.home_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon2 = QIcon()
        icon2.addFile(u":/images/Vector.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(64, 128))

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.home_page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon3 = QIcon()
        icon3.addFile(u":/images/michu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.home_page)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_2.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.home_page)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.home_page)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_2.addWidget(self.pushButton_10, 3, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.home_page)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.home_page)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_3 = QLabel(self.about_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 65, 301, 111))
        self.stackedWidget.addWidget(self.about_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.label_6 = QLabel(self.update_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 170, 221, 101))
        self.stackedWidget.addWidget(self.update_page)
        self.pc_info_page = QWidget()
        self.pc_info_page.setObjectName(u"pc_info_page")
        self.widget = QWidget(self.pc_info_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 291, 251))
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 30, 181, 21))
        self.widget_2 = QWidget(self.pc_info_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(330, 20, 301, 251))
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 30, 171, 21))
        self.widget_3 = QWidget(self.pc_info_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(650, 20, 301, 251))
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 30, 171, 21))
        self.widget_4 = QWidget(self.pc_info_page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(20, 260, 301, 251))
        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 30, 171, 21))
        self.stackedWidget.addWidget(self.pc_info_page)
        self.apps_page = QWidget()
        self.apps_page.setObjectName(u"apps_page")
        self.label_4 = QLabel(self.apps_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 110, 161, 111))
        self.stackedWidget.addWidget(self.apps_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy1)
        self.icon_only_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align: center;\n"
"border-radius:10px;\n"
"text-alignment:center\n"
"\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_2_button = QPushButton(self.icon_only_widget)
        self.home_2_button.setObjectName(u"home_2_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_2_button.sizePolicy().hasHeightForWidth())
        self.home_2_button.setSizePolicy(sizePolicy2)
        icon4 = QIcon()
        icon4.addFile(u":/images/home_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/images/home_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_2_button.setIcon(icon4)
        self.home_2_button.setIconSize(QSize(32, 32))
        self.home_2_button.setCheckable(True)
        self.home_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2_button)

        self.app_2_button = QPushButton(self.icon_only_widget)
        self.app_2_button.setObjectName(u"app_2_button")
        icon5 = QIcon()
        icon5.addFile(u":/images/apps_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/images/apps_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.app_2_button.setIcon(icon5)
        self.app_2_button.setIconSize(QSize(32, 32))
        self.app_2_button.setCheckable(True)
        self.app_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.app_2_button)

        self.about_2_button = QPushButton(self.icon_only_widget)
        self.about_2_button.setObjectName(u"about_2_button")
        icon6 = QIcon()
        icon6.addFile(u":/images/about_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/images/about_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.about_2_button.setIcon(icon6)
        self.about_2_button.setIconSize(QSize(32, 32))
        self.about_2_button.setCheckable(True)
        self.about_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.about_2_button)

        self.update_2_button = QPushButton(self.icon_only_widget)
        self.update_2_button.setObjectName(u"update_2_button")
        icon7 = QIcon()
        icon7.addFile(u":/images/update_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/images/update_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.update_2_button.setIcon(icon7)
        self.update_2_button.setIconSize(QSize(32, 32))
        self.update_2_button.setCheckable(True)
        self.update_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_2_button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_2_button = QPushButton(self.icon_only_widget)
        self.exit_2_button.setObjectName(u"exit_2_button")
        icon8 = QIcon()
        icon8.addFile(u":/images/logout_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/images/logout_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.exit_2_button.setIcon(icon8)
        self.exit_2_button.setIconSize(QSize(32, 32))
        self.exit_2_button.setCheckable(True)
        self.exit_2_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.exit_2_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.icon_name_widget.sizePolicy().hasHeightForWidth())
        self.icon_name_widget.setSizePolicy(sizePolicy3)
        self.icon_name_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-top-left-radius:10px;\n"
"\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(48, 48))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 146, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.home_1_button = QPushButton(self.icon_name_widget)
        self.home_1_button.setObjectName(u"home_1_button")
        font3 = QFont()
        font3.setFamilies([u"Roboto Medium"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.home_1_button.setFont(font3)
        self.home_1_button.setIcon(icon4)
        self.home_1_button.setIconSize(QSize(32, 32))
        self.home_1_button.setCheckable(True)
        self.home_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1_button)

        self.app_1_button = QPushButton(self.icon_name_widget)
        self.app_1_button.setObjectName(u"app_1_button")
        self.app_1_button.setFont(font1)
        self.app_1_button.setIcon(icon5)
        self.app_1_button.setIconSize(QSize(32, 32))
        self.app_1_button.setCheckable(True)
        self.app_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.app_1_button)

        self.about_1_button = QPushButton(self.icon_name_widget)
        self.about_1_button.setObjectName(u"about_1_button")
        self.about_1_button.setFont(font1)
        self.about_1_button.setIcon(icon6)
        self.about_1_button.setIconSize(QSize(32, 32))
        self.about_1_button.setCheckable(True)
        self.about_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.about_1_button)

        self.update_1_button = QPushButton(self.icon_name_widget)
        self.update_1_button.setObjectName(u"update_1_button")
        self.update_1_button.setFont(font1)
        self.update_1_button.setIcon(icon7)
        self.update_1_button.setIconSize(QSize(32, 32))
        self.update_1_button.setCheckable(True)
        self.update_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_1_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exit_1_button = QPushButton(self.icon_name_widget)
        self.exit_1_button.setObjectName(u"exit_1_button")
        self.exit_1_button.setFont(font1)
        self.exit_1_button.setIcon(icon8)
        self.exit_1_button.setIconSize(QSize(32, 32))
        self.exit_1_button.setCheckable(True)
        self.exit_1_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.exit_1_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_19.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_19.toggled.connect(self.icon_name_widget.setVisible)
        self.home_2_button.toggled.connect(self.home_1_button.setChecked)
        self.app_2_button.toggled.connect(self.app_1_button.setChecked)
        self.about_2_button.toggled.connect(self.about_1_button.setChecked)
        self.update_2_button.toggled.connect(self.update_1_button.setChecked)
        self.exit_2_button.toggled.connect(self.exit_1_button.setChecked)
        self.exit_1_button.toggled.connect(self.exit_2_button.setChecked)
        self.update_1_button.toggled.connect(self.update_2_button.setChecked)
        self.about_1_button.toggled.connect(self.about_2_button.setChecked)
        self.app_1_button.toggled.connect(self.app_2_button.setChecked)
        self.home_1_button.toggled.connect(self.home_2_button.setChecked)
        self.exit_2_button.toggled.connect(MainWindow.close)
        self.exit_1_button.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_19.setText("")
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"CAO Cash Management ", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Coop History", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Coop Alhuda", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PC info", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PhoneBook", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"CoopURL", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Michu", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"CoopayEbirr", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Coop Conventional Product ", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"COOPAPP", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Remittance Guide", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"CRM Guide", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About PAGE ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"update page ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Network Information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ram Usage", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Disk Usage", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apps Page", None))
        self.label.setText("")
        self.home_2_button.setText("")
        self.app_2_button.setText("")
        self.about_2_button.setText("")
        self.update_2_button.setText("")
        self.exit_2_button.setText("")
        self.label_2.setText("")
        self.home_1_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.app_1_button.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.about_1_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.update_1_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.exit_1_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coopDesk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1199, 735)
        MainWindow.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_19 = QPushButton(self.main_menu)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/menu_icon_blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/menu_icon_blue_inverted.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_19.setIcon(icon)
        self.pushButton_19.setIconSize(QSize(24, 24))
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_19)

        self.horizontalSpacer = QSpacerItem(668, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"QPushButton{\n"
"  background:none;\n"
"  border: none;\n"
"\n"
"\n"
"}")
        self.gridLayout_2 = QGridLayout(self.home_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.pushButton_11 = QPushButton(self.home_page)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon1 = QIcon()
        icon1.addFile(u":/homeicons/teller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_11, 3, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.home_page)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon2 = QIcon()
        icon2.addFile(u":/homeicons/about_coop.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/homeicons/conventinal_products.png", QSize(), QIcon.Selected, QIcon.On)
        self.pushButton_12.setIcon(icon2)
        self.pushButton_12.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_12, 3, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.home_page)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon3 = QIcon()
        icon3.addFile(u":/homeicons/alhuda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.home_page)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon4 = QIcon()
        icon4.addFile(u":/homeicons/phonebook.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.home_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon5 = QIcon()
        icon5.addFile(u":/homeicons/coopurl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.home_page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon6 = QIcon()
        icon6.addFile(u":/homeicons/michu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon6)
        self.pushButton_3.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.home_page)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon7 = QIcon()
        icon7.addFile(u":/homeicons/coopay.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.home_page)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon8 = QIcon()
        icon8.addFile(u":/homeicons/conventinal_products.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.home_page)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon9 = QIcon()
        icon9.addFile(u":/homeicons/coopapp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon9)
        self.pushButton_10.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_10, 3, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.home_page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon10 = QIcon()
        icon10.addFile(u":/homeicons/remittance.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon10)
        self.pushButton_4.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.home_page)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon11 = QIcon()
        icon11.addFile(u":/homeicons/atm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon11)
        self.pushButton_5.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pcinfo_button = QPushButton(self.home_page)
        self.pcinfo_button.setObjectName(u"pcinfo_button")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        self.pcinfo_button.setFont(font2)
        self.pcinfo_button.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/homeicons/pcinfo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pcinfo_button.setIcon(icon12)
        self.pcinfo_button.setIconSize(QSize(128, 128))
        self.pcinfo_button.setCheckable(True)

        self.gridLayout_2.addWidget(self.pcinfo_button, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_3 = QLabel(self.about_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 65, 301, 111))
        self.stackedWidget.addWidget(self.about_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.label_6 = QLabel(self.update_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 170, 221, 101))
        self.stackedWidget.addWidget(self.update_page)
        self.pc_info_page = QWidget()
        self.pc_info_page.setObjectName(u"pc_info_page")
        self.widget = QWidget(self.pc_info_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 291, 251))
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 30, 181, 21))
        self.widget_2 = QWidget(self.pc_info_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(330, 20, 301, 251))
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 30, 171, 21))
        self.widget_3 = QWidget(self.pc_info_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(650, 20, 301, 251))
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 30, 171, 21))
        self.widget_4 = QWidget(self.pc_info_page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(20, 260, 301, 251))
        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 30, 171, 21))
        self.stackedWidget.addWidget(self.pc_info_page)
        self.apps_page = QWidget()
        self.apps_page.setObjectName(u"apps_page")
        self.label_4 = QLabel(self.apps_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 110, 161, 111))
        self.stackedWidget.addWidget(self.apps_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy1)
        self.icon_only_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align: center;\n"
"border-radius:10px;\n"
"text-alignment:center\n"
"\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_2_button = QPushButton(self.icon_only_widget)
        self.home_2_button.setObjectName(u"home_2_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_2_button.sizePolicy().hasHeightForWidth())
        self.home_2_button.setSizePolicy(sizePolicy2)
        icon13 = QIcon()
        icon13.addFile(u":/images/home_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/images/home_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_2_button.setIcon(icon13)
        self.home_2_button.setIconSize(QSize(32, 32))
        self.home_2_button.setCheckable(True)
        self.home_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2_button)

        self.app_2_button = QPushButton(self.icon_only_widget)
        self.app_2_button.setObjectName(u"app_2_button")
        icon14 = QIcon()
        icon14.addFile(u":/images/apps_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon14.addFile(u":/images/apps_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.app_2_button.setIcon(icon14)
        self.app_2_button.setIconSize(QSize(32, 32))
        self.app_2_button.setCheckable(True)
        self.app_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.app_2_button)

        self.about_2_button = QPushButton(self.icon_only_widget)
        self.about_2_button.setObjectName(u"about_2_button")
        icon15 = QIcon()
        icon15.addFile(u":/images/about_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon15.addFile(u":/images/about_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.about_2_button.setIcon(icon15)
        self.about_2_button.setIconSize(QSize(32, 32))
        self.about_2_button.setCheckable(True)
        self.about_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.about_2_button)

        self.update_2_button = QPushButton(self.icon_only_widget)
        self.update_2_button.setObjectName(u"update_2_button")
        icon16 = QIcon()
        icon16.addFile(u":/images/update_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon16.addFile(u":/images/update_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.update_2_button.setIcon(icon16)
        self.update_2_button.setIconSize(QSize(32, 32))
        self.update_2_button.setCheckable(True)
        self.update_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_2_button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_2_button = QPushButton(self.icon_only_widget)
        self.exit_2_button.setObjectName(u"exit_2_button")
        icon17 = QIcon()
        icon17.addFile(u":/images/logout_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon17.addFile(u":/images/logout_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.exit_2_button.setIcon(icon17)
        self.exit_2_button.setIconSize(QSize(32, 32))
        self.exit_2_button.setCheckable(True)
        self.exit_2_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.exit_2_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.icon_name_widget.sizePolicy().hasHeightForWidth())
        self.icon_name_widget.setSizePolicy(sizePolicy3)
        self.icon_name_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-top-left-radius:10px;\n"
"\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(48, 48))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 146, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.home_1_button = QPushButton(self.icon_name_widget)
        self.home_1_button.setObjectName(u"home_1_button")
        font3 = QFont()
        font3.setFamilies([u"Roboto Medium"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.home_1_button.setFont(font3)
        self.home_1_button.setIcon(icon13)
        self.home_1_button.setIconSize(QSize(32, 32))
        self.home_1_button.setCheckable(True)
        self.home_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1_button)

        self.app_1_button = QPushButton(self.icon_name_widget)
        self.app_1_button.setObjectName(u"app_1_button")
        self.app_1_button.setFont(font1)
        self.app_1_button.setIcon(icon14)
        self.app_1_button.setIconSize(QSize(32, 32))
        self.app_1_button.setCheckable(True)
        self.app_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.app_1_button)

        self.about_1_button = QPushButton(self.icon_name_widget)
        self.about_1_button.setObjectName(u"about_1_button")
        self.about_1_button.setFont(font1)
        self.about_1_button.setIcon(icon15)
        self.about_1_button.setIconSize(QSize(32, 32))
        self.about_1_button.setCheckable(True)
        self.about_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.about_1_button)

        self.update_1_button = QPushButton(self.icon_name_widget)
        self.update_1_button.setObjectName(u"update_1_button")
        self.update_1_button.setFont(font1)
        self.update_1_button.setIcon(icon16)
        self.update_1_button.setIconSize(QSize(32, 32))
        self.update_1_button.setCheckable(True)
        self.update_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_1_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exit_1_button = QPushButton(self.icon_name_widget)
        self.exit_1_button.setObjectName(u"exit_1_button")
        self.exit_1_button.setFont(font1)
        self.exit_1_button.setIcon(icon17)
        self.exit_1_button.setIconSize(QSize(32, 32))
        self.exit_1_button.setCheckable(True)
        self.exit_1_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.exit_1_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_19.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_19.toggled.connect(self.icon_name_widget.setVisible)
        self.home_2_button.toggled.connect(self.home_1_button.setChecked)
        self.app_2_button.toggled.connect(self.app_1_button.setChecked)
        self.about_2_button.toggled.connect(self.about_1_button.setChecked)
        self.update_2_button.toggled.connect(self.update_1_button.setChecked)
        self.exit_2_button.toggled.connect(self.exit_1_button.setChecked)
        self.exit_1_button.toggled.connect(self.exit_2_button.setChecked)
        self.update_1_button.toggled.connect(self.update_2_button.setChecked)
        self.about_1_button.toggled.connect(self.about_2_button.setChecked)
        self.app_1_button.toggled.connect(self.app_2_button.setChecked)
        self.home_1_button.toggled.connect(self.home_2_button.setChecked)
        self.exit_2_button.toggled.connect(MainWindow.close)
        self.exit_1_button.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_19.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_8.setText("")
        self.pushButton_6.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_9.setText("")
        self.pushButton_7.setText("")
        self.pushButton_10.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
#if QT_CONFIG(tooltip)
        self.pcinfo_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>PC Information</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pcinfo_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About PAGE ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"update page ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Network Information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ram Usage", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Disk Usage", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apps Page", None))
        self.label.setText("")
        self.home_2_button.setText("")
        self.app_2_button.setText("")
        self.about_2_button.setText("")
        self.update_2_button.setText("")
        self.exit_2_button.setText("")
        self.label_2.setText("")
        self.home_1_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.app_1_button.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.about_1_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.update_1_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.exit_1_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coopDesk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1199, 735)
        MainWindow.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_19 = QPushButton(self.main_menu)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/menu_icon_blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/menu_icon_blue_inverted.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_19.setIcon(icon)
        self.pushButton_19.setIconSize(QSize(24, 24))
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_19)

        self.horizontalSpacer = QSpacerItem(668, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"QPushButton{\n"
"  background:none;\n"
"  border: none;\n"
"\n"
"\n"
"}")
        self.gridLayout_2 = QGridLayout(self.home_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.pushButton_11 = QPushButton(self.home_page)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon1 = QIcon()
        icon1.addFile(u":/homeicons/teller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_11, 3, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.home_page)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon2 = QIcon()
        icon2.addFile(u":/homeicons/about_coop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon2)
        self.pushButton_12.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_12, 3, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.home_page)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon3 = QIcon()
        icon3.addFile(u":/homeicons/alhuda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.home_page)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon4 = QIcon()
        icon4.addFile(u":/homeicons/phonebook.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.home_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon5 = QIcon()
        icon5.addFile(u":/homeicons/coopurl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.home_page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon6 = QIcon()
        icon6.addFile(u":/homeicons/michu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon6)
        self.pushButton_3.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.home_page)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon7 = QIcon()
        icon7.addFile(u":/homeicons/coopay.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.home_page)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon8 = QIcon()
        icon8.addFile(u":/homeicons/conventinal_products.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.home_page)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon9 = QIcon()
        icon9.addFile(u":/homeicons/coopapp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon9)
        self.pushButton_10.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_10, 3, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.home_page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon10 = QIcon()
        icon10.addFile(u":/homeicons/remittance.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon10)
        self.pushButton_4.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.home_page)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon11 = QIcon()
        icon11.addFile(u":/homeicons/atm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon11)
        self.pushButton_5.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton = QPushButton(self.home_page)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/homeicons/pcinfo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon12)
        self.pushButton.setIconSize(QSize(128, 128))
        self.pushButton.setCheckable(True)

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_3 = QLabel(self.about_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 65, 301, 111))
        self.stackedWidget.addWidget(self.about_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.label_6 = QLabel(self.update_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 170, 221, 101))
        self.stackedWidget.addWidget(self.update_page)
        self.pc_info_page = QWidget()
        self.pc_info_page.setObjectName(u"pc_info_page")
        self.widget = QWidget(self.pc_info_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 291, 251))
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 30, 181, 21))
        self.widget_2 = QWidget(self.pc_info_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(330, 20, 301, 251))
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 30, 171, 21))
        self.widget_3 = QWidget(self.pc_info_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(650, 20, 301, 251))
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 30, 171, 21))
        self.widget_4 = QWidget(self.pc_info_page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(20, 260, 301, 251))
        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 30, 171, 21))
        self.stackedWidget.addWidget(self.pc_info_page)
        self.apps_page = QWidget()
        self.apps_page.setObjectName(u"apps_page")
        self.label_4 = QLabel(self.apps_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 110, 161, 111))
        self.stackedWidget.addWidget(self.apps_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy1)
        self.icon_only_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align: center;\n"
"border-radius:10px;\n"
"text-alignment:center\n"
"\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_2_button = QPushButton(self.icon_only_widget)
        self.home_2_button.setObjectName(u"home_2_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_2_button.sizePolicy().hasHeightForWidth())
        self.home_2_button.setSizePolicy(sizePolicy2)
        icon13 = QIcon()
        icon13.addFile(u":/images/home_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/images/home_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_2_button.setIcon(icon13)
        self.home_2_button.setIconSize(QSize(32, 32))
        self.home_2_button.setCheckable(True)
        self.home_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2_button)

        self.app_2_button = QPushButton(self.icon_only_widget)
        self.app_2_button.setObjectName(u"app_2_button")
        icon14 = QIcon()
        icon14.addFile(u":/images/apps_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon14.addFile(u":/images/apps_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.app_2_button.setIcon(icon14)
        self.app_2_button.setIconSize(QSize(32, 32))
        self.app_2_button.setCheckable(True)
        self.app_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.app_2_button)

        self.about_2_button = QPushButton(self.icon_only_widget)
        self.about_2_button.setObjectName(u"about_2_button")
        icon15 = QIcon()
        icon15.addFile(u":/images/about_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon15.addFile(u":/images/about_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.about_2_button.setIcon(icon15)
        self.about_2_button.setIconSize(QSize(32, 32))
        self.about_2_button.setCheckable(True)
        self.about_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.about_2_button)

        self.update_2_button = QPushButton(self.icon_only_widget)
        self.update_2_button.setObjectName(u"update_2_button")
        icon16 = QIcon()
        icon16.addFile(u":/images/update_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon16.addFile(u":/images/update_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.update_2_button.setIcon(icon16)
        self.update_2_button.setIconSize(QSize(32, 32))
        self.update_2_button.setCheckable(True)
        self.update_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_2_button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_2_button = QPushButton(self.icon_only_widget)
        self.exit_2_button.setObjectName(u"exit_2_button")
        icon17 = QIcon()
        icon17.addFile(u":/images/logout_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon17.addFile(u":/images/logout_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.exit_2_button.setIcon(icon17)
        self.exit_2_button.setIconSize(QSize(32, 32))
        self.exit_2_button.setCheckable(True)
        self.exit_2_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.exit_2_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.icon_name_widget.sizePolicy().hasHeightForWidth())
        self.icon_name_widget.setSizePolicy(sizePolicy3)
        self.icon_name_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-top-left-radius:10px;\n"
"\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(48, 48))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 146, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.home_1_button = QPushButton(self.icon_name_widget)
        self.home_1_button.setObjectName(u"home_1_button")
        font3 = QFont()
        font3.setFamilies([u"Roboto Medium"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.home_1_button.setFont(font3)
        self.home_1_button.setIcon(icon13)
        self.home_1_button.setIconSize(QSize(32, 32))
        self.home_1_button.setCheckable(True)
        self.home_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1_button)

        self.app_1_button = QPushButton(self.icon_name_widget)
        self.app_1_button.setObjectName(u"app_1_button")
        self.app_1_button.setFont(font1)
        self.app_1_button.setIcon(icon14)
        self.app_1_button.setIconSize(QSize(32, 32))
        self.app_1_button.setCheckable(True)
        self.app_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.app_1_button)

        self.about_1_button = QPushButton(self.icon_name_widget)
        self.about_1_button.setObjectName(u"about_1_button")
        self.about_1_button.setFont(font1)
        self.about_1_button.setIcon(icon15)
        self.about_1_button.setIconSize(QSize(32, 32))
        self.about_1_button.setCheckable(True)
        self.about_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.about_1_button)

        self.update_1_button = QPushButton(self.icon_name_widget)
        self.update_1_button.setObjectName(u"update_1_button")
        self.update_1_button.setFont(font1)
        self.update_1_button.setIcon(icon16)
        self.update_1_button.setIconSize(QSize(32, 32))
        self.update_1_button.setCheckable(True)
        self.update_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_1_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exit_1_button = QPushButton(self.icon_name_widget)
        self.exit_1_button.setObjectName(u"exit_1_button")
        self.exit_1_button.setFont(font1)
        self.exit_1_button.setIcon(icon17)
        self.exit_1_button.setIconSize(QSize(32, 32))
        self.exit_1_button.setCheckable(True)
        self.exit_1_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.exit_1_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_19.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_19.toggled.connect(self.icon_name_widget.setVisible)
        self.home_2_button.toggled.connect(self.home_1_button.setChecked)
        self.app_2_button.toggled.connect(self.app_1_button.setChecked)
        self.about_2_button.toggled.connect(self.about_1_button.setChecked)
        self.update_2_button.toggled.connect(self.update_1_button.setChecked)
        self.exit_2_button.toggled.connect(self.exit_1_button.setChecked)
        self.exit_1_button.toggled.connect(self.exit_2_button.setChecked)
        self.update_1_button.toggled.connect(self.update_2_button.setChecked)
        self.about_1_button.toggled.connect(self.about_2_button.setChecked)
        self.app_1_button.toggled.connect(self.app_2_button.setChecked)
        self.home_1_button.toggled.connect(self.home_2_button.setChecked)
        self.exit_2_button.toggled.connect(MainWindow.close)
        self.exit_1_button.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_19.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_8.setText("")
        self.pushButton_6.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_9.setText("")
        self.pushButton_7.setText("")
        self.pushButton_10.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>PC Information</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About PAGE ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"update page ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Network Information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ram Usage", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Disk Usage", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apps Page", None))
        self.label.setText("")
        self.home_2_button.setText("")
        self.app_2_button.setText("")
        self.about_2_button.setText("")
        self.update_2_button.setText("")
        self.exit_2_button.setText("")
        self.label_2.setText("")
        self.home_1_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.app_1_button.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.about_1_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.update_1_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.exit_1_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coopDesk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1199, 735)
        MainWindow.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_19 = QPushButton(self.main_menu)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/menu_icon_blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/menu_icon_blue_inverted.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_19.setIcon(icon)
        self.pushButton_19.setIconSize(QSize(24, 24))
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_19)

        self.horizontalSpacer = QSpacerItem(668, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"QPushButton{\n"
"  background:none;\n"
"  border: none;\n"
"\n"
"\n"
"}")
        self.gridLayout_2 = QGridLayout(self.home_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.pushButton_11 = QPushButton(self.home_page)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon1 = QIcon()
        icon1.addFile(u":/homeicons/teller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_11, 3, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.home_page)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon2 = QIcon()
        icon2.addFile(u":/homeicons/about_coop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon2)
        self.pushButton_12.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_12, 3, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.home_page)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon3 = QIcon()
        icon3.addFile(u":/homeicons/alhuda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.home_page)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon4 = QIcon()
        icon4.addFile(u":/homeicons/phonebook.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.home_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon5 = QIcon()
        icon5.addFile(u":/homeicons/coopurl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.home_page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon6 = QIcon()
        icon6.addFile(u":/homeicons/michu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon6)
        self.pushButton_3.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.home_page)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon7 = QIcon()
        icon7.addFile(u":/homeicons/coopay.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.home_page)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon8 = QIcon()
        icon8.addFile(u":/homeicons/conventinal_products.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.home_page)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon9 = QIcon()
        icon9.addFile(u":/homeicons/coopapp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon9)
        self.pushButton_10.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_10, 3, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.home_page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon10 = QIcon()
        icon10.addFile(u":/homeicons/remittance.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon10)
        self.pushButton_4.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.home_page)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon11 = QIcon()
        icon11.addFile(u":/homeicons/atm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon11)
        self.pushButton_5.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pcinfo_button = QPushButton(self.home_page)
        self.pcinfo_button.setObjectName(u"pcinfo_button")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        self.pcinfo_button.setFont(font2)
        self.pcinfo_button.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/homeicons/pcinfo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pcinfo_button.setIcon(icon12)
        self.pcinfo_button.setIconSize(QSize(128, 128))
        self.pcinfo_button.setCheckable(True)

        self.gridLayout_2.addWidget(self.pcinfo_button, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_3 = QLabel(self.about_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 65, 301, 111))
        self.stackedWidget.addWidget(self.about_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.label_6 = QLabel(self.update_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 170, 221, 101))
        self.stackedWidget.addWidget(self.update_page)
        self.pc_info_page = QWidget()
        self.pc_info_page.setObjectName(u"pc_info_page")
        self.widget = QWidget(self.pc_info_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 291, 251))
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 30, 181, 21))
        self.widget_2 = QWidget(self.pc_info_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(330, 20, 301, 251))
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 30, 171, 21))
        self.widget_3 = QWidget(self.pc_info_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(650, 20, 301, 251))
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 30, 171, 21))
        self.widget_4 = QWidget(self.pc_info_page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(20, 260, 301, 251))
        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 30, 171, 21))
        self.stackedWidget.addWidget(self.pc_info_page)
        self.apps_page = QWidget()
        self.apps_page.setObjectName(u"apps_page")
        self.label_4 = QLabel(self.apps_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 110, 161, 111))
        self.stackedWidget.addWidget(self.apps_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy1)
        self.icon_only_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align: center;\n"
"border-radius:10px;\n"
"text-alignment:center\n"
"\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_2_button = QPushButton(self.icon_only_widget)
        self.home_2_button.setObjectName(u"home_2_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_2_button.sizePolicy().hasHeightForWidth())
        self.home_2_button.setSizePolicy(sizePolicy2)
        icon13 = QIcon()
        icon13.addFile(u":/images/home_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/images/home_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_2_button.setIcon(icon13)
        self.home_2_button.setIconSize(QSize(32, 32))
        self.home_2_button.setCheckable(True)
        self.home_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2_button)

        self.app_2_button = QPushButton(self.icon_only_widget)
        self.app_2_button.setObjectName(u"app_2_button")
        icon14 = QIcon()
        icon14.addFile(u":/images/apps_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon14.addFile(u":/images/apps_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.app_2_button.setIcon(icon14)
        self.app_2_button.setIconSize(QSize(32, 32))
        self.app_2_button.setCheckable(True)
        self.app_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.app_2_button)

        self.about_2_button = QPushButton(self.icon_only_widget)
        self.about_2_button.setObjectName(u"about_2_button")
        icon15 = QIcon()
        icon15.addFile(u":/images/about_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon15.addFile(u":/images/about_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.about_2_button.setIcon(icon15)
        self.about_2_button.setIconSize(QSize(32, 32))
        self.about_2_button.setCheckable(True)
        self.about_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.about_2_button)

        self.update_2_button = QPushButton(self.icon_only_widget)
        self.update_2_button.setObjectName(u"update_2_button")
        icon16 = QIcon()
        icon16.addFile(u":/images/update_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon16.addFile(u":/images/update_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.update_2_button.setIcon(icon16)
        self.update_2_button.setIconSize(QSize(32, 32))
        self.update_2_button.setCheckable(True)
        self.update_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_2_button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_2_button = QPushButton(self.icon_only_widget)
        self.exit_2_button.setObjectName(u"exit_2_button")
        icon17 = QIcon()
        icon17.addFile(u":/images/logout_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon17.addFile(u":/images/logout_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.exit_2_button.setIcon(icon17)
        self.exit_2_button.setIconSize(QSize(32, 32))
        self.exit_2_button.setCheckable(True)
        self.exit_2_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.exit_2_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.icon_name_widget.sizePolicy().hasHeightForWidth())
        self.icon_name_widget.setSizePolicy(sizePolicy3)
        self.icon_name_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-top-left-radius:10px;\n"
"\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(48, 48))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 146, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.home_1_button = QPushButton(self.icon_name_widget)
        self.home_1_button.setObjectName(u"home_1_button")
        font3 = QFont()
        font3.setFamilies([u"Roboto Medium"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.home_1_button.setFont(font3)
        self.home_1_button.setIcon(icon13)
        self.home_1_button.setIconSize(QSize(32, 32))
        self.home_1_button.setCheckable(True)
        self.home_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1_button)

        self.app_1_button = QPushButton(self.icon_name_widget)
        self.app_1_button.setObjectName(u"app_1_button")
        self.app_1_button.setFont(font1)
        self.app_1_button.setIcon(icon14)
        self.app_1_button.setIconSize(QSize(32, 32))
        self.app_1_button.setCheckable(True)
        self.app_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.app_1_button)

        self.about_1_button = QPushButton(self.icon_name_widget)
        self.about_1_button.setObjectName(u"about_1_button")
        self.about_1_button.setFont(font1)
        self.about_1_button.setIcon(icon15)
        self.about_1_button.setIconSize(QSize(32, 32))
        self.about_1_button.setCheckable(True)
        self.about_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.about_1_button)

        self.update_1_button = QPushButton(self.icon_name_widget)
        self.update_1_button.setObjectName(u"update_1_button")
        self.update_1_button.setFont(font1)
        self.update_1_button.setIcon(icon16)
        self.update_1_button.setIconSize(QSize(32, 32))
        self.update_1_button.setCheckable(True)
        self.update_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_1_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exit_1_button = QPushButton(self.icon_name_widget)
        self.exit_1_button.setObjectName(u"exit_1_button")
        self.exit_1_button.setFont(font1)
        self.exit_1_button.setIcon(icon17)
        self.exit_1_button.setIconSize(QSize(32, 32))
        self.exit_1_button.setCheckable(True)
        self.exit_1_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.exit_1_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_19.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_19.toggled.connect(self.icon_name_widget.setVisible)
        self.home_2_button.toggled.connect(self.home_1_button.setChecked)
        self.app_2_button.toggled.connect(self.app_1_button.setChecked)
        self.about_2_button.toggled.connect(self.about_1_button.setChecked)
        self.update_2_button.toggled.connect(self.update_1_button.setChecked)
        self.exit_2_button.toggled.connect(self.exit_1_button.setChecked)
        self.exit_1_button.toggled.connect(self.exit_2_button.setChecked)
        self.update_1_button.toggled.connect(self.update_2_button.setChecked)
        self.about_1_button.toggled.connect(self.about_2_button.setChecked)
        self.app_1_button.toggled.connect(self.app_2_button.setChecked)
        self.home_1_button.toggled.connect(self.home_2_button.setChecked)
        self.exit_2_button.toggled.connect(MainWindow.close)
        self.exit_1_button.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_19.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_8.setText("")
        self.pushButton_6.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_9.setText("")
        self.pushButton_7.setText("")
        self.pushButton_10.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
#if QT_CONFIG(tooltip)
        self.pcinfo_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>PC Information</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pcinfo_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About PAGE ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"update page ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Network Information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ram Usage", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Disk Usage", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apps Page", None))
        self.label.setText("")
        self.home_2_button.setText("")
        self.app_2_button.setText("")
        self.about_2_button.setText("")
        self.update_2_button.setText("")
        self.exit_2_button.setText("")
        self.label_2.setText("")
        self.home_1_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.app_1_button.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.about_1_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.update_1_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.exit_1_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coopDesk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1199, 735)
        MainWindow.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_19 = QPushButton(self.main_menu)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/menu_icon_blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/menu_icon_blue_inverted.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_19.setIcon(icon)
        self.pushButton_19.setIconSize(QSize(24, 24))
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_19)

        self.horizontalSpacer = QSpacerItem(668, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"QPushButton{\n"
"  background:none;\n"
"  border: none;\n"
"\n"
"\n"
"}")
        self.gridLayout_2 = QGridLayout(self.home_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.pushButton_11 = QPushButton(self.home_page)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon1 = QIcon()
        icon1.addFile(u":/homeicons/teller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_11, 3, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.home_page)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon2 = QIcon()
        icon2.addFile(u":/homeicons/about_coop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon2)
        self.pushButton_12.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_12, 3, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.home_page)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon3 = QIcon()
        icon3.addFile(u":/homeicons/alhuda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.home_page)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon4 = QIcon()
        icon4.addFile(u":/homeicons/phonebook.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.home_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon5 = QIcon()
        icon5.addFile(u":/homeicons/coopurl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.home_page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon6 = QIcon()
        icon6.addFile(u":/homeicons/michu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon6)
        self.pushButton_3.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.home_page)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon7 = QIcon()
        icon7.addFile(u":/homeicons/coopay.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.home_page)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon8 = QIcon()
        icon8.addFile(u":/homeicons/conventinal_products.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.home_page)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon9 = QIcon()
        icon9.addFile(u":/homeicons/coopapp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon9)
        self.pushButton_10.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_10, 3, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.home_page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon10 = QIcon()
        icon10.addFile(u":/homeicons/remittance.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon10)
        self.pushButton_4.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.home_page)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon11 = QIcon()
        icon11.addFile(u":/homeicons/atm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon11)
        self.pushButton_5.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pcinfo_button = QPushButton(self.home_page)
        self.pcinfo_button.setObjectName(u"pcinfo_button")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        self.pcinfo_button.setFont(font2)
        self.pcinfo_button.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/homeicons/pcinfo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pcinfo_button.setIcon(icon12)
        self.pcinfo_button.setIconSize(QSize(128, 128))
        self.pcinfo_button.setCheckable(True)

        self.gridLayout_2.addWidget(self.pcinfo_button, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_3 = QLabel(self.about_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 65, 301, 111))
        self.stackedWidget.addWidget(self.about_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.label_6 = QLabel(self.update_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 170, 221, 101))
        self.stackedWidget.addWidget(self.update_page)
        self.pc_info_page = QWidget()
        self.pc_info_page.setObjectName(u"pc_info_page")
        self.widget = QWidget(self.pc_info_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 291, 251))
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 30, 181, 21))
        self.widget_2 = QWidget(self.pc_info_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(330, 20, 301, 251))
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 30, 171, 21))
        self.widget_3 = QWidget(self.pc_info_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(650, 20, 301, 251))
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 30, 171, 21))
        self.widget_4 = QWidget(self.pc_info_page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(20, 260, 301, 251))
        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 30, 171, 21))
        self.stackedWidget.addWidget(self.pc_info_page)
        self.apps_page = QWidget()
        self.apps_page.setObjectName(u"apps_page")
        self.label_4 = QLabel(self.apps_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 110, 161, 111))
        self.stackedWidget.addWidget(self.apps_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy1)
        self.icon_only_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align: center;\n"
"border-radius:10px;\n"
"text-alignment:center\n"
"\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_2_button = QPushButton(self.icon_only_widget)
        self.home_2_button.setObjectName(u"home_2_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_2_button.sizePolicy().hasHeightForWidth())
        self.home_2_button.setSizePolicy(sizePolicy2)
        icon13 = QIcon()
        icon13.addFile(u":/images/home_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/images/home_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_2_button.setIcon(icon13)
        self.home_2_button.setIconSize(QSize(32, 32))
        self.home_2_button.setCheckable(True)
        self.home_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2_button)

        self.app_2_button = QPushButton(self.icon_only_widget)
        self.app_2_button.setObjectName(u"app_2_button")
        icon14 = QIcon()
        icon14.addFile(u":/images/apps_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon14.addFile(u":/images/apps_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.app_2_button.setIcon(icon14)
        self.app_2_button.setIconSize(QSize(32, 32))
        self.app_2_button.setCheckable(True)
        self.app_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.app_2_button)

        self.about_2_button = QPushButton(self.icon_only_widget)
        self.about_2_button.setObjectName(u"about_2_button")
        icon15 = QIcon()
        icon15.addFile(u":/images/about_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon15.addFile(u":/images/about_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.about_2_button.setIcon(icon15)
        self.about_2_button.setIconSize(QSize(32, 32))
        self.about_2_button.setCheckable(True)
        self.about_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.about_2_button)

        self.update_2_button = QPushButton(self.icon_only_widget)
        self.update_2_button.setObjectName(u"update_2_button")
        icon16 = QIcon()
        icon16.addFile(u":/images/update_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon16.addFile(u":/images/update_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.update_2_button.setIcon(icon16)
        self.update_2_button.setIconSize(QSize(32, 32))
        self.update_2_button.setCheckable(True)
        self.update_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_2_button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_2_button = QPushButton(self.icon_only_widget)
        self.exit_2_button.setObjectName(u"exit_2_button")
        icon17 = QIcon()
        icon17.addFile(u":/images/logout_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon17.addFile(u":/images/logout_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.exit_2_button.setIcon(icon17)
        self.exit_2_button.setIconSize(QSize(32, 32))
        self.exit_2_button.setCheckable(True)
        self.exit_2_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.exit_2_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.icon_name_widget.sizePolicy().hasHeightForWidth())
        self.icon_name_widget.setSizePolicy(sizePolicy3)
        self.icon_name_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-top-left-radius:10px;\n"
"\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(48, 48))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 146, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.home_1_button = QPushButton(self.icon_name_widget)
        self.home_1_button.setObjectName(u"home_1_button")
        font3 = QFont()
        font3.setFamilies([u"Roboto Medium"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.home_1_button.setFont(font3)
        self.home_1_button.setIcon(icon13)
        self.home_1_button.setIconSize(QSize(32, 32))
        self.home_1_button.setCheckable(True)
        self.home_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1_button)

        self.app_1_button = QPushButton(self.icon_name_widget)
        self.app_1_button.setObjectName(u"app_1_button")
        self.app_1_button.setFont(font1)
        self.app_1_button.setIcon(icon14)
        self.app_1_button.setIconSize(QSize(32, 32))
        self.app_1_button.setCheckable(True)
        self.app_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.app_1_button)

        self.about_1_button = QPushButton(self.icon_name_widget)
        self.about_1_button.setObjectName(u"about_1_button")
        self.about_1_button.setFont(font1)
        self.about_1_button.setIcon(icon15)
        self.about_1_button.setIconSize(QSize(32, 32))
        self.about_1_button.setCheckable(True)
        self.about_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.about_1_button)

        self.update_1_button = QPushButton(self.icon_name_widget)
        self.update_1_button.setObjectName(u"update_1_button")
        self.update_1_button.setFont(font1)
        self.update_1_button.setIcon(icon16)
        self.update_1_button.setIconSize(QSize(32, 32))
        self.update_1_button.setCheckable(True)
        self.update_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_1_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exit_1_button = QPushButton(self.icon_name_widget)
        self.exit_1_button.setObjectName(u"exit_1_button")
        self.exit_1_button.setFont(font1)
        self.exit_1_button.setIcon(icon17)
        self.exit_1_button.setIconSize(QSize(32, 32))
        self.exit_1_button.setCheckable(True)
        self.exit_1_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.exit_1_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_19.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_19.toggled.connect(self.icon_name_widget.setVisible)
        self.home_2_button.toggled.connect(self.home_1_button.setChecked)
        self.app_2_button.toggled.connect(self.app_1_button.setChecked)
        self.about_2_button.toggled.connect(self.about_1_button.setChecked)
        self.update_2_button.toggled.connect(self.update_1_button.setChecked)
        self.exit_2_button.toggled.connect(self.exit_1_button.setChecked)
        self.exit_1_button.toggled.connect(self.exit_2_button.setChecked)
        self.update_1_button.toggled.connect(self.update_2_button.setChecked)
        self.about_1_button.toggled.connect(self.about_2_button.setChecked)
        self.app_1_button.toggled.connect(self.app_2_button.setChecked)
        self.home_1_button.toggled.connect(self.home_2_button.setChecked)
        self.exit_2_button.toggled.connect(MainWindow.close)
        self.exit_1_button.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_19.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_8.setText("")
        self.pushButton_6.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_9.setText("")
        self.pushButton_7.setText("")
        self.pushButton_10.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
#if QT_CONFIG(tooltip)
        self.pcinfo_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>PC Information</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pcinfo_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About PAGE ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"update page ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Network Information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ram Usage", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Disk Usage", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apps Page", None))
        self.label.setText("")
        self.home_2_button.setText("")
        self.app_2_button.setText("")
        self.about_2_button.setText("")
        self.update_2_button.setText("")
        self.exit_2_button.setText("")
        self.label_2.setText("")
        self.home_1_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.app_1_button.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.about_1_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.update_1_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.exit_1_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coopDesk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1199, 735)
        MainWindow.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_19 = QPushButton(self.main_menu)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/menu_icon_blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/menu_icon_blue_inverted.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_19.setIcon(icon)
        self.pushButton_19.setIconSize(QSize(24, 24))
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_19)

        self.horizontalSpacer = QSpacerItem(668, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"QPushButton{\n"
"  background:none;\n"
"  border: none;\n"
"\n"
"\n"
"}")
        self.gridLayout_2 = QGridLayout(self.home_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.pushButton_11 = QPushButton(self.home_page)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon1 = QIcon()
        icon1.addFile(u":/homeicons/teller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_11, 3, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.home_page)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon2 = QIcon()
        icon2.addFile(u":/homeicons/about_coop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon2)
        self.pushButton_12.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_12, 3, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.home_page)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon3 = QIcon()
        icon3.addFile(u":/homeicons/alhuda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.home_page)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon4 = QIcon()
        icon4.addFile(u":/homeicons/phonebook.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.home_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon5 = QIcon()
        icon5.addFile(u":/homeicons/coopurl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.home_page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon6 = QIcon()
        icon6.addFile(u":/homeicons/michu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon6)
        self.pushButton_3.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.home_page)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon7 = QIcon()
        icon7.addFile(u":/homeicons/coopay.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.home_page)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon8 = QIcon()
        icon8.addFile(u":/homeicons/conventinal_products.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.home_page)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon9 = QIcon()
        icon9.addFile(u":/homeicons/coopapp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon9)
        self.pushButton_10.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_10, 3, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.home_page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon10 = QIcon()
        icon10.addFile(u":/homeicons/remittance.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon10)
        self.pushButton_4.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.home_page)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon11 = QIcon()
        icon11.addFile(u":/homeicons/atm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon11)
        self.pushButton_5.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pcinfo_button = QPushButton(self.home_page)
        self.pcinfo_button.setObjectName(u"pcinfo_button")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        self.pcinfo_button.setFont(font2)
        self.pcinfo_button.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/homeicons/pcinfo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pcinfo_button.setIcon(icon12)
        self.pcinfo_button.setIconSize(QSize(128, 128))
        self.pcinfo_button.setCheckable(True)

        self.gridLayout_2.addWidget(self.pcinfo_button, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_3 = QLabel(self.about_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 65, 301, 111))
        self.stackedWidget.addWidget(self.about_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.label_6 = QLabel(self.update_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 170, 221, 101))
        self.stackedWidget.addWidget(self.update_page)
        self.pc_info_page = QWidget()
        self.pc_info_page.setObjectName(u"pc_info_page")
        self.widget = QWidget(self.pc_info_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 291, 251))
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 30, 181, 21))
        self.widget_2 = QWidget(self.pc_info_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(330, 20, 301, 251))
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 30, 171, 21))
        self.widget_3 = QWidget(self.pc_info_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(650, 20, 301, 251))
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 30, 171, 21))
        self.widget_4 = QWidget(self.pc_info_page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(20, 260, 301, 251))
        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 30, 171, 21))
        self.stackedWidget.addWidget(self.pc_info_page)
        self.apps_page = QWidget()
        self.apps_page.setObjectName(u"apps_page")
        self.label_4 = QLabel(self.apps_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 110, 161, 111))
        self.stackedWidget.addWidget(self.apps_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy1)
        self.icon_only_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align: center;\n"
"border-radius:10px;\n"
"text-alignment:center\n"
"\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_2_button = QPushButton(self.icon_only_widget)
        self.home_2_button.setObjectName(u"home_2_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_2_button.sizePolicy().hasHeightForWidth())
        self.home_2_button.setSizePolicy(sizePolicy2)
        icon13 = QIcon()
        icon13.addFile(u":/images/home_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/images/home_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_2_button.setIcon(icon13)
        self.home_2_button.setIconSize(QSize(32, 32))
        self.home_2_button.setCheckable(True)
        self.home_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2_button)

        self.app_2_button = QPushButton(self.icon_only_widget)
        self.app_2_button.setObjectName(u"app_2_button")
        icon14 = QIcon()
        icon14.addFile(u":/images/apps_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon14.addFile(u":/images/apps_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.app_2_button.setIcon(icon14)
        self.app_2_button.setIconSize(QSize(32, 32))
        self.app_2_button.setCheckable(True)
        self.app_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.app_2_button)

        self.about_2_button = QPushButton(self.icon_only_widget)
        self.about_2_button.setObjectName(u"about_2_button")
        icon15 = QIcon()
        icon15.addFile(u":/images/about_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon15.addFile(u":/images/about_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.about_2_button.setIcon(icon15)
        self.about_2_button.setIconSize(QSize(32, 32))
        self.about_2_button.setCheckable(True)
        self.about_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.about_2_button)

        self.update_2_button = QPushButton(self.icon_only_widget)
        self.update_2_button.setObjectName(u"update_2_button")
        icon16 = QIcon()
        icon16.addFile(u":/images/update_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon16.addFile(u":/images/update_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.update_2_button.setIcon(icon16)
        self.update_2_button.setIconSize(QSize(32, 32))
        self.update_2_button.setCheckable(True)
        self.update_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_2_button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_2_button = QPushButton(self.icon_only_widget)
        self.exit_2_button.setObjectName(u"exit_2_button")
        icon17 = QIcon()
        icon17.addFile(u":/images/logout_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon17.addFile(u":/images/logout_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.exit_2_button.setIcon(icon17)
        self.exit_2_button.setIconSize(QSize(32, 32))
        self.exit_2_button.setCheckable(True)
        self.exit_2_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.exit_2_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.icon_name_widget.sizePolicy().hasHeightForWidth())
        self.icon_name_widget.setSizePolicy(sizePolicy3)
        self.icon_name_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-top-left-radius:10px;\n"
"\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(48, 48))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 146, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.home_1_button = QPushButton(self.icon_name_widget)
        self.home_1_button.setObjectName(u"home_1_button")
        font3 = QFont()
        font3.setFamilies([u"Roboto Medium"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.home_1_button.setFont(font3)
        self.home_1_button.setIcon(icon13)
        self.home_1_button.setIconSize(QSize(32, 32))
        self.home_1_button.setCheckable(True)
        self.home_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1_button)

        self.app_1_button = QPushButton(self.icon_name_widget)
        self.app_1_button.setObjectName(u"app_1_button")
        self.app_1_button.setFont(font1)
        self.app_1_button.setIcon(icon14)
        self.app_1_button.setIconSize(QSize(32, 32))
        self.app_1_button.setCheckable(True)
        self.app_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.app_1_button)

        self.about_1_button = QPushButton(self.icon_name_widget)
        self.about_1_button.setObjectName(u"about_1_button")
        self.about_1_button.setFont(font1)
        self.about_1_button.setIcon(icon15)
        self.about_1_button.setIconSize(QSize(32, 32))
        self.about_1_button.setCheckable(True)
        self.about_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.about_1_button)

        self.update_1_button = QPushButton(self.icon_name_widget)
        self.update_1_button.setObjectName(u"update_1_button")
        self.update_1_button.setFont(font1)
        self.update_1_button.setIcon(icon16)
        self.update_1_button.setIconSize(QSize(32, 32))
        self.update_1_button.setCheckable(True)
        self.update_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_1_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exit_1_button = QPushButton(self.icon_name_widget)
        self.exit_1_button.setObjectName(u"exit_1_button")
        self.exit_1_button.setFont(font1)
        self.exit_1_button.setIcon(icon17)
        self.exit_1_button.setIconSize(QSize(32, 32))
        self.exit_1_button.setCheckable(True)
        self.exit_1_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.exit_1_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_19.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_19.toggled.connect(self.icon_name_widget.setVisible)
        self.home_2_button.toggled.connect(self.home_1_button.setChecked)
        self.app_2_button.toggled.connect(self.app_1_button.setChecked)
        self.about_2_button.toggled.connect(self.about_1_button.setChecked)
        self.update_2_button.toggled.connect(self.update_1_button.setChecked)
        self.exit_2_button.toggled.connect(self.exit_1_button.setChecked)
        self.exit_1_button.toggled.connect(self.exit_2_button.setChecked)
        self.update_1_button.toggled.connect(self.update_2_button.setChecked)
        self.about_1_button.toggled.connect(self.about_2_button.setChecked)
        self.app_1_button.toggled.connect(self.app_2_button.setChecked)
        self.home_1_button.toggled.connect(self.home_2_button.setChecked)
        self.exit_2_button.toggled.connect(MainWindow.close)
        self.exit_1_button.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_19.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_8.setText("")
        self.pushButton_6.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_9.setText("")
        self.pushButton_7.setText("")
        self.pushButton_10.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
#if QT_CONFIG(tooltip)
        self.pcinfo_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>PC Information</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pcinfo_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About PAGE ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"update page ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Network Information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ram Usage", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Disk Usage", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apps Page", None))
        self.label.setText("")
        self.home_2_button.setText("")
        self.app_2_button.setText("")
        self.about_2_button.setText("")
        self.update_2_button.setText("")
        self.exit_2_button.setText("")
        self.label_2.setText("")
        self.home_1_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.app_1_button.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.about_1_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.update_1_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.exit_1_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coopDesk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1199, 735)
        MainWindow.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy)
        self.main_menu.setStyleSheet(u"QToolTip {\n"
"    background:white;\n"
"    color: #00AEEF; \n"
"    border: 3px solid #00AEEF;\n"
"    font-size: 16pt;\n"
"    font-family: Arial;\n"
"    padding: 5px;\n"
"    border-radius:3px\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_19 = QPushButton(self.main_menu)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/menu_icon_blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/menu_icon_blue_inverted.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_19.setIcon(icon)
        self.pushButton_19.setIconSize(QSize(24, 24))
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_19)

        self.horizontalSpacer = QSpacerItem(668, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"QPushButton{\n"
"  background:none;\n"
"  border: none;\n"
"\n"
"\n"
"}")
        self.gridLayout_2 = QGridLayout(self.home_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.cashmanage_button = QPushButton(self.home_page)
        self.cashmanage_button.setObjectName(u"cashmanage_button")
        icon1 = QIcon()
        icon1.addFile(u":/homeicons/teller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cashmanage_button.setIcon(icon1)
        self.cashmanage_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.cashmanage_button, 3, 1, 1, 1)

        self.about_coop_button = QPushButton(self.home_page)
        self.about_coop_button.setObjectName(u"about_coop_button")
        icon2 = QIcon()
        icon2.addFile(u":/homeicons/about_coop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.about_coop_button.setIcon(icon2)
        self.about_coop_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.about_coop_button, 3, 2, 1, 1)

        self.alhuda_button = QPushButton(self.home_page)
        self.alhuda_button.setObjectName(u"alhuda_button")
        icon3 = QIcon()
        icon3.addFile(u":/homeicons/alhuda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.alhuda_button.setIcon(icon3)
        self.alhuda_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.alhuda_button, 2, 1, 1, 1)

        self.phonebook_button = QPushButton(self.home_page)
        self.phonebook_button.setObjectName(u"phonebook_button")
        icon4 = QIcon()
        icon4.addFile(u":/homeicons/phonebook.png", QSize(), QIcon.Normal, QIcon.Off)
        self.phonebook_button.setIcon(icon4)
        self.phonebook_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.phonebook_button, 1, 2, 1, 1)

        self.coopurl_button = QPushButton(self.home_page)
        self.coopurl_button.setObjectName(u"coopurl_button")
        icon5 = QIcon()
        icon5.addFile(u":/homeicons/coopurl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coopurl_button.setIcon(icon5)
        self.coopurl_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.coopurl_button, 0, 1, 1, 1)

        self.michu_button = QPushButton(self.home_page)
        self.michu_button.setObjectName(u"michu_button")
        icon6 = QIcon()
        icon6.addFile(u":/homeicons/michu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.michu_button.setIcon(icon6)
        self.michu_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.michu_button, 0, 2, 1, 1)

        self.coopay_button = QPushButton(self.home_page)
        self.coopay_button.setObjectName(u"coopay_button")
        icon7 = QIcon()
        icon7.addFile(u":/homeicons/coopay.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coopay_button.setIcon(icon7)
        self.coopay_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.coopay_button, 2, 2, 1, 1)

        self.conventional_button = QPushButton(self.home_page)
        self.conventional_button.setObjectName(u"conventional_button")
        icon8 = QIcon()
        icon8.addFile(u":/homeicons/conventinal_products.png", QSize(), QIcon.Normal, QIcon.Off)
        self.conventional_button.setIcon(icon8)
        self.conventional_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.conventional_button, 2, 0, 1, 1)

        self.coopapp_button = QPushButton(self.home_page)
        self.coopapp_button.setObjectName(u"coopapp_button")
        icon9 = QIcon()
        icon9.addFile(u":/homeicons/coopapp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coopapp_button.setIcon(icon9)
        self.coopapp_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.coopapp_button, 3, 0, 1, 1)

        self.remittance_button = QPushButton(self.home_page)
        self.remittance_button.setObjectName(u"remittance_button")
        icon10 = QIcon()
        icon10.addFile(u":/homeicons/remittance.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remittance_button.setIcon(icon10)
        self.remittance_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.remittance_button, 1, 0, 1, 1)

        self.atm_button = QPushButton(self.home_page)
        self.atm_button.setObjectName(u"atm_button")
        icon11 = QIcon()
        icon11.addFile(u":/homeicons/atm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.atm_button.setIcon(icon11)
        self.atm_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.atm_button, 1, 1, 1, 1)

        self.pcinfo_button = QPushButton(self.home_page)
        self.pcinfo_button.setObjectName(u"pcinfo_button")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        self.pcinfo_button.setFont(font2)
        self.pcinfo_button.setToolTipDuration(-4)
        self.pcinfo_button.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/homeicons/pcinfo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pcinfo_button.setIcon(icon12)
        self.pcinfo_button.setIconSize(QSize(128, 128))
        self.pcinfo_button.setCheckable(True)

        self.gridLayout_2.addWidget(self.pcinfo_button, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_3 = QLabel(self.about_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 65, 301, 111))
        self.stackedWidget.addWidget(self.about_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.label_6 = QLabel(self.update_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 170, 221, 101))
        self.stackedWidget.addWidget(self.update_page)
        self.pc_info_page = QWidget()
        self.pc_info_page.setObjectName(u"pc_info_page")
        self.widget = QWidget(self.pc_info_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 291, 251))
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 30, 181, 21))
        self.widget_2 = QWidget(self.pc_info_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(330, 20, 301, 251))
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 30, 171, 21))
        self.widget_3 = QWidget(self.pc_info_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(650, 20, 301, 251))
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 30, 171, 21))
        self.stackedWidget.addWidget(self.pc_info_page)
        self.apps_page = QWidget()
        self.apps_page.setObjectName(u"apps_page")
        self.label_4 = QLabel(self.apps_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 110, 161, 111))
        self.stackedWidget.addWidget(self.apps_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy1)
        self.icon_only_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align: center;\n"
"border-radius:10px;\n"
"text-alignment:center\n"
"\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_2_button = QPushButton(self.icon_only_widget)
        self.home_2_button.setObjectName(u"home_2_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_2_button.sizePolicy().hasHeightForWidth())
        self.home_2_button.setSizePolicy(sizePolicy2)
        icon13 = QIcon()
        icon13.addFile(u":/images/home_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/images/home_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_2_button.setIcon(icon13)
        self.home_2_button.setIconSize(QSize(32, 32))
        self.home_2_button.setCheckable(True)
        self.home_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2_button)

        self.app_2_button = QPushButton(self.icon_only_widget)
        self.app_2_button.setObjectName(u"app_2_button")
        icon14 = QIcon()
        icon14.addFile(u":/images/apps_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon14.addFile(u":/images/apps_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.app_2_button.setIcon(icon14)
        self.app_2_button.setIconSize(QSize(32, 32))
        self.app_2_button.setCheckable(True)
        self.app_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.app_2_button)

        self.about_2_button = QPushButton(self.icon_only_widget)
        self.about_2_button.setObjectName(u"about_2_button")
        icon15 = QIcon()
        icon15.addFile(u":/images/about_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon15.addFile(u":/images/about_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.about_2_button.setIcon(icon15)
        self.about_2_button.setIconSize(QSize(32, 32))
        self.about_2_button.setCheckable(True)
        self.about_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.about_2_button)

        self.update_2_button = QPushButton(self.icon_only_widget)
        self.update_2_button.setObjectName(u"update_2_button")
        icon16 = QIcon()
        icon16.addFile(u":/images/update_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon16.addFile(u":/images/update_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.update_2_button.setIcon(icon16)
        self.update_2_button.setIconSize(QSize(32, 32))
        self.update_2_button.setCheckable(True)
        self.update_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_2_button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_2_button = QPushButton(self.icon_only_widget)
        self.exit_2_button.setObjectName(u"exit_2_button")
        icon17 = QIcon()
        icon17.addFile(u":/images/logout_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon17.addFile(u":/images/logout_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.exit_2_button.setIcon(icon17)
        self.exit_2_button.setIconSize(QSize(32, 32))
        self.exit_2_button.setCheckable(True)
        self.exit_2_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.exit_2_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.icon_name_widget.sizePolicy().hasHeightForWidth())
        self.icon_name_widget.setSizePolicy(sizePolicy3)
        self.icon_name_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-top-left-radius:10px;\n"
"\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(48, 48))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 146, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.home_1_button = QPushButton(self.icon_name_widget)
        self.home_1_button.setObjectName(u"home_1_button")
        font3 = QFont()
        font3.setFamilies([u"Roboto Medium"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.home_1_button.setFont(font3)
        self.home_1_button.setIcon(icon13)
        self.home_1_button.setIconSize(QSize(32, 32))
        self.home_1_button.setCheckable(True)
        self.home_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1_button)

        self.app_1_button = QPushButton(self.icon_name_widget)
        self.app_1_button.setObjectName(u"app_1_button")
        self.app_1_button.setFont(font1)
        self.app_1_button.setIcon(icon14)
        self.app_1_button.setIconSize(QSize(32, 32))
        self.app_1_button.setCheckable(True)
        self.app_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.app_1_button)

        self.about_1_button = QPushButton(self.icon_name_widget)
        self.about_1_button.setObjectName(u"about_1_button")
        self.about_1_button.setFont(font1)
        self.about_1_button.setIcon(icon15)
        self.about_1_button.setIconSize(QSize(32, 32))
        self.about_1_button.setCheckable(True)
        self.about_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.about_1_button)

        self.update_1_button = QPushButton(self.icon_name_widget)
        self.update_1_button.setObjectName(u"update_1_button")
        self.update_1_button.setFont(font1)
        self.update_1_button.setIcon(icon16)
        self.update_1_button.setIconSize(QSize(32, 32))
        self.update_1_button.setCheckable(True)
        self.update_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_1_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exit_1_button = QPushButton(self.icon_name_widget)
        self.exit_1_button.setObjectName(u"exit_1_button")
        self.exit_1_button.setFont(font1)
        self.exit_1_button.setIcon(icon17)
        self.exit_1_button.setIconSize(QSize(32, 32))
        self.exit_1_button.setCheckable(True)
        self.exit_1_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.exit_1_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_19.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_19.toggled.connect(self.icon_name_widget.setVisible)
        self.home_2_button.toggled.connect(self.home_1_button.setChecked)
        self.app_2_button.toggled.connect(self.app_1_button.setChecked)
        self.about_2_button.toggled.connect(self.about_1_button.setChecked)
        self.update_2_button.toggled.connect(self.update_1_button.setChecked)
        self.exit_2_button.toggled.connect(self.exit_1_button.setChecked)
        self.exit_1_button.toggled.connect(self.exit_2_button.setChecked)
        self.update_1_button.toggled.connect(self.update_2_button.setChecked)
        self.about_1_button.toggled.connect(self.about_2_button.setChecked)
        self.app_1_button.toggled.connect(self.app_2_button.setChecked)
        self.home_1_button.toggled.connect(self.home_2_button.setChecked)
        self.exit_2_button.toggled.connect(MainWindow.close)
        self.exit_1_button.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_19.setText("")
#if QT_CONFIG(tooltip)
        self.cashmanage_button.setToolTip(QCoreApplication.translate("MainWindow", u"Daily Cash Management", None))
#endif // QT_CONFIG(tooltip)
        self.cashmanage_button.setText("")
#if QT_CONFIG(tooltip)
        self.about_coop_button.setToolTip(QCoreApplication.translate("MainWindow", u"About Coop", None))
#endif // QT_CONFIG(tooltip)
        self.about_coop_button.setText("")
#if QT_CONFIG(tooltip)
        self.alhuda_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop Alhuda ", None))
#endif // QT_CONFIG(tooltip)
        self.alhuda_button.setText("")
#if QT_CONFIG(tooltip)
        self.phonebook_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop PhoneBook", None))
#endif // QT_CONFIG(tooltip)
        self.phonebook_button.setText("")
#if QT_CONFIG(tooltip)
        self.coopurl_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop URLS", None))
#endif // QT_CONFIG(tooltip)
        self.coopurl_button.setText("")
#if QT_CONFIG(tooltip)
        self.michu_button.setToolTip(QCoreApplication.translate("MainWindow", u"Michu Guide", None))
#endif // QT_CONFIG(tooltip)
        self.michu_button.setText("")
#if QT_CONFIG(tooltip)
        self.coopay_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop Ebirr", None))
#endif // QT_CONFIG(tooltip)
        self.coopay_button.setText("")
#if QT_CONFIG(tooltip)
        self.conventional_button.setToolTip(QCoreApplication.translate("MainWindow", u"Conventional Products", None))
#endif // QT_CONFIG(tooltip)
        self.conventional_button.setText("")
#if QT_CONFIG(tooltip)
        self.coopapp_button.setToolTip(QCoreApplication.translate("MainWindow", u"CoopApp", None))
#endif // QT_CONFIG(tooltip)
        self.coopapp_button.setText("")
#if QT_CONFIG(tooltip)
        self.remittance_button.setToolTip(QCoreApplication.translate("MainWindow", u"Remittance Guide", None))
#endif // QT_CONFIG(tooltip)
        self.remittance_button.setText("")
#if QT_CONFIG(tooltip)
        self.atm_button.setToolTip(QCoreApplication.translate("MainWindow", u"CRM and NCR Guide", None))
#endif // QT_CONFIG(tooltip)
        self.atm_button.setText("")
#if QT_CONFIG(tooltip)
        self.pcinfo_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>PC Information</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pcinfo_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About PAGE ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"update page ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Network Information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ram Usage", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apps Page", None))
        self.label.setText("")
        self.home_2_button.setText("")
        self.app_2_button.setText("")
        self.about_2_button.setText("")
        self.update_2_button.setText("")
        self.exit_2_button.setText("")
        self.label_2.setText("")
        self.home_1_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.app_1_button.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.about_1_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.update_1_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.exit_1_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coopDesk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1172, 735)
        MainWindow.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_name_widget.sizePolicy().hasHeightForWidth())
        self.icon_name_widget.setSizePolicy(sizePolicy)
        self.icon_name_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-top-left-radius:10px;\n"
"\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(48, 48))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 146, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.home_1_button = QPushButton(self.icon_name_widget)
        self.home_1_button.setObjectName(u"home_1_button")
        font1 = QFont()
        font1.setFamilies([u"Roboto Medium"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.home_1_button.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/images/home_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/home_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_1_button.setIcon(icon)
        self.home_1_button.setIconSize(QSize(32, 32))
        self.home_1_button.setCheckable(True)
        self.home_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1_button)

        self.app_1_button = QPushButton(self.icon_name_widget)
        self.app_1_button.setObjectName(u"app_1_button")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.app_1_button.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/images/apps_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/apps_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.app_1_button.setIcon(icon1)
        self.app_1_button.setIconSize(QSize(32, 32))
        self.app_1_button.setCheckable(True)
        self.app_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.app_1_button)

        self.about_1_button = QPushButton(self.icon_name_widget)
        self.about_1_button.setObjectName(u"about_1_button")
        self.about_1_button.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/images/about_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/images/about_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.about_1_button.setIcon(icon2)
        self.about_1_button.setIconSize(QSize(32, 32))
        self.about_1_button.setCheckable(True)
        self.about_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.about_1_button)

        self.update_1_button = QPushButton(self.icon_name_widget)
        self.update_1_button.setObjectName(u"update_1_button")
        self.update_1_button.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/images/update_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/images/update_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.update_1_button.setIcon(icon3)
        self.update_1_button.setIconSize(QSize(32, 32))
        self.update_1_button.setCheckable(True)
        self.update_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_1_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exit_1_button = QPushButton(self.icon_name_widget)
        self.exit_1_button.setObjectName(u"exit_1_button")
        self.exit_1_button.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(u":/images/logout_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/images/logout_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.exit_1_button.setIcon(icon4)
        self.exit_1_button.setIconSize(QSize(32, 32))
        self.exit_1_button.setCheckable(True)
        self.exit_1_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.exit_1_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy1)
        self.icon_only_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align: center;\n"
"border-radius:10px;\n"
"text-alignment:center\n"
"\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_2_button = QPushButton(self.icon_only_widget)
        self.home_2_button.setObjectName(u"home_2_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_2_button.sizePolicy().hasHeightForWidth())
        self.home_2_button.setSizePolicy(sizePolicy2)
        self.home_2_button.setIcon(icon)
        self.home_2_button.setIconSize(QSize(32, 32))
        self.home_2_button.setCheckable(True)
        self.home_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2_button)

        self.app_2_button = QPushButton(self.icon_only_widget)
        self.app_2_button.setObjectName(u"app_2_button")
        self.app_2_button.setIcon(icon1)
        self.app_2_button.setIconSize(QSize(32, 32))
        self.app_2_button.setCheckable(True)
        self.app_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.app_2_button)

        self.about_2_button = QPushButton(self.icon_only_widget)
        self.about_2_button.setObjectName(u"about_2_button")
        self.about_2_button.setIcon(icon2)
        self.about_2_button.setIconSize(QSize(32, 32))
        self.about_2_button.setCheckable(True)
        self.about_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.about_2_button)

        self.update_2_button = QPushButton(self.icon_only_widget)
        self.update_2_button.setObjectName(u"update_2_button")
        self.update_2_button.setIcon(icon3)
        self.update_2_button.setIconSize(QSize(32, 32))
        self.update_2_button.setCheckable(True)
        self.update_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_2_button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_2_button = QPushButton(self.icon_only_widget)
        self.exit_2_button.setObjectName(u"exit_2_button")
        self.exit_2_button.setIcon(icon4)
        self.exit_2_button.setIconSize(QSize(32, 32))
        self.exit_2_button.setCheckable(True)
        self.exit_2_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.exit_2_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(15)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy3)
        self.main_menu.setStyleSheet(u"QToolTip {\n"
"    background:white;\n"
"    color: #00AEEF; \n"
"    border: 3px solid #00AEEF;\n"
"    font-size: 16pt;\n"
"    font-family: Arial;\n"
"    padding: 5px;\n"
"    border-radius:3px\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_19 = QPushButton(self.main_menu)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/images/menu_icon_blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/images/menu_icon_blue_inverted.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_19.setIcon(icon5)
        self.pushButton_19.setIconSize(QSize(24, 24))
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_19)

        self.horizontalSpacer = QSpacerItem(668, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"QPushButton{\n"
"  background:none;\n"
"  border: none;\n"
"\n"
"\n"
"}")
        self.gridLayout_2 = QGridLayout(self.home_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.cashmanage_button = QPushButton(self.home_page)
        self.cashmanage_button.setObjectName(u"cashmanage_button")
        icon6 = QIcon()
        icon6.addFile(u":/homeicons/teller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cashmanage_button.setIcon(icon6)
        self.cashmanage_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.cashmanage_button, 3, 1, 1, 1)

        self.about_coop_button = QPushButton(self.home_page)
        self.about_coop_button.setObjectName(u"about_coop_button")
        icon7 = QIcon()
        icon7.addFile(u":/homeicons/about_coop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.about_coop_button.setIcon(icon7)
        self.about_coop_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.about_coop_button, 3, 2, 1, 1)

        self.alhuda_button = QPushButton(self.home_page)
        self.alhuda_button.setObjectName(u"alhuda_button")
        icon8 = QIcon()
        icon8.addFile(u":/homeicons/alhuda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.alhuda_button.setIcon(icon8)
        self.alhuda_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.alhuda_button, 2, 1, 1, 1)

        self.phonebook_button = QPushButton(self.home_page)
        self.phonebook_button.setObjectName(u"phonebook_button")
        icon9 = QIcon()
        icon9.addFile(u":/homeicons/phonebook.png", QSize(), QIcon.Normal, QIcon.Off)
        self.phonebook_button.setIcon(icon9)
        self.phonebook_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.phonebook_button, 1, 2, 1, 1)

        self.coopurl_button = QPushButton(self.home_page)
        self.coopurl_button.setObjectName(u"coopurl_button")
        icon10 = QIcon()
        icon10.addFile(u":/homeicons/coopurl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coopurl_button.setIcon(icon10)
        self.coopurl_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.coopurl_button, 0, 1, 1, 1)

        self.michu_button = QPushButton(self.home_page)
        self.michu_button.setObjectName(u"michu_button")
        icon11 = QIcon()
        icon11.addFile(u":/homeicons/michu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.michu_button.setIcon(icon11)
        self.michu_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.michu_button, 0, 2, 1, 1)

        self.coopay_button = QPushButton(self.home_page)
        self.coopay_button.setObjectName(u"coopay_button")
        icon12 = QIcon()
        icon12.addFile(u":/homeicons/coopay.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coopay_button.setIcon(icon12)
        self.coopay_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.coopay_button, 2, 2, 1, 1)

        self.conventional_button = QPushButton(self.home_page)
        self.conventional_button.setObjectName(u"conventional_button")
        icon13 = QIcon()
        icon13.addFile(u":/homeicons/conventinal_products.png", QSize(), QIcon.Normal, QIcon.Off)
        self.conventional_button.setIcon(icon13)
        self.conventional_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.conventional_button, 2, 0, 1, 1)

        self.coopapp_button = QPushButton(self.home_page)
        self.coopapp_button.setObjectName(u"coopapp_button")
        icon14 = QIcon()
        icon14.addFile(u":/homeicons/coopapp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coopapp_button.setIcon(icon14)
        self.coopapp_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.coopapp_button, 3, 0, 1, 1)

        self.remittance_button = QPushButton(self.home_page)
        self.remittance_button.setObjectName(u"remittance_button")
        icon15 = QIcon()
        icon15.addFile(u":/homeicons/remittance.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remittance_button.setIcon(icon15)
        self.remittance_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.remittance_button, 1, 0, 1, 1)

        self.atm_button = QPushButton(self.home_page)
        self.atm_button.setObjectName(u"atm_button")
        icon16 = QIcon()
        icon16.addFile(u":/homeicons/atm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.atm_button.setIcon(icon16)
        self.atm_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.atm_button, 1, 1, 1, 1)

        self.pcinfo_button = QPushButton(self.home_page)
        self.pcinfo_button.setObjectName(u"pcinfo_button")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(14)
        self.pcinfo_button.setFont(font3)
        self.pcinfo_button.setToolTipDuration(-4)
        self.pcinfo_button.setStyleSheet(u"")
        icon17 = QIcon()
        icon17.addFile(u":/homeicons/pcinfo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pcinfo_button.setIcon(icon17)
        self.pcinfo_button.setIconSize(QSize(128, 128))
        self.pcinfo_button.setCheckable(True)

        self.gridLayout_2.addWidget(self.pcinfo_button, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_3 = QLabel(self.about_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 65, 301, 111))
        self.stackedWidget.addWidget(self.about_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.label_6 = QLabel(self.update_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 170, 221, 101))
        self.stackedWidget.addWidget(self.update_page)
        self.pc_info_page = QWidget()
        self.pc_info_page.setObjectName(u"pc_info_page")
        self.gridLayout_3 = QGridLayout(self.pc_info_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_3 = QFrame(self.pc_info_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(80, 10, 121, 16))
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(40, 70, 61, 16))
        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(40, 90, 61, 16))
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(110, 70, 81, 20))
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(40, 110, 41, 16))
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(110, 90, 91, 16))
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(40, 50, 61, 16))
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(110, 50, 91, 16))
        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(110, 110, 91, 16))

        self.gridLayout_3.addWidget(self.frame_3, 1, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(252, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 2, 1, 1, 2)

        self.frame_4 = QFrame(self.pc_info_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_42 = QLabel(self.frame_4)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(80, 10, 121, 16))
        self.label_43 = QLabel(self.frame_4)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(30, 60, 61, 16))
        self.label_44 = QLabel(self.frame_4)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(40, 80, 61, 16))
        self.label_45 = QLabel(self.frame_4)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(130, 60, 81, 20))
        self.label_46 = QLabel(self.frame_4)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(40, 100, 41, 16))
        self.label_47 = QLabel(self.frame_4)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(130, 80, 91, 16))
        self.label_48 = QLabel(self.frame_4)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(30, 40, 101, 16))
        self.label_49 = QLabel(self.frame_4)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(130, 40, 91, 16))
        self.label_50 = QLabel(self.frame_4)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(130, 100, 91, 16))

        self.gridLayout_3.addWidget(self.frame_4, 1, 2, 1, 2)

        self.frame_2 = QFrame(self.pc_info_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(210, 20, 121, 16))
        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(50, 70, 91, 16))
        self.label_26 = QLabel(self.frame_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(130, 70, 281, 16))
        self.label_27 = QLabel(self.frame_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(90, 90, 61, 16))
        self.label_28 = QLabel(self.frame_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(140, 90, 81, 20))
        self.label_29 = QLabel(self.frame_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(30, 110, 101, 16))
        self.label_30 = QLabel(self.frame_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(140, 110, 321, 16))
        self.label_31 = QLabel(self.frame_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(60, 50, 61, 16))
        self.label_32 = QLabel(self.frame_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(130, 50, 381, 16))

        self.gridLayout_3.addWidget(self.frame_2, 0, 2, 1, 5)

        self.horizontalSpacer_3 = QSpacerItem(252, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 2, 4, 1, 2)

        self.pushButton_3 = QPushButton(self.pc_info_page)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_3.addWidget(self.pushButton_3, 2, 3, 1, 1)

        self.frame = QFrame(self.pc_info_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 20, 121, 16))
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 70, 61, 16))
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(110, 70, 61, 16))
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 90, 61, 16))
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(110, 90, 81, 20))
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 110, 91, 16))
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(110, 110, 91, 16))
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(60, 50, 61, 16))
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(110, 50, 91, 16))

        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 2)

        self.pushButton = QPushButton(self.pc_info_page)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 2, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.pc_info_page)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 2, 6, 1, 1)

        self.frame_5 = QFrame(self.pc_info_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_5.setLineWidth(2)
        self.label_60 = QLabel(self.frame_5)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(140, 10, 121, 16))
        self.widget = QWidget(self.frame_5)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 50, 381, 66))
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_13)

        self.label_66 = QLabel(self.widget)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(32, 32))
        self.label_66.setMaximumSize(QSize(64, 64))
        self.label_66.setPixmap(QPixmap(u":/perfomance_icons/cpu_icon.png"))
        self.label_66.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_66)

        self.horizontalSpacer_4 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.label_67 = QLabel(self.widget)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_6.addWidget(self.label_67)

        self.horizontalSpacer_5 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.frame_6 = QFrame(self.widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(24, 24))
        self.frame_6.setMaximumSize(QSize(24, 24))
        self.frame_6.setStyleSheet(u"background-color:rgb(255, 85, 0)")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_6.addWidget(self.frame_6)

        self.horizontalSpacer_10 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.widget1 = QWidget(self.frame_5)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 120, 381, 66))
        self.horizontalLayout_7 = QHBoxLayout(self.widget1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_14)

        self.label_61 = QLabel(self.widget1)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(32, 32))
        self.label_61.setMaximumSize(QSize(64, 64))
        self.label_61.setPixmap(QPixmap(u":/perfomance_icons/ram_icon.png"))
        self.label_61.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_61)

        self.horizontalSpacer_6 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.label_63 = QLabel(self.widget1)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_7.addWidget(self.label_63)

        self.horizontalSpacer_7 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.frame_7 = QFrame(self.widget1)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(24, 24))
        self.frame_7.setMaximumSize(QSize(24, 24))
        self.frame_7.setStyleSheet(u"background-color:rgb(0, 255, 0)")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_7.addWidget(self.frame_7)

        self.horizontalSpacer_11 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)

        self.widget2 = QWidget(self.frame_5)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(0, 190, 381, 66))
        self.horizontalLayout_8 = QHBoxLayout(self.widget2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_15 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_15)

        self.label_62 = QLabel(self.widget2)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(32, 32))
        self.label_62.setMaximumSize(QSize(64, 64))
        self.label_62.setPixmap(QPixmap(u":/perfomance_icons/ssd_cion.png"))
        self.label_62.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_62)

        self.horizontalSpacer_8 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.label_65 = QLabel(self.widget2)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_8.addWidget(self.label_65)

        self.horizontalSpacer_9 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.frame_8 = QFrame(self.widget2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(24, 24))
        self.frame_8.setMaximumSize(QSize(24, 24))
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_8.addWidget(self.frame_8)

        self.horizontalSpacer_12 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.gridLayout_3.addWidget(self.frame_5, 1, 4, 1, 3)

        self.stackedWidget.addWidget(self.pc_info_page)
        self.apps_page = QWidget()
        self.apps_page.setObjectName(u"apps_page")
        self.label_4 = QLabel(self.apps_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 110, 161, 111))
        self.stackedWidget.addWidget(self.apps_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_19.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_19.toggled.connect(self.icon_name_widget.setVisible)
        self.home_2_button.toggled.connect(self.home_1_button.setChecked)
        self.app_2_button.toggled.connect(self.app_1_button.setChecked)
        self.about_2_button.toggled.connect(self.about_1_button.setChecked)
        self.update_2_button.toggled.connect(self.update_1_button.setChecked)
        self.exit_2_button.toggled.connect(self.exit_1_button.setChecked)
        self.exit_1_button.toggled.connect(self.exit_2_button.setChecked)
        self.update_1_button.toggled.connect(self.update_2_button.setChecked)
        self.about_1_button.toggled.connect(self.about_2_button.setChecked)
        self.app_1_button.toggled.connect(self.app_2_button.setChecked)
        self.home_1_button.toggled.connect(self.home_2_button.setChecked)
        self.exit_2_button.toggled.connect(MainWindow.close)
        self.exit_1_button.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.home_1_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.app_1_button.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.about_1_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.update_1_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.exit_1_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText("")
        self.home_2_button.setText("")
        self.app_2_button.setText("")
        self.about_2_button.setText("")
        self.update_2_button.setText("")
        self.exit_2_button.setText("")
        self.pushButton_19.setText("")
#if QT_CONFIG(tooltip)
        self.cashmanage_button.setToolTip(QCoreApplication.translate("MainWindow", u"Daily Cash Management", None))
#endif // QT_CONFIG(tooltip)
        self.cashmanage_button.setText("")
#if QT_CONFIG(tooltip)
        self.about_coop_button.setToolTip(QCoreApplication.translate("MainWindow", u"About Coop", None))
#endif // QT_CONFIG(tooltip)
        self.about_coop_button.setText("")
#if QT_CONFIG(tooltip)
        self.alhuda_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop Alhuda ", None))
#endif // QT_CONFIG(tooltip)
        self.alhuda_button.setText("")
#if QT_CONFIG(tooltip)
        self.phonebook_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop PhoneBook", None))
#endif // QT_CONFIG(tooltip)
        self.phonebook_button.setText("")
#if QT_CONFIG(tooltip)
        self.coopurl_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop URLS", None))
#endif // QT_CONFIG(tooltip)
        self.coopurl_button.setText("")
#if QT_CONFIG(tooltip)
        self.michu_button.setToolTip(QCoreApplication.translate("MainWindow", u"Michu Guide", None))
#endif // QT_CONFIG(tooltip)
        self.michu_button.setText("")
#if QT_CONFIG(tooltip)
        self.coopay_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop Ebirr", None))
#endif // QT_CONFIG(tooltip)
        self.coopay_button.setText("")
#if QT_CONFIG(tooltip)
        self.conventional_button.setToolTip(QCoreApplication.translate("MainWindow", u"Conventional Products", None))
#endif // QT_CONFIG(tooltip)
        self.conventional_button.setText("")
#if QT_CONFIG(tooltip)
        self.coopapp_button.setToolTip(QCoreApplication.translate("MainWindow", u"CoopApp", None))
#endif // QT_CONFIG(tooltip)
        self.coopapp_button.setText("")
#if QT_CONFIG(tooltip)
        self.remittance_button.setToolTip(QCoreApplication.translate("MainWindow", u"Remittance Guide", None))
#endif // QT_CONFIG(tooltip)
        self.remittance_button.setText("")
#if QT_CONFIG(tooltip)
        self.atm_button.setToolTip(QCoreApplication.translate("MainWindow", u"CRM and NCR Guide", None))
#endif // QT_CONFIG(tooltip)
        self.atm_button.setText("")
#if QT_CONFIG(tooltip)
        self.pcinfo_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>PC Information</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pcinfo_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About PAGE ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"update page ", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Storage ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Used", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"300GB", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Vendor ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"500GB", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"221GB", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"SAMSUNG", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Display ", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Bit/pixel", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"2k", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Vendor ", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"30bit/pixel", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Adapte Type", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Intel Iris Graphics ", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"SAMSUNG", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"System Info", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"System Type :", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"64-bit operating system, x64-based processor", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"RAM : ", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"8GB", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Platform Version:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Windows 11, Version 23H2", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Processor :", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"11th Gen Intel(R) Core(TM) i5-11320H @ 3.20GHz   3.19 GHz", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Task Manager ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ethernet IP info", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"IP address  :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"10.1.15.7", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Subnet:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"255.255.255.0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Default Gateway :", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"10.1.15.1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Status :", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"connected", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add Printers", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Performance", None))
        self.label_66.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"3.1gHz (3.2%)", None))
        self.label_61.setText("")
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"6.7/8 GB (90%)", None))
        self.label_62.setText("")
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"40kb/s", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apps Page", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coopDesk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1172, 735)
        MainWindow.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_name_widget.sizePolicy().hasHeightForWidth())
        self.icon_name_widget.setSizePolicy(sizePolicy)
        self.icon_name_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-top-left-radius:10px;\n"
"\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(48, 48))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 146, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.home_1_button = QPushButton(self.icon_name_widget)
        self.home_1_button.setObjectName(u"home_1_button")
        font1 = QFont()
        font1.setFamilies([u"Roboto Medium"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.home_1_button.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/images/home_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/home_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_1_button.setIcon(icon)
        self.home_1_button.setIconSize(QSize(32, 32))
        self.home_1_button.setCheckable(True)
        self.home_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1_button)

        self.app_1_button = QPushButton(self.icon_name_widget)
        self.app_1_button.setObjectName(u"app_1_button")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.app_1_button.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/images/apps_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/apps_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.app_1_button.setIcon(icon1)
        self.app_1_button.setIconSize(QSize(32, 32))
        self.app_1_button.setCheckable(True)
        self.app_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.app_1_button)

        self.about_1_button = QPushButton(self.icon_name_widget)
        self.about_1_button.setObjectName(u"about_1_button")
        self.about_1_button.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/images/about_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/images/about_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.about_1_button.setIcon(icon2)
        self.about_1_button.setIconSize(QSize(32, 32))
        self.about_1_button.setCheckable(True)
        self.about_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.about_1_button)

        self.update_1_button = QPushButton(self.icon_name_widget)
        self.update_1_button.setObjectName(u"update_1_button")
        self.update_1_button.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/images/update_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/images/update_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.update_1_button.setIcon(icon3)
        self.update_1_button.setIconSize(QSize(32, 32))
        self.update_1_button.setCheckable(True)
        self.update_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_1_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exit_1_button = QPushButton(self.icon_name_widget)
        self.exit_1_button.setObjectName(u"exit_1_button")
        self.exit_1_button.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(u":/images/logout_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/images/logout_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.exit_1_button.setIcon(icon4)
        self.exit_1_button.setIconSize(QSize(32, 32))
        self.exit_1_button.setCheckable(True)
        self.exit_1_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.exit_1_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy1)
        self.icon_only_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align: center;\n"
"border-radius:10px;\n"
"text-alignment:center\n"
"\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_2_button = QPushButton(self.icon_only_widget)
        self.home_2_button.setObjectName(u"home_2_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_2_button.sizePolicy().hasHeightForWidth())
        self.home_2_button.setSizePolicy(sizePolicy2)
        self.home_2_button.setIcon(icon)
        self.home_2_button.setIconSize(QSize(32, 32))
        self.home_2_button.setCheckable(True)
        self.home_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2_button)

        self.app_2_button = QPushButton(self.icon_only_widget)
        self.app_2_button.setObjectName(u"app_2_button")
        self.app_2_button.setIcon(icon1)
        self.app_2_button.setIconSize(QSize(32, 32))
        self.app_2_button.setCheckable(True)
        self.app_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.app_2_button)

        self.about_2_button = QPushButton(self.icon_only_widget)
        self.about_2_button.setObjectName(u"about_2_button")
        self.about_2_button.setIcon(icon2)
        self.about_2_button.setIconSize(QSize(32, 32))
        self.about_2_button.setCheckable(True)
        self.about_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.about_2_button)

        self.update_2_button = QPushButton(self.icon_only_widget)
        self.update_2_button.setObjectName(u"update_2_button")
        self.update_2_button.setIcon(icon3)
        self.update_2_button.setIconSize(QSize(32, 32))
        self.update_2_button.setCheckable(True)
        self.update_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_2_button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_2_button = QPushButton(self.icon_only_widget)
        self.exit_2_button.setObjectName(u"exit_2_button")
        self.exit_2_button.setIcon(icon4)
        self.exit_2_button.setIconSize(QSize(32, 32))
        self.exit_2_button.setCheckable(True)
        self.exit_2_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.exit_2_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(15)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy3)
        self.main_menu.setStyleSheet(u"QToolTip {\n"
"    background:white;\n"
"    color: #00AEEF; \n"
"    border: 3px solid #00AEEF;\n"
"    font-size: 16pt;\n"
"    font-family: Arial;\n"
"    padding: 5px;\n"
"    border-radius:3px\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_19 = QPushButton(self.main_menu)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/images/menu_icon_blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/images/menu_icon_blue_inverted.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_19.setIcon(icon5)
        self.pushButton_19.setIconSize(QSize(24, 24))
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_19)

        self.horizontalSpacer = QSpacerItem(668, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"QPushButton{\n"
"  background:none;\n"
"  border: none;\n"
"\n"
"\n"
"}")
        self.gridLayout_2 = QGridLayout(self.home_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.cashmanage_button = QPushButton(self.home_page)
        self.cashmanage_button.setObjectName(u"cashmanage_button")
        icon6 = QIcon()
        icon6.addFile(u":/homeicons/teller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cashmanage_button.setIcon(icon6)
        self.cashmanage_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.cashmanage_button, 3, 1, 1, 1)

        self.about_coop_button = QPushButton(self.home_page)
        self.about_coop_button.setObjectName(u"about_coop_button")
        icon7 = QIcon()
        icon7.addFile(u":/homeicons/about_coop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.about_coop_button.setIcon(icon7)
        self.about_coop_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.about_coop_button, 3, 2, 1, 1)

        self.alhuda_button = QPushButton(self.home_page)
        self.alhuda_button.setObjectName(u"alhuda_button")
        icon8 = QIcon()
        icon8.addFile(u":/homeicons/alhuda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.alhuda_button.setIcon(icon8)
        self.alhuda_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.alhuda_button, 2, 1, 1, 1)

        self.phonebook_button = QPushButton(self.home_page)
        self.phonebook_button.setObjectName(u"phonebook_button")
        icon9 = QIcon()
        icon9.addFile(u":/homeicons/phonebook.png", QSize(), QIcon.Normal, QIcon.Off)
        self.phonebook_button.setIcon(icon9)
        self.phonebook_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.phonebook_button, 1, 2, 1, 1)

        self.coopurl_button = QPushButton(self.home_page)
        self.coopurl_button.setObjectName(u"coopurl_button")
        icon10 = QIcon()
        icon10.addFile(u":/homeicons/coopurl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coopurl_button.setIcon(icon10)
        self.coopurl_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.coopurl_button, 0, 1, 1, 1)

        self.michu_button = QPushButton(self.home_page)
        self.michu_button.setObjectName(u"michu_button")
        icon11 = QIcon()
        icon11.addFile(u":/homeicons/michu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.michu_button.setIcon(icon11)
        self.michu_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.michu_button, 0, 2, 1, 1)

        self.coopay_button = QPushButton(self.home_page)
        self.coopay_button.setObjectName(u"coopay_button")
        icon12 = QIcon()
        icon12.addFile(u":/homeicons/coopay.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coopay_button.setIcon(icon12)
        self.coopay_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.coopay_button, 2, 2, 1, 1)

        self.conventional_button = QPushButton(self.home_page)
        self.conventional_button.setObjectName(u"conventional_button")
        icon13 = QIcon()
        icon13.addFile(u":/homeicons/conventinal_products.png", QSize(), QIcon.Normal, QIcon.Off)
        self.conventional_button.setIcon(icon13)
        self.conventional_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.conventional_button, 2, 0, 1, 1)

        self.coopapp_button = QPushButton(self.home_page)
        self.coopapp_button.setObjectName(u"coopapp_button")
        icon14 = QIcon()
        icon14.addFile(u":/homeicons/coopapp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coopapp_button.setIcon(icon14)
        self.coopapp_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.coopapp_button, 3, 0, 1, 1)

        self.remittance_button = QPushButton(self.home_page)
        self.remittance_button.setObjectName(u"remittance_button")
        icon15 = QIcon()
        icon15.addFile(u":/homeicons/remittance.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remittance_button.setIcon(icon15)
        self.remittance_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.remittance_button, 1, 0, 1, 1)

        self.atm_button = QPushButton(self.home_page)
        self.atm_button.setObjectName(u"atm_button")
        icon16 = QIcon()
        icon16.addFile(u":/homeicons/atm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.atm_button.setIcon(icon16)
        self.atm_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.atm_button, 1, 1, 1, 1)

        self.pcinfo_button = QPushButton(self.home_page)
        self.pcinfo_button.setObjectName(u"pcinfo_button")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(14)
        self.pcinfo_button.setFont(font3)
        self.pcinfo_button.setToolTipDuration(-4)
        self.pcinfo_button.setStyleSheet(u"")
        icon17 = QIcon()
        icon17.addFile(u":/homeicons/pcinfo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pcinfo_button.setIcon(icon17)
        self.pcinfo_button.setIconSize(QSize(128, 128))
        self.pcinfo_button.setCheckable(True)

        self.gridLayout_2.addWidget(self.pcinfo_button, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_3 = QLabel(self.about_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 65, 301, 111))
        self.stackedWidget.addWidget(self.about_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.label_6 = QLabel(self.update_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 170, 221, 101))
        self.stackedWidget.addWidget(self.update_page)
        self.pc_info_page = QWidget()
        self.pc_info_page.setObjectName(u"pc_info_page")
        self.gridLayout_3 = QGridLayout(self.pc_info_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton = QPushButton(self.pc_info_page)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(252, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 2, 1, 1, 2)

        self.frame_4 = QFrame(self.pc_info_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_42 = QLabel(self.frame_4)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(80, 10, 121, 16))
        self.label_43 = QLabel(self.frame_4)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(30, 60, 61, 16))
        self.label_44 = QLabel(self.frame_4)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(40, 80, 61, 16))
        self.label_45 = QLabel(self.frame_4)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(130, 60, 81, 20))
        self.label_46 = QLabel(self.frame_4)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(40, 100, 41, 16))
        self.label_47 = QLabel(self.frame_4)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(130, 80, 91, 16))
        self.label_48 = QLabel(self.frame_4)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(30, 40, 101, 16))
        self.label_49 = QLabel(self.frame_4)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(130, 40, 91, 16))
        self.label_50 = QLabel(self.frame_4)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(130, 100, 91, 16))

        self.gridLayout_3.addWidget(self.frame_4, 1, 2, 1, 2)

        self.frame_3 = QFrame(self.pc_info_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(80, 10, 121, 16))
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(40, 70, 61, 16))
        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(40, 90, 61, 16))
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(110, 70, 81, 20))
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(40, 110, 41, 16))
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(110, 90, 91, 16))
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(40, 50, 61, 16))
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(110, 50, 91, 16))
        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(110, 110, 91, 16))

        self.gridLayout_3.addWidget(self.frame_3, 1, 0, 1, 2)

        self.pushButton_3 = QPushButton(self.pc_info_page)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_3.addWidget(self.pushButton_3, 2, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.pc_info_page)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 2, 6, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(252, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 2, 4, 1, 2)

        self.frame_5 = QFrame(self.pc_info_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_5.setLineWidth(2)
        self.label_60 = QLabel(self.frame_5)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(140, 30, 151, 16))
        self.widget = QWidget(self.frame_5)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(53, 51, 281, 221))
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self.widget)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(32, 32))
        self.label_66.setMaximumSize(QSize(64, 64))
        self.label_66.setPixmap(QPixmap(u":/perfomance_icons/cpu_icon.png"))
        self.label_66.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_66, 0, 0, 1, 1)

        self.label_63 = QLabel(self.widget)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_63, 1, 1, 1, 1)

        self.frame_6 = QFrame(self.widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(24, 24))
        self.frame_6.setMaximumSize(QSize(24, 24))
        self.frame_6.setStyleSheet(u"background-color:rgb(255, 85, 0)")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_4.addWidget(self.frame_6, 0, 2, 1, 1)

        self.label_65 = QLabel(self.widget)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_65, 2, 1, 1, 1)

        self.label_62 = QLabel(self.widget)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(32, 32))
        self.label_62.setMaximumSize(QSize(64, 64))
        self.label_62.setPixmap(QPixmap(u":/perfomance_icons/ssd_cion.png"))
        self.label_62.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_62, 2, 0, 1, 1)

        self.label_67 = QLabel(self.widget)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_67, 0, 1, 1, 1)

        self.frame_8 = QFrame(self.widget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(24, 24))
        self.frame_8.setMaximumSize(QSize(24, 24))
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_4.addWidget(self.frame_8, 2, 2, 1, 1)

        self.frame_7 = QFrame(self.widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(24, 24))
        self.frame_7.setMaximumSize(QSize(24, 24))
        self.frame_7.setStyleSheet(u"background-color:rgb(0, 255, 0)")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_4.addWidget(self.frame_7, 1, 2, 1, 1)

        self.label_61 = QLabel(self.widget)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(32, 32))
        self.label_61.setMaximumSize(QSize(64, 64))
        self.label_61.setPixmap(QPixmap(u":/perfomance_icons/ram_icon.png"))
        self.label_61.setScaledContents(True)
        self.label_61.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_61, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_5, 1, 4, 1, 3)

        self.frame_2 = QFrame(self.pc_info_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(240, 30, 121, 16))
        self.widget1 = QWidget(self.frame_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(70, 50, 401, 201))
        self.gridLayout_5 = QGridLayout(self.widget1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.widget1)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_5.addWidget(self.label_36, 5, 1, 1, 1)

        self.label_31 = QLabel(self.widget1)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_5.addWidget(self.label_31, 0, 0, 1, 1)

        self.label_25 = QLabel(self.widget1)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_5.addWidget(self.label_25, 1, 0, 1, 1)

        self.label_26 = QLabel(self.widget1)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 1, 1, 1, 1)

        self.label_35 = QLabel(self.widget1)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_5.addWidget(self.label_35, 5, 0, 1, 1)

        self.label_27 = QLabel(self.widget1)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_5.addWidget(self.label_27, 2, 0, 1, 1)

        self.label_17 = QLabel(self.widget1)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 4, 0, 1, 1)

        self.label_29 = QLabel(self.widget1)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_5.addWidget(self.label_29, 3, 0, 1, 1)

        self.label_34 = QLabel(self.widget1)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_5.addWidget(self.label_34, 4, 1, 1, 1)

        self.label_32 = QLabel(self.widget1)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_5.addWidget(self.label_32, 0, 1, 1, 1)

        self.label_28 = QLabel(self.widget1)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 2, 1, 1, 1)

        self.label_30 = QLabel(self.widget1)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_5.addWidget(self.label_30, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 0, 3, 1, 4)

        self.frame = QFrame(self.pc_info_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(150, 10, 121, 16))
        self.label_54 = QLabel(self.frame)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(70, 240, 291, 16))
        self.widget2 = QWidget(self.frame)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(70, 40, 261, 181))
        self.gridLayout_6 = QGridLayout(self.widget2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_14 = QLabel(self.widget2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 0, 1, 1, 1)

        self.label_7 = QLabel(self.widget2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_8 = QLabel(self.widget2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 1, 1, 1, 1)

        self.label_9 = QLabel(self.widget2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_10 = QLabel(self.widget2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_6.addWidget(self.label_10, 2, 1, 1, 1)

        self.label_11 = QLabel(self.widget2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_6.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_12 = QLabel(self.widget2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 3, 1, 1, 1)

        self.label_37 = QLabel(self.widget2)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_6.addWidget(self.label_37, 4, 0, 1, 1)

        self.label_38 = QLabel(self.widget2)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_6.addWidget(self.label_38, 4, 1, 1, 1)

        self.label_39 = QLabel(self.widget2)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_6.addWidget(self.label_39, 5, 0, 1, 1)

        self.label_40 = QLabel(self.widget2)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_6.addWidget(self.label_40, 5, 1, 1, 1)

        self.label_41 = QLabel(self.widget2)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_6.addWidget(self.label_41, 6, 0, 1, 1)

        self.label_51 = QLabel(self.widget2)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_6.addWidget(self.label_51, 6, 1, 1, 1)

        self.label_52 = QLabel(self.widget2)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_6.addWidget(self.label_52, 7, 0, 1, 1)

        self.label_53 = QLabel(self.widget2)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_6.addWidget(self.label_53, 7, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.pc_info_page)
        self.apps_page = QWidget()
        self.apps_page.setObjectName(u"apps_page")
        self.label_4 = QLabel(self.apps_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 110, 161, 111))
        self.stackedWidget.addWidget(self.apps_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_19.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_19.toggled.connect(self.icon_name_widget.setVisible)
        self.home_2_button.toggled.connect(self.home_1_button.setChecked)
        self.app_2_button.toggled.connect(self.app_1_button.setChecked)
        self.about_2_button.toggled.connect(self.about_1_button.setChecked)
        self.update_2_button.toggled.connect(self.update_1_button.setChecked)
        self.exit_2_button.toggled.connect(self.exit_1_button.setChecked)
        self.exit_1_button.toggled.connect(self.exit_2_button.setChecked)
        self.update_1_button.toggled.connect(self.update_2_button.setChecked)
        self.about_1_button.toggled.connect(self.about_2_button.setChecked)
        self.app_1_button.toggled.connect(self.app_2_button.setChecked)
        self.home_1_button.toggled.connect(self.home_2_button.setChecked)
        self.exit_2_button.toggled.connect(MainWindow.close)
        self.exit_1_button.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.home_1_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.app_1_button.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.about_1_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.update_1_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.exit_1_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText("")
        self.home_2_button.setText("")
        self.app_2_button.setText("")
        self.about_2_button.setText("")
        self.update_2_button.setText("")
        self.exit_2_button.setText("")
        self.pushButton_19.setText("")
#if QT_CONFIG(tooltip)
        self.cashmanage_button.setToolTip(QCoreApplication.translate("MainWindow", u"Daily Cash Management", None))
#endif // QT_CONFIG(tooltip)
        self.cashmanage_button.setText("")
#if QT_CONFIG(tooltip)
        self.about_coop_button.setToolTip(QCoreApplication.translate("MainWindow", u"About Coop", None))
#endif // QT_CONFIG(tooltip)
        self.about_coop_button.setText("")
#if QT_CONFIG(tooltip)
        self.alhuda_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop Alhuda ", None))
#endif // QT_CONFIG(tooltip)
        self.alhuda_button.setText("")
#if QT_CONFIG(tooltip)
        self.phonebook_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop PhoneBook", None))
#endif // QT_CONFIG(tooltip)
        self.phonebook_button.setText("")
#if QT_CONFIG(tooltip)
        self.coopurl_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop URLS", None))
#endif // QT_CONFIG(tooltip)
        self.coopurl_button.setText("")
#if QT_CONFIG(tooltip)
        self.michu_button.setToolTip(QCoreApplication.translate("MainWindow", u"Michu Guide", None))
#endif // QT_CONFIG(tooltip)
        self.michu_button.setText("")
#if QT_CONFIG(tooltip)
        self.coopay_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop Ebirr", None))
#endif // QT_CONFIG(tooltip)
        self.coopay_button.setText("")
#if QT_CONFIG(tooltip)
        self.conventional_button.setToolTip(QCoreApplication.translate("MainWindow", u"Conventional Products", None))
#endif // QT_CONFIG(tooltip)
        self.conventional_button.setText("")
#if QT_CONFIG(tooltip)
        self.coopapp_button.setToolTip(QCoreApplication.translate("MainWindow", u"CoopApp", None))
#endif // QT_CONFIG(tooltip)
        self.coopapp_button.setText("")
#if QT_CONFIG(tooltip)
        self.remittance_button.setToolTip(QCoreApplication.translate("MainWindow", u"Remittance Guide", None))
#endif // QT_CONFIG(tooltip)
        self.remittance_button.setText("")
#if QT_CONFIG(tooltip)
        self.atm_button.setToolTip(QCoreApplication.translate("MainWindow", u"CRM and NCR Guide", None))
#endif // QT_CONFIG(tooltip)
        self.atm_button.setText("")
#if QT_CONFIG(tooltip)
        self.pcinfo_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>PC Information</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pcinfo_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About PAGE ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"update page ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Display ", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Bit/pixel", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"2k", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Vendor ", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"30bit/pixel", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Adapte Type", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Intel Iris Graphics ", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"SAMSUNG", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Storage ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Used", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"300GB", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Vendor ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"500GB", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"221GB", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"SAMSUNG", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Task Manager ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add Printers", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Performance (Usage %)", None))
        self.label_66.setText("")
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"6.7/8 GB (90%)", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"0.04%", None))
        self.label_62.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"3.1gHz (3.2%)", None))
        self.label_61.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"System Info", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Professional", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Processor :", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"System Type :", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"64-bit operating system, x64-based processor", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Edition:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Installed RAM : ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CPU cores:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Platform :", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"8 Cores (Logical Processors)", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"11th Gen Intel(R) Core(TM) i5-11320H @ 3.20GHz   3.19 GHz", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"8GB", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Windows 11, Version 23H2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ethernet IP info", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Seems you PC is not connected to Wired LAN!", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Adapter:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Ethernet 3", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"IP Address:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"10.1.15.7", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Subnet mask:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"255.255.255.0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Default Gateway :", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"10.1.15.1", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Default DNS:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"10.1.70.10", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Alternative DNS:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"4.4.2.2", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"MAC  Address", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"W3HR5YR5RY6FC4B4", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"100Mbps", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apps Page", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coopDesk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1172, 735)
        MainWindow.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_name_widget.sizePolicy().hasHeightForWidth())
        self.icon_name_widget.setSizePolicy(sizePolicy)
        self.icon_name_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-top-left-radius:10px;\n"
"\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(48, 48))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 146, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.home_1_button = QPushButton(self.icon_name_widget)
        self.home_1_button.setObjectName(u"home_1_button")
        font1 = QFont()
        font1.setFamilies([u"Roboto Medium"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.home_1_button.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/images/home_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/home_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_1_button.setIcon(icon)
        self.home_1_button.setIconSize(QSize(32, 32))
        self.home_1_button.setCheckable(True)
        self.home_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1_button)

        self.app_1_button = QPushButton(self.icon_name_widget)
        self.app_1_button.setObjectName(u"app_1_button")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.app_1_button.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/images/apps_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/apps_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.app_1_button.setIcon(icon1)
        self.app_1_button.setIconSize(QSize(32, 32))
        self.app_1_button.setCheckable(True)
        self.app_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.app_1_button)

        self.about_1_button = QPushButton(self.icon_name_widget)
        self.about_1_button.setObjectName(u"about_1_button")
        self.about_1_button.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/images/about_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/images/about_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.about_1_button.setIcon(icon2)
        self.about_1_button.setIconSize(QSize(32, 32))
        self.about_1_button.setCheckable(True)
        self.about_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.about_1_button)

        self.update_1_button = QPushButton(self.icon_name_widget)
        self.update_1_button.setObjectName(u"update_1_button")
        self.update_1_button.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/images/update_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/images/update_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.update_1_button.setIcon(icon3)
        self.update_1_button.setIconSize(QSize(32, 32))
        self.update_1_button.setCheckable(True)
        self.update_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_1_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exit_1_button = QPushButton(self.icon_name_widget)
        self.exit_1_button.setObjectName(u"exit_1_button")
        self.exit_1_button.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(u":/images/logout_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/images/logout_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.exit_1_button.setIcon(icon4)
        self.exit_1_button.setIconSize(QSize(32, 32))
        self.exit_1_button.setCheckable(True)
        self.exit_1_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.exit_1_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy1)
        self.icon_only_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align: center;\n"
"border-radius:10px;\n"
"text-alignment:center\n"
"\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_2_button = QPushButton(self.icon_only_widget)
        self.home_2_button.setObjectName(u"home_2_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_2_button.sizePolicy().hasHeightForWidth())
        self.home_2_button.setSizePolicy(sizePolicy2)
        self.home_2_button.setIcon(icon)
        self.home_2_button.setIconSize(QSize(32, 32))
        self.home_2_button.setCheckable(True)
        self.home_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2_button)

        self.app_2_button = QPushButton(self.icon_only_widget)
        self.app_2_button.setObjectName(u"app_2_button")
        self.app_2_button.setIcon(icon1)
        self.app_2_button.setIconSize(QSize(32, 32))
        self.app_2_button.setCheckable(True)
        self.app_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.app_2_button)

        self.about_2_button = QPushButton(self.icon_only_widget)
        self.about_2_button.setObjectName(u"about_2_button")
        self.about_2_button.setIcon(icon2)
        self.about_2_button.setIconSize(QSize(32, 32))
        self.about_2_button.setCheckable(True)
        self.about_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.about_2_button)

        self.update_2_button = QPushButton(self.icon_only_widget)
        self.update_2_button.setObjectName(u"update_2_button")
        self.update_2_button.setIcon(icon3)
        self.update_2_button.setIconSize(QSize(32, 32))
        self.update_2_button.setCheckable(True)
        self.update_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_2_button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_2_button = QPushButton(self.icon_only_widget)
        self.exit_2_button.setObjectName(u"exit_2_button")
        self.exit_2_button.setIcon(icon4)
        self.exit_2_button.setIconSize(QSize(32, 32))
        self.exit_2_button.setCheckable(True)
        self.exit_2_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.exit_2_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(15)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy3)
        self.main_menu.setStyleSheet(u"QToolTip {\n"
"    background:white;\n"
"    color: #00AEEF; \n"
"    border: 3px solid #00AEEF;\n"
"    font-size: 16pt;\n"
"    font-family: Arial;\n"
"    padding: 5px;\n"
"    border-radius:3px\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_19 = QPushButton(self.main_menu)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/images/menu_icon_blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/images/menu_icon_blue_inverted.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_19.setIcon(icon5)
        self.pushButton_19.setIconSize(QSize(24, 24))
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_19)

        self.horizontalSpacer = QSpacerItem(668, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"QPushButton{\n"
"  background:none;\n"
"  border: none;\n"
"\n"
"\n"
"}")
        self.gridLayout_2 = QGridLayout(self.home_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.cashmanage_button = QPushButton(self.home_page)
        self.cashmanage_button.setObjectName(u"cashmanage_button")
        icon6 = QIcon()
        icon6.addFile(u":/homeicons/teller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cashmanage_button.setIcon(icon6)
        self.cashmanage_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.cashmanage_button, 3, 1, 1, 1)

        self.about_coop_button = QPushButton(self.home_page)
        self.about_coop_button.setObjectName(u"about_coop_button")
        icon7 = QIcon()
        icon7.addFile(u":/homeicons/about_coop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.about_coop_button.setIcon(icon7)
        self.about_coop_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.about_coop_button, 3, 2, 1, 1)

        self.alhuda_button = QPushButton(self.home_page)
        self.alhuda_button.setObjectName(u"alhuda_button")
        icon8 = QIcon()
        icon8.addFile(u":/homeicons/alhuda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.alhuda_button.setIcon(icon8)
        self.alhuda_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.alhuda_button, 2, 1, 1, 1)

        self.phonebook_button = QPushButton(self.home_page)
        self.phonebook_button.setObjectName(u"phonebook_button")
        icon9 = QIcon()
        icon9.addFile(u":/homeicons/phonebook.png", QSize(), QIcon.Normal, QIcon.Off)
        self.phonebook_button.setIcon(icon9)
        self.phonebook_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.phonebook_button, 1, 2, 1, 1)

        self.coopurl_button = QPushButton(self.home_page)
        self.coopurl_button.setObjectName(u"coopurl_button")
        icon10 = QIcon()
        icon10.addFile(u":/homeicons/coopurl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coopurl_button.setIcon(icon10)
        self.coopurl_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.coopurl_button, 0, 1, 1, 1)

        self.michu_button = QPushButton(self.home_page)
        self.michu_button.setObjectName(u"michu_button")
        icon11 = QIcon()
        icon11.addFile(u":/homeicons/michu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.michu_button.setIcon(icon11)
        self.michu_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.michu_button, 0, 2, 1, 1)

        self.coopay_button = QPushButton(self.home_page)
        self.coopay_button.setObjectName(u"coopay_button")
        icon12 = QIcon()
        icon12.addFile(u":/homeicons/coopay.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coopay_button.setIcon(icon12)
        self.coopay_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.coopay_button, 2, 2, 1, 1)

        self.conventional_button = QPushButton(self.home_page)
        self.conventional_button.setObjectName(u"conventional_button")
        icon13 = QIcon()
        icon13.addFile(u":/homeicons/conventinal_products.png", QSize(), QIcon.Normal, QIcon.Off)
        self.conventional_button.setIcon(icon13)
        self.conventional_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.conventional_button, 2, 0, 1, 1)

        self.coopapp_button = QPushButton(self.home_page)
        self.coopapp_button.setObjectName(u"coopapp_button")
        icon14 = QIcon()
        icon14.addFile(u":/homeicons/coopapp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coopapp_button.setIcon(icon14)
        self.coopapp_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.coopapp_button, 3, 0, 1, 1)

        self.remittance_button = QPushButton(self.home_page)
        self.remittance_button.setObjectName(u"remittance_button")
        icon15 = QIcon()
        icon15.addFile(u":/homeicons/remittance.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remittance_button.setIcon(icon15)
        self.remittance_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.remittance_button, 1, 0, 1, 1)

        self.atm_button = QPushButton(self.home_page)
        self.atm_button.setObjectName(u"atm_button")
        icon16 = QIcon()
        icon16.addFile(u":/homeicons/atm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.atm_button.setIcon(icon16)
        self.atm_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.atm_button, 1, 1, 1, 1)

        self.pcinfo_button = QPushButton(self.home_page)
        self.pcinfo_button.setObjectName(u"pcinfo_button")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(14)
        self.pcinfo_button.setFont(font3)
        self.pcinfo_button.setToolTipDuration(-4)
        self.pcinfo_button.setStyleSheet(u"")
        icon17 = QIcon()
        icon17.addFile(u":/homeicons/pcinfo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pcinfo_button.setIcon(icon17)
        self.pcinfo_button.setIconSize(QSize(128, 128))
        self.pcinfo_button.setCheckable(True)

        self.gridLayout_2.addWidget(self.pcinfo_button, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_3 = QLabel(self.about_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 65, 301, 111))
        self.stackedWidget.addWidget(self.about_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.label_6 = QLabel(self.update_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 170, 221, 101))
        self.stackedWidget.addWidget(self.update_page)
        self.pc_info_page = QWidget()
        self.pc_info_page.setObjectName(u"pc_info_page")
        self.gridLayout_3 = QGridLayout(self.pc_info_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton = QPushButton(self.pc_info_page)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(252, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 2, 1, 1, 2)

        self.frame_4 = QFrame(self.pc_info_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_42 = QLabel(self.frame_4)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(80, 10, 121, 16))
        self.label_43 = QLabel(self.frame_4)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(30, 60, 61, 16))
        self.label_44 = QLabel(self.frame_4)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(40, 80, 61, 16))
        self.label_45 = QLabel(self.frame_4)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(130, 60, 81, 20))
        self.label_46 = QLabel(self.frame_4)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(40, 100, 41, 16))
        self.label_47 = QLabel(self.frame_4)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(130, 80, 91, 16))
        self.label_48 = QLabel(self.frame_4)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(30, 40, 101, 16))
        self.label_49 = QLabel(self.frame_4)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(130, 40, 91, 16))
        self.label_50 = QLabel(self.frame_4)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(130, 100, 91, 16))

        self.gridLayout_3.addWidget(self.frame_4, 1, 2, 1, 2)

        self.frame_3 = QFrame(self.pc_info_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(80, 10, 121, 16))
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(40, 70, 61, 16))
        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(40, 90, 61, 16))
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(110, 70, 81, 20))
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(40, 110, 41, 16))
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(110, 90, 91, 16))
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(40, 50, 61, 16))
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(110, 50, 91, 16))
        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(110, 110, 91, 16))

        self.gridLayout_3.addWidget(self.frame_3, 1, 0, 1, 2)

        self.pushButton_3 = QPushButton(self.pc_info_page)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_3.addWidget(self.pushButton_3, 2, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.pc_info_page)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 2, 6, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(252, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 2, 4, 1, 2)

        self.frame_5 = QFrame(self.pc_info_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_5.setLineWidth(2)
        self.label_60 = QLabel(self.frame_5)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(140, 30, 151, 16))
        self.widget = QWidget(self.frame_5)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(53, 51, 281, 221))
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self.widget)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(32, 32))
        self.label_66.setMaximumSize(QSize(64, 64))
        self.label_66.setPixmap(QPixmap(u":/perfomance_icons/cpu_icon.png"))
        self.label_66.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_66, 0, 0, 1, 1)

        self.label_63 = QLabel(self.widget)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_63, 1, 1, 1, 1)

        self.frame_6 = QFrame(self.widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(24, 24))
        self.frame_6.setMaximumSize(QSize(24, 24))
        self.frame_6.setStyleSheet(u"background-color:rgb(255, 85, 0)")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_4.addWidget(self.frame_6, 0, 2, 1, 1)

        self.label_65 = QLabel(self.widget)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_65, 2, 1, 1, 1)

        self.label_62 = QLabel(self.widget)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(32, 32))
        self.label_62.setMaximumSize(QSize(64, 64))
        self.label_62.setPixmap(QPixmap(u":/perfomance_icons/ssd_cion.png"))
        self.label_62.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_62, 2, 0, 1, 1)

        self.label_67 = QLabel(self.widget)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_67, 0, 1, 1, 1)

        self.frame_8 = QFrame(self.widget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(24, 24))
        self.frame_8.setMaximumSize(QSize(24, 24))
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_4.addWidget(self.frame_8, 2, 2, 1, 1)

        self.frame_7 = QFrame(self.widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(24, 24))
        self.frame_7.setMaximumSize(QSize(24, 24))
        self.frame_7.setStyleSheet(u"background-color:rgb(0, 255, 0)")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_4.addWidget(self.frame_7, 1, 2, 1, 1)

        self.label_61 = QLabel(self.widget)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(32, 32))
        self.label_61.setMaximumSize(QSize(64, 64))
        self.label_61.setPixmap(QPixmap(u":/perfomance_icons/ram_icon.png"))
        self.label_61.setScaledContents(True)
        self.label_61.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_61, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_5, 1, 4, 1, 3)

        self.frame_2 = QFrame(self.pc_info_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(240, 30, 121, 16))
        self.widget1 = QWidget(self.frame_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(70, 50, 401, 201))
        self.gridLayout_5 = QGridLayout(self.widget1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.widget1)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_5.addWidget(self.label_36, 5, 1, 1, 1)

        self.label_31 = QLabel(self.widget1)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_5.addWidget(self.label_31, 0, 0, 1, 1)

        self.label_25 = QLabel(self.widget1)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_5.addWidget(self.label_25, 1, 0, 1, 1)

        self.label_26 = QLabel(self.widget1)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 1, 1, 1, 1)

        self.label_35 = QLabel(self.widget1)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_5.addWidget(self.label_35, 5, 0, 1, 1)

        self.label_27 = QLabel(self.widget1)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_5.addWidget(self.label_27, 2, 0, 1, 1)

        self.label_17 = QLabel(self.widget1)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 4, 0, 1, 1)

        self.label_29 = QLabel(self.widget1)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_5.addWidget(self.label_29, 3, 0, 1, 1)

        self.label_34 = QLabel(self.widget1)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_5.addWidget(self.label_34, 4, 1, 1, 1)

        self.label_32 = QLabel(self.widget1)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_5.addWidget(self.label_32, 0, 1, 1, 1)

        self.label_28 = QLabel(self.widget1)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 2, 1, 1, 1)

        self.label_30 = QLabel(self.widget1)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_5.addWidget(self.label_30, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 0, 3, 1, 4)

        self.frame = QFrame(self.pc_info_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(150, 10, 121, 16))
        self.label_54 = QLabel(self.frame)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(70, 240, 291, 16))
        self.widget2 = QWidget(self.frame)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(70, 40, 261, 181))
        self.gridLayout_6 = QGridLayout(self.widget2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_14 = QLabel(self.widget2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 0, 1, 1, 1)

        self.label_7 = QLabel(self.widget2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_8 = QLabel(self.widget2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 1, 1, 1, 1)

        self.label_9 = QLabel(self.widget2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_10 = QLabel(self.widget2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_6.addWidget(self.label_10, 2, 1, 1, 1)

        self.label_11 = QLabel(self.widget2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_6.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_12 = QLabel(self.widget2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 3, 1, 1, 1)

        self.label_37 = QLabel(self.widget2)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_6.addWidget(self.label_37, 4, 0, 1, 1)

        self.label_38 = QLabel(self.widget2)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_6.addWidget(self.label_38, 4, 1, 1, 1)

        self.label_39 = QLabel(self.widget2)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_6.addWidget(self.label_39, 5, 0, 1, 1)

        self.label_40 = QLabel(self.widget2)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_6.addWidget(self.label_40, 5, 1, 1, 1)

        self.label_41 = QLabel(self.widget2)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_6.addWidget(self.label_41, 6, 0, 1, 1)

        self.label_51 = QLabel(self.widget2)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_6.addWidget(self.label_51, 6, 1, 1, 1)

        self.label_52 = QLabel(self.widget2)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_6.addWidget(self.label_52, 7, 0, 1, 1)

        self.label_53 = QLabel(self.widget2)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_6.addWidget(self.label_53, 7, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.pc_info_page)
        self.apps_page = QWidget()
        self.apps_page.setObjectName(u"apps_page")
        self.label_4 = QLabel(self.apps_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 110, 161, 111))
        self.stackedWidget.addWidget(self.apps_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_19.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_19.toggled.connect(self.icon_name_widget.setVisible)
        self.home_2_button.toggled.connect(self.home_1_button.setChecked)
        self.app_2_button.toggled.connect(self.app_1_button.setChecked)
        self.about_2_button.toggled.connect(self.about_1_button.setChecked)
        self.update_2_button.toggled.connect(self.update_1_button.setChecked)
        self.exit_2_button.toggled.connect(self.exit_1_button.setChecked)
        self.exit_1_button.toggled.connect(self.exit_2_button.setChecked)
        self.update_1_button.toggled.connect(self.update_2_button.setChecked)
        self.about_1_button.toggled.connect(self.about_2_button.setChecked)
        self.app_1_button.toggled.connect(self.app_2_button.setChecked)
        self.home_1_button.toggled.connect(self.home_2_button.setChecked)
        self.exit_2_button.toggled.connect(MainWindow.close)
        self.exit_1_button.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.home_1_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.app_1_button.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.about_1_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.update_1_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.exit_1_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText("")
        self.home_2_button.setText("")
        self.app_2_button.setText("")
        self.about_2_button.setText("")
        self.update_2_button.setText("")
        self.exit_2_button.setText("")
        self.pushButton_19.setText("")
#if QT_CONFIG(tooltip)
        self.cashmanage_button.setToolTip(QCoreApplication.translate("MainWindow", u"Daily Cash Management", None))
#endif // QT_CONFIG(tooltip)
        self.cashmanage_button.setText("")
#if QT_CONFIG(tooltip)
        self.about_coop_button.setToolTip(QCoreApplication.translate("MainWindow", u"About Coop", None))
#endif // QT_CONFIG(tooltip)
        self.about_coop_button.setText("")
#if QT_CONFIG(tooltip)
        self.alhuda_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop Alhuda ", None))
#endif // QT_CONFIG(tooltip)
        self.alhuda_button.setText("")
#if QT_CONFIG(tooltip)
        self.phonebook_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop PhoneBook", None))
#endif // QT_CONFIG(tooltip)
        self.phonebook_button.setText("")
#if QT_CONFIG(tooltip)
        self.coopurl_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop URLS", None))
#endif // QT_CONFIG(tooltip)
        self.coopurl_button.setText("")
#if QT_CONFIG(tooltip)
        self.michu_button.setToolTip(QCoreApplication.translate("MainWindow", u"Michu Guide", None))
#endif // QT_CONFIG(tooltip)
        self.michu_button.setText("")
#if QT_CONFIG(tooltip)
        self.coopay_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop Ebirr", None))
#endif // QT_CONFIG(tooltip)
        self.coopay_button.setText("")
#if QT_CONFIG(tooltip)
        self.conventional_button.setToolTip(QCoreApplication.translate("MainWindow", u"Conventional Products", None))
#endif // QT_CONFIG(tooltip)
        self.conventional_button.setText("")
#if QT_CONFIG(tooltip)
        self.coopapp_button.setToolTip(QCoreApplication.translate("MainWindow", u"CoopApp", None))
#endif // QT_CONFIG(tooltip)
        self.coopapp_button.setText("")
#if QT_CONFIG(tooltip)
        self.remittance_button.setToolTip(QCoreApplication.translate("MainWindow", u"Remittance Guide", None))
#endif // QT_CONFIG(tooltip)
        self.remittance_button.setText("")
#if QT_CONFIG(tooltip)
        self.atm_button.setToolTip(QCoreApplication.translate("MainWindow", u"CRM and NCR Guide", None))
#endif // QT_CONFIG(tooltip)
        self.atm_button.setText("")
#if QT_CONFIG(tooltip)
        self.pcinfo_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>PC Information</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pcinfo_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About PAGE ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"update page ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Display ", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Bit/pixel", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"2k", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Vendor ", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"30bit/pixel", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Adapte Type", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Intel Iris Graphics ", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"SAMSUNG", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Storage ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Used", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"300GB", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Vendor ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"500GB", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"221GB", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"SAMSUNG", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Task Manager ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add Printers", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Performance (Usage %)", None))
        self.label_66.setText("")
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"6.7/8 GB (90%)", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"0.04%", None))
        self.label_62.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"3.1gHz (3.2%)", None))
        self.label_61.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"System Info", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Professional", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Processor :", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"System Type :", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"64-bit operating system, x64-based processor", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Edition:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Installed RAM : ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CPU cores:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Platform :", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"8 Cores (Logical Processors)", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"11th Gen Intel(R) Core(TM) i5-11320H @ 3.20GHz   3.19 GHz", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"8GB", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Windows 11, Version 23H2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ethernet IP info", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Seems you PC is not connected to Wired LAN!", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Adapter:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Ethernet 3", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"IP Address:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"10.1.15.7", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Subnet mask:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"255.255.255.0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Default Gateway :", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"10.1.15.1", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Default DNS:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"10.1.70.10", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Alternative DNS:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"4.4.2.2", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"MAC  Address", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"W3HR5YR5RY6FC4B4", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"100Mbps", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apps Page", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coopDesk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1172, 735)
        MainWindow.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        MainWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_name_widget.sizePolicy().hasHeightForWidth())
        self.icon_name_widget.setSizePolicy(sizePolicy)
        self.icon_name_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"border-top-left-radius:10px;\n"
"\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(48, 48))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 146, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 1, -1)
        self.home_1_button = QPushButton(self.icon_name_widget)
        self.home_1_button.setObjectName(u"home_1_button")
        font1 = QFont()
        font1.setFamilies([u"Roboto Medium"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.home_1_button.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/images/home_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/home_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_1_button.setIcon(icon)
        self.home_1_button.setIconSize(QSize(32, 32))
        self.home_1_button.setCheckable(True)
        self.home_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1_button)

        self.app_1_button = QPushButton(self.icon_name_widget)
        self.app_1_button.setObjectName(u"app_1_button")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.app_1_button.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/images/apps_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/apps_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.app_1_button.setIcon(icon1)
        self.app_1_button.setIconSize(QSize(32, 32))
        self.app_1_button.setCheckable(True)
        self.app_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.app_1_button)

        self.about_1_button = QPushButton(self.icon_name_widget)
        self.about_1_button.setObjectName(u"about_1_button")
        self.about_1_button.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/images/about_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/images/about_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.about_1_button.setIcon(icon2)
        self.about_1_button.setIconSize(QSize(32, 32))
        self.about_1_button.setCheckable(True)
        self.about_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.about_1_button)

        self.update_1_button = QPushButton(self.icon_name_widget)
        self.update_1_button.setObjectName(u"update_1_button")
        self.update_1_button.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/images/update_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/images/update_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.update_1_button.setIcon(icon3)
        self.update_1_button.setIconSize(QSize(32, 32))
        self.update_1_button.setCheckable(True)
        self.update_1_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_1_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exit_1_button = QPushButton(self.icon_name_widget)
        self.exit_1_button.setObjectName(u"exit_1_button")
        self.exit_1_button.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(u":/images/logout_icon_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/images/logout_icon_blue.svg", QSize(), QIcon.Normal, QIcon.On)
        self.exit_1_button.setIcon(icon4)
        self.exit_1_button.setIconSize(QSize(32, 32))
        self.exit_1_button.setCheckable(True)
        self.exit_1_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.exit_1_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_only_widget.setSizePolicy(sizePolicy1)
        self.icon_only_widget.setStyleSheet(u"QWidget{background-color: rgb(8, 176, 240);}\n"
"QPushButton {\n"
"\n"
" color: white;\n"
"text-align:left;\n"
"height:40px;\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align: center;\n"
"border-radius:10px;\n"
"text-alignment:center\n"
"\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u":/images/logo_white.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_2_button = QPushButton(self.icon_only_widget)
        self.home_2_button.setObjectName(u"home_2_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_2_button.sizePolicy().hasHeightForWidth())
        self.home_2_button.setSizePolicy(sizePolicy2)
        self.home_2_button.setIcon(icon)
        self.home_2_button.setIconSize(QSize(32, 32))
        self.home_2_button.setCheckable(True)
        self.home_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2_button)

        self.app_2_button = QPushButton(self.icon_only_widget)
        self.app_2_button.setObjectName(u"app_2_button")
        self.app_2_button.setIcon(icon1)
        self.app_2_button.setIconSize(QSize(32, 32))
        self.app_2_button.setCheckable(True)
        self.app_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.app_2_button)

        self.about_2_button = QPushButton(self.icon_only_widget)
        self.about_2_button.setObjectName(u"about_2_button")
        self.about_2_button.setIcon(icon2)
        self.about_2_button.setIconSize(QSize(32, 32))
        self.about_2_button.setCheckable(True)
        self.about_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.about_2_button)

        self.update_2_button = QPushButton(self.icon_only_widget)
        self.update_2_button.setObjectName(u"update_2_button")
        self.update_2_button.setIcon(icon3)
        self.update_2_button.setIconSize(QSize(32, 32))
        self.update_2_button.setCheckable(True)
        self.update_2_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_2_button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_2_button = QPushButton(self.icon_only_widget)
        self.exit_2_button.setObjectName(u"exit_2_button")
        self.exit_2_button.setIcon(icon4)
        self.exit_2_button.setIconSize(QSize(32, 32))
        self.exit_2_button.setCheckable(True)
        self.exit_2_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.exit_2_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(15)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy3)
        self.main_menu.setStyleSheet(u"QToolTip {\n"
"    background:white;\n"
"    color: #00AEEF; \n"
"    border: 3px solid #00AEEF;\n"
"    font-size: 16pt;\n"
"    font-family: Arial;\n"
"    padding: 5px;\n"
"    border-radius:3px\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_19 = QPushButton(self.main_menu)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/images/menu_icon_blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/images/menu_icon_blue_inverted.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_19.setIcon(icon5)
        self.pushButton_19.setIconSize(QSize(24, 24))
        self.pushButton_19.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_19)

        self.horizontalSpacer = QSpacerItem(668, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"QPushButton{\n"
"  background:none;\n"
"  border: none;\n"
"\n"
"\n"
"}")
        self.gridLayout_2 = QGridLayout(self.home_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.cashmanage_button = QPushButton(self.home_page)
        self.cashmanage_button.setObjectName(u"cashmanage_button")
        icon6 = QIcon()
        icon6.addFile(u":/homeicons/teller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cashmanage_button.setIcon(icon6)
        self.cashmanage_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.cashmanage_button, 3, 1, 1, 1)

        self.about_coop_button = QPushButton(self.home_page)
        self.about_coop_button.setObjectName(u"about_coop_button")
        icon7 = QIcon()
        icon7.addFile(u":/homeicons/about_coop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.about_coop_button.setIcon(icon7)
        self.about_coop_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.about_coop_button, 3, 2, 1, 1)

        self.alhuda_button = QPushButton(self.home_page)
        self.alhuda_button.setObjectName(u"alhuda_button")
        icon8 = QIcon()
        icon8.addFile(u":/homeicons/alhuda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.alhuda_button.setIcon(icon8)
        self.alhuda_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.alhuda_button, 2, 1, 1, 1)

        self.phonebook_button = QPushButton(self.home_page)
        self.phonebook_button.setObjectName(u"phonebook_button")
        icon9 = QIcon()
        icon9.addFile(u":/homeicons/phonebook.png", QSize(), QIcon.Normal, QIcon.Off)
        self.phonebook_button.setIcon(icon9)
        self.phonebook_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.phonebook_button, 1, 2, 1, 1)

        self.coopurl_button = QPushButton(self.home_page)
        self.coopurl_button.setObjectName(u"coopurl_button")
        icon10 = QIcon()
        icon10.addFile(u":/homeicons/coopurl.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coopurl_button.setIcon(icon10)
        self.coopurl_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.coopurl_button, 0, 1, 1, 1)

        self.michu_button = QPushButton(self.home_page)
        self.michu_button.setObjectName(u"michu_button")
        icon11 = QIcon()
        icon11.addFile(u":/homeicons/michu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.michu_button.setIcon(icon11)
        self.michu_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.michu_button, 0, 2, 1, 1)

        self.coopay_button = QPushButton(self.home_page)
        self.coopay_button.setObjectName(u"coopay_button")
        icon12 = QIcon()
        icon12.addFile(u":/homeicons/coopay.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coopay_button.setIcon(icon12)
        self.coopay_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.coopay_button, 2, 2, 1, 1)

        self.conventional_button = QPushButton(self.home_page)
        self.conventional_button.setObjectName(u"conventional_button")
        icon13 = QIcon()
        icon13.addFile(u":/homeicons/conventinal_products.png", QSize(), QIcon.Normal, QIcon.Off)
        self.conventional_button.setIcon(icon13)
        self.conventional_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.conventional_button, 2, 0, 1, 1)

        self.coopapp_button = QPushButton(self.home_page)
        self.coopapp_button.setObjectName(u"coopapp_button")
        icon14 = QIcon()
        icon14.addFile(u":/homeicons/coopapp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coopapp_button.setIcon(icon14)
        self.coopapp_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.coopapp_button, 3, 0, 1, 1)

        self.remittance_button = QPushButton(self.home_page)
        self.remittance_button.setObjectName(u"remittance_button")
        icon15 = QIcon()
        icon15.addFile(u":/homeicons/remittance.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remittance_button.setIcon(icon15)
        self.remittance_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.remittance_button, 1, 0, 1, 1)

        self.atm_button = QPushButton(self.home_page)
        self.atm_button.setObjectName(u"atm_button")
        icon16 = QIcon()
        icon16.addFile(u":/homeicons/atm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.atm_button.setIcon(icon16)
        self.atm_button.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.atm_button, 1, 1, 1, 1)

        self.pcinfo_button = QPushButton(self.home_page)
        self.pcinfo_button.setObjectName(u"pcinfo_button")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(14)
        self.pcinfo_button.setFont(font3)
        self.pcinfo_button.setToolTipDuration(-4)
        self.pcinfo_button.setStyleSheet(u"")
        icon17 = QIcon()
        icon17.addFile(u":/homeicons/pcinfo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pcinfo_button.setIcon(icon17)
        self.pcinfo_button.setIconSize(QSize(128, 128))
        self.pcinfo_button.setCheckable(True)

        self.gridLayout_2.addWidget(self.pcinfo_button, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.label_3 = QLabel(self.about_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 65, 301, 111))
        self.stackedWidget.addWidget(self.about_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.label_6 = QLabel(self.update_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 170, 221, 101))
        self.stackedWidget.addWidget(self.update_page)
        self.pc_info_page = QWidget()
        self.pc_info_page.setObjectName(u"pc_info_page")
        self.gridLayout_3 = QGridLayout(self.pc_info_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton = QPushButton(self.pc_info_page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(8, 176, 240);\n"
"border:none;\n"
"color:white ;\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(252, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 2, 1, 1, 2)

        self.display = QFrame(self.pc_info_page)
        self.display.setObjectName(u"display")
        self.display.setFrameShape(QFrame.Shape.StyledPanel)
        self.display.setFrameShadow(QFrame.Shadow.Raised)
        self.label_42 = QLabel(self.display)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(80, 10, 121, 16))
        self.label_43 = QLabel(self.display)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(30, 60, 61, 16))
        self.label_44 = QLabel(self.display)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(40, 80, 61, 16))
        self.label_45 = QLabel(self.display)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(130, 60, 81, 20))
        self.label_46 = QLabel(self.display)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(40, 100, 41, 16))
        self.label_47 = QLabel(self.display)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(130, 80, 91, 16))
        self.label_48 = QLabel(self.display)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(30, 40, 101, 16))
        self.label_49 = QLabel(self.display)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(130, 40, 91, 16))
        self.label_50 = QLabel(self.display)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(130, 100, 91, 16))

        self.gridLayout_3.addWidget(self.display, 1, 2, 1, 2)

        self.frame_3 = QFrame(self.pc_info_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(80, 10, 121, 16))
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(40, 70, 61, 16))
        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(40, 90, 61, 16))
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(110, 70, 81, 20))
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(40, 110, 41, 16))
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(110, 90, 91, 16))
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(40, 50, 61, 16))
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(110, 50, 91, 16))
        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(110, 110, 91, 16))

        self.gridLayout_3.addWidget(self.frame_3, 1, 0, 1, 2)

        self.pushButton_3 = QPushButton(self.pc_info_page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"\n"
"border:none\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_3, 2, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.pc_info_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"\n"
"border:none\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_2, 2, 6, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(252, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 2, 4, 1, 2)

        self.pefromance = QFrame(self.pc_info_page)
        self.pefromance.setObjectName(u"pefromance")
        self.pefromance.setFrameShape(QFrame.Shape.StyledPanel)
        self.pefromance.setFrameShadow(QFrame.Shadow.Raised)
        self.pefromance.setLineWidth(2)
        self.label_60 = QLabel(self.pefromance)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(140, 30, 151, 16))
        self.widget = QWidget(self.pefromance)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(53, 51, 281, 221))
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self.widget)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(32, 32))
        self.label_66.setMaximumSize(QSize(64, 64))
        self.label_66.setPixmap(QPixmap(u":/perfomance_icons/cpu_icon.png"))
        self.label_66.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_66, 0, 0, 1, 1)

        self.label_63 = QLabel(self.widget)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_63, 1, 1, 1, 1)

        self.frame_6 = QFrame(self.widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(24, 24))
        self.frame_6.setMaximumSize(QSize(24, 24))
        self.frame_6.setStyleSheet(u"background-color:rgb(255, 85, 0)")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_4.addWidget(self.frame_6, 0, 2, 1, 1)

        self.label_65 = QLabel(self.widget)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_65, 2, 1, 1, 1)

        self.label_62 = QLabel(self.widget)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(32, 32))
        self.label_62.setMaximumSize(QSize(64, 64))
        self.label_62.setPixmap(QPixmap(u":/perfomance_icons/ssd_cion.png"))
        self.label_62.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_62, 2, 0, 1, 1)

        self.label_67 = QLabel(self.widget)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_67, 0, 1, 1, 1)

        self.frame_8 = QFrame(self.widget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(24, 24))
        self.frame_8.setMaximumSize(QSize(24, 24))
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_4.addWidget(self.frame_8, 2, 2, 1, 1)

        self.frame_7 = QFrame(self.widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(24, 24))
        self.frame_7.setMaximumSize(QSize(24, 24))
        self.frame_7.setStyleSheet(u"background-color:rgb(0, 255, 0)")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_4.addWidget(self.frame_7, 1, 2, 1, 1)

        self.label_61 = QLabel(self.widget)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(32, 32))
        self.label_61.setMaximumSize(QSize(64, 64))
        self.label_61.setPixmap(QPixmap(u":/perfomance_icons/ram_icon.png"))
        self.label_61.setScaledContents(True)
        self.label_61.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_61, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.pefromance, 1, 4, 1, 3)

        self.frame_2 = QFrame(self.pc_info_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(240, 30, 121, 16))
        self.widget1 = QWidget(self.frame_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(70, 50, 401, 201))
        self.gridLayout_5 = QGridLayout(self.widget1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.widget1)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_5.addWidget(self.label_36, 5, 1, 1, 1)

        self.label_31 = QLabel(self.widget1)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_5.addWidget(self.label_31, 0, 0, 1, 1)

        self.label_25 = QLabel(self.widget1)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_5.addWidget(self.label_25, 1, 0, 1, 1)

        self.label_26 = QLabel(self.widget1)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 1, 1, 1, 1)

        self.label_35 = QLabel(self.widget1)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_5.addWidget(self.label_35, 5, 0, 1, 1)

        self.label_27 = QLabel(self.widget1)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_5.addWidget(self.label_27, 2, 0, 1, 1)

        self.label_17 = QLabel(self.widget1)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 4, 0, 1, 1)

        self.label_29 = QLabel(self.widget1)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_5.addWidget(self.label_29, 3, 0, 1, 1)

        self.label_34 = QLabel(self.widget1)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_5.addWidget(self.label_34, 4, 1, 1, 1)

        self.label_32 = QLabel(self.widget1)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_5.addWidget(self.label_32, 0, 1, 1, 1)

        self.label_28 = QLabel(self.widget1)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 2, 1, 1, 1)

        self.label_30 = QLabel(self.widget1)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_5.addWidget(self.label_30, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 0, 3, 1, 4)

        self.frame = QFrame(self.pc_info_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(150, 10, 121, 16))
        self.label_54 = QLabel(self.frame)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(70, 240, 291, 16))
        self.widget2 = QWidget(self.frame)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(70, 40, 261, 181))
        self.gridLayout_6 = QGridLayout(self.widget2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_14 = QLabel(self.widget2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 0, 1, 1, 1)

        self.label_7 = QLabel(self.widget2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_8 = QLabel(self.widget2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 1, 1, 1, 1)

        self.label_9 = QLabel(self.widget2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_10 = QLabel(self.widget2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_6.addWidget(self.label_10, 2, 1, 1, 1)

        self.label_11 = QLabel(self.widget2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_6.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_12 = QLabel(self.widget2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 3, 1, 1, 1)

        self.label_37 = QLabel(self.widget2)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_6.addWidget(self.label_37, 4, 0, 1, 1)

        self.label_38 = QLabel(self.widget2)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_6.addWidget(self.label_38, 4, 1, 1, 1)

        self.label_39 = QLabel(self.widget2)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_6.addWidget(self.label_39, 5, 0, 1, 1)

        self.label_40 = QLabel(self.widget2)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_6.addWidget(self.label_40, 5, 1, 1, 1)

        self.label_41 = QLabel(self.widget2)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_6.addWidget(self.label_41, 6, 0, 1, 1)

        self.label_51 = QLabel(self.widget2)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_6.addWidget(self.label_51, 6, 1, 1, 1)

        self.label_52 = QLabel(self.widget2)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_6.addWidget(self.label_52, 7, 0, 1, 1)

        self.label_53 = QLabel(self.widget2)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_6.addWidget(self.label_53, 7, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.pc_info_page)
        self.apps_page = QWidget()
        self.apps_page.setObjectName(u"apps_page")
        self.label_4 = QLabel(self.apps_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 110, 161, 111))
        self.stackedWidget.addWidget(self.apps_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_19.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_19.toggled.connect(self.icon_name_widget.setVisible)
        self.home_2_button.toggled.connect(self.home_1_button.setChecked)
        self.app_2_button.toggled.connect(self.app_1_button.setChecked)
        self.about_2_button.toggled.connect(self.about_1_button.setChecked)
        self.update_2_button.toggled.connect(self.update_1_button.setChecked)
        self.exit_2_button.toggled.connect(self.exit_1_button.setChecked)
        self.exit_1_button.toggled.connect(self.exit_2_button.setChecked)
        self.update_1_button.toggled.connect(self.update_2_button.setChecked)
        self.about_1_button.toggled.connect(self.about_2_button.setChecked)
        self.app_1_button.toggled.connect(self.app_2_button.setChecked)
        self.home_1_button.toggled.connect(self.home_2_button.setChecked)
        self.exit_2_button.toggled.connect(MainWindow.close)
        self.exit_1_button.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.home_1_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.app_1_button.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.about_1_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.update_1_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.exit_1_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText("")
        self.home_2_button.setText("")
        self.app_2_button.setText("")
        self.about_2_button.setText("")
        self.update_2_button.setText("")
        self.exit_2_button.setText("")
        self.pushButton_19.setText("")
#if QT_CONFIG(tooltip)
        self.cashmanage_button.setToolTip(QCoreApplication.translate("MainWindow", u"Daily Cash Management", None))
#endif // QT_CONFIG(tooltip)
        self.cashmanage_button.setText("")
#if QT_CONFIG(tooltip)
        self.about_coop_button.setToolTip(QCoreApplication.translate("MainWindow", u"About Coop", None))
#endif // QT_CONFIG(tooltip)
        self.about_coop_button.setText("")
#if QT_CONFIG(tooltip)
        self.alhuda_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop Alhuda ", None))
#endif // QT_CONFIG(tooltip)
        self.alhuda_button.setText("")
#if QT_CONFIG(tooltip)
        self.phonebook_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop PhoneBook", None))
#endif // QT_CONFIG(tooltip)
        self.phonebook_button.setText("")
#if QT_CONFIG(tooltip)
        self.coopurl_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop URLS", None))
#endif // QT_CONFIG(tooltip)
        self.coopurl_button.setText("")
#if QT_CONFIG(tooltip)
        self.michu_button.setToolTip(QCoreApplication.translate("MainWindow", u"Michu Guide", None))
#endif // QT_CONFIG(tooltip)
        self.michu_button.setText("")
#if QT_CONFIG(tooltip)
        self.coopay_button.setToolTip(QCoreApplication.translate("MainWindow", u"Coop Ebirr", None))
#endif // QT_CONFIG(tooltip)
        self.coopay_button.setText("")
#if QT_CONFIG(tooltip)
        self.conventional_button.setToolTip(QCoreApplication.translate("MainWindow", u"Conventional Products", None))
#endif // QT_CONFIG(tooltip)
        self.conventional_button.setText("")
#if QT_CONFIG(tooltip)
        self.coopapp_button.setToolTip(QCoreApplication.translate("MainWindow", u"CoopApp", None))
#endif // QT_CONFIG(tooltip)
        self.coopapp_button.setText("")
#if QT_CONFIG(tooltip)
        self.remittance_button.setToolTip(QCoreApplication.translate("MainWindow", u"Remittance Guide", None))
#endif // QT_CONFIG(tooltip)
        self.remittance_button.setText("")
#if QT_CONFIG(tooltip)
        self.atm_button.setToolTip(QCoreApplication.translate("MainWindow", u"CRM and NCR Guide", None))
#endif // QT_CONFIG(tooltip)
        self.atm_button.setText("")
#if QT_CONFIG(tooltip)
        self.pcinfo_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>PC Information</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pcinfo_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About PAGE ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"update page ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Display ", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Bit/pixel", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"2k", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Vendor ", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"30bit/pixel", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Adapte Type", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Intel Iris Graphics ", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"SAMSUNG", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Storage ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Used", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"300GB", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Vendor ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"500GB", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"221GB", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"SAMSUNG", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Task Manager ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add Printers", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Performance (Usage %)", None))
        self.label_66.setText("")
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"6.7/8 GB (90%)", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"0.04%", None))
        self.label_62.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"3.1gHz (3.2%)", None))
        self.label_61.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"System Info", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Professional", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Processor :", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"System Type :", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"64-bit operating system, x64-based processor", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Edition:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Installed RAM : ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CPU cores:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Platform :", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"8 Cores (Logical Processors)", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"11th Gen Intel(R) Core(TM) i5-11320H @ 3.20GHz   3.19 GHz", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"8GB", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Windows 11, Version 23H2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ethernet IP info", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Seems you PC is not connected to Wired LAN!", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Adapter:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Ethernet 3", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"IP Address:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"10.1.15.7", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Subnet mask:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"255.255.255.0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Default Gateway :", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"10.1.15.1", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Default DNS:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"10.1.70.10", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Alternative DNS:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"4.4.2.2", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"MAC  Address", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"W3HR5YR5RY6FC4B4", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"100Mbps", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apps Page", None))
    # retranslateUi

