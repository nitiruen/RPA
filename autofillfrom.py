from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import wikipedia
import time

#ต้องโหลด selenium แล้วเอา chromedriver มาวางไว้ใน folder ของ python หากไท้ได้วางให้ใส่ path ในวงเว็บ chrome แทน
driver = webdriver.Chrome()

url_login = 'http://uncle-machine.com/login/'
driver.get(url_login)

username = driver.find_element_by_id('username')
username.send_keys('uuu@gmail.com')

password = driver.find_element_by_id('password')
password.send_keys('123')

button = driver.find_element_by_xpath('/html/body/div[2]/form/button')
button.click()
time.sleep(1)

#fill data in product page 
url_addproduct = 'http://uncle-machine.com/addproduct/'
driver.get(url_addproduct)

name = driver.find_element_by_id('name')
name.send_keys('กล้วยแขก')

price = driver.find_element_by_id('price')
price.send_keys('1000')

detail = driver.find_element_by_id('detail')
detail.send_keys('กล้วยที่มาจากดาวอังคาร')

button = driver.find_element_by_xpath('/html/body/div[2]/form/button')
button.click()



#website ที่ไม่เป็น static เช่น ptt ราคาน้ำมัน ซึ่งไม่สามารถดูราคาได้จาก view page source
#page_html = driver.page_source #จากนั้นใช้ beautyful soup ดึงข้อมูลมา
#print(page_html)


'''
url = 'https://www.google.com'
driver.get(url)

search = driver.find_element_by_name('q') #find 'q' >>why q beacuse name of html (find from ctl shft I) คล้ายๆ webscrapper
search.send_keys('ราคาทองคำ')
search.send_keys(Keys.RETURN) #press enter
'''