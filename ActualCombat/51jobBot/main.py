# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import pymysql
import requests
from lxml import etree
import urllib.parse
import ast

# 链接数据库
con = pymysql.connect(host='localhost', user='root', password='woaini', database='crawler', port=3306, charset='utf8')
# 创建一个游标
cursor = con.cursor()

print('******************************************************************************************************')
print('\t\t\t\t\t\t\t\t\t\t欢迎使用51jobBot！')
print('******************************************************************************************************')
print('在使用前需要配置以下内容：')

while True:
    try:
        keyword = input('请输入你需要搜索的关键字(例:python,java工程师,c++，软件测试)：')
        first_encode = urllib.parse.quote(keyword, encoding='utf8')
        second_encode = urllib.parse.quote(first_encode, encoding='utf8')
        break
    except:
        print('输入错误！')

while True:
    try:
        num = int(input('请选择爬取的页数(1,1001)'))
        if num not in range(1, 1001):
            print('输入错误！')
        else:
            num = num + 1
            break
    except:
        print('输入错误！')


count = 0
for i in range(1, num):
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,' + '99' + ',' + keyword + ',2,' + str(i) + '.html?lang=c&postchannel=0000&workyear=' + '99' + '&cotype=99&degreefrom=' + '99' + '&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    count = count + 1
    while True:
        try:
            res = requests.get(url)
            break
        except:
            continue
    res = res.text
    tre = etree.HTML(res)
    target_data = tre.xpath('//script[@type="text/javascript"]/text()')[0].strip()
    target_data = target_data[27:]
    target_data = ast.literal_eval(target_data)
    if len(target_data['engine_jds']) == 0 and count == 1:
        print('抱歉！当前搜索条件下，未查找到所需要到职位！')
        break
    elif len(target_data['engine_jds']) == 0 and count > 1:
        print('抱歉！职位数目已全部下载！在当前条件下无更多数据！')
    else:
        target_data = target_data['engine_jds']
        for i in target_data:
            temp_l = i['attribute_text']
            if len(temp_l) == 4:
                workarea_text = temp_l[0]
                job_experiences = temp_l[1]
                degreefrom = temp_l[2]
                recruiting_numbers = temp_l[3]
            elif len(temp_l) == 3:
                for j in temp_l:
                    if '经验' in j:
                        job_experiences = j
                    workarea_text = temp_l[0]
                    recruiting_numbers = temp_l[(len(temp_l)-1)]
            jobwelf = i['jobwelf']
            providesalary_text = i['providesalary_text']
            providesalary_text = providesalary_text.replace(r'\/', '/')
            jobwelf = jobwelf

            # 执行插入语句
            sql = "insert into new_51job VALUES ('%s','%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s')" % (i['job_name'],
                                                                                       i['company_name'],
                                                                                       workarea_text,
                                                                                       job_experiences,
                                                                                       degreefrom,
                                                                                       recruiting_numbers,
                                                                                    providesalary_text,
                                                                                       jobwelf,
                                                                                       i['companysize_text'],
                                                                                       i['company_href'])
            print('1')

            cursor.execute(sql)
            # 提交sql语句
            con.commit()
# 释放资源
cursor.close()
con.close()