#coding:utf-8
import os,csv,xlrd
import xml.dom.minidom
def data_dirs():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIRS=(os.path.join(BASE_DIR,'Data-Driven'),)
    d='/'.join(DATA_DIRS)
    return d
def getList():
    list=[['','',u'请您填写手机/邮箱/用户名'],['admin','',u'请您填写密码'],['admin','admin',u'请输入验证码']]
    return list
def readFile(index):
    f=file(data_dirs()+'/system.txt','r')
    d= f.readlines()
    f.close()
    return d[index]
def readCsv(value1,value2):
    rows=[]
    data_file=open(data_dirs()+'/system.csv')
    reader=csv.reader(data_file)
    next(reader,None)
    for row in reader:
        rows.append(row)
    return ''.join(rows[value1][value2]).decode('gb2312')

def readExcel(rowValue,colValue):
    book=xlrd.open_workbook(data_dirs()+'/system.xlsx')
    sheet=book.sheet_by_index(0)
    return sheet.cell_value(rowValue,colValue)
def readExcels():
    rows=[]
    book=xlrd.open_workbook(data_dirs()+'/system.xlsx')
    sheet=book.sheet_by_index(0)
    for row in range(1,sheet.nrows):
        rows.append(list(sheet.row_values(row,0,sheet.ncols)))
    return rows

def getXmlData(value):
    dom=xml.dom.minidom.parse(data_dirs()+'/system.xml')
    db=dom.documentElement
    name=db.getElementsByTagName(value)
    nameValue =name[0]
    return nameValue.firstChild.data

def getXmlUser(parent,child):
    dom=xml.dom.minidom.parse(data_dirs()+'/system.xml')
    db=dom.documentElement
    itemlist=db.getElementsByTagName(parent)
    item=itemlist[0]
    return item.getAttribute(child)

print getXmlData('test')
print getXmlUser('failLogin1','expected')



