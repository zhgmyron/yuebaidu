#coding:utf-8
def fileWrites():
    f= file('c:/text.txt','w+')
    li=["selenium webdriver\n",'自动化测试\n']
    f.writelines(li)
    f.close()

