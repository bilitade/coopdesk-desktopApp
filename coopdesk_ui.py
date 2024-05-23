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
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1281, 816)
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
        self.michu_page = QWidget()
        self.michu_page.setObjectName(u"michu_page")
        self.verticalLayout_6 = QVBoxLayout(self.michu_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.michu_page)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.michu_slider = QStackedWidget(self.frame)
        self.michu_slider.setObjectName(u"michu_slider")
        self.michu_slider.setStyleSheet(u"QStackedWidget {\n"
"                border: 1px solid #dee2e6;\n"
"                background-color: white;\n"
"            }")
        self.container_1 = QWidget()
        self.container_1.setObjectName(u"container_1")
        self.gridLayout_9 = QGridLayout(self.container_1)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.michu_slide_1 = QLabel(self.container_1)
        self.michu_slide_1.setObjectName(u"michu_slide_1")
        self.michu_slide_1.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide1.PNG"))
        self.michu_slide_1.setScaledContents(True)

        self.gridLayout_9.addWidget(self.michu_slide_1, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_1)
        self.container_8 = QWidget()
        self.container_8.setObjectName(u"container_8")
        self.gridLayout_19 = QGridLayout(self.container_8)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_14 = QLabel(self.container_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide8.PNG"))
        self.label_14.setScaledContents(True)

        self.gridLayout_19.addWidget(self.label_14, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_8)
        self.container_9 = QWidget()
        self.container_9.setObjectName(u"container_9")
        self.gridLayout_17 = QGridLayout(self.container_9)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_17 = QLabel(self.container_9)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide9.PNG"))
        self.label_17.setScaledContents(True)

        self.gridLayout_17.addWidget(self.label_17, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_9)
        self.container_10 = QWidget()
        self.container_10.setObjectName(u"container_10")
        self.gridLayout_18 = QGridLayout(self.container_10)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_19 = QLabel(self.container_10)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide10.PNG"))
        self.label_19.setScaledContents(True)

        self.gridLayout_18.addWidget(self.label_19, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_10)
        self.container_11 = QWidget()
        self.container_11.setObjectName(u"container_11")
        self.gridLayout_20 = QGridLayout(self.container_11)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_26 = QLabel(self.container_11)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide11.PNG"))
        self.label_26.setScaledContents(True)

        self.gridLayout_20.addWidget(self.label_26, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_11)
        self.container_2 = QWidget()
        self.container_2.setObjectName(u"container_2")
        self.gridLayout_10 = QGridLayout(self.container_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_3 = QLabel(self.container_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide2.PNG"))
        self.label_3.setScaledContents(True)

        self.gridLayout_10.addWidget(self.label_3, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_2)
        self.container_3 = QWidget()
        self.container_3.setObjectName(u"container_3")
        self.gridLayout_12 = QGridLayout(self.container_3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_4 = QLabel(self.container_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide3.PNG"))
        self.label_4.setScaledContents(True)

        self.gridLayout_12.addWidget(self.label_4, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_3)
        self.container_4 = QWidget()
        self.container_4.setObjectName(u"container_4")
        self.gridLayout_13 = QGridLayout(self.container_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_6 = QLabel(self.container_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide4.PNG"))
        self.label_6.setScaledContents(True)

        self.gridLayout_13.addWidget(self.label_6, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_4)
        self.container_5 = QWidget()
        self.container_5.setObjectName(u"container_5")
        self.gridLayout_14 = QGridLayout(self.container_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_8 = QLabel(self.container_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide5.PNG"))
        self.label_8.setScaledContents(True)

        self.gridLayout_14.addWidget(self.label_8, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_5)
        self.container_6 = QWidget()
        self.container_6.setObjectName(u"container_6")
        self.gridLayout_15 = QGridLayout(self.container_6)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_10 = QLabel(self.container_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide6.PNG"))
        self.label_10.setScaledContents(True)

        self.gridLayout_15.addWidget(self.label_10, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_6)
        self.container_7 = QWidget()
        self.container_7.setObjectName(u"container_7")
        self.gridLayout_16 = QGridLayout(self.container_7)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_12 = QLabel(self.container_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide7.PNG"))
        self.label_12.setScaledContents(True)

        self.gridLayout_16.addWidget(self.label_12, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_7)

        self.gridLayout_7.addWidget(self.michu_slider, 0, 0, 1, 2)

        self.michu_Previous = QPushButton(self.frame)
        self.michu_Previous.setObjectName(u"michu_Previous")
        self.michu_Previous.setStyleSheet(u"QPushButton {\n"
"                background-color: #08B0F0;  /* Bootstrap primary color */\n"
"                color: white;\n"
"                border: none;\n"
"                padding: 5px 5px;\n"
"                font-size: 14px;\n"
"                line-height: 1px;\n"
"                border-radius: 5px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0b5ed7;  /* Bootstrap primary color on hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0a58ca;  /* Bootstrap primary color on active */\n"
"            }")

        self.gridLayout_7.addWidget(self.michu_Previous, 1, 0, 1, 1)

        self.michu_Next = QPushButton(self.frame)
        self.michu_Next.setObjectName(u"michu_Next")
        self.michu_Next.setStyleSheet(u"QPushButton {\n"
"                background-color: #08B0F0;  /* Bootstrap primary color */\n"
"                color: white;\n"
"                border: none;\n"
"                padding: 5px 5px;\n"
"                font-size: 14px;\n"
"                line-height: 1px;\n"
"                border-radius: 5px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0b5ed7;  /* Bootstrap primary color on hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0a58ca;  /* Bootstrap primary color on active */\n"
"            }")

        self.gridLayout_7.addWidget(self.michu_Next, 1, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.frame)

        self.stackedWidget.addWidget(self.michu_page)
        self.pc_info_page = QWidget()
        self.pc_info_page.setObjectName(u"pc_info_page")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.pc_info_page.setFont(font4)
        self.pc_info_page.setStyleSheet(u"QWidget{color: #000000;\n"
"text-size: 13px bold;}\n"
"\n"
"QFrame {\n"
"    background-color: white; /* Card background color */\n"
"    border: 1px solid #ddd; /* Border similar to Bootstrap */\n"
"    border-radius: 5px; /* Rounded corners */\n"
" \n"
"}\n"
"QLabel {\n"
"    qproperty-alignment: 'AlignHCenter | AlignVCenter';\n"
" font-size: 12px;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.pc_info_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.addprinter_button = QPushButton(self.pc_info_page)
        self.addprinter_button.setObjectName(u"addprinter_button")
        self.addprinter_button.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: #00AEEF; /* Bootstrap's primary blue color */\n"
"\n"
"    border-radius: 5px;\n"
"    padding: 8px 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; /* Darker blue on hover */\n"
"    border-color: #0056b3; /* Darker blue border on hover */\n"
"}")
        icon18 = QIcon(QIcon.fromTheme(u"printer"))
        self.addprinter_button.setIcon(icon18)

        self.gridLayout_3.addWidget(self.addprinter_button, 2, 4, 1, 1)

        self.network_layout = QFrame(self.pc_info_page)
        self.network_layout.setObjectName(u"network_layout")
        self.network_layout.setStyleSheet(u"")
        self.network_layout.setFrameShape(QFrame.Shape.StyledPanel)
        self.network_layout.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.network_layout)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(15)
        self.gridLayout_4.setVerticalSpacing(1)
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.ethernet_layout = QGridLayout()
        self.ethernet_layout.setObjectName(u"ethernet_layout")
        self.ethernet_layout.setHorizontalSpacing(8)
        self.ethernet_layout.setContentsMargins(10, 10, 10, 10)
        self.label_91 = QLabel(self.network_layout)
        self.label_91.setObjectName(u"label_91")

        self.ethernet_layout.addWidget(self.label_91, 8, 0, 1, 1)

        self.label_81 = QLabel(self.network_layout)
        self.label_81.setObjectName(u"label_81")

        self.ethernet_layout.addWidget(self.label_81, 3, 0, 1, 1)

        self.ethernet_alternative_DNS_label = QLabel(self.network_layout)
        self.ethernet_alternative_DNS_label.setObjectName(u"ethernet_alternative_DNS_label")

        self.ethernet_layout.addWidget(self.ethernet_alternative_DNS_label, 6, 1, 1, 1)

        self.label_79 = QLabel(self.network_layout)
        self.label_79.setObjectName(u"label_79")

        self.ethernet_layout.addWidget(self.label_79, 2, 0, 1, 1)

        self.ethernet_mac_label = QLabel(self.network_layout)
        self.ethernet_mac_label.setObjectName(u"ethernet_mac_label")

        self.ethernet_layout.addWidget(self.ethernet_mac_label, 7, 1, 1, 1)

        self.label_83 = QLabel(self.network_layout)
        self.label_83.setObjectName(u"label_83")

        self.ethernet_layout.addWidget(self.label_83, 4, 0, 1, 1)

        self.ethernet_Deafult_DNS = QLabel(self.network_layout)
        self.ethernet_Deafult_DNS.setObjectName(u"ethernet_Deafult_DNS")

        self.ethernet_layout.addWidget(self.ethernet_Deafult_DNS, 5, 1, 1, 1)

        self.ethernet_speed_label = QLabel(self.network_layout)
        self.ethernet_speed_label.setObjectName(u"ethernet_speed_label")

        self.ethernet_layout.addWidget(self.ethernet_speed_label, 8, 1, 1, 1)

        self.label_77 = QLabel(self.network_layout)
        self.label_77.setObjectName(u"label_77")

        self.ethernet_layout.addWidget(self.label_77, 1, 0, 1, 1)

        self.ethernet_status = QLabel(self.network_layout)
        self.ethernet_status.setObjectName(u"ethernet_status")

        self.ethernet_layout.addWidget(self.ethernet_status, 9, 1, 1, 1)

        self.label_87 = QLabel(self.network_layout)
        self.label_87.setObjectName(u"label_87")

        self.ethernet_layout.addWidget(self.label_87, 6, 0, 1, 1)

        self.ethernet_defaultGateway_label = QLabel(self.network_layout)
        self.ethernet_defaultGateway_label.setObjectName(u"ethernet_defaultGateway_label")

        self.ethernet_layout.addWidget(self.ethernet_defaultGateway_label, 4, 1, 1, 1)

        self.ethernet_adapter_label = QLabel(self.network_layout)
        self.ethernet_adapter_label.setObjectName(u"ethernet_adapter_label")

        self.ethernet_layout.addWidget(self.ethernet_adapter_label, 1, 1, 1, 1)

        self.ethernet_subnet_label = QLabel(self.network_layout)
        self.ethernet_subnet_label.setObjectName(u"ethernet_subnet_label")

        self.ethernet_layout.addWidget(self.ethernet_subnet_label, 3, 1, 1, 1)

        self.ethernet_ip_label = QLabel(self.network_layout)
        self.ethernet_ip_label.setObjectName(u"ethernet_ip_label")

        self.ethernet_layout.addWidget(self.ethernet_ip_label, 2, 1, 1, 1)

        self.label_5 = QLabel(self.network_layout)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 20))
        self.label_5.setMaximumSize(QSize(16777215, 20))
        font5 = QFont()
        font5.setBold(True)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(2, 193, 254);")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ethernet_layout.addWidget(self.label_5, 0, 0, 1, 2)

        self.label_102 = QLabel(self.network_layout)
        self.label_102.setObjectName(u"label_102")

        self.ethernet_layout.addWidget(self.label_102, 9, 0, 1, 1)

        self.label_85 = QLabel(self.network_layout)
        self.label_85.setObjectName(u"label_85")

        self.ethernet_layout.addWidget(self.label_85, 5, 0, 1, 1)

        self.label_89 = QLabel(self.network_layout)
        self.label_89.setObjectName(u"label_89")

        self.ethernet_layout.addWidget(self.label_89, 7, 0, 1, 1)


        self.gridLayout_4.addLayout(self.ethernet_layout, 0, 1, 1, 1)

        self.wifi_layout = QGridLayout()
        self.wifi_layout.setObjectName(u"wifi_layout")
        self.wifi_layout.setHorizontalSpacing(8)
        self.wifi_layout.setVerticalSpacing(6)
        self.wifi_layout.setContentsMargins(10, 10, 10, 10)
        self.wifi_ip_label = QLabel(self.network_layout)
        self.wifi_ip_label.setObjectName(u"wifi_ip_label")

        self.wifi_layout.addWidget(self.wifi_ip_label, 2, 1, 1, 1)

        self.label_52 = QLabel(self.network_layout)
        self.label_52.setObjectName(u"label_52")

        self.wifi_layout.addWidget(self.label_52, 8, 0, 1, 1)

        self.label_9 = QLabel(self.network_layout)
        self.label_9.setObjectName(u"label_9")

        self.wifi_layout.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_7 = QLabel(self.network_layout)
        self.label_7.setObjectName(u"label_7")

        self.wifi_layout.addWidget(self.label_7, 2, 0, 1, 1)

        self.wifi_default_dns_label = QLabel(self.network_layout)
        self.wifi_default_dns_label.setObjectName(u"wifi_default_dns_label")

        self.wifi_layout.addWidget(self.wifi_default_dns_label, 5, 1, 1, 1)

        self.label_13 = QLabel(self.network_layout)
        self.label_13.setObjectName(u"label_13")

        self.wifi_layout.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_41 = QLabel(self.network_layout)
        self.label_41.setObjectName(u"label_41")

        self.wifi_layout.addWidget(self.label_41, 7, 0, 1, 1)

        self.wifi_speed_label = QLabel(self.network_layout)
        self.wifi_speed_label.setObjectName(u"wifi_speed_label")

        self.wifi_layout.addWidget(self.wifi_speed_label, 8, 1, 1, 1)

        self.wifi_subnet_label = QLabel(self.network_layout)
        self.wifi_subnet_label.setObjectName(u"wifi_subnet_label")

        self.wifi_layout.addWidget(self.wifi_subnet_label, 3, 1, 1, 1)

        self.label_11 = QLabel(self.network_layout)
        self.label_11.setObjectName(u"label_11")

        self.wifi_layout.addWidget(self.label_11, 4, 0, 1, 1)

        self.wifi_adapter_label = QLabel(self.network_layout)
        self.wifi_adapter_label.setObjectName(u"wifi_adapter_label")

        self.wifi_layout.addWidget(self.wifi_adapter_label, 1, 1, 1, 1)

        self.wifi_MAC_label = QLabel(self.network_layout)
        self.wifi_MAC_label.setObjectName(u"wifi_MAC_label")

        self.wifi_layout.addWidget(self.wifi_MAC_label, 7, 1, 1, 1)

        self.wifi_defaultGate_label = QLabel(self.network_layout)
        self.wifi_defaultGate_label.setObjectName(u"wifi_defaultGate_label")

        self.wifi_layout.addWidget(self.wifi_defaultGate_label, 4, 1, 1, 1)

        self.label_93 = QLabel(self.network_layout)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMinimumSize(QSize(0, 20))
        self.label_93.setMaximumSize(QSize(16777215, 20))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(True)
        self.label_93.setFont(font6)
        self.label_93.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(2, 193, 254);")
        self.label_93.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.wifi_layout.addWidget(self.label_93, 0, 0, 1, 2)

        self.wifi_alternat_DNS_label = QLabel(self.network_layout)
        self.wifi_alternat_DNS_label.setObjectName(u"wifi_alternat_DNS_label")

        self.wifi_layout.addWidget(self.wifi_alternat_DNS_label, 6, 1, 1, 1)

        self.label_37 = QLabel(self.network_layout)
        self.label_37.setObjectName(u"label_37")

        self.wifi_layout.addWidget(self.label_37, 5, 0, 1, 1)

        self.label_39 = QLabel(self.network_layout)
        self.label_39.setObjectName(u"label_39")

        self.wifi_layout.addWidget(self.label_39, 6, 0, 1, 1)

        self.label_1256 = QLabel(self.network_layout)
        self.label_1256.setObjectName(u"label_1256")

        self.wifi_layout.addWidget(self.label_1256, 9, 0, 1, 1)

        self.wifi_status_label = QLabel(self.network_layout)
        self.wifi_status_label.setObjectName(u"wifi_status_label")

        self.wifi_layout.addWidget(self.wifi_status_label, 9, 1, 1, 1)


        self.gridLayout_4.addLayout(self.wifi_layout, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.network_layout, 0, 0, 1, 4)

        self.disk_and_display_layout = QFrame(self.pc_info_page)
        self.disk_and_display_layout.setObjectName(u"disk_and_display_layout")
        self.disk_and_display_layout.setStyleSheet(u"")
        self.disk_and_display_layout.setFrameShape(QFrame.Shape.StyledPanel)
        self.disk_and_display_layout.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.disk_and_display_layout)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(30)
        self.gridLayout_5.setContentsMargins(20, 10, 20, 10)
        self.disk_layout = QGridLayout()
        self.disk_layout.setObjectName(u"disk_layout")
        self.disk_layout.setHorizontalSpacing(8)
        self.disk_layout.setVerticalSpacing(6)
        self.disk_layout.setContentsMargins(10, 10, 10, 10)
        self.disk_type = QLabel(self.disk_and_display_layout)
        self.disk_type.setObjectName(u"disk_type")

        self.disk_layout.addWidget(self.disk_type, 6, 1, 1, 1)

        self.label_22 = QLabel(self.disk_and_display_layout)
        self.label_22.setObjectName(u"label_22")

        self.disk_layout.addWidget(self.label_22, 1, 0, 1, 1)

        self.label_21 = QLabel(self.disk_and_display_layout)
        self.label_21.setObjectName(u"label_21")

        self.disk_layout.addWidget(self.label_21, 5, 0, 1, 1)

        self.label_16 = QLabel(self.disk_and_display_layout)
        self.label_16.setObjectName(u"label_16")

        self.disk_layout.addWidget(self.label_16, 2, 0, 1, 1)

        self.disk_desc = QLabel(self.disk_and_display_layout)
        self.disk_desc.setObjectName(u"disk_desc")

        self.disk_layout.addWidget(self.disk_desc, 1, 1, 1, 1)

        self.label_23 = QLabel(self.disk_and_display_layout)
        self.label_23.setObjectName(u"label_23")

        self.disk_layout.addWidget(self.label_23, 6, 0, 1, 1)

        self.disk_byte_sector = QLabel(self.disk_and_display_layout)
        self.disk_byte_sector.setObjectName(u"disk_byte_sector")

        self.disk_layout.addWidget(self.disk_byte_sector, 7, 1, 1, 1)

        self.disk_model = QLabel(self.disk_and_display_layout)
        self.disk_model.setObjectName(u"disk_model")

        self.disk_layout.addWidget(self.disk_model, 3, 1, 1, 1)

        self.label_18 = QLabel(self.disk_and_display_layout)
        self.label_18.setObjectName(u"label_18")

        self.disk_layout.addWidget(self.label_18, 3, 0, 1, 1)

        self.label_33 = QLabel(self.disk_and_display_layout)
        self.label_33.setObjectName(u"label_33")

        self.disk_layout.addWidget(self.label_33, 7, 0, 1, 1)

        self.disk_manu = QLabel(self.disk_and_display_layout)
        self.disk_manu.setObjectName(u"disk_manu")

        self.disk_layout.addWidget(self.disk_manu, 2, 1, 1, 1)

        self.disk_part = QLabel(self.disk_and_display_layout)
        self.disk_part.setObjectName(u"disk_part")

        self.disk_layout.addWidget(self.disk_part, 5, 1, 1, 1)

        self.disk_size = QLabel(self.disk_and_display_layout)
        self.disk_size.setObjectName(u"disk_size")

        self.disk_layout.addWidget(self.disk_size, 4, 1, 1, 1)

        self.label_20 = QLabel(self.disk_and_display_layout)
        self.label_20.setObjectName(u"label_20")

        self.disk_layout.addWidget(self.label_20, 4, 0, 1, 1)

        self.label_15 = QLabel(self.disk_and_display_layout)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 20))
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setFont(font5)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(2, 193, 254);")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.disk_layout.addWidget(self.label_15, 0, 0, 1, 2)


        self.gridLayout_5.addLayout(self.disk_layout, 0, 0, 1, 1)

        self.display_layout = QGridLayout()
        self.display_layout.setObjectName(u"display_layout")
        self.display_layout.setHorizontalSpacing(8)
        self.display_layout.setContentsMargins(10, 10, 10, 10)
        self.display_resolution = QLabel(self.disk_and_display_layout)
        self.display_resolution.setObjectName(u"display_resolution")

        self.display_layout.addWidget(self.display_resolution, 6, 1, 1, 1)

        self.label_42 = QLabel(self.disk_and_display_layout)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 20))
        self.label_42.setMaximumSize(QSize(16777215, 20))
        self.label_42.setFont(font5)
        self.label_42.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(2, 193, 254);")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.display_layout.addWidget(self.label_42, 0, 0, 1, 2)

        self.label_96 = QLabel(self.disk_and_display_layout)
        self.label_96.setObjectName(u"label_96")

        self.display_layout.addWidget(self.label_96, 7, 0, 1, 1)

        self.label_48 = QLabel(self.disk_and_display_layout)
        self.label_48.setObjectName(u"label_48")

        self.display_layout.addWidget(self.label_48, 1, 0, 1, 1)

        self.label_94 = QLabel(self.disk_and_display_layout)
        self.label_94.setObjectName(u"label_94")

        self.display_layout.addWidget(self.label_94, 5, 0, 1, 1)

        self.display_bit_pixel = QLabel(self.disk_and_display_layout)
        self.display_bit_pixel.setObjectName(u"display_bit_pixel")

        self.display_layout.addWidget(self.display_bit_pixel, 7, 1, 1, 1)

        self.display_type = QLabel(self.disk_and_display_layout)
        self.display_type.setObjectName(u"display_type")

        self.display_layout.addWidget(self.display_type, 2, 1, 1, 1)

        self.label_95 = QLabel(self.disk_and_display_layout)
        self.label_95.setObjectName(u"label_95")

        self.display_layout.addWidget(self.label_95, 6, 0, 1, 1)

        self.display_name = QLabel(self.disk_and_display_layout)
        self.display_name.setObjectName(u"display_name")

        self.display_layout.addWidget(self.display_name, 1, 1, 1, 1)

        self.label_44 = QLabel(self.disk_and_display_layout)
        self.label_44.setObjectName(u"label_44")

        self.display_layout.addWidget(self.label_44, 3, 0, 1, 1)

        self.display_driver_version = QLabel(self.disk_and_display_layout)
        self.display_driver_version.setObjectName(u"display_driver_version")

        self.display_layout.addWidget(self.display_driver_version, 5, 1, 1, 1)

        self.display_desc = QLabel(self.disk_and_display_layout)
        self.display_desc.setObjectName(u"display_desc")

        self.display_layout.addWidget(self.display_desc, 3, 1, 1, 1)

        self.display_ram = QLabel(self.disk_and_display_layout)
        self.display_ram.setObjectName(u"display_ram")

        self.display_layout.addWidget(self.display_ram, 4, 1, 1, 1)

        self.label_43 = QLabel(self.disk_and_display_layout)
        self.label_43.setObjectName(u"label_43")

        self.display_layout.addWidget(self.label_43, 2, 0, 1, 1)

        self.label_46 = QLabel(self.disk_and_display_layout)
        self.label_46.setObjectName(u"label_46")

        self.display_layout.addWidget(self.label_46, 4, 0, 1, 1)


        self.gridLayout_5.addLayout(self.display_layout, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.disk_and_display_layout, 1, 0, 1, 4)

        self.back_home_button = QPushButton(self.pc_info_page)
        self.back_home_button.setObjectName(u"back_home_button")
        self.back_home_button.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: #00AEEF; /* Bootstrap's primary blue color */\n"
"\n"
"    border-radius: 5px;\n"
"    padding: 8px 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; /* Darker blue on hover */\n"
"    border-color: #0056b3; /* Darker blue border on hover */\n"
"}")
        icon19 = QIcon(QIcon.fromTheme(u"document-revert"))
        self.back_home_button.setIcon(icon19)

        self.gridLayout_3.addWidget(self.back_home_button, 2, 0, 1, 1)

        self.taskmanager_button = QPushButton(self.pc_info_page)
        self.taskmanager_button.setObjectName(u"taskmanager_button")
        self.taskmanager_button.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: #00AEEF; /* Bootstrap's primary blue color */\n"
"\n"
"    border-radius: 5px;\n"
"    padding: 8px 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; /* Darker blue on hover */\n"
"    border-color: #0056b3; /* Darker blue border on hover */\n"
"}")
        icon20 = QIcon(QIcon.fromTheme(u"task"))
        self.taskmanager_button.setIcon(icon20)

        self.gridLayout_3.addWidget(self.taskmanager_button, 2, 2, 1, 1)

        self.sysinfo = QFrame(self.pc_info_page)
        self.sysinfo.setObjectName(u"sysinfo")
        self.sysinfo.setStyleSheet(u"")
        self.sysinfo.setFrameShape(QFrame.Shape.StyledPanel)
        self.sysinfo.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_11 = QGridLayout(self.sysinfo)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setVerticalSpacing(25)
        self.gridLayout_11.setContentsMargins(10, -1, -1, -1)
        self.syslayout = QGridLayout()
        self.syslayout.setObjectName(u"syslayout")
        self.syslayout.setHorizontalSpacing(8)
        self.syslayout.setVerticalSpacing(10)
        self.syslayout.setContentsMargins(5, 5, 5, 5)
        self.sysprocessor_manu = QLabel(self.sysinfo)
        self.sysprocessor_manu.setObjectName(u"sysprocessor_manu")

        self.syslayout.addWidget(self.sysprocessor_manu, 2, 1, 1, 1)

        self.sys_processor_name = QLabel(self.sysinfo)
        self.sys_processor_name.setObjectName(u"sys_processor_name")

        self.syslayout.addWidget(self.sys_processor_name, 1, 1, 1, 1)

        self.label_113 = QLabel(self.sysinfo)
        self.label_113.setObjectName(u"label_113")

        self.syslayout.addWidget(self.label_113, 11, 0, 1, 1)

        self.label_115 = QLabel(self.sysinfo)
        self.label_115.setObjectName(u"label_115")

        self.syslayout.addWidget(self.label_115, 13, 0, 1, 1)

        self.sys_processor_max_clock = QLabel(self.sysinfo)
        self.sys_processor_max_clock.setObjectName(u"sys_processor_max_clock")

        self.syslayout.addWidget(self.sys_processor_max_clock, 3, 1, 1, 1)

        self.label_27 = QLabel(self.sysinfo)
        self.label_27.setObjectName(u"label_27")

        self.syslayout.addWidget(self.label_27, 3, 0, 1, 1)

        self.label_25 = QLabel(self.sysinfo)
        self.label_25.setObjectName(u"label_25")

        self.syslayout.addWidget(self.label_25, 2, 0, 1, 1)

        self.sys_ram = QLabel(self.sysinfo)
        self.sys_ram.setObjectName(u"sys_ram")

        self.syslayout.addWidget(self.sys_ram, 13, 1, 1, 1)

        self.label7869 = QLabel(self.sysinfo)
        self.label7869.setObjectName(u"label7869")

        self.syslayout.addWidget(self.label7869, 9, 0, 1, 1)

        self.sys_processor_num_core = QLabel(self.sysinfo)
        self.sys_processor_num_core.setObjectName(u"sys_processor_num_core")

        self.syslayout.addWidget(self.sys_processor_num_core, 4, 1, 1, 1)

        self.label7865 = QLabel(self.sysinfo)
        self.label7865.setObjectName(u"label7865")

        self.syslayout.addWidget(self.label7865, 5, 0, 1, 1)

        self.label46547 = QLabel(self.sysinfo)
        self.label46547.setObjectName(u"label46547")

        self.syslayout.addWidget(self.label46547, 6, 0, 1, 1)

        self.sys_system_type = QLabel(self.sysinfo)
        self.sys_system_type.setObjectName(u"sys_system_type")

        self.syslayout.addWidget(self.sys_system_type, 9, 1, 1, 1)

        self.sys_processor_logical_num_core = QLabel(self.sysinfo)
        self.sys_processor_logical_num_core.setObjectName(u"sys_processor_logical_num_core")

        self.syslayout.addWidget(self.sys_processor_logical_num_core, 5, 1, 1, 1)

        self.label_31 = QLabel(self.sysinfo)
        self.label_31.setObjectName(u"label_31")

        self.syslayout.addWidget(self.label_31, 1, 0, 1, 1)

        self.label_24 = QLabel(self.sysinfo)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 20))
        self.label_24.setMaximumSize(QSize(16777215, 20))
        self.label_24.setFont(font5)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(2, 193, 254);")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.syslayout.addWidget(self.label_24, 0, 0, 1, 2)

        self.sys_os_name = QLabel(self.sysinfo)
        self.sys_os_name.setObjectName(u"sys_os_name")

        self.syslayout.addWidget(self.sys_os_name, 10, 1, 1, 1)

        self.sys_os_version = QLabel(self.sysinfo)
        self.sys_os_version.setObjectName(u"sys_os_version")

        self.syslayout.addWidget(self.sys_os_version, 11, 1, 1, 1)

        self.label_114 = QLabel(self.sysinfo)
        self.label_114.setObjectName(u"label_114")

        self.syslayout.addWidget(self.label_114, 12, 0, 1, 1)

        self.sys_os_manu = QLabel(self.sysinfo)
        self.sys_os_manu.setObjectName(u"sys_os_manu")

        self.syslayout.addWidget(self.sys_os_manu, 12, 1, 1, 1)

        self.label_112 = QLabel(self.sysinfo)
        self.label_112.setObjectName(u"label_112")

        self.syslayout.addWidget(self.label_112, 10, 0, 1, 1)

        self.label5743 = QLabel(self.sysinfo)
        self.label5743.setObjectName(u"label5743")

        self.syslayout.addWidget(self.label5743, 8, 0, 1, 1)

        self.sys_system_manu = QLabel(self.sysinfo)
        self.sys_system_manu.setObjectName(u"sys_system_manu")

        self.syslayout.addWidget(self.sys_system_manu, 7, 1, 1, 1)

        self.label6854 = QLabel(self.sysinfo)
        self.label6854.setObjectName(u"label6854")

        self.syslayout.addWidget(self.label6854, 7, 0, 1, 1)

        self.sys_system_model = QLabel(self.sysinfo)
        self.sys_system_model.setObjectName(u"sys_system_model")

        self.syslayout.addWidget(self.sys_system_model, 8, 1, 1, 1)

        self.pic42524 = QLabel(self.sysinfo)
        self.pic42524.setObjectName(u"pic42524")

        self.syslayout.addWidget(self.pic42524, 4, 0, 1, 1)

        self.sys_system_name = QLabel(self.sysinfo)
        self.sys_system_name.setObjectName(u"sys_system_name")

        self.syslayout.addWidget(self.sys_system_name, 6, 1, 1, 1)


        self.gridLayout_11.addLayout(self.syslayout, 0, 0, 1, 1)

        self.perfomrncelgrdlayout_2 = QGridLayout()
        self.perfomrncelgrdlayout_2.setObjectName(u"perfomrncelgrdlayout_2")
        self.perfomrncelgrdlayout_2.setHorizontalSpacing(10)
        self.perfomrncelgrdlayout_2.setVerticalSpacing(8)
        self.perfomrncelgrdlayout_2.setContentsMargins(10, 10, 10, 10)
        self.cpu_ram_free_used_ratio = QLabel(self.sysinfo)
        self.cpu_ram_free_used_ratio.setObjectName(u"cpu_ram_free_used_ratio")
        self.cpu_ram_free_used_ratio.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cpu_ram_free_used_ratio.setMargin(10)

        self.perfomrncelgrdlayout_2.addWidget(self.cpu_ram_free_used_ratio, 1, 2, 1, 1)

        self.label_124 = QLabel(self.sysinfo)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(32, 32))
        self.label_124.setMaximumSize(QSize(64, 64))
        self.label_124.setPixmap(QPixmap(u":/perfomance_icons/ram_icon.png"))
        self.label_124.setScaledContents(True)
        self.label_124.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.perfomrncelgrdlayout_2.addWidget(self.label_124, 1, 0, 1, 1)

        self.cpu_progress_bar = QProgressBar(self.sysinfo)
        self.cpu_progress_bar.setObjectName(u"cpu_progress_bar")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(False)
        self.cpu_progress_bar.setFont(font7)
        self.cpu_progress_bar.setStyleSheet(u"QProgressBar {\n"
"    background-color: #C0C0C0; /* Background color */\n"
"    border: 2px solid grey; /* Border color */\n"
"    border-radius: 5px; /* Border radius */\n"
"\n"
"    \n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #00ADEF; /* Progress color */\n"
"}")
        self.cpu_progress_bar.setValue(0)
        self.cpu_progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cpu_progress_bar.setInvertedAppearance(False)

        self.perfomrncelgrdlayout_2.addWidget(self.cpu_progress_bar, 0, 1, 1, 1)

        self.label65746 = QLabel(self.sysinfo)
        self.label65746.setObjectName(u"label65746")
        self.label65746.setMinimumSize(QSize(32, 32))
        self.label65746.setMaximumSize(QSize(64, 64))
        self.label65746.setPixmap(QPixmap(u":/perfomance_icons/cpu_icon.png"))
        self.label65746.setScaledContents(True)

        self.perfomrncelgrdlayout_2.addWidget(self.label65746, 0, 0, 1, 1)

        self.ram_progressbar = QProgressBar(self.sysinfo)
        self.ram_progressbar.setObjectName(u"ram_progressbar")
        self.ram_progressbar.setFont(font7)
        self.ram_progressbar.setStyleSheet(u"QProgressBar {\n"
"    background-color: #C0C0C0; /* Background color */\n"
"    border: 2px solid grey; /* Border color */\n"
"    border-radius: 5px; /* Border radius */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #00ADEF; /* Progress color */\n"
"}")
        self.ram_progressbar.setValue(0)
        self.ram_progressbar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ram_progressbar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.perfomrncelgrdlayout_2.addWidget(self.ram_progressbar, 1, 1, 1, 1)

        self.cpu_frequency_label = QLabel(self.sysinfo)
        self.cpu_frequency_label.setObjectName(u"cpu_frequency_label")
        self.cpu_frequency_label.setMargin(10)

        self.perfomrncelgrdlayout_2.addWidget(self.cpu_frequency_label, 0, 2, 1, 1)


        self.gridLayout_11.addLayout(self.perfomrncelgrdlayout_2, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.sysinfo, 0, 4, 2, 2)

        self.stackedWidget.addWidget(self.pc_info_page)
        self.coopurl_page = QWidget()
        self.coopurl_page.setObjectName(u"coopurl_page")
        self.coopurl_page.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.gridLayout_8 = QGridLayout(self.coopurl_page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.searchbarHorintoallayout = QHBoxLayout()
        self.searchbarHorintoallayout.setObjectName(u"searchbarHorintoallayout")
        self.searchbarHorintoallayout.setContentsMargins(40, -1, 40, -1)
        self.coopurl_search_lineedit = QLineEdit(self.coopurl_page)
        self.coopurl_search_lineedit.setObjectName(u"coopurl_search_lineedit")
        self.coopurl_search_lineedit.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.coopurl_search_lineedit.setClearButtonEnabled(True)

        self.searchbarHorintoallayout.addWidget(self.coopurl_search_lineedit)

        self.coopurl_Search_button = QPushButton(self.coopurl_page)
        self.coopurl_Search_button.setObjectName(u"coopurl_Search_button")
        self.coopurl_Search_button.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: #00AEEF; /* Bootstrap's primary blue color */\n"
"\n"
"    border-radius: 5px;\n"
"    padding: 8px 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; /* Darker blue on hover */\n"
"    border-color: #0056b3; /* Darker blue border on hover */\n"
"}")
        icon21 = QIcon(QIcon.fromTheme(u"edit-find"))
        self.coopurl_Search_button.setIcon(icon21)

        self.searchbarHorintoallayout.addWidget(self.coopurl_Search_button)


        self.gridLayout_6.addLayout(self.searchbarHorintoallayout, 0, 0, 1, 1)

        self.coopurl_table = QTableWidget(self.coopurl_page)
        if (self.coopurl_table.columnCount() < 2):
            self.coopurl_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.coopurl_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.coopurl_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.coopurl_table.setObjectName(u"coopurl_table")

        self.gridLayout_6.addWidget(self.coopurl_table, 1, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.coopurl_page)

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

        self.stackedWidget.setCurrentIndex(1)
        self.michu_slider.setCurrentIndex(0)


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
        self.michu_slide_1.setText("")
        self.label_14.setText("")
        self.label_17.setText("")
        self.label_19.setText("")
        self.label_26.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_6.setText("")
        self.label_8.setText("")
        self.label_10.setText("")
        self.label_12.setText("")
        self.michu_Previous.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.michu_Next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.addprinter_button.setText(QCoreApplication.translate("MainWindow", u"Add Printers", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Subnet mask:", None))
        self.ethernet_alternative_DNS_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"IP Address:", None))
        self.ethernet_mac_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Default Gateway :", None))
        self.ethernet_Deafult_DNS.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.ethernet_speed_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Adapter:", None))
        self.ethernet_status.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Alternative DNS:", None))
        self.ethernet_defaultGateway_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.ethernet_adapter_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.ethernet_subnet_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.ethernet_ip_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ethernet IP info", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Network Status ", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Default DNS:", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"MAC  Address:", None))
        self.wifi_ip_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Speed:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u" Subnet mask:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u" IP Address:", None))
        self.wifi_default_dns_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u" Adapter:", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"MAC  Address:", None))
        self.wifi_speed_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.wifi_subnet_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Default Gateway :", None))
        self.wifi_adapter_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.wifi_MAC_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.wifi_defaultGate_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Wifi", None))
        self.wifi_alternat_DNS_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Default DNS:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Alternative DNS:", None))
        self.label_1256.setText(QCoreApplication.translate("MainWindow", u"Network Status ", None))
        self.wifi_status_label.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
        self.disk_type.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Partitions", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Manufacturer", None))
        self.disk_desc.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Media Type", None))
        self.disk_byte_sector.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.disk_model.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Bytes/Sector", None))
        self.disk_manu.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.disk_part.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.disk_size.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Disk", None))
        self.display_resolution.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Display ", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Bits/Pixel", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Driver Version", None))
        self.display_bit_pixel.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.display_type.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.display_name.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Adapter Description", None))
        self.display_driver_version.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.display_desc.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.display_ram.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Adapter Type", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Adapter RAM", None))
        self.back_home_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.taskmanager_button.setText(QCoreApplication.translate("MainWindow", u"Task Manager ", None))
        self.sysprocessor_manu.setText("")
        self.sys_processor_name.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Installed RAM", None))
        self.sys_processor_max_clock.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Processor Max Clock Speed", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Processor Manufacturer", None))
        self.sys_ram.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label7869.setText(QCoreApplication.translate("MainWindow", u"System Type", None))
        self.sys_processor_num_core.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label7865.setText(QCoreApplication.translate("MainWindow", u"Number of Logical Processors", None))
        self.label46547.setText(QCoreApplication.translate("MainWindow", u"System Name", None))
        self.sys_system_type.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.sys_processor_logical_num_core.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Processor Name", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"System Info", None))
        self.sys_os_name.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.sys_os_version.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"OS Manufacturer", None))
        self.sys_os_manu.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"OS Name", None))
        self.label5743.setText(QCoreApplication.translate("MainWindow", u"System Model", None))
        self.sys_system_manu.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label6854.setText(QCoreApplication.translate("MainWindow", u"System Manufacturer\"", None))
        self.sys_system_model.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pic42524.setText(QCoreApplication.translate("MainWindow", u"Number of Cores", None))
        self.sys_system_name.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.cpu_ram_free_used_ratio.setText(QCoreApplication.translate("MainWindow", u"Loading...", None))
        self.label_124.setText("")
        self.label65746.setText("")
        self.cpu_frequency_label.setText(QCoreApplication.translate("MainWindow", u"Loading...", None))
        self.coopurl_search_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search URLS", None))
        self.coopurl_Search_button.setText("")
        ___qtablewidgetitem = self.coopurl_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Site Name", None));
        ___qtablewidgetitem1 = self.coopurl_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"URL", None));
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
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1281, 816)
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
        self.michu_page = QWidget()
        self.michu_page.setObjectName(u"michu_page")
        self.verticalLayout_6 = QVBoxLayout(self.michu_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.michu_page)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.michu_slider = QStackedWidget(self.frame)
        self.michu_slider.setObjectName(u"michu_slider")
        self.michu_slider.setStyleSheet(u"QStackedWidget {\n"
"                border: 1px solid #dee2e6;\n"
"                background-color: white;\n"
"            }")
        self.container_1 = QWidget()
        self.container_1.setObjectName(u"container_1")
        self.gridLayout_9 = QGridLayout(self.container_1)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.michu_slide_1 = QLabel(self.container_1)
        self.michu_slide_1.setObjectName(u"michu_slide_1")
        self.michu_slide_1.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide1.PNG"))
        self.michu_slide_1.setScaledContents(True)

        self.gridLayout_9.addWidget(self.michu_slide_1, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_1)
        self.container_2 = QWidget()
        self.container_2.setObjectName(u"container_2")
        self.gridLayout_10 = QGridLayout(self.container_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_3 = QLabel(self.container_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide2.PNG"))
        self.label_3.setScaledContents(True)

        self.gridLayout_10.addWidget(self.label_3, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_2)
        self.container_3 = QWidget()
        self.container_3.setObjectName(u"container_3")
        self.gridLayout_12 = QGridLayout(self.container_3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_4 = QLabel(self.container_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide3.PNG"))
        self.label_4.setScaledContents(True)

        self.gridLayout_12.addWidget(self.label_4, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_3)
        self.container_4 = QWidget()
        self.container_4.setObjectName(u"container_4")
        self.gridLayout_13 = QGridLayout(self.container_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_6 = QLabel(self.container_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide4.PNG"))
        self.label_6.setScaledContents(True)

        self.gridLayout_13.addWidget(self.label_6, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_4)
        self.container_5 = QWidget()
        self.container_5.setObjectName(u"container_5")
        self.gridLayout_14 = QGridLayout(self.container_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_8 = QLabel(self.container_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide5.PNG"))
        self.label_8.setScaledContents(True)

        self.gridLayout_14.addWidget(self.label_8, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_5)
        self.container_6 = QWidget()
        self.container_6.setObjectName(u"container_6")
        self.gridLayout_15 = QGridLayout(self.container_6)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_10 = QLabel(self.container_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide6.PNG"))
        self.label_10.setScaledContents(True)

        self.gridLayout_15.addWidget(self.label_10, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_6)
        self.container_7 = QWidget()
        self.container_7.setObjectName(u"container_7")
        self.gridLayout_16 = QGridLayout(self.container_7)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_12 = QLabel(self.container_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide7.PNG"))
        self.label_12.setScaledContents(True)

        self.gridLayout_16.addWidget(self.label_12, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_7)
        self.container_8 = QWidget()
        self.container_8.setObjectName(u"container_8")
        self.gridLayout_19 = QGridLayout(self.container_8)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_14 = QLabel(self.container_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide8.PNG"))
        self.label_14.setScaledContents(True)

        self.gridLayout_19.addWidget(self.label_14, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_8)
        self.container_9 = QWidget()
        self.container_9.setObjectName(u"container_9")
        self.gridLayout_17 = QGridLayout(self.container_9)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_17 = QLabel(self.container_9)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide9.PNG"))
        self.label_17.setScaledContents(True)

        self.gridLayout_17.addWidget(self.label_17, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_9)
        self.container_10 = QWidget()
        self.container_10.setObjectName(u"container_10")
        self.gridLayout_18 = QGridLayout(self.container_10)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_19 = QLabel(self.container_10)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide10.PNG"))
        self.label_19.setScaledContents(True)

        self.gridLayout_18.addWidget(self.label_19, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_10)
        self.container_11 = QWidget()
        self.container_11.setObjectName(u"container_11")
        self.gridLayout_20 = QGridLayout(self.container_11)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_26 = QLabel(self.container_11)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setPixmap(QPixmap(u":/michusliders/michu_slide/Slide11.PNG"))
        self.label_26.setScaledContents(True)

        self.gridLayout_20.addWidget(self.label_26, 0, 0, 1, 1)

        self.michu_slider.addWidget(self.container_11)

        self.gridLayout_7.addWidget(self.michu_slider, 0, 0, 1, 2)

        self.michu_Previous = QPushButton(self.frame)
        self.michu_Previous.setObjectName(u"michu_Previous")
        self.michu_Previous.setStyleSheet(u"QPushButton {\n"
"                background-color: #08B0F0;  /* Bootstrap primary color */\n"
"                color: white;\n"
"                border: none;\n"
"                padding: 5px 5px;\n"
"                font-size: 14px;\n"
"                line-height: 1px;\n"
"                border-radius: 5px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0b5ed7;  /* Bootstrap primary color on hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0a58ca;  /* Bootstrap primary color on active */\n"
"            }")

        self.gridLayout_7.addWidget(self.michu_Previous, 1, 0, 1, 1)

        self.michu_Next = QPushButton(self.frame)
        self.michu_Next.setObjectName(u"michu_Next")
        self.michu_Next.setStyleSheet(u"QPushButton {\n"
"                background-color: #08B0F0;  /* Bootstrap primary color */\n"
"                color: white;\n"
"                border: none;\n"
"                padding: 5px 5px;\n"
"                font-size: 14px;\n"
"                line-height: 1px;\n"
"                border-radius: 5px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0b5ed7;  /* Bootstrap primary color on hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0a58ca;  /* Bootstrap primary color on active */\n"
"            }")

        self.gridLayout_7.addWidget(self.michu_Next, 1, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.frame)

        self.stackedWidget.addWidget(self.michu_page)
        self.pc_info_page = QWidget()
        self.pc_info_page.setObjectName(u"pc_info_page")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.pc_info_page.setFont(font4)
        self.pc_info_page.setStyleSheet(u"QWidget{color: #000000;\n"
"text-size: 13px bold;}\n"
"\n"
"QFrame {\n"
"    background-color: white; /* Card background color */\n"
"    border: 1px solid #ddd; /* Border similar to Bootstrap */\n"
"    border-radius: 5px; /* Rounded corners */\n"
" \n"
"}\n"
"QLabel {\n"
"    qproperty-alignment: 'AlignHCenter | AlignVCenter';\n"
" font-size: 12px;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.pc_info_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.addprinter_button = QPushButton(self.pc_info_page)
        self.addprinter_button.setObjectName(u"addprinter_button")
        self.addprinter_button.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: #00AEEF; /* Bootstrap's primary blue color */\n"
"\n"
"    border-radius: 5px;\n"
"    padding: 8px 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; /* Darker blue on hover */\n"
"    border-color: #0056b3; /* Darker blue border on hover */\n"
"}")
        icon18 = QIcon(QIcon.fromTheme(u"printer"))
        self.addprinter_button.setIcon(icon18)

        self.gridLayout_3.addWidget(self.addprinter_button, 2, 4, 1, 1)

        self.network_layout = QFrame(self.pc_info_page)
        self.network_layout.setObjectName(u"network_layout")
        self.network_layout.setStyleSheet(u"")
        self.network_layout.setFrameShape(QFrame.Shape.StyledPanel)
        self.network_layout.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.network_layout)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(15)
        self.gridLayout_4.setVerticalSpacing(1)
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.ethernet_layout = QGridLayout()
        self.ethernet_layout.setObjectName(u"ethernet_layout")
        self.ethernet_layout.setHorizontalSpacing(8)
        self.ethernet_layout.setContentsMargins(10, 10, 10, 10)
        self.label_91 = QLabel(self.network_layout)
        self.label_91.setObjectName(u"label_91")

        self.ethernet_layout.addWidget(self.label_91, 8, 0, 1, 1)

        self.label_81 = QLabel(self.network_layout)
        self.label_81.setObjectName(u"label_81")

        self.ethernet_layout.addWidget(self.label_81, 3, 0, 1, 1)

        self.ethernet_alternative_DNS_label = QLabel(self.network_layout)
        self.ethernet_alternative_DNS_label.setObjectName(u"ethernet_alternative_DNS_label")

        self.ethernet_layout.addWidget(self.ethernet_alternative_DNS_label, 6, 1, 1, 1)

        self.label_79 = QLabel(self.network_layout)
        self.label_79.setObjectName(u"label_79")

        self.ethernet_layout.addWidget(self.label_79, 2, 0, 1, 1)

        self.ethernet_mac_label = QLabel(self.network_layout)
        self.ethernet_mac_label.setObjectName(u"ethernet_mac_label")

        self.ethernet_layout.addWidget(self.ethernet_mac_label, 7, 1, 1, 1)

        self.label_83 = QLabel(self.network_layout)
        self.label_83.setObjectName(u"label_83")

        self.ethernet_layout.addWidget(self.label_83, 4, 0, 1, 1)

        self.ethernet_Deafult_DNS = QLabel(self.network_layout)
        self.ethernet_Deafult_DNS.setObjectName(u"ethernet_Deafult_DNS")

        self.ethernet_layout.addWidget(self.ethernet_Deafult_DNS, 5, 1, 1, 1)

        self.ethernet_speed_label = QLabel(self.network_layout)
        self.ethernet_speed_label.setObjectName(u"ethernet_speed_label")

        self.ethernet_layout.addWidget(self.ethernet_speed_label, 8, 1, 1, 1)

        self.label_77 = QLabel(self.network_layout)
        self.label_77.setObjectName(u"label_77")

        self.ethernet_layout.addWidget(self.label_77, 1, 0, 1, 1)

        self.ethernet_status = QLabel(self.network_layout)
        self.ethernet_status.setObjectName(u"ethernet_status")

        self.ethernet_layout.addWidget(self.ethernet_status, 9, 1, 1, 1)

        self.label_87 = QLabel(self.network_layout)
        self.label_87.setObjectName(u"label_87")

        self.ethernet_layout.addWidget(self.label_87, 6, 0, 1, 1)

        self.ethernet_defaultGateway_label = QLabel(self.network_layout)
        self.ethernet_defaultGateway_label.setObjectName(u"ethernet_defaultGateway_label")

        self.ethernet_layout.addWidget(self.ethernet_defaultGateway_label, 4, 1, 1, 1)

        self.ethernet_adapter_label = QLabel(self.network_layout)
        self.ethernet_adapter_label.setObjectName(u"ethernet_adapter_label")

        self.ethernet_layout.addWidget(self.ethernet_adapter_label, 1, 1, 1, 1)

        self.ethernet_subnet_label = QLabel(self.network_layout)
        self.ethernet_subnet_label.setObjectName(u"ethernet_subnet_label")

        self.ethernet_layout.addWidget(self.ethernet_subnet_label, 3, 1, 1, 1)

        self.ethernet_ip_label = QLabel(self.network_layout)
        self.ethernet_ip_label.setObjectName(u"ethernet_ip_label")

        self.ethernet_layout.addWidget(self.ethernet_ip_label, 2, 1, 1, 1)

        self.label_5 = QLabel(self.network_layout)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 20))
        self.label_5.setMaximumSize(QSize(16777215, 20))
        font5 = QFont()
        font5.setBold(True)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(2, 193, 254);")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ethernet_layout.addWidget(self.label_5, 0, 0, 1, 2)

        self.label_102 = QLabel(self.network_layout)
        self.label_102.setObjectName(u"label_102")

        self.ethernet_layout.addWidget(self.label_102, 9, 0, 1, 1)

        self.label_85 = QLabel(self.network_layout)
        self.label_85.setObjectName(u"label_85")

        self.ethernet_layout.addWidget(self.label_85, 5, 0, 1, 1)

        self.label_89 = QLabel(self.network_layout)
        self.label_89.setObjectName(u"label_89")

        self.ethernet_layout.addWidget(self.label_89, 7, 0, 1, 1)


        self.gridLayout_4.addLayout(self.ethernet_layout, 0, 1, 1, 1)

        self.wifi_layout = QGridLayout()
        self.wifi_layout.setObjectName(u"wifi_layout")
        self.wifi_layout.setHorizontalSpacing(8)
        self.wifi_layout.setVerticalSpacing(6)
        self.wifi_layout.setContentsMargins(10, 10, 10, 10)
        self.wifi_ip_label = QLabel(self.network_layout)
        self.wifi_ip_label.setObjectName(u"wifi_ip_label")

        self.wifi_layout.addWidget(self.wifi_ip_label, 2, 1, 1, 1)

        self.label_52 = QLabel(self.network_layout)
        self.label_52.setObjectName(u"label_52")

        self.wifi_layout.addWidget(self.label_52, 8, 0, 1, 1)

        self.label_9 = QLabel(self.network_layout)
        self.label_9.setObjectName(u"label_9")

        self.wifi_layout.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_7 = QLabel(self.network_layout)
        self.label_7.setObjectName(u"label_7")

        self.wifi_layout.addWidget(self.label_7, 2, 0, 1, 1)

        self.wifi_default_dns_label = QLabel(self.network_layout)
        self.wifi_default_dns_label.setObjectName(u"wifi_default_dns_label")

        self.wifi_layout.addWidget(self.wifi_default_dns_label, 5, 1, 1, 1)

        self.label_13 = QLabel(self.network_layout)
        self.label_13.setObjectName(u"label_13")

        self.wifi_layout.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_41 = QLabel(self.network_layout)
        self.label_41.setObjectName(u"label_41")

        self.wifi_layout.addWidget(self.label_41, 7, 0, 1, 1)

        self.wifi_speed_label = QLabel(self.network_layout)
        self.wifi_speed_label.setObjectName(u"wifi_speed_label")

        self.wifi_layout.addWidget(self.wifi_speed_label, 8, 1, 1, 1)

        self.wifi_subnet_label = QLabel(self.network_layout)
        self.wifi_subnet_label.setObjectName(u"wifi_subnet_label")

        self.wifi_layout.addWidget(self.wifi_subnet_label, 3, 1, 1, 1)

        self.label_11 = QLabel(self.network_layout)
        self.label_11.setObjectName(u"label_11")

        self.wifi_layout.addWidget(self.label_11, 4, 0, 1, 1)

        self.wifi_adapter_label = QLabel(self.network_layout)
        self.wifi_adapter_label.setObjectName(u"wifi_adapter_label")

        self.wifi_layout.addWidget(self.wifi_adapter_label, 1, 1, 1, 1)

        self.wifi_MAC_label = QLabel(self.network_layout)
        self.wifi_MAC_label.setObjectName(u"wifi_MAC_label")

        self.wifi_layout.addWidget(self.wifi_MAC_label, 7, 1, 1, 1)

        self.wifi_defaultGate_label = QLabel(self.network_layout)
        self.wifi_defaultGate_label.setObjectName(u"wifi_defaultGate_label")

        self.wifi_layout.addWidget(self.wifi_defaultGate_label, 4, 1, 1, 1)

        self.label_93 = QLabel(self.network_layout)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMinimumSize(QSize(0, 20))
        self.label_93.setMaximumSize(QSize(16777215, 20))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(True)
        self.label_93.setFont(font6)
        self.label_93.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(2, 193, 254);")
        self.label_93.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.wifi_layout.addWidget(self.label_93, 0, 0, 1, 2)

        self.wifi_alternat_DNS_label = QLabel(self.network_layout)
        self.wifi_alternat_DNS_label.setObjectName(u"wifi_alternat_DNS_label")

        self.wifi_layout.addWidget(self.wifi_alternat_DNS_label, 6, 1, 1, 1)

        self.label_37 = QLabel(self.network_layout)
        self.label_37.setObjectName(u"label_37")

        self.wifi_layout.addWidget(self.label_37, 5, 0, 1, 1)

        self.label_39 = QLabel(self.network_layout)
        self.label_39.setObjectName(u"label_39")

        self.wifi_layout.addWidget(self.label_39, 6, 0, 1, 1)

        self.label_1256 = QLabel(self.network_layout)
        self.label_1256.setObjectName(u"label_1256")

        self.wifi_layout.addWidget(self.label_1256, 9, 0, 1, 1)

        self.wifi_status_label = QLabel(self.network_layout)
        self.wifi_status_label.setObjectName(u"wifi_status_label")

        self.wifi_layout.addWidget(self.wifi_status_label, 9, 1, 1, 1)


        self.gridLayout_4.addLayout(self.wifi_layout, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.network_layout, 0, 0, 1, 4)

        self.disk_and_display_layout = QFrame(self.pc_info_page)
        self.disk_and_display_layout.setObjectName(u"disk_and_display_layout")
        self.disk_and_display_layout.setStyleSheet(u"")
        self.disk_and_display_layout.setFrameShape(QFrame.Shape.StyledPanel)
        self.disk_and_display_layout.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.disk_and_display_layout)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(30)
        self.gridLayout_5.setContentsMargins(20, 10, 20, 10)
        self.disk_layout = QGridLayout()
        self.disk_layout.setObjectName(u"disk_layout")
        self.disk_layout.setHorizontalSpacing(8)
        self.disk_layout.setVerticalSpacing(6)
        self.disk_layout.setContentsMargins(10, 10, 10, 10)
        self.disk_type = QLabel(self.disk_and_display_layout)
        self.disk_type.setObjectName(u"disk_type")

        self.disk_layout.addWidget(self.disk_type, 6, 1, 1, 1)

        self.label_22 = QLabel(self.disk_and_display_layout)
        self.label_22.setObjectName(u"label_22")

        self.disk_layout.addWidget(self.label_22, 1, 0, 1, 1)

        self.label_21 = QLabel(self.disk_and_display_layout)
        self.label_21.setObjectName(u"label_21")

        self.disk_layout.addWidget(self.label_21, 5, 0, 1, 1)

        self.label_16 = QLabel(self.disk_and_display_layout)
        self.label_16.setObjectName(u"label_16")

        self.disk_layout.addWidget(self.label_16, 2, 0, 1, 1)

        self.disk_desc = QLabel(self.disk_and_display_layout)
        self.disk_desc.setObjectName(u"disk_desc")

        self.disk_layout.addWidget(self.disk_desc, 1, 1, 1, 1)

        self.label_23 = QLabel(self.disk_and_display_layout)
        self.label_23.setObjectName(u"label_23")

        self.disk_layout.addWidget(self.label_23, 6, 0, 1, 1)

        self.disk_byte_sector = QLabel(self.disk_and_display_layout)
        self.disk_byte_sector.setObjectName(u"disk_byte_sector")

        self.disk_layout.addWidget(self.disk_byte_sector, 7, 1, 1, 1)

        self.disk_model = QLabel(self.disk_and_display_layout)
        self.disk_model.setObjectName(u"disk_model")

        self.disk_layout.addWidget(self.disk_model, 3, 1, 1, 1)

        self.label_18 = QLabel(self.disk_and_display_layout)
        self.label_18.setObjectName(u"label_18")

        self.disk_layout.addWidget(self.label_18, 3, 0, 1, 1)

        self.label_33 = QLabel(self.disk_and_display_layout)
        self.label_33.setObjectName(u"label_33")

        self.disk_layout.addWidget(self.label_33, 7, 0, 1, 1)

        self.disk_manu = QLabel(self.disk_and_display_layout)
        self.disk_manu.setObjectName(u"disk_manu")

        self.disk_layout.addWidget(self.disk_manu, 2, 1, 1, 1)

        self.disk_part = QLabel(self.disk_and_display_layout)
        self.disk_part.setObjectName(u"disk_part")

        self.disk_layout.addWidget(self.disk_part, 5, 1, 1, 1)

        self.disk_size = QLabel(self.disk_and_display_layout)
        self.disk_size.setObjectName(u"disk_size")

        self.disk_layout.addWidget(self.disk_size, 4, 1, 1, 1)

        self.label_20 = QLabel(self.disk_and_display_layout)
        self.label_20.setObjectName(u"label_20")

        self.disk_layout.addWidget(self.label_20, 4, 0, 1, 1)

        self.label_15 = QLabel(self.disk_and_display_layout)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 20))
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setFont(font5)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(2, 193, 254);")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.disk_layout.addWidget(self.label_15, 0, 0, 1, 2)


        self.gridLayout_5.addLayout(self.disk_layout, 0, 0, 1, 1)

        self.display_layout = QGridLayout()
        self.display_layout.setObjectName(u"display_layout")
        self.display_layout.setHorizontalSpacing(8)
        self.display_layout.setContentsMargins(10, 10, 10, 10)
        self.display_resolution = QLabel(self.disk_and_display_layout)
        self.display_resolution.setObjectName(u"display_resolution")

        self.display_layout.addWidget(self.display_resolution, 6, 1, 1, 1)

        self.label_42 = QLabel(self.disk_and_display_layout)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 20))
        self.label_42.setMaximumSize(QSize(16777215, 20))
        self.label_42.setFont(font5)
        self.label_42.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(2, 193, 254);")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.display_layout.addWidget(self.label_42, 0, 0, 1, 2)

        self.label_96 = QLabel(self.disk_and_display_layout)
        self.label_96.setObjectName(u"label_96")

        self.display_layout.addWidget(self.label_96, 7, 0, 1, 1)

        self.label_48 = QLabel(self.disk_and_display_layout)
        self.label_48.setObjectName(u"label_48")

        self.display_layout.addWidget(self.label_48, 1, 0, 1, 1)

        self.label_94 = QLabel(self.disk_and_display_layout)
        self.label_94.setObjectName(u"label_94")

        self.display_layout.addWidget(self.label_94, 5, 0, 1, 1)

        self.display_bit_pixel = QLabel(self.disk_and_display_layout)
        self.display_bit_pixel.setObjectName(u"display_bit_pixel")

        self.display_layout.addWidget(self.display_bit_pixel, 7, 1, 1, 1)

        self.display_type = QLabel(self.disk_and_display_layout)
        self.display_type.setObjectName(u"display_type")

        self.display_layout.addWidget(self.display_type, 2, 1, 1, 1)

        self.label_95 = QLabel(self.disk_and_display_layout)
        self.label_95.setObjectName(u"label_95")

        self.display_layout.addWidget(self.label_95, 6, 0, 1, 1)

        self.display_name = QLabel(self.disk_and_display_layout)
        self.display_name.setObjectName(u"display_name")

        self.display_layout.addWidget(self.display_name, 1, 1, 1, 1)

        self.label_44 = QLabel(self.disk_and_display_layout)
        self.label_44.setObjectName(u"label_44")

        self.display_layout.addWidget(self.label_44, 3, 0, 1, 1)

        self.display_driver_version = QLabel(self.disk_and_display_layout)
        self.display_driver_version.setObjectName(u"display_driver_version")

        self.display_layout.addWidget(self.display_driver_version, 5, 1, 1, 1)

        self.display_desc = QLabel(self.disk_and_display_layout)
        self.display_desc.setObjectName(u"display_desc")

        self.display_layout.addWidget(self.display_desc, 3, 1, 1, 1)

        self.display_ram = QLabel(self.disk_and_display_layout)
        self.display_ram.setObjectName(u"display_ram")

        self.display_layout.addWidget(self.display_ram, 4, 1, 1, 1)

        self.label_43 = QLabel(self.disk_and_display_layout)
        self.label_43.setObjectName(u"label_43")

        self.display_layout.addWidget(self.label_43, 2, 0, 1, 1)

        self.label_46 = QLabel(self.disk_and_display_layout)
        self.label_46.setObjectName(u"label_46")

        self.display_layout.addWidget(self.label_46, 4, 0, 1, 1)


        self.gridLayout_5.addLayout(self.display_layout, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.disk_and_display_layout, 1, 0, 1, 4)

        self.back_home_button = QPushButton(self.pc_info_page)
        self.back_home_button.setObjectName(u"back_home_button")
        self.back_home_button.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: #00AEEF; /* Bootstrap's primary blue color */\n"
"\n"
"    border-radius: 5px;\n"
"    padding: 8px 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; /* Darker blue on hover */\n"
"    border-color: #0056b3; /* Darker blue border on hover */\n"
"}")
        icon19 = QIcon(QIcon.fromTheme(u"document-revert"))
        self.back_home_button.setIcon(icon19)

        self.gridLayout_3.addWidget(self.back_home_button, 2, 0, 1, 1)

        self.taskmanager_button = QPushButton(self.pc_info_page)
        self.taskmanager_button.setObjectName(u"taskmanager_button")
        self.taskmanager_button.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: #00AEEF; /* Bootstrap's primary blue color */\n"
"\n"
"    border-radius: 5px;\n"
"    padding: 8px 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; /* Darker blue on hover */\n"
"    border-color: #0056b3; /* Darker blue border on hover */\n"
"}")
        icon20 = QIcon(QIcon.fromTheme(u"task"))
        self.taskmanager_button.setIcon(icon20)

        self.gridLayout_3.addWidget(self.taskmanager_button, 2, 2, 1, 1)

        self.sysinfo = QFrame(self.pc_info_page)
        self.sysinfo.setObjectName(u"sysinfo")
        self.sysinfo.setStyleSheet(u"")
        self.sysinfo.setFrameShape(QFrame.Shape.StyledPanel)
        self.sysinfo.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_11 = QGridLayout(self.sysinfo)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setVerticalSpacing(25)
        self.gridLayout_11.setContentsMargins(10, -1, -1, -1)
        self.syslayout = QGridLayout()
        self.syslayout.setObjectName(u"syslayout")
        self.syslayout.setHorizontalSpacing(8)
        self.syslayout.setVerticalSpacing(10)
        self.syslayout.setContentsMargins(5, 5, 5, 5)
        self.sysprocessor_manu = QLabel(self.sysinfo)
        self.sysprocessor_manu.setObjectName(u"sysprocessor_manu")

        self.syslayout.addWidget(self.sysprocessor_manu, 2, 1, 1, 1)

        self.sys_processor_name = QLabel(self.sysinfo)
        self.sys_processor_name.setObjectName(u"sys_processor_name")

        self.syslayout.addWidget(self.sys_processor_name, 1, 1, 1, 1)

        self.label_113 = QLabel(self.sysinfo)
        self.label_113.setObjectName(u"label_113")

        self.syslayout.addWidget(self.label_113, 11, 0, 1, 1)

        self.label_115 = QLabel(self.sysinfo)
        self.label_115.setObjectName(u"label_115")

        self.syslayout.addWidget(self.label_115, 13, 0, 1, 1)

        self.sys_processor_max_clock = QLabel(self.sysinfo)
        self.sys_processor_max_clock.setObjectName(u"sys_processor_max_clock")

        self.syslayout.addWidget(self.sys_processor_max_clock, 3, 1, 1, 1)

        self.label_27 = QLabel(self.sysinfo)
        self.label_27.setObjectName(u"label_27")

        self.syslayout.addWidget(self.label_27, 3, 0, 1, 1)

        self.label_25 = QLabel(self.sysinfo)
        self.label_25.setObjectName(u"label_25")

        self.syslayout.addWidget(self.label_25, 2, 0, 1, 1)

        self.sys_ram = QLabel(self.sysinfo)
        self.sys_ram.setObjectName(u"sys_ram")

        self.syslayout.addWidget(self.sys_ram, 13, 1, 1, 1)

        self.label7869 = QLabel(self.sysinfo)
        self.label7869.setObjectName(u"label7869")

        self.syslayout.addWidget(self.label7869, 9, 0, 1, 1)

        self.sys_processor_num_core = QLabel(self.sysinfo)
        self.sys_processor_num_core.setObjectName(u"sys_processor_num_core")

        self.syslayout.addWidget(self.sys_processor_num_core, 4, 1, 1, 1)

        self.label7865 = QLabel(self.sysinfo)
        self.label7865.setObjectName(u"label7865")

        self.syslayout.addWidget(self.label7865, 5, 0, 1, 1)

        self.label46547 = QLabel(self.sysinfo)
        self.label46547.setObjectName(u"label46547")

        self.syslayout.addWidget(self.label46547, 6, 0, 1, 1)

        self.sys_system_type = QLabel(self.sysinfo)
        self.sys_system_type.setObjectName(u"sys_system_type")

        self.syslayout.addWidget(self.sys_system_type, 9, 1, 1, 1)

        self.sys_processor_logical_num_core = QLabel(self.sysinfo)
        self.sys_processor_logical_num_core.setObjectName(u"sys_processor_logical_num_core")

        self.syslayout.addWidget(self.sys_processor_logical_num_core, 5, 1, 1, 1)

        self.label_31 = QLabel(self.sysinfo)
        self.label_31.setObjectName(u"label_31")

        self.syslayout.addWidget(self.label_31, 1, 0, 1, 1)

        self.label_24 = QLabel(self.sysinfo)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 20))
        self.label_24.setMaximumSize(QSize(16777215, 20))
        self.label_24.setFont(font5)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(2, 193, 254);")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.syslayout.addWidget(self.label_24, 0, 0, 1, 2)

        self.sys_os_name = QLabel(self.sysinfo)
        self.sys_os_name.setObjectName(u"sys_os_name")

        self.syslayout.addWidget(self.sys_os_name, 10, 1, 1, 1)

        self.sys_os_version = QLabel(self.sysinfo)
        self.sys_os_version.setObjectName(u"sys_os_version")

        self.syslayout.addWidget(self.sys_os_version, 11, 1, 1, 1)

        self.label_114 = QLabel(self.sysinfo)
        self.label_114.setObjectName(u"label_114")

        self.syslayout.addWidget(self.label_114, 12, 0, 1, 1)

        self.sys_os_manu = QLabel(self.sysinfo)
        self.sys_os_manu.setObjectName(u"sys_os_manu")

        self.syslayout.addWidget(self.sys_os_manu, 12, 1, 1, 1)

        self.label_112 = QLabel(self.sysinfo)
        self.label_112.setObjectName(u"label_112")

        self.syslayout.addWidget(self.label_112, 10, 0, 1, 1)

        self.label5743 = QLabel(self.sysinfo)
        self.label5743.setObjectName(u"label5743")

        self.syslayout.addWidget(self.label5743, 8, 0, 1, 1)

        self.sys_system_manu = QLabel(self.sysinfo)
        self.sys_system_manu.setObjectName(u"sys_system_manu")

        self.syslayout.addWidget(self.sys_system_manu, 7, 1, 1, 1)

        self.label6854 = QLabel(self.sysinfo)
        self.label6854.setObjectName(u"label6854")

        self.syslayout.addWidget(self.label6854, 7, 0, 1, 1)

        self.sys_system_model = QLabel(self.sysinfo)
        self.sys_system_model.setObjectName(u"sys_system_model")

        self.syslayout.addWidget(self.sys_system_model, 8, 1, 1, 1)

        self.pic42524 = QLabel(self.sysinfo)
        self.pic42524.setObjectName(u"pic42524")

        self.syslayout.addWidget(self.pic42524, 4, 0, 1, 1)

        self.sys_system_name = QLabel(self.sysinfo)
        self.sys_system_name.setObjectName(u"sys_system_name")

        self.syslayout.addWidget(self.sys_system_name, 6, 1, 1, 1)


        self.gridLayout_11.addLayout(self.syslayout, 0, 0, 1, 1)

        self.perfomrncelgrdlayout_2 = QGridLayout()
        self.perfomrncelgrdlayout_2.setObjectName(u"perfomrncelgrdlayout_2")
        self.perfomrncelgrdlayout_2.setHorizontalSpacing(10)
        self.perfomrncelgrdlayout_2.setVerticalSpacing(8)
        self.perfomrncelgrdlayout_2.setContentsMargins(10, 10, 10, 10)
        self.cpu_ram_free_used_ratio = QLabel(self.sysinfo)
        self.cpu_ram_free_used_ratio.setObjectName(u"cpu_ram_free_used_ratio")
        self.cpu_ram_free_used_ratio.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cpu_ram_free_used_ratio.setMargin(10)

        self.perfomrncelgrdlayout_2.addWidget(self.cpu_ram_free_used_ratio, 1, 2, 1, 1)

        self.label_124 = QLabel(self.sysinfo)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(32, 32))
        self.label_124.setMaximumSize(QSize(64, 64))
        self.label_124.setPixmap(QPixmap(u":/perfomance_icons/ram_icon.png"))
        self.label_124.setScaledContents(True)
        self.label_124.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.perfomrncelgrdlayout_2.addWidget(self.label_124, 1, 0, 1, 1)

        self.cpu_progress_bar = QProgressBar(self.sysinfo)
        self.cpu_progress_bar.setObjectName(u"cpu_progress_bar")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(False)
        self.cpu_progress_bar.setFont(font7)
        self.cpu_progress_bar.setStyleSheet(u"QProgressBar {\n"
"    background-color: #C0C0C0; /* Background color */\n"
"    border: 2px solid grey; /* Border color */\n"
"    border-radius: 5px; /* Border radius */\n"
"\n"
"    \n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #00ADEF; /* Progress color */\n"
"}")
        self.cpu_progress_bar.setValue(0)
        self.cpu_progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cpu_progress_bar.setInvertedAppearance(False)

        self.perfomrncelgrdlayout_2.addWidget(self.cpu_progress_bar, 0, 1, 1, 1)

        self.label65746 = QLabel(self.sysinfo)
        self.label65746.setObjectName(u"label65746")
        self.label65746.setMinimumSize(QSize(32, 32))
        self.label65746.setMaximumSize(QSize(64, 64))
        self.label65746.setPixmap(QPixmap(u":/perfomance_icons/cpu_icon.png"))
        self.label65746.setScaledContents(True)

        self.perfomrncelgrdlayout_2.addWidget(self.label65746, 0, 0, 1, 1)

        self.ram_progressbar = QProgressBar(self.sysinfo)
        self.ram_progressbar.setObjectName(u"ram_progressbar")
        self.ram_progressbar.setFont(font7)
        self.ram_progressbar.setStyleSheet(u"QProgressBar {\n"
"    background-color: #C0C0C0; /* Background color */\n"
"    border: 2px solid grey; /* Border color */\n"
"    border-radius: 5px; /* Border radius */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #00ADEF; /* Progress color */\n"
"}")
        self.ram_progressbar.setValue(0)
        self.ram_progressbar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ram_progressbar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.perfomrncelgrdlayout_2.addWidget(self.ram_progressbar, 1, 1, 1, 1)

        self.cpu_frequency_label = QLabel(self.sysinfo)
        self.cpu_frequency_label.setObjectName(u"cpu_frequency_label")
        self.cpu_frequency_label.setMargin(10)

        self.perfomrncelgrdlayout_2.addWidget(self.cpu_frequency_label, 0, 2, 1, 1)


        self.gridLayout_11.addLayout(self.perfomrncelgrdlayout_2, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.sysinfo, 0, 4, 2, 2)

        self.stackedWidget.addWidget(self.pc_info_page)
        self.coopurl_page = QWidget()
        self.coopurl_page.setObjectName(u"coopurl_page")
        self.coopurl_page.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.gridLayout_8 = QGridLayout(self.coopurl_page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.searchbarHorintoallayout = QHBoxLayout()
        self.searchbarHorintoallayout.setObjectName(u"searchbarHorintoallayout")
        self.searchbarHorintoallayout.setContentsMargins(40, -1, 40, -1)
        self.coopurl_search_lineedit = QLineEdit(self.coopurl_page)
        self.coopurl_search_lineedit.setObjectName(u"coopurl_search_lineedit")
        self.coopurl_search_lineedit.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.coopurl_search_lineedit.setClearButtonEnabled(True)

        self.searchbarHorintoallayout.addWidget(self.coopurl_search_lineedit)

        self.coopurl_Search_button = QPushButton(self.coopurl_page)
        self.coopurl_Search_button.setObjectName(u"coopurl_Search_button")
        self.coopurl_Search_button.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: #00AEEF; /* Bootstrap's primary blue color */\n"
"\n"
"    border-radius: 5px;\n"
"    padding: 8px 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; /* Darker blue on hover */\n"
"    border-color: #0056b3; /* Darker blue border on hover */\n"
"}")
        icon21 = QIcon(QIcon.fromTheme(u"edit-find"))
        self.coopurl_Search_button.setIcon(icon21)

        self.searchbarHorintoallayout.addWidget(self.coopurl_Search_button)


        self.gridLayout_6.addLayout(self.searchbarHorintoallayout, 0, 0, 1, 1)

        self.coopurl_table = QTableWidget(self.coopurl_page)
        if (self.coopurl_table.columnCount() < 2):
            self.coopurl_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.coopurl_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.coopurl_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.coopurl_table.setObjectName(u"coopurl_table")

        self.gridLayout_6.addWidget(self.coopurl_table, 1, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.coopurl_page)

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

        self.stackedWidget.setCurrentIndex(1)
        self.michu_slider.setCurrentIndex(0)


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
        self.michu_slide_1.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_6.setText("")
        self.label_8.setText("")
        self.label_10.setText("")
        self.label_12.setText("")
        self.label_14.setText("")
        self.label_17.setText("")
        self.label_19.setText("")
        self.label_26.setText("")
        self.michu_Previous.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.michu_Next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.addprinter_button.setText(QCoreApplication.translate("MainWindow", u"Add Printers", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Subnet mask:", None))
        self.ethernet_alternative_DNS_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"IP Address:", None))
        self.ethernet_mac_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Default Gateway :", None))
        self.ethernet_Deafult_DNS.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.ethernet_speed_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Adapter:", None))
        self.ethernet_status.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Alternative DNS:", None))
        self.ethernet_defaultGateway_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.ethernet_adapter_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.ethernet_subnet_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.ethernet_ip_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ethernet IP info", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Network Status ", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Default DNS:", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"MAC  Address:", None))
        self.wifi_ip_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Speed:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u" Subnet mask:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u" IP Address:", None))
        self.wifi_default_dns_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u" Adapter:", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"MAC  Address:", None))
        self.wifi_speed_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.wifi_subnet_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Default Gateway :", None))
        self.wifi_adapter_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.wifi_MAC_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.wifi_defaultGate_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Wifi", None))
        self.wifi_alternat_DNS_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Default DNS:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Alternative DNS:", None))
        self.label_1256.setText(QCoreApplication.translate("MainWindow", u"Network Status ", None))
        self.wifi_status_label.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
        self.disk_type.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Partitions", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Manufacturer", None))
        self.disk_desc.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Media Type", None))
        self.disk_byte_sector.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.disk_model.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Bytes/Sector", None))
        self.disk_manu.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.disk_part.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.disk_size.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Disk", None))
        self.display_resolution.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Display ", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Bits/Pixel", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Driver Version", None))
        self.display_bit_pixel.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.display_type.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.display_name.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Adapter Description", None))
        self.display_driver_version.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.display_desc.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.display_ram.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Adapter Type", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Adapter RAM", None))
        self.back_home_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.taskmanager_button.setText(QCoreApplication.translate("MainWindow", u"Task Manager ", None))
        self.sysprocessor_manu.setText("")
        self.sys_processor_name.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Installed RAM", None))
        self.sys_processor_max_clock.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Processor Max Clock Speed", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Processor Manufacturer", None))
        self.sys_ram.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label7869.setText(QCoreApplication.translate("MainWindow", u"System Type", None))
        self.sys_processor_num_core.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label7865.setText(QCoreApplication.translate("MainWindow", u"Number of Logical Processors", None))
        self.label46547.setText(QCoreApplication.translate("MainWindow", u"System Name", None))
        self.sys_system_type.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.sys_processor_logical_num_core.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Processor Name", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"System Info", None))
        self.sys_os_name.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.sys_os_version.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"OS Manufacturer", None))
        self.sys_os_manu.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"OS Name", None))
        self.label5743.setText(QCoreApplication.translate("MainWindow", u"System Model", None))
        self.sys_system_manu.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label6854.setText(QCoreApplication.translate("MainWindow", u"System Manufacturer\"", None))
        self.sys_system_model.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pic42524.setText(QCoreApplication.translate("MainWindow", u"Number of Cores", None))
        self.sys_system_name.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.cpu_ram_free_used_ratio.setText(QCoreApplication.translate("MainWindow", u"Loading...", None))
        self.label_124.setText("")
        self.label65746.setText("")
        self.cpu_frequency_label.setText(QCoreApplication.translate("MainWindow", u"Loading...", None))
        self.coopurl_search_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search URLS", None))
        self.coopurl_Search_button.setText("")
        ___qtablewidgetitem = self.coopurl_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Site Name", None));
        ___qtablewidgetitem1 = self.coopurl_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"URL", None));
    # retranslateUi

