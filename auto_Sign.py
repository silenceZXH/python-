from selenium import webdriver
import random
import smtplib
from selenium.webdriver.support.ui import WebDriverWait
from email.mime.text import MIMEText
from time import sleep
import time
import json

email_1 = 'norealdeath@163.com'
email_2 = '1789342527@qq.com'
email_3 = '1120124312@qq.com'
email_4 = '734738141@qq.com'
email_5 = 'amareeee@163.com'
passwd_1 = 'amarevpn'
user_email = [email_1,email_2,email_3,email_4,email_5]

driver = webdriver.Chrome() 
driver.implicitly_wait(8)   #打开窗口
driver.get("https://www.shsxs.me/auth/login")
for i in range(len(user_email)):
    email = user_email[i]
    print('当前用户：',email)
    sleep(2)
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("passwd").clear()
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("passwd").send_keys(passwd_1)
    driver.find_element_by_id("login").click()
    time.sleep(10)
    #print('start wait')
    #WebDriverWait(driver,5).until(lambda driver : driver.find_element_by_id('checkin').is_displayed()==True)
    #print('end wait')
    try:
        # driver.find_element_by_link_text("知道了").click()
        # driver.find_element_by_link_text(" 签到续命").click()
        driver.find_element_by_xpath("//*[@id='checkin']").click()
        print("续命成功")
    except:
        print("签到失败") 
    sleep(3) 
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/ul[2]/li/a/span").click()
    driver.find_element_by_link_text("退出网站").click()
    sleep(3)

    
driver.quit()