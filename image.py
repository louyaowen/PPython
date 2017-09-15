# -*- coding:utf-8 -*-
# 图片处理

from PIL import Image, ImageFilter

img = Image.open('files/timg.jpeg')

print(img.format, img.size, img.mode)

w,h = img.size
img.thumbnail((w/2,h/2))
img.filter(ImageFilter.BLUR)
img.save('files/small.jpeg','JPEG')
