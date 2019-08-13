import allure
from selenium.webdriver.common.by import By

from BASE.base_action import BaseAction


class SettingPage(BaseAction):
    # 定位关于百年奥莱  按钮
    about_button = By.XPATH, "//*[@text='关于百年奥莱']"

    # 定位清理缓存  按钮
    clear_cacha_button = By.XPATH, "//*[@text='清理缓存']"

    # 定位清理缓存  按钮
    address_list_button = By.XPATH, "//*[@text='地址管理']"


    # 点击关于百年奥莱  按钮
    @allure.step(title='点击关于百年奥莱  按钮')
    def click_about(self):
        self.find_element_with_scroll(self.about_button).click()


 # 点击清理缓存  按钮
    @allure.step(title='点击清理缓存  按钮')
    def click_clear_cacha(self):
        self.find_element_with_scroll(self.clear_cacha_button).click()


# 点击地址管理 按钮
    @allure.step(title='点击地址管理  按钮')
    def click_address_list(self):
        self.find_element_with_scroll(self.address_list_button).click()




