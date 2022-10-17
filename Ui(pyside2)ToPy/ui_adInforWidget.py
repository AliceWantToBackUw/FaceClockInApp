# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adInforWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AdInforWidget(object):
    def setupUi(self, AdInforWidget):
        if not AdInforWidget.objectName():
            AdInforWidget.setObjectName(u"AdInforWidget")
        AdInforWidget.resize(388, 615)
        self.gridLayout = QGridLayout(AdInforWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_ad_photo = QWidget(AdInforWidget)
        self.widget_ad_photo.setObjectName(u"widget_ad_photo")
        self.gridLayout_2 = QGridLayout(self.widget_ad_photo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ad_photo = QLabel(self.widget_ad_photo)
        self.ad_photo.setObjectName(u"ad_photo")
        self.ad_photo.setMinimumSize(QSize(182, 273))
        self.ad_photo.setMaximumSize(QSize(182, 273))

        self.gridLayout_2.addWidget(self.ad_photo, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_ad_photo, 0, 0, 1, 1)

        self.groupBox_ad_infor = QGroupBox(AdInforWidget)
        self.groupBox_ad_infor.setObjectName(u"groupBox_ad_infor")
        self.groupBox_ad_infor.setMaximumSize(QSize(16777215, 366))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_ad_infor)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_name_ad = QWidget(self.groupBox_ad_infor)
        self.widget_name_ad.setObjectName(u"widget_name_ad")
        self.widget_name_ad.setMaximumSize(QSize(16777215, 107))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_name_ad)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_name_ad = QLabel(self.widget_name_ad)
        self.label_name_ad.setObjectName(u"label_name_ad")
        self.label_name_ad.setMinimumSize(QSize(75, 0))
        self.label_name_ad.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_5.addWidget(self.label_name_ad)

        self.horizontalSpacer_6 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.label_name_value_ad = QLabel(self.widget_name_ad)
        self.label_name_value_ad.setObjectName(u"label_name_value_ad")
        self.label_name_value_ad.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.label_name_value_ad)


        self.verticalLayout_6.addWidget(self.widget_name_ad)

        self.widget_id_ad = QWidget(self.groupBox_ad_infor)
        self.widget_id_ad.setObjectName(u"widget_id_ad")
        self.widget_id_ad.setMaximumSize(QSize(16777215, 107))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_id_ad)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_id_ad = QLabel(self.widget_id_ad)
        self.label_id_ad.setObjectName(u"label_id_ad")
        self.label_id_ad.setMinimumSize(QSize(75, 0))
        self.label_id_ad.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_6.addWidget(self.label_id_ad)

        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.label_id_value_ad = QLabel(self.widget_id_ad)
        self.label_id_value_ad.setObjectName(u"label_id_value_ad")
        self.label_id_value_ad.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_6.addWidget(self.label_id_value_ad)


        self.verticalLayout_6.addWidget(self.widget_id_ad)

        self.widget_time_ad = QWidget(self.groupBox_ad_infor)
        self.widget_time_ad.setObjectName(u"widget_time_ad")
        self.widget_time_ad.setMaximumSize(QSize(16777215, 107))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_time_ad)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_time_ad = QLabel(self.widget_time_ad)
        self.label_time_ad.setObjectName(u"label_time_ad")
        self.label_time_ad.setMinimumSize(QSize(75, 0))
        self.label_time_ad.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_7.addWidget(self.label_time_ad)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.label_time_value_ad = QLabel(self.widget_time_ad)
        self.label_time_value_ad.setObjectName(u"label_time_value_ad")
        self.label_time_value_ad.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_7.addWidget(self.label_time_value_ad)


        self.verticalLayout_6.addWidget(self.widget_time_ad)


        self.gridLayout.addWidget(self.groupBox_ad_infor, 1, 0, 1, 1)

        self.btn_manage_ad = QPushButton(AdInforWidget)
        self.btn_manage_ad.setObjectName(u"btn_manage_ad")

        self.gridLayout.addWidget(self.btn_manage_ad, 2, 0, 1, 1)

        self.btn_back_ad = QPushButton(AdInforWidget)
        self.btn_back_ad.setObjectName(u"btn_back_ad")

        self.gridLayout.addWidget(self.btn_back_ad, 3, 0, 1, 1)


        self.retranslateUi(AdInforWidget)

        QMetaObject.connectSlotsByName(AdInforWidget)
    # setupUi

    def retranslateUi(self, AdInforWidget):
        AdInforWidget.setWindowTitle(QCoreApplication.translate("AdInforWidget", u"\u7ba1\u7406\u5458\u4fe1\u606f", None))
        self.ad_photo.setText(QCoreApplication.translate("AdInforWidget", u"\u7167\u7247", None))
        self.groupBox_ad_infor.setTitle(QCoreApplication.translate("AdInforWidget", u"\u57fa\u672c\u4fe1\u606f", None))
        self.label_name_ad.setText(QCoreApplication.translate("AdInforWidget", u"\u59d3    \u540d:", None))
        self.label_name_value_ad.setText(QCoreApplication.translate("AdInforWidget", u"\u59d3\u540d\u503c", None))
        self.label_id_ad.setText(QCoreApplication.translate("AdInforWidget", u"\u7ba1\u7406\u5458id:", None))
        self.label_id_value_ad.setText(QCoreApplication.translate("AdInforWidget", u"id\u503c", None))
        self.label_time_ad.setText(QCoreApplication.translate("AdInforWidget", u"\u6253\u5361\u65f6\u95f4\uff1a", None))
        self.label_time_value_ad.setText(QCoreApplication.translate("AdInforWidget", u"\u6253\u5361\u65f6\u95f4\u503c", None))
        self.btn_manage_ad.setText(QCoreApplication.translate("AdInforWidget", u"\u7ba1\u7406\u4eba\u5458", None))
        self.btn_back_ad.setText(QCoreApplication.translate("AdInforWidget", u"\u5b8c\u6210", None))
    # retranslateUi

