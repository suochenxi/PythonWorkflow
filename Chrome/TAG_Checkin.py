import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Step1：获取真实地址域名
r = requests.get('http://www.tagvpn.vip',allow_redirects=False)
url = r.headers['Location']

# Step2：登录
driver = webdriver.Chrome()
driver.get(url+'auth/login')
driver.find_element_by_id('email').send_keys('suochenxi@foxmail.com')
driver.find_element_by_id('password').send_keys('suochenxi')
driver.find_element_by_id('password').send_keys(Keys.ENTER)

# Step3:签到
for i in range(300):
    try:
        driver.find_element_by_id('checkin').click()
        print('已签到，程序结束')
        driver.quit()
        break
    except:
        try:
            driver.find_element_by_id('checkin-btn')
            print('检测到已签到，程序结束')
            driver.quit()
            break
        except:
            print('签到失败，100ms后重试')
            time.sleep(0.1)