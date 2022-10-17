from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget

from clock_in_app.adManageWidgetUI import AdManageWidgetUI
from clock_in_app.all_ui.ui_adInforWidget import Ui_AdInforWidget
from clock_in_app.initAllUI import InitAllUI


class AdInforWidgetUI(QWidget):
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_AdInforWidget()
        # 初始化界面
        self.ui.setupUi(self)
        self.ui.btn_back_ad.clicked.connect(self.display_loginWidget)
        self.ui.btn_manage_ad.clicked.connect(self.display_adManageWidget)
        # 加载数据
        self.init_page_Ad_data()

    # 进入人员管理页面
    def display_adManageWidget(self):
        print('进入人员管理页面')
        InitAllUI.adManageWidget = AdManageWidgetUI()
        InitAllUI.adManageWidget.show()
        self.close()

    def display_loginWidget(self):
        print('返回打卡页面')
        self.display_page()
        InitAllUI.loginWidget.show()
        self.close()

    def display_page(self):
        print('换第一面')
        InitAllUI.loginWidget.ui.loginStackWidget.setCurrentIndex(0)

    def get_page_Ad_data(self):
        ad_photo = r'D:\ALL_Project\PythonAllProject\Punch-in_Software\jietu.png'
        ad_name = '涂管理'
        ad_id = '456'
        ad_time = '2022.10.16'
        return ad_photo, ad_name, ad_id, ad_time

    # 加载page_Ad界面的数据
    def init_page_Ad_data(self):
        # 向数据库索要数据
        self.ad_photo, self.ad_name, self.ad_id, self.ad_time = self.get_page_Ad_data()
        # 加载个人图片
        pixmap = QPixmap(self.ad_photo)
        self.ui.ad_photo.setPixmap(pixmap)
        # 加载基本信息
        self.ui.label_name_value_ad.setText(self.ad_name)
        self.ui.label_id_value_ad.setText(self.ad_id)
        self.ui.label_time_value_ad.setText(self.ad_time)
