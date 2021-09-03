# -*- coding: utf-8 -*-
# @Time    : 2021/9/2 18:33
# @Author  : CuiShuangqi
# @Email   : 1159533975@qq.com
# @File    : test_Pytest_demo.py
import pytest


@pytest.fixture(scope="class")
def fun1():
    print("AAA=====================")
    yield
    print("BBB=====================")


def test_fun2(fun1):
    print("BBB")


def test_fun3():
    print("CCC")


if __name__ == '__main__':
    pytest.main(["-s", "test_Pytest_demo.py"])
