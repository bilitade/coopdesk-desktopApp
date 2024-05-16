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

