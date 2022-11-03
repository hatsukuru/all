# -*- coding:utf-8 -*-
'''
@File    : twittere.py
@Time    : 2022/10/28 10:41
@Author  : hatsune
@Email   : l2011617078@163.com
@Software: PyCharm
'''
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from tqdm import tqdm, trange
import ftfy
import scrapy
from scrapy import Request, Spider
import csv
from selenium import webdriver
import time
import datetime
from datetime import datetime
from pyhtml2pdf import converter
import pdfkit
from pymongo import MongoClient
import pandas as pd

options = ChromeOptions()
# options.add_argument("--headless")
# option = ChromeOptions()


options.add_argument(
    f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36')
'''
# 设置开发者模式启动
driver = webdriver.Chrome(options=options)

url = 'https://twitter.com/home'
driver.get(url)
driver.maximize_window()
time.sleep(25) #           l2011617078@163.com

#  102201ryttkx
#
#  +8615028505156
'''

aaa = [
    {'domain': '.twitter.com', 'expiry': 1666893755, 'httpOnly': True, 'name': 'att', 'path': '/', 'sameSite': 'None',
     'secure': True, 'value': '1-rQQH8OYZHJ11EsEbwEvlBjGTkE5oxrtn248B3xJb'},
    {'domain': '.twitter.com', 'expiry': 1701367355, 'httpOnly': False, 'name': 'ct0', 'path': '/', 'sameSite': 'Lax',
     'secure': True,
     'value': '1aec466f95e7615f80a8ec99d83f5b1eae45488d4cf18103e17acf3833100ea279e2b0883c1199c3fec475df8a107975ee39c390e87ac6832a27d67f5e26be7d850e0929baf0abba96ea7d16b76a290a'},
    {'domain': '.twitter.com', 'expiry': 1701367355, 'httpOnly': True, 'name': 'auth_token', 'path': '/',
     'sameSite': 'None', 'secure': True, 'value': '832f2883adc6b22b32bdb1536d128cb0c6e0ca6f'},
    {'domain': 'twitter.com', 'expiry': 1666893742, 'httpOnly': False, 'name': '_sl', 'path': '/', 'secure': True,
     'value': '1'}, {'domain': '.twitter.com', 'expiry': 1701367339, 'httpOnly': False, 'name': 'guest_id', 'path': '/',
                     'sameSite': 'None', 'secure': True, 'value': 'v1%3A166680733933313352'},
    {'domain': '.twitter.com', 'expiry': 1701367355, 'httpOnly': False, 'name': 'twid', 'path': '/', 'sameSite': 'None',
     'secure': True, 'value': '"u=1298635437347606530"'},
    {'domain': '.twitter.com', 'expiry': 1666818142, 'httpOnly': False, 'name': 'gt', 'path': '/', 'secure': True,
     'value': '1585331011855929344'},
    {'domain': '.twitter.com', 'expiry': 1701367343, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
     'value': 'GA1.2.521968786.1666807344'},
    {'domain': '.twitter.com', 'expiry': 1701367355, 'httpOnly': True, 'name': 'kdt', 'path': '/', 'secure': True,
     'value': 'Suw8EuI0dvI3MkpDYbKe1RIKglVuoPnpht6FmsEr'},
    {'domain': '.twitter.com', 'expiry': 1666893743, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
     'value': 'GA1.2.997858195.1666807344'},
    {'domain': '.twitter.com', 'expiry': 1701367339, 'httpOnly': False, 'name': 'personalization_id', 'path': '/',
     'sameSite': 'None', 'secure': True, 'value': '"v1_VZR2RAZw8YMvr0roN9g+LA=="'},
    {'domain': '.twitter.com', 'expiry': 1701367339, 'httpOnly': False, 'name': 'guest_id_ads', 'path': '/',
     'sameSite': 'None', 'secure': True, 'value': 'v1%3A166680733933313352'},
    {'domain': '.twitter.com', 'httpOnly': True, 'name': '_twitter_sess', 'path': '/', 'secure': True,
     'value': 'BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCJCldRWEAToMY3NyZl9p%250AZCIlYjhjZTM5NjgwZjE5YTgyMDcyY2Y5YzM3MzliYmRhNTU6B2lkIiU2MTU0%250ANDZmOTFiZTBmOWFiYWMzMzY3N2M4Y2NjNzliZA%253D%253D--d0b2224076d46d6be5c5a3ab8346010da2ffff3b'},
    {'domain': '.twitter.com', 'expiry': 1701367339, 'httpOnly': False, 'name': 'guest_id_marketing', 'path': '/',
     'sameSite': 'None', 'secure': True, 'value': 'v1%3A166680733933313352'}]

savedCookies = aaa
print(savedCookies)
a = ['美國公布中國火箭軍','火箭军基地坐标','PLARF organization','PLA Rocket Force']
driver2 = webdriver.Chrome()
urla = 'https://twitter.com/search?q='
urlb = '&src=typed_query&f=live'

for i in range(0,4):
    urll = urla + a[i] + urlb

    driver2.get(urll)
    driver2.delete_all_cookies()
    for cookie in savedCookies:
        for k in {'name', 'value', 'domain', 'path', 'expiry'}:
            if k not in list(cookie.keys()):
                if k == 'expiry':
                    t = time.time()
                    cookie[k] = int(t)
        driver2.add_cookie({k: cookie[k] for k in {'name', 'value', 'domain', 'path', 'expiry'}})
    # driver.close()
    driver2.get(urll)
    print(driver2.get_cookies())

    time.sleep(5)
    # js = "var q=document.body.scrollTop=10000"
    # driver2.execute_script(js)


    path = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div'
    ele = driver2.find_element(By.XPATH, path)
    data = ele.get_attribute("style")
    data = int(data[32:37].strip('px').strip(')').strip('p').strip('px);'))
    print(data)

    time.sleep(3)

    list1 = []
    try:
        try:
            for i in range(1,30):
                aa = []
                path_all = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[{}]'.format(i)
                ele_ = driver2.find_element(By.XPATH,path_all)
                driver2.execute_script("arguments[0].scrollIntoView();", ele_)
                data_ = ele_.get_attribute("style")
                data__ = data_[22:27].strip('px').strip(')').strip('p').strip('px);')
                print(data__)
                driver2.execute_script("window.scrollTo(0,{})".format(data__))
                time.sleep(3)


                path_user = '/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/a/div/div[1]/span/span'
                ele_user = driver2.find_element(By.XPATH, path_all + path_user)
                data_user = ele_user.get_attribute("textContent")


                # print(data_user)
                aa.append(data_user)
                try:
                    path_forward = '/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/div[2]/span/span/span'
                    ele_forward = driver2.find_element(By.XPATH, path_all + path_forward)
                    data_forward = ele_forward.get_attribute("textContent")
                    # print(data_forward)
                    aa.append(data_forward)
                except:
                    forward = '0'
                    aa.append(forward)
                try:
                    path_love = '/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div[2]/span/span/span'
                    ele_love = driver2.find_element(By.XPATH, path_all + path_love)
                    data_love = ele_love.get_attribute("textContent")
                    # print(data_love)
                    aa.append(data_love)
                except:
                    love = '0'
                    aa.append(love)
                try:
                    path_comment = '/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/div/div[2]/span/span/span'
                    ele_comment = driver2.find_element(By.XPATH, path_all + path_comment)
                    data_comment = ele_comment.get_attribute("textContent")
                    # print(data_comment)
                    aa.append(data_comment)
                except:
                    comment = '0'
                    aa.append(comment)
                path_time = '/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[3]/a/time'
                ele_time = driver2.find_element(By.XPATH, path_all + path_time)
                data_time = ele_time.get_attribute("datetime")
                # print(data_time)###str
                aa.append(data_time)
                # div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span[2]
                content = '/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div'
                ele_content = driver2.find_element(By.XPATH, path_all + content)
                data_content = ele_content.get_attribute("textContent")
                # print(data_content)
                aa.append(data_content)
                list1.append(aa)
                print(list1)
                name = ['name', 'forward-number', 'thumbs-up-number', 'comment-number', 'date', 'content']
                test = pd.DataFrame(columns=name, data=list1)
                test.to_csv('testcsv.csv', mode='a+')


                # csv_file = open('twitter.csv', 'w', newline='', encoding='gbk')
                # writer = csv.writer(csv_file)
                # writer.writerow([' 1', ' 2','3','4','5','6','7'])
        except:
            driver2.execute_script("window.scrollTo(0,10000)")
            time.sleep(5)

            for i in range(7,16):
                aa = []
                path_all = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[{}]'.format(i)
                ele_ = driver2.find_element(By.XPATH,path_all)
                driver2.execute_script("arguments[0].scrollIntoView();", ele_)
                data_ = ele_.get_attribute("style")
                data__ = data_[22:27].strip('px').strip(')').strip('p').strip('px);')
                print(data__)
                driver2.execute_script("window.scrollTo(0,{})".format(data__))
                time.sleep(3)
                path_user = '/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/a/div/div[1]/span/span'
                ele_user = driver2.find_element(By.XPATH, path_all + path_user)
                data_user = ele_user.get_attribute("textContent")


                # print(data_user)
                aa.append(data_user)
                try:
                    path_forward = '/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/div[2]/span/span/span'
                    ele_forward = driver2.find_element(By.XPATH, path_all + path_forward)
                    data_forward = ele_forward.get_attribute("textContent")
                    # print(data_forward)
                    aa.append(data_forward)
                except:
                    forward = '0'
                    aa.append(forward)
                try:
                    path_love = '/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div[2]/span/span/span'
                    ele_love = driver2.find_element(By.XPATH, path_all + path_love)
                    data_love = ele_love.get_attribute("textContent")
                    # print(data_love)
                    aa.append(data_love)
                except:
                    love = '0'
                    aa.append(love)
                try:
                    path_comment = '/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/div/div[2]/span/span/span'
                    ele_comment = driver2.find_element(By.XPATH, path_all + path_comment)
                    data_comment = ele_comment.get_attribute("textContent")
                    # print(data_comment)
                    aa.append(data_comment)
                except:
                    comment = '0'
                    aa.append(comment)
                path_time = '/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[3]/a/time'
                ele_time = driver2.find_element(By.XPATH, path_all + path_time)
                data_time = ele_time.get_attribute("datetime")
                # print(data_time)###str
                aa.append(data_time)
                # div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span[2]
                content = '/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div'
                ele_content = driver2.find_element(By.XPATH, path_all + content)
                data_content = ele_content.get_attribute("textContent")
                # print(data_content)
                aa.append(data_content)
                list1.append(aa)
                print(list1)
                name = ['name', 'forward-number', 'thumbs-up-number', 'comment-number', 'date', 'content']
                test = pd.DataFrame(columns=name, data=list1)
                test.to_csv('testcsv.csv', mode='a+')

                # csv_file = open('twitter.csv', 'w', newline='', encoding='gbk')
                # writer = csv.writer(csv_file)
                # writer.writerow([' 1', ' 2','3','4','5','6','7'])
        finally:
            driver2.execute_script("window.scrollTo(0,{})".format(data))
            for i in range(5,16):
                aa = []
                path_all = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[{}]'.format(i)
                ele_ = driver2.find_element(By.XPATH,path_all)
                driver2.execute_script("arguments[0].scrollIntoView();", ele_)
                data_ = ele_.get_attribute("style")
                data__ = data_[22:27].strip('px').strip(')').strip('p').strip('px);')
                print(data__)
                driver2.execute_script("window.scrollTo(0,{})".format(data__))
                time.sleep(3)
                path_user = '/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/a/div/div[1]/span/span'
                ele_user = driver2.find_element(By.XPATH, path_all + path_user)
                data_user = ele_user.get_attribute("textContent")


                # print(data_user)
                aa.append(data_user)
                try:
                    path_forward = '/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/div[2]/span/span/span'
                    ele_forward = driver2.find_element(By.XPATH, path_all + path_forward)
                    data_forward = ele_forward.get_attribute("textContent")
                    # print(data_forward)
                    aa.append(data_forward)
                except:
                    forward = '0'
                    aa.append(forward)
                try:
                    path_love = '/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div[2]/span/span/span'
                    ele_love = driver2.find_element(By.XPATH, path_all + path_love)
                    data_love = ele_love.get_attribute("textContent")
                    # print(data_love)
                    aa.append(data_love)
                except:
                    love = '0'
                    aa.append(love)
                try:
                    path_comment = '/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/div/div[2]/span/span/span'
                    ele_comment = driver2.find_element(By.XPATH, path_all + path_comment)
                    data_comment = ele_comment.get_attribute("textContent")
                    # print(data_comment)
                    aa.append(data_comment)
                except:
                    comment = '0'
                    aa.append(comment)
                path_time = '/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[3]/a/time'
                ele_time = driver2.find_element(By.XPATH, path_all + path_time)
                data_time = ele_time.get_attribute("datetime")
                # print(data_time)###str
                aa.append(data_time)
                # div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span[2]
                content = '/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div'
                ele_content = driver2.find_element(By.XPATH, path_all + content)
                data_content = ele_content.get_attribute("textContent")
                # print(data_content)
                aa.append(data_content)
                list1.append(aa)
                print(list1)
                name = ['name', 'forward-number', 'thumbs-up-number', 'comment-number', 'date', 'content']
                test = pd.DataFrame(columns=name, data=list1)
                test.to_csv('testcsv.csv', mode='a+')

                # csv_file = open('twitter.csv', 'w', newline='', encoding='gbk')
                # writer = csv.writer(csv_file)
                # writer.writerow([' 1', ' 2','3','4','5','6','7'])

    except:

        pass




'''
    
    time.sleep(5)
    driver2.execute_script("window.scrollTo(0,10000)")
    time.sleep(5)
    driver2.execute_script("window.scrollTo(0,12000)")
    time.sleep(5)
    driver2.execute_script("window.scrollTo(0,13000)")
    time.sleep(5)
    driver2.execute_script("window.scrollTo(0,14000)")
    time.sleep(5)
    driver2.execute_script("window.scrollTo(0,15000)")
    list1 = []
    try:
        for i in range(1, 10):
            aa = []
            path_all = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[{}]/'.format(
                i)  # /html/body/div[6]/div[2]/div[2]/div/ul[1]/li[1]/a/span
            path_user = 'div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/a/div/div[1]/span/span'
            ele_user = driver2.find_element(By.XPATH, path_all + path_user)
            data_user = ele_user.get_attribute("textContent")

            driver2.execute_script("arguments[0].scrollIntoView();", ele_user)
            # print(data_user)
            aa.append(data_user)
            try:
                path_forward = 'div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/div[2]/span/span/span'
                ele_forward = driver2.find_element(By.XPATH, path_all + path_forward)
                data_forward = ele_forward.get_attribute("textContent")
                # print(data_forward)
                aa.append(data_forward)
            except:
                forward = '0'
                aa.append(forward)
            try:
                path_love = 'div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div[2]/span/span/span'
                ele_love = driver2.find_element(By.XPATH, path_all + path_love)
                data_love = ele_love.get_attribute("textContent")
                # print(data_love)
                aa.append(data_love)
            except:
                love = '0'
                aa.append(love)
            try:
                path_comment = 'div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/div/div[2]/span/span/span'
                ele_comment = driver2.find_element(By.XPATH, path_all + path_comment)
                data_comment = ele_comment.get_attribute("textContent")
                # print(data_comment)
                aa.append(data_comment)
            except:
                comment = '0'
                aa.append(comment)
            path_time = 'div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[3]/a/time'
            ele_time = driver2.find_element(By.XPATH, path_all + path_time)
            data_time = ele_time.get_attribute("datetime")
            # print(data_time)###str
            aa.append(data_time)
            # div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span[2]
            content = 'div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div'
            ele_content = driver2.find_element(By.XPATH, path_all + content)
            data_content = ele_content.get_attribute("textContent")
            # print(data_content)
            aa.append(data_content)
            list1.append(aa)
            print(list1)
            name = ['name', 'forward-number', 'thumbs-up-number', 'comment-number', 'date', 'content']
            test = pd.DataFrame(columns=name, data=list1)
            test.to_csv('testcsv.csv',  mode='a+')

            # csv_file = open('twitter.csv', 'w', newline='', encoding='gbk')
            # writer = csv.writer(csv_file)
            # writer.writerow([' 1', ' 2','3','4','5','6','7'])
        # writer.writerow(aa)
        # csv_file.close()
    except:
        pass
    time.sleep(5)
    js = "var q=document.body.scrollTop=12000"
    driver2.execute_script(js)
    time.sleep(5)
    print('11111111111111111111111111111111')
    driver2.execute_script("window.scrollTo(0,11000)")


'''
