from selenium  import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import logging 
import unittest
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from  email.header import Header
from email.mime.multipart import MIMEMultipart
import os

#发送邮箱服务器
smtpserver='webmaster@zloving.com'
#发送邮箱用户/密码
user='webmaster@zloving.com'
password='DJOslNK35zMdlOpy'
#发送邮箱
sender='xiongxiongjiayou1@163.com'
#接收邮箱
receiver='2275028513@qq.com'

def send_mail(file_new):
	f=open(file_new,'rb')
	mail_boby=f.read()
	f.close()
	msg=MIMEText(mail_boby,_subtype='html',_charset='gb2312')
	msg['Subject']='sub'
	smtp=smtplib.SMTP()
	smtp.connect(smtpserver)
	smtp.login(user,password)
	smtp.sendmail(sender,receiver,msg.as_string())
	smtp.quit()
	print 'email has send out!'

class niaoyun(unittest.TestCase):
	def setUp(self):
		self.dirver=webdriver.Firefox()
		url='https://www.niaoyun.com/login/'
		self.dirver.get(url)
		self.dirver.set_window_size(800,600)
		time.sleep(2)
	
	def test_niaoyun(self):
		u'''这是一个对于鸟云的登录'''
		logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s',\
			                 datefmt='%a,%d %b %Y %H:%M:%S',filename='myapp.log',filemode='w')
		dirver=self.dirver
		dirver.find_element_by_xpath("//input[@id='userName']").send_keys('18025414846')
		dirver.find_element_by_xpath("//input[@id='passwordInput']").send_keys('123456xx')
		dirver.find_element_by_xpath("//input[@id='loginSubmit']").click()
		cookie=dirver.get_cookie('name')
		print cookie
		cookie1=dirver.get_cookie('PHPSESSID')
		print cookie1
		dirver.get_screenshot_as_file('D:\\test\\niaoyun.jpg')
		js='window.scrollTo(100,450);'
		dirver.execute_script(js)
		dirver.get_screenshot_as_file('D:\\test\\niaoyun1.jpg')
		time.sleep(3)

	def tearDown(self):
		self.dirver.quit()

if __name__=="__main__":
	testunit=unittest.TestSuite()
	testunit.addTest(niaoyun('test_niaoyun'))
	fp=open('D:\\test\\result.html','wb')
	runner=HTMLTestRunner(stream=fp,title=u'鸟云测试报告',description=u'用例执行情况:')
	runner.run(testunit)
	file_new='D:\\test\\result.html'
	send_mail(file_new)
	fp.close()