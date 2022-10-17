# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eeInforWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EeInforWidget(object):
    def setupUi(self, EeInforWidget):
        if not EeInforWidget.objectName():
            EeInforWidget.setObjectName(u"EeInforWidget")
        EeInforWidget.resize(426, 672)
        self.verticalLayout = QVBoxLayout(EeInforWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_ee_photo = QWidget(EeInforWidget)
        self.widget_ee_photo.setObjectName(u"widget_ee_photo")
        self.gridLayout_2 = QGridLayout(self.widget_ee_photo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ee_photo = QLabel(self.widget_ee_photo)
        self.ee_photo.setObjectName(u"ee_photo")
        self.ee_photo.setMinimumSize(QSize(182, 273))
        self.ee_photo.setMaximumSize(QSize(182, 273))

        self.gridLayout_2.addWidget(self.ee_photo, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_ee_photo)

        self.groupBox_ee_infor = QGroupBox(EeInforWidget)
        self.groupBox_ee_infor.setObjectName(u"groupBox_ee_infor")
        self.groupBox_ee_infor.setMaximumSize(QSize(16777215, 366))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_ee_infor)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_name_ee = QWidget(self.groupBox_ee_infor)
        self.widget_name_ee.setObjectName(u"widget_name_ee")
        self.widget_name_ee.setMaximumSize(QSize(16777215, 107))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_name_ee)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_name_ee = QLabel(self.widget_name_ee)
        self.label_name_ee.setObjectName(u"label_name_ee")
        self.label_name_ee.setMinimumSize(QSize(75, 0))
        self.label_name_ee.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_2.addWidget(self.label_name_ee)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_name_value_ee = QLabel(self.widget_name_ee)
        self.label_name_value_ee.setObjectName(u"label_name_value_ee")
        self.label_name_value_ee.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.label_name_value_ee)


        self.verticalLayout_2.addWidget(self.widget_name_ee)

        self.widget_id_ee = QWidget(self.groupBox_ee_infor)
        self.widget_id_ee.setObjectName(u"widget_id_ee")
        self.widget_id_ee.setMaximumSize(QSize(16777215, 107))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_id_ee)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_id_ee = QLabel(self.widget_id_ee)
        self.label_id_ee.setObjectName(u"label_id_ee")
        self.label_id_ee.setMinimumSize(QSize(75, 0))
        self.label_id_ee.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_3.addWidget(self.label_id_ee)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_id_value_ee = QLabel(self.widget_id_ee)
        self.label_id_value_ee.setObjectName(u"label_id_value_ee")
        self.label_id_value_ee.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_3.addWidget(self.label_id_value_ee)


        self.verticalLayout_2.addWidget(self.widget_id_ee)

        self.widget_time_ee = QWidget(self.groupBox_ee_infor)
        self.widget_time_ee.setObjectName(u"widget_time_ee")
        self.widget_time_ee.setMaximumSize(QSize(16777215, 107))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_time_ee)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_time_ee = QLabel(self.widget_time_ee)
        self.label_time_ee.setObjectName(u"label_time_ee")
        self.label_time_ee.setMinimumSize(QSize(75, 0))
        self.label_time_ee.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_4.addWidget(self.label_time_ee)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.label_time_value_ee = QLabel(self.widget_time_ee)
        self.label_time_value_ee.setObjectName(u"label_time_value_ee")
        self.label_time_value_ee.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.label_time_value_ee)


        self.verticalLayout_2.addWidget(self.widget_time_ee)


        self.verticalLayout.addWidget(self.groupBox_ee_infor)

        self.btn_back_ee = QPushButton(EeInforWidget)
        self.btn_back_ee.setObjectName(u"btn_back_ee")

        self.verticalLayout.addWidget(self.btn_back_ee)


        self.retranslateUi(EeInforWidget)

        QMetaObject.connectSlotsByName(EeInforWidget)
    # setupUi

    def retranslateUi(self, EeInforWidget):
        EeInforWidget.setWindowTitle(QCoreApplication.translate("EeInforWidget", u"\u5458\u5de5\u4fe1\u606f", None))
        self.ee_photo.setText(QCoreApplication.translate("EeInforWidget", u"\u7167\u7247", None))
        self.groupBox_ee_infor.setTitle(QCoreApplication.translate("EeInforWidget", u"\u57fa\u672c\u4fe1\u606f", None))
        self.label_name_ee.setText(QCoreApplication.translate("EeInforWidget", u"\u59d3    \u540d:", None))
        self.label_name_value_ee.setText(QCoreApplication.translate("EeInforWidget", u"\u59d3\u540d\u503c", None))
        self.label_id_ee.setText(QCoreApplication.translate("EeInforWidget", u"\u5458 \u5de5 id:", None))
        self.label_id_value_ee.setText(QCoreApplication.translate("EeInforWidget", u"id\u503c", None))
        self.label_time_ee.setText(QCoreApplication.translate("EeInforWidget", u"\u6253\u5361\u65f6\u95f4\uff1a", None))
        self.label_time_value_ee.setText(QCoreApplication.translate("EeInforWidget", u"\u6253\u5361\u65f6\u95f4\u503c", None))
        self.btn_back_ee.setText(QCoreApplication.translate("EeInforWidget", u"\u5b8c\u6210", None))
    # retranslateUi

