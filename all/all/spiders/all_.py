import scrapy
import re
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions,Chrome
from tqdm import trange
import ftfy
import time
import datetime
import os
from datetime import datetime
from pyhtml2pdf import converter
from pymongo import MongoClient
from all.items import AllItem
from selenium import webdriver
from all.settings import MONGODB_URL
from all.settings import USER_AGENT
import pdfkit
import difflib
import Levenshtein
import string
import minio
from minio import Minio
class AllSpider(scrapy.Spider):###        scrapy crawl all_
    name = 'all_'
    allowed_domains = ['www.sec.gov']
    start_urls = ['https://www.sec.gov/edgar/browse/?CIK=1804583&owner=exclude']
    url = 'https://www.sec.gov/edgar/search/#/q='
    urls = 'https://www.sec.gov/edgar/search/#/entityName='
    urlss = 'https://www.sec.gov/edgar/search/#/dateRange=all&entityName='
    urlsss = 'https://www.sec.gov/Archives/edgar/data/'


    URL = 'https://www.sec.gov/edgar/browse/?CIK=1804583&owner=exclude'

    minio_conf = {
        'endpoint': 'http://140.24.1.107:29000',
        'access_key': 'minioadmin',
        'secret_key': 'minioadmin',
        'secure': False
    }





    ###        scrapy crawl all_
    def parse(self, response):
        options = ChromeOptions()
        #options.add_argument("--headless")
        #option = ChromeOptions()
        #请求头出问题了
        #options.add_argument(f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36')


        options.add_experimental_option('excludeSwitches', ['enable - logging']) ###这句代码很重要，不太清楚为什么加上这句代码就可以查询数据了
        #设置开发者模式启动
        self.driver = webdriver.Chrome(options=options)

        self.client = MongoClient(MONGODB_URL)
        DB = self.client['collect_data']
        mycol11 = DB['ent_info_fws']

        for a in mycol11.find({}, {'_id': 0, 'ent_ename': 1,'ent_cname':1,'cid':1}).limit(1).skip(164):#######连接数据库的第一个表
            Z = a['ent_ename']
            B = str(a['ent_cname']).strip()####数据库有空字符导致运行pdf下载不了
            C = a['cid']
            mycol = DB['ent_detail_fws']


            for i in mycol.find({}, {'_id': 0, 'stk_code': 1, 'cid': 1}).limit(170).skip(1):###三个数据库表的选择匹配
                if a['cid'] == i['cid']:
                    A = i['stk_code']
                    D = {}
                    DB = self.client['collect_data']
                    mycol1 = DB['list_ent_anns']
                    for l in mycol1.find({}, {'_id': 0, 'related_id': 1, 'cid': 1}):
                        if i['cid'] == l['cid']:
                            C = l['related_id']
                            D.setdefault('AA', []).append(C)
                            E = D['AA']
                    f = []
                    for m in E:
                        if m not in f:
                            f.append(m)
                    #print(f)

                    c = f[0]
                    #print(c[13:13+len(A)])
                    if c[13:13+len(A)] ==A:
                        L = c








            url = self.url+Z
            #print(url)
            upprr = str(Z).title()
            self.driver.get(url=url)
            ###        scrapy crawl all_

        #self.driver.get(self.start_urls[0]) #这句话是必须要有的，不然无法使用接下来的cookie
            from_driver_cookie = [
                {'domain': 'sec.gov', 'httpOnly': False, 'name': '__utma', 'path': '/', 'secure': False,
                    'value': '27389246.276973811.1659496272.1660022790.1660022790.1'},
                {'domain': 'sec.gov', 'httpOnly': True, 'name': 'ak_bmsc', 'path': '/',
                    'secure': True,
                    'value': '40E7317FF13AF46476A23721B5E7C019~000000000000000000000000000000~YAAQTS43F7Aau+aDAQAA1b5v8xH72KuAQ+Ug3oc/FGuCQ/cphzEuDAeQ9z2F3XaQm9ZM5QvUFTV2zWUHiGNdus0s21KJMkRaHSi9HrptqUGa7V+qoiAJPkim0lMVZfZ5graWeuBsWtdW7lo7C0SNXVkkIWHmoX7hcPsJ6GJpSH2cpz37QYlWCC6WGBKxQCyLTyw2lCsJeVqF8v4ORTbxNt4gSc/N9OaeAJWNlOZCz8U8xMUyRwFTjjBd0RcnYQO1NoKwo7sdk4ChZLgQxH3nR5ZfTO/3zyl4qEss3oqBVl+3LpgV0meQbAX8UWhuhgZWKm7Yh6c477z1zoj7FpPnyVfKxEH56T3jkbzoHZvm7rNw4/APqviVNj8C8TCQqtuXx5yvV36baJW2'}]


            self.driver.add_cookie(cookie_dict=from_driver_cookie[1])

            #self.driver.get(url=self.URL)

