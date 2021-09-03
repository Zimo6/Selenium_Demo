# -*- coding: utf-8 -*-
# @Time    : 2021/9/1 19:37
# @Author  : CuiShuangqi
# @Email   : 1159533975@qq.com
# @File    : test_001_baiduSearch.py
import os
import time
import pytest
import allure
from time import sleep
from selenium import webdriver
from PageObject.baiduIndex import BaiduIndex

driver = webdriver.Chrome()
baidu_index = BaiduIndex(driver)


@pytest.fixture(scope="class")
def init():
    # 打开浏览器,访问登录页面
    baidu_index.logger.info("\nWebDriver 正在初始化...")
    driver.get(baidu_index.baidu_index_url)
    baidu_index.logger.info(f"打开链接: {baidu_index.baidu_index_url}...")
    # 窗口最大化
    driver.maximize_window()
    # 隐式等待
    driver.implicitly_wait(10)
    baidu_index.logger.info("WebDriver 初始化完成！")
    yield
    driver.quit()
    baidu_index.logger.info("WebDriver 成功退出...")


@allure.feature("百度搜索")
class TestBaiduSearch:

    @allure.story("搜索指定关键字")
    @pytest.mark.baidu_search
    @pytest.mark.parametrize("key_word", [
        "哈哈",
        "呵呵",
    ], )
    def test_search(self, init, key_word):
        # @pytest.mark.parametrize 参数化
        baidu_index.search_key(key_word)
        web_title = driver.title
        assert "哈哈_百度搜索" == web_title

    @allure.story("这是一个demo")
    @pytest.mark.test_demo
    def test_demo(self):
        assert 1 == 2


if __name__ == '__main__':
    # 当前时间
    now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
    # allure 测试报告路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    report_path = os.path.join(os.path.dirname(cur_path), f'Report\\{now_time}')

    # -s : 打印信息
    # -m ：运行含标签的用例
    pytest.main(["-s", "-m", "baidu_search or test_demo", "test_001_baiduSearch.py::TestBaiduSearch", "--alluredir",
                 report_path])
    # TODO 执行: allure serve ./Report 解析测试报告
    os.system(f"allure serve {report_path}")
    # 执行多个标签
    # pytest.main(["-s", "-m", "baidu_search or test_demo", "test_001_baiduSearch.py::TestBaiduSearch"])
