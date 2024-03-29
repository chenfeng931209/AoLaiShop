import time

import pytest

from BASE.base_analyze import analyze_file
from BASE.base_driver import init_driver
from page.page import Page


class TestVip:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()
    @pytest.mark.parametrize("args",analyze_file("vip_data.yaml","test_vip"))
    def test_vip(self,args):
        keyworw = args["keyword"]
        expect = args["expect"]

        # 如果没有登录,先登录
        self.page.home.login_if_not(self.page)
        # 我 -- 点击加入VIP
        self.page.me.click_be_vip()
        # 切换 web环境
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        # vip 输入 邀请码
        self.page.vip.input_invite(keyworw)
        # vip 点击 加入会员
        self.page.vip.click_be_vip()

        # 断言，"邀请码输入不正确" 是否在 page_source 中
        assert self.page.vip.is_keyword_in_page_source(expect), "%s不在page_source中" % expect

        self.driver.switch_to.context("NATIVE_APP")


