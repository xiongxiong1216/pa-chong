# -*- coding:utf-8 -*-

import sys,requests,json,time,smtplib
reload(sys)
sys.setdefaultencoding('utf-8')

#这是发送天气短信的
def weathermail(city):
    url='https://api.seniverse.com/v3/weather/now.json?key=nuvsytsinmz49ufn&location={city}&language=zh-Hans&unit=c'.format(city=city)
    res=requests.get(url)
    dict=json.loads(res.text,encoding='utf-8')
    localhost=dict[u'results'][0][u'location'][u'name']
    weather=dict[u'results'][0][u'now'][u'text']
    temperature=dict[u'results'][0][u'now'][u'temperature']
    today=time.ctime(time.time())
    weather_info=[u'地方:'+localhost+'\n'+u'天气:'+weather+'\n'+u'温度:'+temperature+'\n'+u'日期:'+today]
    return weather_info

Fromeaddress='xiongxiongjiayou1@163.com'
Toaddress='2275028513@qq.com'
serversmtp='smtp.163.com'

server=smtplib.SMTP(serversmtp,25)
msghead=['From:xiongxiongjiayou1@163.com','To:2275028513@qq.com','Subject:weather mail']
msgboby=weathermail('shenzhen')
# msgBoby=['Hello!','This is my first python mail']
msg='\r\n\r\n'.join(['\r\n'.join(msghead),'\r\n'.join(msgboby)])
server.set_debuglevel(1)
server.login(Fromeaddress,'******')
server.sendmail(Fromeaddress,Toaddress,msg)
print u'邮件发送成功'
server.quit()

