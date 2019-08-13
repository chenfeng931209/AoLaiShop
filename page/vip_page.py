import allure
from selenium.webdriver.common.by import By

from BASE.base_action import BaseAction


class VipPage(BaseAction):
    # 邀请码输入框
    invite_edit_text = By.XPATH, "//*[@type='tel']"

    # 立即成为会员
    be_vip_button = By.XPATH, "//*[@value='立即成为会员']"

    @allure.step(title='输入邀请码')
    def input_invite(self,text):
        self.input(self.invite_edit_text,text)

    @allure.step(title='点击加入超级会员')
    def click_be_vip(self):
        self.click(self.be_vip_button)