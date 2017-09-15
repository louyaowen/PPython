# -*- coding:utf-8 -*-

import threading
import io, sys

from wsgiref.simple_server import make_server
from my_web import application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class hello(object):

    def sum(self, a, b):
         return a + b

    @staticmethod
    def classSum(a, b):
        print('类方法')
        return a + b
    
    def good(self):
        print('实例方法')
    
    def __luck(self):
        print('私有方法')


def normalize(name):
    return str(name).capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def loop():
    x = 8800
    for i in range(10):
        x += x*0.06
        print('人均GDP %.2f'%x,'美元')
    
def loop2(x,y):
    x += x*0.06
    y -= 1
    print('人均GDP %.2f'%x,'美元')
    if y != 0:
        loop2(x,y)

loop2(8800,10)
loop()