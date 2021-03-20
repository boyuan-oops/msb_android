#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

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
        # caps["noReset"] = True
        # caps["autoGrantPermissions"] = "true"
        caps['settings[waitForIdleTimeout]'] = 0 # 缩短动态页面的等待时间
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_msb(self):
        print(self.driver.page_source)
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'权限')]/..//*[@text='允许']").click()
        # time.sleep(1)
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'权限')]/..//*[@text='允许']").click()
        # time.sleep(1)
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'权限')]/..//*[@text='允许']").click()
        # time.sleep(1)
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'权限')]/..//*[@text='允许']").click()
        # time.sleep(1)
        # self.driver.find_element(MobileBy.ID, "com.meishubao.client:id/tv_jump1").click()
        # time.sleep(1)
        #
        # el1 = self.driver.find_element(MobileBy.XPATH, "//*[@content-desc='已点评']")
        # el1.click()
        # time.sleep(3)
        # el2 = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.view.ViewGroup'][2]")
        # el2.click()
        # time.sleep(3)
        # el3 = self.driver.find_element(MobileBy.ID,"com.meishubao.client:id/iv_title_back")
        # el3.click()
        #Appium滚动查找：
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("打卡").instance(0));').click()