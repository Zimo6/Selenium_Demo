# -*- coding: utf-8 -*-
# @Time    : 2021/9/2 15:31
# @Author  : CuiShuangqi
# @Email   : 1159533975@qq.com
# @File    : main.py
import os
import time
import pytest

if __name__ == '__main__':
    # 当前时间
    now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
    # allure 测试报告路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    report_path = os.path.join(cur_path, f'Report\\{now_time}')

    # -s : 打印信息
    # -m ：运行含标签的用例
    pytest.main(["-s", "-m", "baidu_search or test_demo", f"{cur_path}\\TestCase\\test_001_baiduSearch.py::TestBaiduSearch", "--alluredir", report_path])
    # 解析测试报告，执行: allure serve {report_path}
    os.system(f"allure serve {report_path}")