# -*- coding: utf-8 -*-
# @Time    : 2021/9/2 11:20
# @Author  : CuiShuangqi
# @Email   : 1159533975@qq.com
# @File    : getDriverTest.py
from time import sleep

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(10)

result = driver.find_element_by_id("su").get_attribute("value")
print(result)

sleep(5)
driver.quit()