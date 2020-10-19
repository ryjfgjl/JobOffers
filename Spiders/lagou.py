import requests
from bs4 import BeautifulSoup
import json
from Spiders.sql import Sql
import time

from selenium import webdriver
from selenium.webdriver import ActionChains


Sql = Sql()
driver = webdriver.Chrome()
db_conn = Sql.conn_db('')
base_url = 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE?px=new&gx=%E5%85%A8%E8%81%8C&city=%E6%88%90%E9%83%BD#order'
driver.get(base_url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
total_page = soup.find('span', 'totalNum')
total_page = int(total_page.get_text())



for page in range(total_page):
    positions = driver.find_elements_by_xpath('//div[@id="s_position_list"]/ul/li[*]/div/div/div/a/h3')
    for position in positions:
        actions = ActionChains(driver)
        actions.move_to_element(position)
        actions.click(position)
        actions.perform()
        driver.switch_to.window(driver.window_handles[1])
        html = driver.page_source
        driver.close()
        driver.switch_to.window(driver.window_handles[0])




    response = session.post(url=data_url, headers=headers, data=data)
    response.encoding = 'utf8'
    html = response.text
    positions = json.loads(html)['content']['positionResult']['result']
    showId = json.loads(html)['content']['showId']
    s = 0
    for position in positions:
        print(position)
        positionId = position['positionId']
        positionName = position['positionName']
        companyId = position['companyId']
        companyFullName = position['companyFullName']
        companyShortName = position['companyShortName']
        companySize = position['companySize']
        industryField = position['industryField']
        financeStage = position['financeStage']
        companyLabelList = position['companyLabelList']
        firstType = position['firstType']
        secondType = position['secondType']
        thirdType = position['thirdType']
        skillLables = position['skillLables']
        positionLables = position['positionLables']
        industryLables = position['industryLables']
        createTime = position['createTime']
        city = position['city']
        district = position['district']
        salary = position['salary']
        salaryMonth = position['salaryMonth']
        workYear = position['workYear']
        jobNature = position['jobNature']
        education = position['education']
        positionAdvantage = position['positionAdvantage']
        subwayline = position['subwayline']
        stationname = position['stationname']
        linestaion = position['linestaion']
        isSchoolJob = position['isSchoolJob']

        """
        detail_url = 'https://www.lagou.com/jobs/{}.html?show={}'.format(positionId, showId)
        driver.get(detail_url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        
        try:
            jobAdvantage = soup.find('dd', 'job-advantage').find('p').get_text()
            jobDescription = soup.find('dd', 'job_bt').find('div', 'job-detail').get_text()
            workAddr = soup.find('div', 'work_addr').get_text()
            print('Complete')
        except:
            print(html)
            print('Failed')"""

    print(page)




    session.close()











c1 = "user_trace_token=20200817155304-6c61f340-342a-44fe-932b-53f6a390cca2; _ga=GA1.2.969164119.1597650793; LGUID=20200817155314-19d8910e-8a4b-49c9-b580-1c48f11f460a; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=17; privacyPolicyPopup=false; index_location_city=%E6%88%90%E9%83%BD; RECOMMEND_TIP=true; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221752b4e8ae261-0627acd84b7736-383e570a-1440000-1752b4e8ae39a9%22%2C%22%24device_id%22%3A%221752b4e8ae261-0627acd84b7736-383e570a-1440000-1752b4e8ae39a9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=ABAAABAABAGABFA27029468A4B8FFE71BDEEE7D3B172913; WEBTJ-ID=20201019100843-1753e9db1ffa87-05501286d98254-383e570a-1440000-1753e9db2009dd; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1602749358,1602815600,1603073324; _gid=GA1.2.1630139589.1603073324; TG-TRACK-CODE=search_code; LGSID=20201019142523-a08d6476-faa5-4c18-b3aa-a43d4e21cd71; _gat=1; login=false; unick=""; _putrc=""; SEARCH_ID=36768b8ea59b4e1fb347a127cf2588e4; X_HTTP_TOKEN=427f33ba8b88041e79129030617637e509131b7d2d; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1603092196; LGRID=20201019152317-e3f28784-3adb-47e6-8664-a523e4ee7308"
c2 = "user_trace_token=20200817155304-6c61f340-342a-44fe-932b-53f6a390cca2; _ga=GA1.2.969164119.1597650793; LGUID=20200817155314-19d8910e-8a4b-49c9-b580-1c48f11f460a; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=17; privacyPolicyPopup=false; index_location_city=%E6%88%90%E9%83%BD; RECOMMEND_TIP=true; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221752b4e8ae261-0627acd84b7736-383e570a-1440000-1752b4e8ae39a9%22%2C%22%24device_id%22%3A%221752b4e8ae261-0627acd84b7736-383e570a-1440000-1752b4e8ae39a9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=ABAAABAABAGABFA27029468A4B8FFE71BDEEE7D3B172913; WEBTJ-ID=20201019100843-1753e9db1ffa87-05501286d98254-383e570a-1440000-1753e9db2009dd; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1602749358,1602815600,1603073324; _gid=GA1.2.1630139589.1603073324; TG-TRACK-CODE=search_code; LGSID=20201019142523-a08d6476-faa5-4c18-b3aa-a43d4e21cd71; _gat=1; login=false; unick=""; _putrc=""; SEARCH_ID=7a956f6c3db04492828c0b75a104b231; X_HTTP_TOKEN=427f33ba8b88041e58129030617637e509131b7d2d; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1603092184; LGRID=20201019152305-f1d2d97f-e5df-4048-8582-b4a06d37022a"
v1 = "user_trace_token=20200817155304-6c61f340-342a-44fe-932b-53f6a390cca2; _ga=GA1.2.969164119.1597650793; LGUID=20200817155314-19d8910e-8a4b-49c9-b580-1c48f11f460a; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=17; privacyPolicyPopup=false; index_location_city=%E6%88%90%E9%83%BD; RECOMMEND_TIP=true; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221752b4e8ae261-0627acd84b7736-383e570a-1440000-1752b4e8ae39a9%22%2C%22%24device_id%22%3A%221752b4e8ae261-0627acd84b7736-383e570a-1440000-1752b4e8ae39a9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=ABAAABAABAGABFA27029468A4B8FFE71BDEEE7D3B172913; WEBTJ-ID=20201019100843-1753e9db1ffa87-05501286d98254-383e570a-1440000-1753e9db2009dd; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1602749358,1602815600,1603073324; _gid=GA1.2.1630139589.1603073324; TG-TRACK-CODE=search_code; LGSID=20201019142523-a08d6476-faa5-4c18-b3aa-a43d4e21cd71; _gat=1; login=false; unick=""; _putrc=""; X_HTTP_TOKEN=427f33ba8b88041e58129030617637e509131b7d2d; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1603092184; LGRID=20201019152305-f1d2d97f-e5df-4048-8582-b4a06d37022a; SEARCH_ID=36768b8ea59b4e1fb347a127cf2588e4"

