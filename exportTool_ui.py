# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exportTool.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dbSettingsFrame = QFrame(self.centralwidget)
        self.dbSettingsFrame.setObjectName(u"dbSettingsFrame")
        self.dbSettingsFrame.setGeometry(QRect(30, 30, 431, 211))
        self.dbSettingsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.dbSettingsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.testConnectionPushButton = QPushButton(self.dbSettingsFrame)
        self.testConnectionPushButton.setObjectName(u"testConnectionPushButton")
        self.testConnectionPushButton.setGeometry(QRect(30, 170, 81, 24))
        self.testConnectionPushButton.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.layoutWidget = QWidget(self.dbSettingsFrame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 20, 381, 136))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.serverLabel = QLabel(self.layoutWidget)
        self.serverLabel.setObjectName(u"serverLabel")

        self.gridLayout.addWidget(self.serverLabel, 0, 0, 1, 1)

        self.serverLineEdit = QLineEdit(self.layoutWidget)
        self.serverLineEdit.setObjectName(u"serverLineEdit")

        self.gridLayout.addWidget(self.serverLineEdit, 0, 1, 1, 1)

        self.portLabel = QLabel(self.layoutWidget)
        self.portLabel.setObjectName(u"portLabel")

        self.gridLayout.addWidget(self.portLabel, 1, 0, 1, 1)

        self.portLineEdit = QLineEdit(self.layoutWidget)
        self.portLineEdit.setObjectName(u"portLineEdit")

        self.gridLayout.addWidget(self.portLineEdit, 1, 1, 1, 1)

        self.databaseLabel = QLabel(self.layoutWidget)
        self.databaseLabel.setObjectName(u"databaseLabel")

        self.gridLayout.addWidget(self.databaseLabel, 2, 0, 1, 1)

        self.databaseLineEdit = QLineEdit(self.layoutWidget)
        self.databaseLineEdit.setObjectName(u"databaseLineEdit")

        self.gridLayout.addWidget(self.databaseLineEdit, 2, 1, 1, 1)

        self.userNameLabel = QLabel(self.layoutWidget)
        self.userNameLabel.setObjectName(u"userNameLabel")

        self.gridLayout.addWidget(self.userNameLabel, 3, 0, 1, 1)

        self.userNameLineEdit = QLineEdit(self.layoutWidget)
        self.userNameLineEdit.setObjectName(u"userNameLineEdit")

        self.gridLayout.addWidget(self.userNameLineEdit, 3, 1, 1, 1)

        self.passwordLabel = QLabel(self.layoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.gridLayout.addWidget(self.passwordLabel, 4, 0, 1, 1)

        self.passwordLineEdit = QLineEdit(self.layoutWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.gridLayout.addWidget(self.passwordLineEdit, 4, 1, 1, 1)

        self.dbSettingsLabel = QLabel(self.centralwidget)
        self.dbSettingsLabel.setObjectName(u"dbSettingsLabel")
        self.dbSettingsLabel.setGeometry(QRect(30, 10, 171, 16))
        self.objectNameLabel = QLabel(self.centralwidget)
        self.objectNameLabel.setObjectName(u"objectNameLabel")
        self.objectNameLabel.setGeometry(QRect(210, 260, 101, 16))
        self.exportPushButton = QPushButton(self.centralwidget)
        self.exportPushButton.setObjectName(u"exportPushButton")
        self.exportPushButton.setGeometry(QRect(550, 210, 161, 51))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.exportPushButton.setFont(font)
        self.exportPushButton.setStyleSheet(u"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.previewTableWidget = QTableWidget(self.centralwidget)
        self.previewTableWidget.setObjectName(u"previewTableWidget")
        self.previewTableWidget.setGeometry(QRect(30, 330, 761, 211))
        self.previewLabel = QLabel(self.centralwidget)
        self.previewLabel.setObjectName(u"previewLabel")
        self.previewLabel.setGeometry(QRect(30, 310, 81, 16))
        self.objectTypeComboBox = QComboBox(self.centralwidget)
        self.objectTypeComboBox.setObjectName(u"objectTypeComboBox")
        self.objectTypeComboBox.setGeometry(QRect(30, 280, 161, 24))
        self.objectNameComboBox = QComboBox(self.centralwidget)
        self.objectNameComboBox.setObjectName(u"objectNameComboBox")
        self.objectNameComboBox.setGeometry(QRect(210, 280, 301, 24))
        self.objectTypeLabel = QLabel(self.centralwidget)
        self.objectTypeLabel.setObjectName(u"objectTypeLabel")
        self.objectTypeLabel.setGeometry(QRect(30, 260, 161, 16))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(470, 20, 151, 171))
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 70, 92, 20))
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(20, 30, 92, 20))
        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(20, 100, 92, 20))
        self.radioButton_4 = QRadioButton(self.groupBox)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(20, 130, 92, 20))
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 130, 31, 22))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(630, 20, 161, 171))
        self.radioButton_5 = QRadioButton(self.groupBox_2)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(10, 60, 131, 20))
        self.radioButton_6 = QRadioButton(self.groupBox_2)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(10, 90, 141, 20))
        self.radioButton_7 = QRadioButton(self.groupBox_2)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setGeometry(QRect(10, 30, 141, 20))
        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(60, 120, 31, 22))
        self.radioButton_8 = QRadioButton(self.groupBox_2)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setGeometry(QRect(10, 120, 92, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuOhje = QMenu(self.menubar)
        self.menuOhje.setObjectName(u"menuOhje")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOhje.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.testConnectionPushButton.setText(QCoreApplication.translate("MainWindow", u"Testaa yhteys", None))
        self.serverLabel.setText(QCoreApplication.translate("MainWindow", u"Palvelin", None))
        self.serverLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Palvelimen nimi tai IP-sosoite", None))
        self.portLabel.setText(QCoreApplication.translate("MainWindow", u"Portti", None))
        self.portLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TCP-portin numero, oletus 5432", None))
        self.databaseLabel.setText(QCoreApplication.translate("MainWindow", u"Tietokanta", None))
        self.databaseLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tietokannan nimi, hallintatietokanta postgres", None))
        self.userNameLabel.setText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4tunnus", None))
        self.userNameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4tunnus, oletusp\u00e4\u00e4k\u00e4ytt\u00e4j\u00e4 postgres", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Salasana", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4n salasana", None))
        self.dbSettingsLabel.setText(QCoreApplication.translate("MainWindow", u"Tietokantayhteyden asetukset", None))
        self.objectNameLabel.setText(QCoreApplication.translate("MainWindow", u"Objektin nimi", None))
        self.exportPushButton.setText(QCoreApplication.translate("MainWindow", u"Vie tiedostoon", None))
        self.previewLabel.setText(QCoreApplication.translate("MainWindow", u"Esikatselu", None))
        self.objectTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Objektin tyyppi", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sarake-erotin ", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"pilkku (,)", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"puolipiste (;)", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Sarkain", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Muu", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Tekstin tunniste", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"lainausmerkit (\")", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"Puolilainausmerkit (')", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"Ei mit\u00e4\u00e4n", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"Muu", None))
        self.menuOhje.setTitle(QCoreApplication.translate("MainWindow", u"Ohje", None))
    # retranslateUi

