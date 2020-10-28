#stock2.py

from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from songline import Sendline

token = 'biKDaA8oQM5iIvD5kvIWTcDzFETv3HpYD1ZPgIcwcIY'
messenger = Sendline(token)

def checkprice(stock):
    url = 'https://www.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol={}&ssoPageId=9&selectPage=1'.format(stock)

    webopen = req(url)
    page_html = webopen.read()
    webopen.close()

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
    
    #print(type(price)) #เชคว่าข้อความเป็นขนิดไหน
    text = '\n{}\nStock: {} price:{} baht'.format(update1,stock,price)
    print(text)
    print('----'*10)

    messenger.sendtext(text)

checkprice('AOT')
checkprice('UTP')
checkprice('THANI')

