#coding:utf-8
def fileWrites():
    f= file('f:/text.txt','w+')
    li=["selenium webdriver\n",'自动化测试\n']
    f.writelines(li)
    f.close()
def readFile():
     f= file('f:/text.txt','r')
     print f.read()
     f.close()
if __name__=='__main__':
    fileWrites()
    readFile()
