# -*- encoding : utf-8 -*-
# @Author : Fenglchen
# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests
import json
import pymysql
# 添加用户标识为:Baiduspider 为百度爬虫 获取更多权限
headers = {
    'User-Agent': 'Baiduspider'
}
# 读取百家姓文件 用以进行后续步骤中的遍历查找
with open('/ActualCombat/scrapy_sxr/bai.txt', encoding='utf-8') as r:
    firstnames = r.readlines()
# 对读取百家姓内的数据进行处理 去除'\n'
firstnames = [i.strip() for i in firstnames]
# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='woaini', database='crawler', port=3306, charset='utf8')
# 创建数据库游标 用以执行sql语句
cursor = conn.cursor()

def Bot(name_first_index,name_list_index,first_num,list_num):
    with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/people_with_poor_creditBot/V3/old_first_name.txt'
            , mode='a+') as wof:
        wof.write('姓下标:')
        wof.write(str(name_first_index))
        wof.write(' ')
        wof.write(str(name_list_index))
        wof.write(' ')
        wof.write('页面下标:')
        wof.write(str(first_num))
        wof.write(' ')
        wof.write(str(list_num))
        wof.write('\n')
    first_num = first_num * 10
    list_num = list_num * 10
    print(firstnames)
    for index in range(name_first_index, name_list_index+1):
        firstname = firstnames[index]
        bad_num = 0
        for page_num in range(first_num,list_num+1, 10):
            if bad_num == 200:
                print('姓：%s 数据过少！发生大量重复！')
                break
            try:
                # 目标url 进行拼接查找内容以及页麻 python中requests会自动进行编码 所以可以直接进行拼接中文
                url = 'https://sp1.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E8%A2%AB%E6%89%A7%E8%A1%8C%E4%BA%BA%E5%90%8D%E5%8D%95&cardNum=&iname=' + firstname + '&areaName=&pn='+str(page_num)+'&rn=100&from_mid=1&ie=utf-8&oe=utf-8&format=json&t=1632363317807&cb=jQuery1102037220282079843114_1632362748911&_=1632362748913'
                # 对目标url发送请求获取响应 其中头文件使用上述的Baiduspider
                res = requests.get(url=url, headers=headers, timeout=2)
                # 对获得对响应进行处理并转换为字典类型
                res = json.loads(res.text[47:-2])
                # 在上步处理后的数据进行筛选有用的数据 因为'data'键所对应的值结构为{'data':[{'disp_data':[{xx}]}] } 最终获得的pepo为字典
                for peop in res['data'][0]['disp_data']:
                    # 获取对应的姓名
                    name = peop['iname']
                    # 获取对应的案号
                    case_num = peop['gistId']
                    # 获取对应的法院
                    gistUnit = peop['gistUnit']
                    # 获取对应的地区
                    areaName = peop['areaName']
                    # 进行写入数据库 因为数据库内添加了主键，以案号为主键 ，重复数据会报错，所以需要对异常处理
                    try:
                        # sql语句进行向shixinren表内插入数据
                        sql = 'insert into crawler.final_people_with_poor_credit VALUES (%s,%s,%s,%s)'
                        # 执行sql语句 数据需要为元组
                        cursor.execute(sql, (name, case_num, gistUnit, areaName))
                        # 因为对数据库进行了修改 所以需要提交数据库
                        conn.commit()
                        print('插入成功！')
                    # 发送重复数据
                    except:
                        bad_num = bad_num + 1
                        # 进行跳过
                        pass
            except:
                print('姓：%s，页%s 无法访问！'%(firstname, page_num))
                with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/people_with_poor_creditBot/V3/bad_page.txt'
                          ,mode='a+') as wbp:
                    wbp.write(firstname)
                    wbp.write(' ')
                    wbp.write(str(page_num))
                    wbp.write('\n')
