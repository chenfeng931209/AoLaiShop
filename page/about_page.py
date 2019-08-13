import allure
from selenium.webdriver.common.by import By

from BASE.base_action import BaseAction


class AboutPage(BaseAction):

    # 定位版本更新 按钮
    update_button = By.XPATH, "//*[@text='版本更新']"

    # 点击版本更新
    @allure.step(title='版本更新')
    def click_update(self):
        self.click(self.update_button)


