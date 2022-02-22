# -*- encoding : utf-8 -*-
# @Author : Fenglchen
# 导入requests包 用以发送请求
import requests
# 导入json包 用以进行类型转换
import json
# 导入mysql 用以进行数据库操作
import pymysql

headers = {
    'User-Agent': 'Baiduspider'
}
# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='woaini', database='crawler', port=3306, charset='utf8')

# 创建数据库游标 用以执行sql语句
cursor = conn.cursor()

# 读取百家姓文件 用以进行后续步骤中的遍历查找
with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/people_with_poor_creditBot/中国姓氏大全(修改后).txt', 'r', encoding='utf-8') as r:
    firstnames = r.readlines()
count = 0
urls = []
# 对读取百家姓内的数据进行处理 去除'\n'
firstnames = [i.strip() for i in firstnames]
for firstname in firstnames:
    for page in range(10, 2001, 10):
        # 目标url 进行拼接查找内容以及页麻 python中requests会自动进行编码 所以可以直接进行拼接中文
        url = 'https://sp1.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E8%A2%AB%E6%89%A7%E8%A1%8C%E4%BA%BA%E5%90%8D%E5%8D%95&cardNum=&iname=' + firstname + '&areaName=&pn='+str(page)+'&rn=100&from_mid=1&ie=utf-8&oe=utf-8&format=json&t=1632363317807&cb=jQuery1102037220282079843114_1632362748911&_=1632362748913'
        # 对目标url发送请求获取响应 其中头文件使用上述的Baiduspider
        try:
            print('1')
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
                # 发送重复数据
                except:
                    # 进行跳过
                    pass
            count +=1
            print(count)
        except:
            pass


# print(len(urls))
# with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/people_with_poor_creditBot/V2/all_urls.txt', mode='w') as wau:
#     for u_rl in urls:
#         wau.write(u_rl)
#         wau.write('\n')