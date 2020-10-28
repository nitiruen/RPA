from pdf2image import convert_from_path

image = convert_from_path('TEST1.pdf', poppler_path=r'C:\poppler-20.09.0\bin')
#print(image)
#print(len(image))
#image[0].show()
#image[0].save('TEST1.jpg')

img = image[0]

location = (131,483,583,701) #ระบุ location
address = img.crop(location) #crop รูปออกมา
address.show()




