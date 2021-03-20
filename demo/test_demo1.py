#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import datetime
from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestMsb:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0.1"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.meishubao.client"
        caps["appActivity"] = ".activity.SplashActivity"
        caps["noReset"] = True
        caps['settings[waitForIdleTimeout]'] = 0  # 缩短动态页面的等待时间

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_msb(self):
        dick = datetime.datetime.now()
        print(dick)
        sleep(5)
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='圈子']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.meishubao.client:id/tabs']//*[contains(@content-desc,'关注')]").click()
        self.driver.find_element(MobileBy.ID, "com.meishubao.client:id/main_post_iv").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.TextView' and @text='聊一聊']").click()
        self.driver.find_element(MobileBy.ID, "com.meishubao.client:id/input").send_keys(f"测试发个聊一聊{dick}")
        self.driver.find_element(MobileBy.ID, "com.meishubao.client:id/rightTv").click()
        sleep(2)
        self.driver.find_element(MobileBy.ID, "com.meishubao.client:id/main_tab_tv_3").click()
        sleep(2)
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "我发布的").click()
        sleep(3)
        questext = self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.meishubao.client:id/recycler_view']/android.widget.LinearLayout[1]//*[@resource-id='com.meishubao.client:id/questtext']").text
        assert f"测试发个聊一聊{dick}" in questext