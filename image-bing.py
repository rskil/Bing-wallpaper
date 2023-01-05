import requests
import os

# 接口
# Webpage = requests.get('http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1').text.split(',')

Webpage = requests.get('https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US').text.split(',')

# 获取图片地址
# (https://s.cn.bing.net/th?id=OHR.Perihelion_EN-CN9143824587_1920x1080.jpg);
Picture_address = f"https://s.cn.bing.net/{Webpage[3].split('/')[1].split('&')[0]}"

print(Webpage)
print()
print(Picture_address)

# 图片名称
image_name = Picture_address.split('Schnee_')[1]
print(image_name)

# 图片 title
# title =
# 下载图片
os.system(f'wget {Picture_address} -O {image_name}')
os.system('ls')
