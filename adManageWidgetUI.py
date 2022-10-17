from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QTableWidgetItem
# from faker.contrib.pytest.plugin import faker
from pandas import DataFrame, isnull

from clock_in_app.all_ui.ui_adManageWidget import Ui_AdManageWidget
from clock_in_app.initAllUI import InitAllUI

import pandas as pd


class AdManageWidgetUI(QWidget):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_AdManageWidget()
        # 初始化界面
        self.ui.setupUi(self)
        self.ui.sw_manage.setCurrentIndex(0)
        # 初始化数据
        self.df = None
        # 初始化功能
        # page1
        self.ui.btn_ad_condition.clicked.connect(self.display_page)
        self.ui.btn_ee_infor.clicked.connect(self.display_page_2)
        self.ui.btn_condition_back.clicked.connect(self.display_loginWidget)
        self.ui.btn_select_infor.clicked.connect(self.select_condiction)
        self.ui.btn_infor_tocsv.clicked.connect(self.toCSV_condiction)
        self.init_page1_tabel()

        # page2
        self.ui.btn_back.clicked.connect(self.display_loginWidget)
        self.ui.btn_select.clicked.connect(self.select_infor)
        self.ui.btn_delete.clicked.connect(self.delete_infor)
        self.ui.btn_add.clicked.connect(self.add_infor)
        self.ui.btn_condition_tocsv.clicked.connect(self.ee_infor_tocsv)

    # 页面1的功能函数
    # 查询功能，查看打卡情况
    def select_condiction(self):
        print('正在查询')
        pass

    # 导出打卡情况csv文件功能
    def toCSV_condiction(self):
        print('正在导出csv文件')
        pass

    def init_page1_tabel(self):
        # 初始化清空表格的信息
        self.ui.tw_infor.clearContents()
        self.ui.tw_infor.setRowCount(0)
        self.items = 0
        self.te_data = []

        for index in range(1, 10):
            self.te_data.append({
                "id": '1',
                "姓名": '2',
                "打卡时间": '3:',
            })

        self.df = pd.DataFrame(self.te_data)
        print('-----------------')
        self.ui.tw_infor.setColumnCount(len(self.te_data[0].keys()))
        self.ui.tw_infor.setHorizontalHeaderLabels(self.te_data[0].keys())

        self.fillConditionTable()

    def fillConditionTable(self):
        for tempData in self.te_data:
            id_item = QTableWidgetItem(tempData['id'])
            name_item = QTableWidgetItem(tempData['姓名'])
            time_item = QTableWidgetItem(tempData['打卡时间'])
            # price_item.setTextAlignment(Qt.AlignRight)
            self.ui.tw_infor.insertRow(self.items)
            self.ui.tw_infor.setItem(self.items, 0, id_item)
            self.ui.tw_infor.setItem(self.items, 1, name_item)
            self.ui.tw_infor.setItem(self.items, 2, time_item)
            self.items += 1

    # def setDfData(self):
    #     # self.df = df
    #     # 先计算 后预览
    #     self.calculateRowCountParams()
    #     self.pdToQTableWidget()
    #
    # def calculateRowCountParams(self):
    #     if any(self.df):
    #         # 先计算
    #         rowHeight = self.ui.tw_infor.rowHeight(0)
    #         rowHeight = 30 if rowHeight == 0 else rowHeight
    #         tableHeight = self.ui.tw_infor.height()
    #         self.rowCount = int(tableHeight / rowHeight) - 1
    #         # print("每页行数", self.rowCount, sep=":")
    #         # 更新table的行数
    #         self.ui.tw_infor.setRowCount(self.rowCount)
    #         # 滑块的长度
    #         scrollbar_count = int(self.df.index.size / self.rowCount)
    #         # print("滑块长度", scrollbar_count, sep=":")
    #         self.scrollbar.setMaximum(scrollbar_count * 9)
    #
    # def pdToQTableWidget(self):
    #     if any(self.df):
    #         df_columns = self.df.columns.size
    #         df_header = self.df.columns.values.tolist()
    #         self.ui.tw_infor.setColumnCount(df_columns)
    #         self.ui.tw_infor.setHorizontalHeaderLabels(df_header)
    #
    #         start_row = int(self.scrollbar.value() / 9 * self.rowCount)
    #         end_row = int((self.scrollbar.value() / 9 + 1) * self.rowCount)
    #         # 数据预览窗口
    #         for row in range(start_row, end_row):
    #             for column in range(df_columns):
    #                 value = ''
    #                 if row < self.df.index.size:
    #                     value = '' if isnull(self.df.iloc[row, column]) else str(self.df.iloc[row, column])
    #                 tempItem = QTableWidgetItem(value)
    #                 self.ui.tw_infor.setItem((row - start_row), column, tempItem)
    #                 self.ui.tw_infor.item((row - start_row), column).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    # 回到打卡界面
    def display_loginWidget(self):
        print('返回打卡页面的第一面')
        InitAllUI.loginWidget.ui.loginStackWidget.setCurrentIndex(0)
        InitAllUI.loginWidget.show()
        self.close()

    # 页面2的功能设计
    def select_infor(self):
        print('进行页面2的界设计')

    def delete_infor(self):
        print('进行页面2的数据删除')

    def ee_infor_tocsv(self):
        print('进行页面2的导出csv文件')

    def add_infor(self):
        print('进行页面2的新增员工')

    # 展示页面
    def display_page(self):
        print('换到第一面')
        self.ui.sw_manage.setCurrentIndex(0)

    def display_page_2(self):
        print('换到第二面')
        self.ui.sw_manage.setCurrentIndex(1)
