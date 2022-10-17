from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget

from clock_in_app.all_ui.ui_eeInforWidget import Ui_EeInforWidget
from clock_in_app.initAllUI import InitAllUI


class EeInforWidgetUI(QWidget):
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_EeInforWidget()
        # 初始化界面
        self.ui.setupUi(self)
        self.ui.btn_back_ee.clicked.connect(self.display_loginWidget)
        # 加载数据
        self.init_page_Ee_data()

    def display_loginWidget(self):
        print('返回打卡页面')
        self.display_page()
        InitAllUI.loginWidget.show()
        self.close()

    def display_page(self):
        print('换第一面')
        InitAllUI.loginWidget.ui.loginStackWidget.setCurrentIndex(0)

    # 索要数据
    def get_page_Ee_data(self):
        ee_photo = r'D:\ALL_Project\PythonAllProject\Punch-in_Software\jietu.png'
        ee_name = '涂'
        ee_id = '123'
        ee_time = '2022.10.16'
        return ee_photo, ee_name, ee_id, ee_time

    # 加载page_Ee界面的数据
    def init_page_Ee_data(self):
        # 向数据库索要数据
        self.ee_photo, self.ee_name, self.ee_id, self.ee_time = self.get_page_Ee_data()
        # 加载个人图片
        pixmap = QPixmap(self.ee_photo)
        self.ui.ee_photo.setPixmap(pixmap)
        # 加载基本信息
        self.ui.label_name_value_ee.setText(self.ee_name)
        self.ui.label_id_value_ee.setText(self.ee_id)
        self.ui.label_time_value_ee.setText(self.ee_time)
