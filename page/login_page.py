import allure
from selenium.webdriver.common.by import By

from BASE.base_action import BaseAction


class LoginPage(BaseAction):
    # 定位用户名
    username_edit_text = By.ID, "com.yunmall.lc:id/logon_account_textview"
    # 定位密码框
    password_edit_text = By.ID, "com.yunmall.lc:id/logon_password_textview"
    # 定位登录按钮
    login_button = By.ID, "com.yunmall.lc:id/logon_button"

    # 输入用户名
    @allure.step(title='输入用户名')
    def input_username(self,text):
        self.input(self.username_edit_text,text)

    # 输入密码
    @allure.step(title='输入密码')
    def input_password(self, text):
        self.input(self.password_edit_text, text)

    # 点击登录
    @allure.step(title='点击登录')
    def click_login(self):
        self.click(self.login_button)