#######  scrapy crawl all_
            time.sleep(3)
            path_cik = '/html/body/div[3]/div[2]/div[2]/div[2]/fieldset/div[3]'
            ele_cik = self.driver.find_element(By.XPATH, path_cik)
            ele_cik_click = ele_cik.click()
            data_clk = ele_cik.get_attribute("textContent")

            ###        scrapy crawl all_

            try:
                #####获取公司名称##############相似度匹配
                for p in range(1,10):
                    path = '/html/body/div[3]/div[2]/div[2]/table/tbody/tr[{}]/'.format(p)
                    path_company = 'td[4]'
                    ele_company = self.driver.find_element(By.XPATH,path+path_company)
                    data_company = ele_company.get_attribute("textContent").title()
                    #print(data_company)
                    AAA = difflib.SequenceMatcher(None, data_company,upprr).ratio()
                    #print(AAA)

                    path_cik = 'td[5]'
                    ele_cik = self.driver.find_element(By.XPATH,path+ path_cik)
                    data_clksss = ele_cik.get_attribute("textContent")
                    data_clksssss = data_clksss.replace(' ','%')
                    #print(len(data_clksssss))
                    data_clkss = data_clksssss[0:14]
                    #print(data_clkss)


                    ###cik添加
                    b = '2520'
                    str_list = list(data_clkss)
                    str_list.insert(4, b)
                    a_b = ''.join(str_list)
                    ####获得clk后七位
                    data_clkss_number = data_clksss[7:14]
                    #print(data_clkss_number)
                    #print(data_clkss)
                    if AAA > float(0.4):
                        mm = 0
                        for v in range(1,4):
                            mm = mm+1
                            mmm = str(mm)
                            page = '&page={}'.format(v)
                            urlss = self.urlss+a_b+page
                            print(a_b)
                            print(urlss)
                            self.driver.get(url=urlss)
                            time.sleep(1)
                            print(url)
                            ia = 0
                            try:
                                ######确认是否有结果
                                path_mio = '/html/body/div[3]/div[1]/div/h4'
                                ele_mio = self.driver.find_element(By.XPATH, path_mio)
                                data_mio = ele_mio.get_attribute("textContent")
                                string_mio = 'No results found for your search!'
                                print('asddddasdasdddddd')
                                self.driver.refresh()
                                if data_mio == string_mio:
                                    print("asdascxvytyrtyrtuuiyiuyiyuiyu")
                                    break
                                else:
                                    try:
                                        self.driver.refresh()
                                        for i in range(1, 101):
                                            try:
                                                time.sleep(1)
                                                ia = ia + 1
                                                iaa = str(ia)
                                                path_all = '/html/body/div[3]/div[2]/div[2]/table/tbody/tr[{}]/'.format(
                                                    i)
                                                path_ann_type = 'td[1]/a'
                                                ele_ann_type = self.driver.find_element(By.XPATH,
                                                                                        path_all + path_ann_type)
                                                data_ann_type = ele_ann_type.get_attribute("textContent")
                                                publisher = B + '官网'
                                                source = '美国证券交易委员会'
                                                # print(data_ann_type)
                                                ####date
                                                try:  # /html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[5]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span[6]
                                                    try:
                                                        path_ann_data1 = 'td[3]'
                                                        ele_ann_data1 = self.driver.find_element(By.XPATH,
                                                                                                 path_all + path_ann_data1)
                                                        data_ann_data1 = ele_ann_data1.get_attribute("textContent")
                                                        # print(data_ann_data1)
                                                        aaa = len(data_ann_data1)
                                                        aaa > 2
                                                        path_a = 'td[1]/a'
                                                        ele_a = self.driver.find_element(By.XPATH, path_all + path_a)
                                                        data_aa = ele_a.get_attribute("data-adsh")
                                                        ##去掉-
                                                        data_a = re.sub('-', '', data_aa)
                                                        data_b = ele_a.get_attribute("data-file-name")
                                                        # print(data_a,data_b)
                                                        url_public = self.urlsss + data_clkss_number + '/' + data_a + '/' + data_b
                                                        # print(url_public)
                                                        self.driver.get(url=url_public)
                                                        iia = str(ia)
                                                        aAA = str(mmm + iia + B + data_ann_data1 + '.pdf')
                                                        # print(aAA)
                                                        bB = 'http://140.24.1.107:29000/pcdd/%s' % aAA
                                                        s = '[' + '{' + '"' + 'name' + '"' + ':' + '"' + aAA + '"' + ',' + '"' + 'url' + '"' + ':' + '"' + bB + '"'
                                                        print(s)
                                                        # 数据更新日期
                                                        date_now__ = datetime.today()
                                                        date_now = str(date_now__.now())
                                                        # print(date_now)
                                                        #######  scrapy crawl all_
                                                        ###开始进行pdf保存
                                                        path_wkthmltopdf = r'D:\\wkhtmltopdf\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
                                                        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
                                                        print('asdasdasdasdsaasd')
                                                        time.sleep(2)
                                                        pdfkit.from_url(url_public, r"E:\PDFs\%s%s%s%s.pdf" % (
                                                        mmm, iaa, B, data_ann_data1), configuration=config)
                                                        print('okkkkkkkkkkkkkk')
                                                        ###content——————————————————pdf
                                                        content = []
                                                        try:
                                                            for i in range(3, 25):
                                                                path_content = '/html/body/div[2]/div/div[2]/div[{}]'.format(
                                                                    i)
                                                                element_content = self.driver.find_element(By.XPATH,
                                                                                                           path_content)
                                                                data_content = element_content.get_attribute(
                                                                    "textContent")
                                                                # print(data_content)
                                                                content.append(data_content)
                                                        except:
                                                            pass
                                                        try:
                                                            for i in range(3, 55):
                                                                path_content = '/html/body/document/type/sequence/filename/description/text/center[1]/div/p[{}]'.format(
                                                                    i)
                                                                element_content = self.driver.find_element(By.XPATH,
                                                                                                           path_content)
                                                                data_content = element_content.get_attribute(
                                                                    "textContent")
                                                                # print(data_content)
                                                                content.append(data_content)
                                                                # print(content)
                                                        except:
                                                            pass
                                                        # print(content)
                                                        Q = ''
                                                        items = AllItem()
                                                        items['cid'] = C
                                                        items['company'] = B
                                                        items['ann_content'] = content
                                                        items['ann_title'] = Q
                                                        items['ann_date'] = data_ann_data1
                                                        items['ann_addr'] = url_public
                                                        items['publisher'] = publisher
                                                        items['source'] = source
                                                        items['data_update_date'] = date_now
                                                        items['related_id'] = L
                                                        items['attachment'] = s
                                                        items['ann_type'] = data_ann_type
                                                        yield items
                                                        # print(items)
                                                        time.sleep(2)
                                                        self.driver.back()
                                                    except:
                                                        path_ann_data2 = 'td[2]'
                                                        ele_ann_data2 = self.driver.find_element(By.XPATH,
                                                                                                 path_all + path_ann_data2)
                                                        data_ann_data2 = ele_ann_data2.get_attribute("textContent")
                                                        # print(data_ann_data1)
                                                        aaa = len(data_ann_data2)
                                                        aaa > 2
                                                        path_a = 'td[1]/a'
                                                        ele_a = self.driver.find_element(By.XPATH, path_all + path_a)
                                                        data_aa = ele_a.get_attribute("data-adsh")
                                                        ##去掉-
                                                        data_a = re.sub('-', '', data_aa)
                                                        data_b = ele_a.get_attribute("data-file-name")
                                                        # print(data_a,data_b)
                                                        url_public = self.urlsss + data_clkss_number + '/' + data_a + '/' + data_b
                                                        # print(url_public)
                                                        self.driver.get(url=url_public)
                                                        iia = str(ia)
                                                        aAA = str(mmm + iia + B + data_ann_data2 + '.pdf')
                                                        # print(aAA)
                                                        bB = 'http://140.24.1.107:29000/pcdd/%s' % aAA
                                                        s = '[' + '{' + '"' + 'name' + '"' + ':' + '"' + aAA + '"' + ',' + '"' + 'url' + '"' + ':' + '"' + bB + '"'
                                                        print(s)
                                                        # 数据更新日期
                                                        date_now__ = datetime.today()
                                                        date_now = str(date_now__.now())
                                                        # print(date_now)
                                                        #######  scrapy crawl all_
                                                        ###开始进行pdf保存
                                                        path_wkthmltopdf = r'D:\\wkhtmltopdf\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
                                                        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
                                                        print('asdasdasdasdsaasd')
                                                        time.sleep(2)
                                                        pdfkit.from_url(url_public,
                                                                        r"E:\PDFs\%s%s%s%s.pdf" % (
                                                                        mmm, iaa, B, data_ann_data2),
                                                                        configuration=config)
                                                        print('okkkkkkkkkkkkkk')
                                                        ###content——————————————————pdf
                                                        content = []
                                                        try:
                                                            for i in range(3, 25):
                                                                path_content = '/html/body/div[2]/div/div[2]/div[{}]'.format(
                                                                    i)
                                                                element_content = self.driver.find_element(By.XPATH,
                                                                                                           path_content)
                                                                data_content = element_content.get_attribute(
                                                                    "textContent")
                                                                # print(data_content)
                                                                content.append(data_content)
                                                        except:
                                                            pass
                                                        try:
                                                            for i in range(3, 55):
                                                                path_content = '/html/body/document/type/sequence/filename/description/text/center[1]/div/p[{}]'.format(
                                                                    i)
                                                                element_content = self.driver.find_element(By.XPATH,
                                                                                                           path_content)
                                                                data_content = element_content.get_attribute(
                                                                    "textContent")
                                                                # print(data_content)
                                                                content.append(data_content)
                                                                # print(content)
                                                        except:
                                                            pass
                                                        # print(content)
                                                        Q = ''
                                                        items = AllItem()
                                                        items['cid'] = C
                                                        items['company'] = B
                                                        items['ann_content'] = content
                                                        items['ann_title'] = Q
                                                        items['ann_date'] = data_ann_data2
                                                        items['ann_addr'] = url_public
                                                        items['publisher'] = publisher
                                                        items['source'] = source
                                                        items['data_update_date'] = date_now
                                                        items['related_id'] = L
                                                        items['attachment'] = s
                                                        items['ann_type'] = data_ann_type
                                                        yield items
                                                        # print(items)
                                                        time.sleep(4)
                                                        self.driver.back()
                                                except:
                                                    self.driver.back()
                                            except:
                                                pass


                                    except:
                                        pass

                                #####
                            except:
                                print('asdasdfgvbcvbnbbvnvbmnvbmbvmbvmb')





                        break
                    else:
                        continue


            except:
                pass
        self.driver.quit()
