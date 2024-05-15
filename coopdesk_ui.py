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

