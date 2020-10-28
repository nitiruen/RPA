from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os #check directory

def convertPDF (filepath='TEST1.pdf', page=0, loca=(131,483,583,701), lang='tha',save=False):
	image = convert_from_path(filepath, poppler_path=r'C:\poppler-20.09.0\bin')
	img = image[page]
	fliename = filepath[:-4]
	#save file
	if save == True:
		savename = '{} page{}.jpg'.format(fliename,page+1)
		img.save(savename)

	location = loca #ระบุ location
	address = img.crop(location)

	result = pytesseract.image_to_string(address, lang=lang)
	result = result.replace('\n',' ').replace('\x0c','')
	return result

#for multiple file
allfile = os.listdir() #check number of files
pdffile = [] #sotre pdf only file
for file in allfile:
	if file[-3:] == 'pdf':
		pdffile.append(file)

for pdf in pdffile:
	text = convertPDF(pdf)
	print(text)

