# coding=gb2312
# pillow 库的使用
from PIL import Image
from PIL import ImageFilter  # 滤镜
im = Image.open('bing42.jpg')
w, h = im.size
print('width : %s, height : %s' % (w, h))
# 设置缩放图
im.thumbnail((w // 2, h // 2))
im.save('thumbnail1.png', 'png')
# 模糊效果 使用滤镜
im = Image.open('thumbnail1.png')
im2 = im.filter(ImageFilter.BLUR)
im2.save('thumbnail_blur.png')