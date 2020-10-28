import webbrowser
import time
import pyautogui as pg
from datetime import datetime
import pyperclip

'''
#กรณีต้องการเปิด Browser โดยตรง
from subprocess import Popen
#ต้องเปิด Chrome.exe
path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
Popen(path)
'''

'''
#1. open webbroser
url = 'https://google.co.th'
webbrowser.open(url)
time.sleep(3) #หยุด 3 วินาที เพื่อให้ program เปิดเว็บเสร็จ เป็นต้น 

#2. type: Thailand
pg.write('Thailand', interval = 0.2)

#3. Enter
pg.press('enter')
time.sleep(3)

#4. screenshort
im = pg.screenshot( name+'.jpg')'''

def search(keyword, eng = False):
    url = 'https://google.co.th'
    webbrowser.open(url) #open webbrowser
    time.sleep(3)

    if eng == True:
        pg. write(keyword, interval = 0.01) #type keyword
    else:
        pyperclip.copy(keyword) #if not ENG then copy paste
        time.sleep(1)
        pg.hotkey('ctrl', 'v')

        
    pg.press('enter') #press enter
    time.sleep(2)

    dt = datetime.now().strftime('%Y-%m-%d %H-%M-%S') #strftime
    pg.screenshot(r'C:\Users\life_\Desktop\RPA\Picture\{} {}.jpg'.format(keyword,dt),
                  region = (261,416,1053,674))
    time.sleep(1.5)
    pg.hotkey('ctrl', 'w')

search('ราคาทองคำ')
search('USD to THB',eng=True)
#search('EUR to THB')
#search('CNY to THB')
#search('THB to JPY')
#search('TWD to THB')



    
    
