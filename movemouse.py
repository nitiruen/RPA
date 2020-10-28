Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pyautogui as pg
>>> import random

>>> pg.size()
Size(width=1920, height=1080)
>>> pg.onScreen()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    pg.onScreen()
TypeError: onScreen() missing 1 required positional argument: 'x'
>>> pg.onScreen(-400,-200)
False
>>> random.randint(0,999)
763
>>> for i range (5):
	
SyntaxError: invalid syntax
>>> for i in range (10):
	x = random.randint(0,1919)
	y = random.randint(0,1079)
	pg.moveTo(x,y, duration=2)

	
>>> 