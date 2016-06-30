#coding:utf-8
import unittest,os,sys,HTMLTestRunner,time

def suite():
    dir_case=unittest.defaultTestLoader.discover(
        'F:\ASK_TEST\yuebaidu\TestCase',
        pattern='test_baidu.py',
        top_level_dir=None
        )
    return dir_case


#获取当前时间另外一种方式是:
nowTime=time.strftime('%Y-%m-%d %X',time.localtime())

def getNowTime():
	return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))




def runAutomation():
	filename='F:/ASK_TEST/yuebaidu/Report/'+getNowTime()+'TestReport.html'
	fp=file(filename,'wb')
	runner=HTMLTestRunner.HTMLTestRunner(
		stream=fp,
		title=u'自动化测试报告',
		description=u'自动化测试报告详细的信息'
	)
	runner.run(suite())

if __name__=='__main__':
    #unittest.TextTestRunner(verbosity=2).run(suite())
    runAutomation()

