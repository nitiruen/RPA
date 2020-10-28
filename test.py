Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pyautogui as pg
>>> pg.position
<function position at 0x000002B7DA26D940>
>>> pg.position()
Point(x=1141, y=281)
>>> pg.write('Thailand')
Thailand
>>> pg.write('Thailand', interval=0.25)
Thailand
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> pyautogui.moveTo(1823,1054,duration=10)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    pyautogui.moveTo(1823,1054,duration=10)
NameError: name 'pyautogui' is not defined
>>> 
>>> pg.moveTo(1823,1054,duration=10)
>>> pg.write('Thailand')
ธ้ฟรสฟืก
>>> pg.write('Thailand')
Thailand
>>> pg.position()
Point(x=28, y=97)
>>> pg.moveTo(28,97)
>>> pg.moveTo(28,97)
>>> def testtype():
	pg.click(28,97)
	pg.write('Thailand',interval=0.4)

	
>>> testtype()
>>> testtype()
>>> testtype()
>>> testtype()
>>> testtype()
>>> for i in range (5):
	print(i, "Hello")

	
0 Hello
1 Hello
2 Hello
3 Hello
4 Hello
>>> def testtype(keywaord):
	pg.click(28,97)
	for i in range (5):
		pg.write(keywaord,interval=0.4)
		pg.press("enter")

		
>>> testtype(Waranyu)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    testtype(Waranyu)
NameError: name 'Waranyu' is not defined
>>> testtype('Waranyu')
>>> def testtype(keywaord):
	pg.click(28,97)
	for i in range (5):
		pg.write(keywaord,interval=0.2)
		pg.press("enter")

		
>>> testtype('Waranyu')
>>> def testtype(keywaord):
	pg.click(28,97)
	for i in range (5):
		pg.write(keywaord)
		pg.press("enter")

		
>>> testtype('Waranyu')
>>> testtype('Waranyu')
>>> def testtype(keywaord):
	pg.click(50,97)
	for i in range (5):
		pg.write(keywaord,interval=0.2)
		pg.press("enter")

		
>>> testtype('Waranyu')
>>> 
>>> def testtype(keywaord):
	pg.click(50,97)
	for i in range (5):
		pg.write(keywaord)
		pg.press("enter")

		
>>> testtype('Waranyu')
>>> testtype('Waranyu')
>>> pg.position()
Point(x=410, y=311)
>>> def testtype(keywaord):
	pg.click(410,311)
	for i in range (5):
		pg.write(keywaord)
		pg.press("enter")

		
>>> testtype('Waranyu')
>>> testtype('Waranyu')
>>> testtype('Waranyu')
>>> testtype('Waranyu')
>>> testtype('Waranyu')
>>> testtype('Waranyu')
>>> 
>>> pg.size()
Size(width=1920, height=1080)
>>> import random
>>> random.randint(0,99)
47
>>> random.randint(0,99)
79
>>> random.randint(110,99)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    random.randint(110,99)
  File "C:\Users\life_\AppData\Local\Programs\Python\Python38\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
  File "C:\Users\life_\AppData\Local\Programs\Python\Python38\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (110, 100, -10)
>>> 
>>> 
>>> 
>>> friend = ["a", "b", "c"]
>>> random.choice(friend)
'c'
>>> for i in range (20):
	x = random.randint(0,1919)
	y = random.randint(0,1079)
	pg.moveTo(x,y,duration=1)

	
>>> for i in range (20):
	x = random.randint(-444,1919)
	y = random.randint(0,1079)
	pg.moveTo(x,y,duration=1)

	

>>> for i in range (20):
	x = random.randint(0,1919)
	y = random.randint(0,1079)
	pg.moveTo(x,y,duration=1)

	
>>> def test()
SyntaxError: invalid syntax
>>> def test():
	webbrowser.open('http://google.co.th')

	
>>> pg.position
<function position at 0x000002B7DA26D940>
>>> pg.position()
Point(x=-1509, y=615)
>>> def test():
	webbrowser.open('http://google.co.th')
	pg.click(-1509,615)

	
>>> test()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    test()
  File "<pyshell#90>", line 2, in test
    webbrowser.open('http://google.co.th')
NameError: name 'webbrowser' is not defined
>>> import webbrowser
>>> test()
>>> def test():
	webbrowser.open('http://google.co.th', new=2)
	pg.click(-1509,615)

	
>>> test()
>>> test()
>>> def test():
	webbrowser.open('http://google.co.th', new=2)
	pg.click(-1509,615)
	pg.write('Thailand')
	pg.press('enter')

	
>>> test()
>>> def test():
	webbrowser.open('http://google.co.th')
	time.sleep(3)
	pg.click(-1509,615)
	pg.write('Thailand')
	pg.press('enter')

	
>>> test()
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    test()
  File "<pyshell#104>", line 3, in test
    time.sleep(3)
NameError: name 'time' is not defined
>>> import time
>>> test()
>>> pg.position()
Point(x=-1543, y=660)
>>> def test():
	webbrowser.open('http://google.co.th')
	time.sleep(3)
	pg.click(-1543,660)
	pg.write('Thailand')
	pg.press('enter')

	
>>> test()
>>> def test():
	webbrowser.open('http://google.co.th')
	time.sleep(3)
	pg.click(-1543,660)
	pg.write('Thailand')
	pg.press('enter')
	img = pg.screenshot('Thailand.jpg')