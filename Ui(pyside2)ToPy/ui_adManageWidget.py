# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adManageWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AdManageWidget(object):
    def setupUi(self, AdManageWidget):
        if not AdManageWidget.objectName():
            AdManageWidget.setObjectName(u"AdManageWidget")
        AdManageWidget.resize(1317, 650)
        self.verticalLayout = QVBoxLayout(AdManageWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(AdManageWidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_ad_condition = QPushButton(self.widget)
        self.btn_ad_condition.setObjectName(u"btn_ad_condition")

        self.horizontalLayout.addWidget(self.btn_ad_condition)

        self.btn_ee_infor = QPushButton(self.widget)
        self.btn_ee_infor.setObjectName(u"btn_ee_infor")

        self.horizontalLayout.addWidget(self.btn_ee_infor)

        self.verticalLayout.addWidget(self.widget)

        self.sw_manage = QStackedWidget(AdManageWidget)
        self.sw_manage.setObjectName(u"sw_manage")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sw_manage.sizePolicy().hasHeightForWidth())
        self.sw_manage.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.tw_infor = QTableWidget(self.page)
        if (self.tw_infor.columnCount() < 3):
            self.tw_infor.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_infor.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_infor.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_infor.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tw_infor.rowCount() < 3):
            self.tw_infor.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_infor.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_infor.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_infor.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_infor.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_infor.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_infor.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_infor.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tw_infor.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tw_infor.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tw_infor.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tw_infor.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tw_infor.setItem(2, 2, __qtablewidgetitem14)
        self.tw_infor.setObjectName(u"tw_infor")
        self.tw_infor.setGeometry(QRect(10, 10, 801, 551))
        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(820, 0, 481, 141))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_start = QLabel(self.groupBox)
        self.lb_start.setObjectName(u"lb_start")

        self.gridLayout.addWidget(self.lb_start, 0, 0, 1, 1)

        self.te_start = QTimeEdit(self.groupBox)
        self.te_start.setObjectName(u"te_start")

        self.gridLayout.addWidget(self.te_start, 0, 1, 1, 1)

        self.lb_end = QLabel(self.groupBox)
        self.lb_end.setObjectName(u"lb_end")

        self.gridLayout.addWidget(self.lb_end, 0, 2, 1, 1)

        self.te_end = QTimeEdit(self.groupBox)
        self.te_end.setObjectName(u"te_end")

        self.gridLayout.addWidget(self.te_end, 0, 3, 1, 1)

        self.btn_select_infor = QPushButton(self.groupBox)
        self.btn_select_infor.setObjectName(u"btn_select_infor")

        self.gridLayout.addWidget(self.btn_select_infor, 1, 0, 1, 2)

        self.btn_infor_tocsv = QPushButton(self.groupBox)
        self.btn_infor_tocsv.setObjectName(u"btn_infor_tocsv")

        self.gridLayout.addWidget(self.btn_infor_tocsv, 1, 2, 1, 2)

        self.btn_condition_back = QPushButton(self.groupBox)
        self.btn_condition_back.setObjectName(u"btn_condition_back")

        self.gridLayout.addWidget(self.btn_condition_back, 2, 0, 1, 4)

        self.sa_html = QScrollArea(self.page)
        self.sa_html.setObjectName(u"sa_html")
        self.sa_html.setGeometry(QRect(820, 140, 471, 411))
        self.sa_html.setWidgetResizable(True)
        self.sa_widget = QWidget()
        self.sa_widget.setObjectName(u"sa_widget")
        self.sa_widget.setGeometry(QRect(0, 0, 469, 409))
        self.sa_html.setWidget(self.sa_widget)
        self.sw_manage.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.btn_add = QPushButton(self.page_2)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(1060, 130, 171, 51))
        self.btn_select = QPushButton(self.page_2)
        self.btn_select.setObjectName(u"btn_select")
        self.btn_select.setGeometry(QRect(1060, 20, 171, 51))
        self.tw_condition = QTableWidget(self.page_2)
        if (self.tw_condition.columnCount() < 3):
            self.tw_condition.setColumnCount(3)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tw_condition.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tw_condition.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tw_condition.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        if (self.tw_condition.rowCount() < 2):
            self.tw_condition.setRowCount(2)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tw_condition.setVerticalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tw_condition.setVerticalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tw_condition.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tw_condition.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tw_condition.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tw_condition.setItem(1, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tw_condition.setItem(1, 1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tw_condition.setItem(1, 2, __qtablewidgetitem25)
        self.tw_condition.setObjectName(u"tw_condition")
        self.tw_condition.setGeometry(QRect(10, 20, 981, 521))
        self.btn_condition_tocsv = QPushButton(self.page_2)
        self.btn_condition_tocsv.setObjectName(u"btn_condition_tocsv")
        self.btn_condition_tocsv.setGeometry(QRect(1060, 370, 171, 51))
        self.btn_back = QPushButton(self.page_2)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(1060, 500, 171, 41))
        self.btn_delete = QPushButton(self.page_2)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(1060, 240, 171, 51))
        self.sw_manage.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.sw_manage)

        self.retranslateUi(AdManageWidget)

        self.sw_manage.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(AdManageWidget)

    # setupUi

    def retranslateUi(self, AdManageWidget):
        AdManageWidget.setWindowTitle(QCoreApplication.translate("AdManageWidget", u"\u4eba\u5458\u7ba1\u7406", None))
        self.btn_ad_condition.setText(QCoreApplication.translate("AdManageWidget", u"\u6253\u5361\u72b6\u6001", None))
        self.btn_ee_infor.setText(
            QCoreApplication.translate("AdManageWidget", u"\u4fee\u6539\u5458\u5de5\u4fe1\u606f", None))
        ___qtablewidgetitem = self.tw_infor.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AdManageWidget", u"id", None));
        ___qtablewidgetitem1 = self.tw_infor.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AdManageWidget", u"\u59d3\u540d", None));
        ___qtablewidgetitem2 = self.tw_infor.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AdManageWidget", u"\u6253\u5361\u65f6\u95f4", None));
        ___qtablewidgetitem3 = self.tw_infor.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AdManageWidget", u"1", None));
        ___qtablewidgetitem4 = self.tw_infor.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AdManageWidget", u"2", None));
        ___qtablewidgetitem5 = self.tw_infor.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AdManageWidget", u"3", None));

        __sortingEnabled = self.tw_infor.isSortingEnabled()
        self.tw_infor.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tw_infor.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AdManageWidget", u"2021215219", None));
        ___qtablewidgetitem7 = self.tw_infor.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AdManageWidget", u"\u6d82\u946b\u5e73", None));
        ___qtablewidgetitem8 = self.tw_infor.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("AdManageWidget", u"22:56", None));
        ___qtablewidgetitem9 = self.tw_infor.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("AdManageWidget", u"2021215218", None));
        ___qtablewidgetitem10 = self.tw_infor.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("AdManageWidget", u"tutu", None));
        ___qtablewidgetitem11 = self.tw_infor.item(1, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("AdManageWidget", u"22:59", None));
        ___qtablewidgetitem12 = self.tw_infor.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("AdManageWidget", u"2021215217", None));
        ___qtablewidgetitem13 = self.tw_infor.item(2, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("AdManageWidget", u"dada", None));
        ___qtablewidgetitem14 = self.tw_infor.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("AdManageWidget", u"\u672a\u6253\u5361", None));
        self.tw_infor.setSortingEnabled(__sortingEnabled)

        self.groupBox.setTitle(QCoreApplication.translate("AdManageWidget", u"GroupBox", None))
        self.lb_start.setText(QCoreApplication.translate("AdManageWidget", u"\u8d77\u59cb\u65f6\u95f4", None))
        self.lb_end.setText(QCoreApplication.translate("AdManageWidget", u"\u7ed3\u675f\u65f6\u95f4", None))
        self.btn_select_infor.setText(QCoreApplication.translate("AdManageWidget", u"\u67e5\u8be2", None))
        self.btn_infor_tocsv.setText(QCoreApplication.translate("AdManageWidget", u"\u5bfc\u51facsv\u6587\u4ef6", None))
        self.btn_condition_back.setText(QCoreApplication.translate("AdManageWidget", u"\u9000\u51fa", None))
        self.btn_add.setText(
            QCoreApplication.translate("AdManageWidget", u"\u65b0\u589e\u4eba\u5458\u4fe1\u606f", None))
        self.btn_select.setText(QCoreApplication.translate("AdManageWidget", u"\u67e5\u8be2\u5458\u5de5", None))
        ___qtablewidgetitem15 = self.tw_condition.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("AdManageWidget", u"id", None));
        ___qtablewidgetitem16 = self.tw_condition.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("AdManageWidget", u"\u5934\u50cf", None));
        ___qtablewidgetitem17 = self.tw_condition.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("AdManageWidget", u"\u59d3\u540d", None));
        ___qtablewidgetitem18 = self.tw_condition.verticalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("AdManageWidget", u"1", None));
        ___qtablewidgetitem19 = self.tw_condition.verticalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("AdManageWidget", u"2", None));

        __sortingEnabled1 = self.tw_condition.isSortingEnabled()
        self.tw_condition.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tw_condition.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("AdManageWidget", u"2021215219", None));
        ___qtablewidgetitem21 = self.tw_condition.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("AdManageWidget", u"zhaopian", None));
        ___qtablewidgetitem22 = self.tw_condition.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("AdManageWidget", u"\u6d82\u946b\u5e73", None));
        ___qtablewidgetitem23 = self.tw_condition.item(1, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("AdManageWidget", u"2021215218", None));
        ___qtablewidgetitem24 = self.tw_condition.item(1, 1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("AdManageWidget", u"zhaopian", None));
        ___qtablewidgetitem25 = self.tw_condition.item(1, 2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("AdManageWidget", u"tutu", None));
        self.tw_condition.setSortingEnabled(__sortingEnabled1)

        self.btn_condition_tocsv.setText(
            QCoreApplication.translate("AdManageWidget", u"\u5bfc\u51fa\u4e3acsv\u6587\u4ef6", None))
        self.btn_back.setText(QCoreApplication.translate("AdManageWidget", u"\u9000\u51fa", None))
        self.btn_delete.setText(
            QCoreApplication.translate("AdManageWidget", u"\u5220\u51cf\u4eba\u5458\u4fe1\u606f", None))
    # retranslateUi
