#!/usr/bin/python
#-*- coding:utf-8 -*-

import xlrd
import requests
import unittest
from jiekou_kuang.report import HTMLTestRunner


def shuju():
    shuju=[]
    f=xlrd.open_workbook('b.xlsx')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        a=sheet.row_values(i)
        shuju.append(a)
        return shuju
class qwe(unittest.TestCase):
    shuju=shuju()
    def xuexiao(self,address):

        url = "http://testsupport-be.haofenshu.com/v1/schools/infos"

        querystring = {"filterInput":"%s"}%(address)

        headers = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cache-Control': "max-age=0",
        'Connection': "keep-alive",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Postman-Token': "d037c64a-db46-485c-859a-9df6bb0ed285"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        res = response.json()
        return res

    def test_1(self):
        aa = self.xuexiao(int(self.shuju[0][0]))
        self.assertEqual(aa['code'], 0)

    def test_2(self):
        for i in range(1, len(self.shuju)):
            bb = self.xuexiao(int(sheet.cell(a[i], a[0]).value))
            self.assertNotEqual(bb['code'], 0)
if __name__ == '__main__':

    suit = unittest.TestSuite()     #创建测试套件
    suit.addTest(qwe('test_1'))
    suit.addTest(qwe('test_2'))     #将测试用力添加到测试套件里（单个添加）

    # suit.addTest(unittest.makeSuite(qwe))   #将qwe类中所有以test开头的函数都添加到测试套件中
    f=open('ab.html','wb')        #打开一个空文件
    runner= HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='薛', description='结果如下')   #定义测试报告信息
    runner.run(suit)
    f.close()