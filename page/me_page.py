import time

import allure
from selenium.webdriver.common.by import By

from BASE.base_action import BaseAction


class MePage(BaseAction):
    # 定位昵称
    nick_name_text_view = By.ID, "com.yunmall.lc:id/tv_user_nikename"
    # 定位设置按钮
    setting_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
    # 定位 加入超级VIP 按钮
    be_vip_button = By.XPATH, "//*[@text='加入超级VIP']"



    # 获取昵称
    @allure.step(title='获取昵称')
    def get_nick_name_text(self):
        return self.find_element(self.nick_name_text_view).text

    # 点击设置
    @allure.step(title='点击设置')
    def click_setting(self):
        self.find_element_with_scroll(self.setting_button).click()

    # 点击 加入超级VIP
    @allure.step(title='点击 加入超级VIP')
    def click_be_vip(self):
        self.find_element_with_scroll(self.be_vip_button).click()
        time.sleep(10)