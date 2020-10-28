Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pyautogui
>>> pyautogui.size()
Size(width=1920, height=1080)
>>> pyautogui.position()
Point(x=1772, y=1052)
>>> pyautogui.position()
Point(x=210, y=860)
>>> import pyautogui as pg
>>> pg.write('Thailand')
Thailand
>>> pyautogui.write('Thailand')
Thailand
>>> pg.write('Thailand', interval=0.3)
Thailand
>>> def testtype():
	pg.click(1172,1052)

	
>>> testtype
<function testtype at 0x0000016DE0DA34C0>
>>> testtype()
>>> pg.position()
Point(x=1140, y=971)
>>> pg.position()
Point(x=348, y=585)
>>> def testtype():
	pg.click(348,585)
	pg.write('Thailand', interval=0.1)

	
>>> testtype()
>>> def testtype(inserttext):
	pg.click(348,585)
	for i in range (5):
		pg.write('inserttext', interval=0.1)
		pg.press('enter')

		
>>> testtype(555)
>>> def testtype(inserttext):
	pg.click(348,585)
	for i in range (5):
		pg.write(inserttext, interval=0.1)
		pg.press('enter')

		
>>> testtype(5555)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    testtype(5555)
  File "<pyshell#25>", line 4, in testtype
    pg.write(inserttext, interval=0.1)
  File "C:\Users\life_\AppData\Local\Programs\Python\Python38\lib\site-packages\pyautogui\__init__.py", line 588, in wrapper
    returnVal = wrappedFunction(*args, **kwargs)
  File "C:\Users\life_\AppData\Local\Programs\Python\Python38\lib\site-packages\pyautogui\__init__.py", line 1626, in typewrite
    for c in message:
TypeError: 'int' object is not iterable
>>> testtype(jdfghdgh)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    testtype(jdfghdgh)
NameError: name 'jdfghdgh' is not defined
>>> testtype('jdjgfjdgfg')
>>> testtype('Data science')
>>> testtype('555')
>>> 