# coding=gb2312
# pillow ���ʹ��
from PIL import Image
from PIL import ImageFilter  # �˾�
im = Image.open('bing42.jpg')
w, h = im.size
print('width : %s, height : %s' % (w, h))
# ��������ͼ
im.thumbnail((w // 2, h // 2))
im.save('thumbnail1.png', 'png')
# ģ��Ч�� ʹ���˾�
im = Image.open('thumbnail1.png')
im2 = im.filter(ImageFilter.BLUR)
im2.save('thumbnail_blur.png')