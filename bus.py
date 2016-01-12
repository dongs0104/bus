#-*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

ip = "211.236.110.97"
ip2 = "211.236.110.110"
#serverCheck
if urllib2.urlopen("http://"+ip).getcode() == 200:
    url = "http://"+ ip +"/GMBIS/m/page/srchBusArr.do?act=srchBusArr&stopId=132&stopKname=%EA%B8%88%EC%98%A4%EA%B3%B5%EB%8C%80%EC%A2%85%EC%A0%90&menuCode=1_03&stopServiceid=10132"
elif urllib2.urlopen("http://"+ip2).getcode() == 200:
    url = "http://"+ ip2 +"/GMBIS/m/page/srchBusArr.do?act=srchBusArr&stopId=132&stopKname=%EA%B8%88%EC%98%A4%EA%B3%B5%EB%8C%80%EC%A2%85%EC%A0%90&menuCode=1_03&stopServiceid=10132"
#contents open
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html,"lxml")
bus = open("/var/www/html/webapp/buson132-2.txt", 'w')
for ultag in soup.find_all('ul', {'class': 'arrive_desc'}):
    busNo = ultag.find('li', {'class': 'bus_no'})
    busState = ultag.find('li', {'class': 'bus_state'})
    busLocal = ultag.find('li', {'style' : 'margin:2px;font-size:13px;'})
    if busLocal is None:
        busLocal = '기점출발예정'
    else:
        busLocal =  busLocal.text
    bus.write(busNo.text + ' ' + busState.text + busLocal + "</br>")
bus.close()

