# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget):
        if not LoginWidget.objectName():
            LoginWidget.setObjectName(u"LoginWidget")
        LoginWidget.resize(417, 672)
        self.horizontalLayout = QHBoxLayout(LoginWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.loginStackWidget = QStackedWidget(LoginWidget)
        self.loginStackWidget.setObjectName(u"loginStackWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_clock_in = QPushButton(self.page)
        self.btn_clock_in.setObjectName(u"btn_clock_in")

        self.verticalLayout.addWidget(self.btn_clock_in)

        self.loginStackWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_2 = QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_identify = QLabel(self.page_2)
        self.label_identify.setObjectName(u"label_identify")
        self.label_identify.setStyleSheet(u"background-color: rgb(255, 164, 99);")

        self.horizontalLayout_2.addWidget(self.label_identify)

        self.loginStackWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.loginStackWidget)

        self.retranslateUi(LoginWidget)

        self.loginStackWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(LoginWidget)

    # setupUi

    def retranslateUi(self, LoginWidget):
        LoginWidget.setWindowTitle(QCoreApplication.translate("LoginWidget", u"\u6253\u5361", None))
        self.btn_clock_in.setText(QCoreApplication.translate("LoginWidget", u"\u6253\u5361", None))
        self.label_identify.setText(QCoreApplication.translate("LoginWidget", u"\u4eba\u8138\u8bc6\u522b", None))
    # retranslateUi
