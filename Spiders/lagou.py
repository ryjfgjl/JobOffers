
from bs4 import BeautifulSoup
from datetime import datetime, date
from sql import Sql
import time
import random
import os, sys
import pymysql

from selenium import webdriver
from selenium.webdriver import ActionChains

import smtplib
from email.mime.text import MIMEText
from email.header import Header


Sql = Sql()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

db_conn = Sql.conn_db('joboffers')
base_url = 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE?px=new&gx=%E5%85%A8%E8%81%8C&city=%E6%88%90%E9%83%BD#order'
driver.get(base_url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
total_page = soup.find('span', 'totalNum')
total_page = int(total_page.get_text())

keyWord = '数据'
createTime = datetime.now()
sql_path = os.path.split(os.path.realpath(sys.argv[0]))[0]
dataclean = sql_path + r'\clean.sql'
error_position = sql_path+r'\error_position.sql'
with open(error_position, 'w') as f:
    f.truncate()

for page in range(total_page):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    positions = soup.find(id="s_position_list").find('ul').find_all('li', 'con_list_item')

    for index in range(len(positions)):
        sql = ''
        try:
            position = positions[index]
            positionId = position['data-positionid']
            salary = position['data-salary']
            companyName = position['data-company']
            positionName = position['data-positionname']
            if 'java' in positionName or '实习生' in positionName or 'hadoop' in positionName or 'Oracle' in positionName:
                continue
            companyId = position['data-companyid']
            positionLink = position.find('a', 'position_link')['href']
            district = position.find('a', 'position_link').find('span', 'add').get_text()

            publishTime = position.find('div', 'position').find('span', 'format-time').get_text()
            workYear = position.find('div', 'position').find('div', 'p_bot').find('div', 'li_b_l').get_text().split('/')[0].split('\n')[-1].strip()
            if workYear not in ('经验3-5年', '经验1-3年', '经验不限', '经验1年以下'):
                continue
            education = position.find('div', 'position').find('div', 'p_bot').find('div', 'li_b_l').get_text().split('/')[-1].strip()
            if education in ('硕士', '博士'):
                continue
            industry = position.find('div', 'company').find('div', 'industry').get_text().strip()
            skillLables = position.find('div', 'list_item_bot').find('div', 'li_b_l').find_all('span')
            skillLables = ' | '.join([skillLable.get_text() for skillLable in skillLables])

            companyLabeles = position.find('div', 'list_item_bot').find('div', 'li_b_r').get_text()[1:-2]

            position = driver.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[{}]/div[1]/div[1]/div[1]/a/h3'.format(index+1))
            actions = ActionChains(driver)
            actions.move_to_element(position)
            actions.click(position)
            actions.perform()
            time.sleep(random.randrange(3, 8))
            driver.switch_to.window(driver.window_handles[1])
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            jobDetail = soup.find(id='job_detail').find('dd', 'job_bt').find('div', 'job-detail').get_text().replace('"',"'")
            jobAddr = soup.find(id='job_detail').find('dd', 'job-address').find('div', 'work_addr').get_text()

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

            sql = 'insert into lagou_job(positionId,salary,companyName,positionName,companyId,positionLink,district,publishTime,workYear,education,industry,skillLables,companyLabeles,jobDetail,jobAddr,keyWord,createTime) ' \
                  'values ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}");'.format(
                positionId, salary, companyName, positionName, companyId, positionLink, district, publishTime, workYear,
                education, industry, skillLables, companyLabeles, jobDetail, jobAddr,keyWord,createTime
            )
            Sql.exec_sql(db_conn, sql)
            print(positionName, 'Complete')
        except pymysql.err.ProgrammingError as reason:
            sql = sql + '\n'
            with open(sql_path+r'\error_position.sql', 'a+', encoding='utf8') as fa:
                fa.write(sql)
            print('sql ProgrammingError')
        except Exception as reason:
            print(str(reason))

    next_page = driver.find_element_by_class_name('pager_next ')
    next_page.click()
    time.sleep(random.randrange(3,4))
driver.close()

# sql script
cmd = 'mysql -uroot -proot joboffers --default-character-set=utf8 < {}'.format(error_position)
os.system(cmd)
cmd = 'mysql -uroot -proot joboffers --default-character-set=utf8 < {}'.format(dataclean)
os.system(cmd)

# send email
sql = 'select * from lagou_job_new'
positions = Sql.exec_sql(db_conn, sql)
positions = positions.fetchall()
msg = ''
for position in positions:
    positionName = position[0]
    salary = position[1]
    skillLables = position[2]
    companyName = position[3]
    companyLabeles = position[4]
    jobDetail = position[5]
    jobAddr = position[6]
    positionLink = position[7]
    msg = msg + positionName + '({})'.format(salary) + '\n' + skillLables \
        + '\n' + companyName + '\n' + companyLabeles \
        + '\n' + jobAddr \
        + '\n\n' + jobDetail \
        + '\n\n' + positionLink \
        + '\n====================================================================================================\n'

# 第三方 SMTP 服务
mail_host="smtp.sina.com"  #设置服务器
mail_user="ryjfgjl@sina.com"    #用户名
mail_pass="4d0eff8533e6d492"   #口令(此处密码用*代替,使用时请注意更正)

#this one is also username too.
sender = 'ryjfgjl@sina.com'
# 接收邮件，可设置为你的QQ邮箱或者其他邮箱
receivers = ['2577154121@qq.com']

message = MIMEText(msg, 'plain', 'utf-8')
#this on also must be the sender's address
message['From'] = "ryjfgjl@sina.com"
message['To'] =  "xiaobo zhang"  #receiver's name could be customized

subject = '拉勾新增职位 {}'.format(date.today()) #title
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException as e:
    print (e)



