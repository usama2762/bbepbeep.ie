print ('usama')
#driver = webdriver.Chrome()
print ('jamil')
# stuff ...

#driver.close()
#display.stop()
import os
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import requests
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
from subprocess import call
import psycopg2


#call(["killall", "chrome"])
time.sleep(1)
conn = psycopg2.connect(host="elmer.db.elephantsql.com",database="mxywyuox", user="mxywyuox", password="vpK0uG4-H1k1JJM4E1TNVfdbEVNCN1Mq")
print ("Opened database successfully")

cur = conn.cursor()
#os.system("killalll chrome")
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "bin/chromedriver")
print (DRIVER_BIN)
#chrome = webdriver.Chrome(DRIVER_BIN)
#PROXY = "96.80.89.69:8080" # IP:PORT or HOST:PORT
path=os.getcwd()

idd=0
chrome=webdriver.Chrome(executable_path = DRIVER_BIN)   #webdriver.Chrome(DRIVER_BIN)
xpatht=''
def find(driver):
    element = driver.find_elements_by_xpath(xpatht)
    if element:
        return element
    else:
        return False
chrome.get('http://www.beepbeep.ie/price-guide/')
listx=chrome.find_element_by_xpath('//*[@id="make"]')
finallist=listx.find_elements_by_tag_name('option')
ixnt=0
for item in finallist:
	if ixnt>0:
		temp=chrome.find_element_by_xpath('//*[@id="make"]')
		time.sleep(2)
		temp.send_keys(item.text)
	time.sleep(2)
	txt=''
	fx=chrome.find_element_by_xpath('//*[@id="site_content"]/div[1]/div[4]')
	ft=fx.find_elements_by_class_name('row')
	length=len(ft)
	for i in range(0,length):
		xpath='//*[@id="site_content"]/div[1]/div[4]/div['
		for ix in range(1,8):
			xp=xpath+str(i)+"]/div["+str(ix)+']'
			temp=chrome.find_elements_by_xpath(xp)
			if len(temp)>0:
				txt+=str(temp[0].text)
				txt+=','
		#txt+='\n'
		arr=txt.split(',')
		if len(arr)>5:
			values1=[]
			values2=[]
			values1.append(str(arr[0]))
			values2.append(str(arr[0]))
			values2.append(str(arr[1]))
			values2.append(str(arr[2]))
			values2.append(str(arr[3]))
			values2.append(str(arr[4]))
			values2.append(str(arr[5]))
			values2.append(str(arr[6]))
			values2.append(str(arr[7]))
			cur.execute('''INSERT INTO CAR_MAKE(Make) VALUES(%s)''' , values1)
			print ("Inserted 1")
			cur.execute('''INSERT INTO CAR_MODEL(Make,CAR_MODEL,body_type,co2,vrt_band,annual_road_tax,engine_cc,rrp ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)''' , values2)
			print ("Inserted 2")
			print (arr)
			conn.commit()
		txt=''
		
		idd=idd+1



conn.commit()
cur.close()
conn.close()
chrome.quit()
