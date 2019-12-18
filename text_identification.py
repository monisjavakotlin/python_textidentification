#pip install pillow
#pip install pytesseract
#coding: utf-8

from PIL import Image
import pytesseract
img = Image.open('test1.jpg')
img = img.convert('L')
ans1 = pytesseract.image_to_string(img,'chi_tra')
ans2 = pytesseract.image_to_string(img,'chi_sim')
ans3 = pytesseract.image_to_string(img,'eng')

# 開啟檔案
fp = open("result.txt", "w")

# 寫入 This is a testing! 到檔案
fp.write(ans1)

# 關閉檔案
fp.close()


print(ans1)
print('\n')
print(ans2)
print('\n')
print(ans3)