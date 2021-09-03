# -*- coding: utf-8 -*-
# @Time    : 2021/9/2 15:44
# @Author  : CuiShuangqi
# @Email   : 1159533975@qq.com
# @File    : pytestParaTest.py

import pytest
from selenium import webdriver
from time import sleep

"""
    pytest 参数化
    当一组测试用例有固定的测试数据时，就可以通过参数化的方式简化测试用例的编写
    通过pytest.mark.parametrzie()方法设置参数：
    参数名："search_key,expected"
    参数值：通过数组定义参数值时，每一个元组都是一条测试用例的测试数据
    ids参数：默认None，用来重新定义测试用例的名称
"""


# 百度搜索案例
# 参数化
@pytest.mark.parametrize(
    "search_key,expected",
    [
        ("哈哈哈", "哈哈哈_百度搜索"),
        ("呵呵呵", "呵呵呵_百度不想搜索"),
    ],
    ids=["case1", "case2"]
)
def test_baidu_search(search_key, expected):
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.implicitly_wait(10)
    driver.find_element_by_id("kw").send_keys(search_key)
    driver.find_element_by_id("su").click()
    sleep(3)
    # == 断言
    # 窗口的 title判断
    web_title = driver.title
    assert expected == web_title
    driver.quit()
    print("driver已退出！")


if __name__ == '__main__':
    pytest.main(["-s", "pytestParaTest.py"])