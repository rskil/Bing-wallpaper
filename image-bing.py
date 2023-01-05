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

    # 获取图片地址
    # url 类似于 https://s.cn.bing.net/th?id=OHR.Perihelion_EN-CN9143824587_1920x1080.jpg
    Picture_address = f"https://s.cn.bing.net/{api.split(',')[3].split('/')[1].split('&')[0]}"

    # 获取图片名称
    if 'EN-US' in api:
        image_name = Picture_address.split('HIISSF_EN-US')[1]
    if 'ZH-CN' in api:
        image_name = Picture_address.split('Schnee_ZH-CN')[1]

    # 输出看效果
    print(api)

    return Picture_address, image_name


def download():
    # 以月份创建文件夹
    year = datetime.datetime.now().strftime('%Y')
    month = datetime.datetime.now().strftime('%Y-%m')
    print(year, month)
    # 新建文件夹
    os.system(f'mkdir /Wallpaper/{year}/{month}')
    # 图片下载位置
    os.system(f'wget {Picture_address} -O /Wallpaper/{year}/{month}/{image_name}')


def push():
    # 邮箱
    os.system('git config --global user.email renhang0203@88.com')
    # 用户名
    os.system('git config --global user.name rskil')
    # 上传的文件夹
    os.system('git add ./Wallpaper/*')
    # 上传备注
    os.system('git commit -m "Update on $(date +%F' '%X) :sunny:" -a')
    # 上传
    os.system('git push')
    print(f"推送成功 - {datetime.datetime.now().strftime('%Y-%m-%d')}")


def start_up():
    api()
    download()
    push()

    
if __name__ == '__main__':
    start_up()
    
    
