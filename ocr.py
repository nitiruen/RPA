from PIL import Image
import pytesseract

img = Image.open('invoice.jpg')
location = (131,483,583,701) #ระบุ location

address = img.crop(location) #crop รูปออกมา
address.show()
result = pytesseract.image_to_string(address, lang='tha')

print(result)
print([result]) #check ว่ามีอ่านได้อะไรบ้าง จะเจอว่ามี \n

result = result.replace('\n','')
print([result])