import allure
import time
from selenium.webdriver.common.by import By

from BASE.base_action import BaseAction


class HomePage(BaseAction):
    # 定位"我"
    me_button = By.ID, "com.yunmall.lc:id/tab_me"

    # 点击我
    def click_me(self):
        self.click(self.me_button)

    @allure.step(title='设置登录页面')
    def login_if_not(self,page):
        self.click_me()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return

        # 没有登录就去登陆
        # 点击已有账号
        page.register.click_login()

        # 输入用户名
        page.login.input_username("itheima_test")

        # 输入密码
        page.login.input_password("itheima")

        # 点击登录
        page.login.click_login()

        time.sleep(5)