# -*- coding: utf-8 -*-
# @Time    : 2021/9/2 18:43
# @Author  : CuiShuangqi
# @Email   : 1159533975@qq.com
# @File    : unitTest.py
import unittest


class T(unittest.TestCase):

    def setUp(self):
        print("setUp=============")

    def tearDown(self):
        print("tearDown=============")

    @classmethod
    def setUpClass(cls) -> None:
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    @classmethod
    def tearDownClass(cls) -> None:
        print("BBBBBBBBBBBBBBBBBBBBBBBBBBBB")

    def test01_aaa(self):
        print("test01_aaa")

    def test01_bbb(self):
        print("test01_bbb")


if __name__ == '__main__':
    unittest.main()
