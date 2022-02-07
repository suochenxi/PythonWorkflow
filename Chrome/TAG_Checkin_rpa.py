import requests
import rpa as r

def tag_login():
    r. hover('//*[@id="email"]')
    print('页面加载成功')
    r.type('//*[@id="email"]','suochenxi@foxmail.com')
    r.type('//*[@id="password"]','suochenxi[enter]')

    return None

def tag_checkin():
    if(r.exist('//*[@id="checkin"]')):
        print('检测到签到按钮，尝试进行点击')
        r.click('//*[@id="checkin"]')
    elif(r.exist('//*[@id="checkin-btn"]')):
        print('今日已签到')
    else:
        print('异常，签到失败')
    return None


# Step1：获取真实地址域名
root_url = requests.get('http://www.tagvpn.vip',allow_redirects=False).headers['Location']

print(root_url)

r.init(visual_automation = True)

# Step2：尝试进用户中心，失败则登录
r.url(root_url+'user')

url_jump = r.url()

if(url_jump.replace(root_url,'') == 'auth/login'):
    print('当前未登录，执行登录操作')
    tag_login()
elif(url_jump.replace(root_url,'') == 'user'):
    print('当前已登录，尝试进行签到')
else:
    print('URL 异常')

# Step3：执行签到
tag_checkin()
    
r.close()
