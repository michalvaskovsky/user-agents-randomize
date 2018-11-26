# -*- coding: utf-8 -*-
import time
import requests
import lxml.html
from random import randint

#
# get random Chrome user agent
class UserAgentRandomizer():
    def __init__(self):
        self.url = 'http://www.useragentstring.com/pages/useragentstring.php?name=Chrome'
        self.limit = 50
        self.retrymax = 5
        self.retrydelay = 2
        self.lst = self._getList()

    def _get(self):
        ret = requests.get(self.url)
        if ret.status_code != 200:
            raise Exception(
                'Status code {status} for url {url}\n{content}'.format(
                    status=ret.status_code, url=self.url, content=ret.text))
        return ret.text

    def _getWithRetry(self):
        for i in range(self.retrymax):
            try:
                return self._get()
            except Exception:
                time.sleep(self.retrydelay)

        raise Exception("ERROR. Failed to download list of user agents.")

    def _getList(self):
        data = self._getWithRetry()
        html = lxml.html.fromstring(data)
        elems = html.xpath('//*[@id="liste"]/ul/li/a')
        final = [elems[i].text for i in range(self.limit)]
        return final

    def getRandomUa(self):
        return self.lst[randint(0, len(self.lst))]

import unittest
class test_getuserAgent(unittest.TestCase):

    def test_1(self):
        u = UserAgentRandomizer()
        lst = u._getList()
        for e in lst:
            print e

    def test_2(self):
        u = UserAgentRandomizer()
        for i in range(10):
            print u.getRandomUa()









