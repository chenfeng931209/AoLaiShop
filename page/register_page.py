import allure
from selenium.webdriver.common.by import By

from BASE.base_action import BaseAction


class RegisterPage(BaseAction):
    # 定位已有账号去登陆
    login_button = By.XPATH,"//*[@text='已有账号，去登录']"

    # 点击 已有账号去登陆
    @allure.step(title='点击 已有账号去登陆')
    def click_login(self):
        self.click(self.login_button)

