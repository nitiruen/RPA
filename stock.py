# เราจะดึงข้อมูลแบบไม่เปิด web

from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

url = 'https://www.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol=aot&ssoPageId=9&selectPage=1'

webopen = req(url) #เปิดเว็บโดยไม่ต้องเปิด Chrome
page_html = webopen.read()#สั่งให้ program อ่านออกมาเป็นตัวอักษร
webopen.close()#ปิดการเชื่อมต่อ

data = soup(page_html, 'html.parser')

rawdata = data.find_all('div', 'col-xs-6')
stock = rawdata[0].text #name stock
price = float(rawdata[2].text) #price stock

update = data.find_all('div', 'flex-item text-left padding-8')
update1 = update[0].text
#print([update1]) #เชคว่ามีตัวไรบ้าง เช่นพวก tab enter จะแสดงถ้าเราใส่ list ไป เพื่อใช้ replace
#ในการตัดข้อความที่ไม่ต้องการออก
update1 = update1.replace('\n','')
update1 = update1.replace('สถานะตลาด : Closed','')
update1 = update1.replace('ข้อมูลล่าสุด','')[1:] #remove space ตัวแรกออก
print(update1)

#print(type(price)) #เชคว่าข้อความเป็นขนิดไหน
text = 'Stock: {} price:{} baht'.format(stock,price)

print(text)


'''
#หรือสามาระใช้ for loop check ว่าข้อมูลที่เราต้องการอยู่ index ส่วนไหน
for i,r in enumerate(rawdata):
    print(i)
    print(r.text)
    print('____________')
'''


