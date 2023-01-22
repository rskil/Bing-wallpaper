#! python3
import datetime
import requests
import os


def api():
    # 定义全局变量
    global image_name, Picture_address

    # 壁纸接口
    # api = requests.get('http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1').text.split(',')
    api = requests.get('https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US').text
    # 打印访问接口返回信息
    print(api)
    
    # 获取图片地址
    # url 类似于 https://s.cn.bing.net/th?id=OHR.Perihelion_EN-CN9143824587_1920x1080.jpg
    Picture_address = f"https://s.cn.bing.net/{api.split(',')[3].split('/')[1].split('&')[0]}"
    
    # 获取图片名称
    if 'EN-US' in api:
        image_name = Picture_address.split('EN-US')[1]
    if 'ZH-CN' in api:
        image_name = Picture_address.split('ZH-CN')[1]


    return Picture_address, image_name


# 下载壁纸 存放到对应月份目录
def download():
    # 以月份创建文件夹
    year  = datetime.datetime.now().strftime('%Y')
    month = datetime.datetime.now().strftime('%Y-%m')
    print(year, month)
    # 新建文件夹
    os.system(f'mkdir -p ./Wallpaper/{year}/{month}')
    # 图片下载位置
    os.system(f'wget {Picture_address} -O ./Wallpaper/{year}/{month}/{image_name}')
    os.system(f'tree ./Wallpaper/{year}/{month}')

    
# 向模板内添加图片地址
def addimg():
    os.system(f'echo "- {Picture_address} \" >>  ./Wallpaper/Template.txt'  )
    

# 自述文件更新
def readme():
    # 模板文件内加入数据 
    addimg()
    with open("./Wallpaper/Template.txt", "r", encoding="utf-8") as f:  # 打开文件
        # 读取文件
        data = f.read()  
        # 将模板中对应部分替换
        data = data.replace('URL', f'{Picture_address}').replace('TIME',
                                                                 f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        # 将替换后的内容写到新的文件
        with open("./Wallpaper/new_readme.txt", 'w', encoding="utf-8") as f_new:
            f_new.write(data)
            f_new.close()
        f.close()
    # 更新自述文件 README.md
    os.system('cat ./Wallpaper/new_readme.txt && cat ./Wallpaper/new_readme.txt > ./README.md')

    
if __name__ == '__main__':
    api()
    download()
    readme()
    