#######  scrapy crawl all_
###程序从533行开始执行












'''


                    for i in range(1,50):
                        path_Filing_entity_person_url = '//*[@id="hits"]/table/tbody/tr[1]/td[{}]/a'.format(i)
                        element_Filing_url = self.driver.find_element(By.XPATH,path_Filing_entity_person_url)
                        data_Filing_url = element_Filing_url.get_attribute("href")
                        print("84484894123")
                        self.driver.get(data_Filing_url)







                    for o in range(1,45):
                        path_all_url = '/html/body/div[4]/div[4]/table/tbody/tr[{}]/td[2]/a[1]'.format(o)
                        element_all_url = self.driver.find_element(By.XPATH,path_all_url)
                        element_all_url.click()

                        path_ann_type = '//*[@id="formDiv"]/div/table/tbody/tr[2]/td[4]'
                        element_ann_type = self.driver.find_element(By.XPATH,path_ann_type)
                        data_ann_type = element_ann_type.get_attribute("textContent")
                        print(data_ann_type)

                        path_ann_date = '//*[@id="formDiv"]/div[2]/div[2]/div[2]/font/font'
                        element_ann_date = self.driver.find_element(By.XPATH,path_ann_date)
                        data_ann_date = element_ann_date.get_attribute("textContent")
                        print(data_ann_date)

                        path_ann_addr = '//*[@id="formDiv"]/div/table/tbody/tr[2]/td[3]/a'
                        element_ann_addr = self.driver.find_element(By.XPATH,path_ann_addr)
                        data_ann_addr = element_ann_addr.get_attribute("href")
                        print(data_ann_addr)

                        element_ann_addr.click()
                        path_ann_addr_content ='/html/body/document/type/sequence/filename/description/text/div[1]'
                        element_addr_content = self.driver.find_element(By.XPATH,path_ann_addr_content)
                        content = element_addr_content.get_attribute("textContent")
                        print(content)



                        company = A  ##################################################数据库的company
                        source = 'sec备案'
                        publisher = 'sec备案'

                        item = AllItem()


                        ######退出content标签页，并返回之前标签页
                        self.driver.close()
                        time.sleep(3)
                        self.driver.back()


                    next_page = '//*[@id="contentDiv"]/div[5]/form/table/tbody/tr/td/input'
                    element_next_page = self.driver.find_element(By.XPATH,next_page)
                    element_next_page.click()
                    self.driver.implicitly_wait(3)








                else:
                    pass


'''



###        scrapy crawl all_
