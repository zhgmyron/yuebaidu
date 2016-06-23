#coding:utf-8
import os
def data_dirs():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print BASE_DIR
    DATA_DIRS=(os.path.join(BASE_DIR,'Data-Driven'),)
    d='/'.join(DATA_DIRS)
    return d

def readFile(index):
    f=file(data_dirs()+'/system.txt','r')
    d= f.readlines()
    f.close()
    return d[index]

print readFile(2)
