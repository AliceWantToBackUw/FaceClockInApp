import random

from PySide2.QtWidgets import QApplication, QWidget

from clock_in_app.adInforWidgetUI import AdInforWidgetUI
from clock_in_app.eeInforWidgetUI import EeInforWidgetUI
from clock_in_app.initAllUI import InitAllUI
from clock_in_app.all_ui.ui_loginWidget import Ui_LoginWidget


class LoginWidgetUI(QWidget):
    def display_page_2(self):
        print('换页面')
        self.ui.loginStackWidget.setCurrentIndex(1)

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_LoginWidget()
        # 初始化界面
        self.ui.setupUi(self)
        self.ui.loginStackWidget.setCurrentIndex(0)
        # 初始化功能
        self.ui.btn_clock_in.clicked.connect(self.display_page_2)
        self.ui.btn_clock_in.clicked.connect(self.function_identify_face)

    # 人脸识别功能函数
    def function_identify_face(self):
        print('正在执行人脸识别')
        # 如果人脸识别出是管理员，返回值为1
        # 如果识别出是员工，放回值为0
        temp = random.randint(1, 11)
        if temp % 2:
            self.hide()
            InitAllUI.adInforWidget = AdInforWidgetUI()
            InitAllUI.adInforWidget.show()
            print('ad,login隐藏')
        else:
            # self.display_page_ee_infor()
            self.hide()
            InitAllUI.eeInforWidget = EeInforWidgetUI()
            InitAllUI.eeInforWidget.show()
            print('login隐藏')


if __name__ == '__main__':
    app = QApplication([])
    InitAllUI.loginWidget = LoginWidgetUI()
    InitAllUI.loginWidget.show()
    app.exec_()
