# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests
from lxml import etree
import pymysql
import time
import random

# 注销用户数量
fail_uesr_num = 0

# 目标all_user_id
target_all_user_id = []
# cookies内容
cookie = {
    'Cookies': 'guider_quick_search=on; accessID=20210916190140167327; myuid=293241775; PHPSESSID=961a6a1bcb914fcb1c8cd6d42958a6b5; main_search:294241775=|||00; is_searchv2=1; save_jy_login_name=19834523498; stadate1=293241775; myloc=12|1201; myage=39; mysex=m; myincome=60; COMMON_HASH=6baecf9a6d747da235d017ed9035956d; last_login_time=1631925445; upt=-mni9lJ5d-nmSDgP2yfKDT7GP2I*2dp4DoGZcHFbxgPktsy3hYnz2j68RDnlQjt5DrIJHxPijlgva30aGpXKFig.; user_attr=000000; user_access=1; SESSION_HASH=1ab4aa8d0e18f6fd2441b35b53dd8ba2cdd310c8; pop_time=1631962117397; pop_avatar=1; PROFILE=294241775:%E5%AD%A4%E7%8B%AC%E7%9A%84%E7%8B%BC:m:images1.jyimg.com/w4/global/i:0::1:zwzp_m.jpg:1:1:50:10:3; RAW_HASH=RuCT39Jv*hMuewpyMpQbIQcH-Hv4N5S2FMdkTMpOKGVCPM5uoF34PUvsbR4T-Aq9e1R4quPtp33GjozX9HkzWRSAFCDsHCc69f*bITPUzgow6JY.'
    # 'Cookies': 'guider_quick_search=on; accessID=20210916190140167327; myuid=293241775; PHPSESSID=961a6a1bcb914fcb1c8cd6d42958a6b5; main_search:294241775=|||00; is_searchv2=1; SESSION_HASH=392ee6f402761cdbe32543e0faa28e4a972d31e8; pop_time=1631925445832; save_jy_login_name=19834523498; stadate1=293241775; myloc=12|1201; myage=39; PROFILE=294241775:%E5%AD%A4%E7%8B%AC%E7%9A%84%E7%8B%BC:m:images1.jyimg.com/w4/global/i:0::1:zwzp_m.jpg:1:1:50:10:3; mysex=m; myincome=60; COMMON_HASH=6baecf9a6d747da235d017ed9035956d; sl_jumper=&cou=17&omsg=0&dia=0&lst=2021-09-17; last_login_time=1631925445;upt=-mni9lJ5d-nmSDgP2yfKDT7GP2I*2dp4DoGZcHFbxgPktsy3hYnz2j68RDnlQjt5DrIJHxPijlgva30aGpXKFig.;user_attr=000000; user_access=1; pop_avatar=1;RAW_HASH=JXSOL7Sa3mPg-u9Go9J8Hgw-PglQxWABaaluB8deQvSn88zVMN8qN6*WeRTjAc9Wj-6wSBNm5mqa0UrWm5bJnHNXx16VSXReBZlLw9zxP4Mc38w.'
}
# headers内容
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Referer': 'https://search.jiayuan.com/v2/index.php?key=&sex=f&stc=2:18.25&sn=default&sv=1&p=1&pt=106683&ft=off&f=select&mt=d'
}
# 对all_user_id_pool进行读取
with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/jiayuanBot/Pool/final_all_user_id_pool.txt',
          mode='r') as rauip:
    all_user_id = rauip.readlines()
# 对读取对数据进行处理
for id in all_user_id:
    target_all_user_id.append(id.replace('"realUid":', '').replace('\n', ''))
# 对内容进行爬取
for realuid in target_all_user_id:
    # 目标url
    goal_url = 'https://www.jiayuan.com/' + realuid + '?fxly=pmtq-ss-211&pv.mark=s_p_c|' + realuid + '|294241775'
    print(goal_url)
    # 获取目标网页请求
    goal_res = requests.get(url=goal_url, headers=headers, cookies=cookie)
    # 进行读取
    goal_res = goal_res.text
    # 创建goal_etree
    goal_etree = etree.HTML(goal_res)
    id = realuid
    username = goal_etree.xpath('//div[@class="member_info_r yh"]/h4/text()')[0]
    age_marital_status_location = goal_etree.xpath('//h6[@class="member_name"]/text()')[0]
    age_marital_status_location = str(age_marital_status_location).split('，')
    age = age_marital_status_location[0]
    marital_status = age_marital_status_location[1]
    location = goal_etree.xpath('//h6[@class="member_name"]/a/text()')[0]
    education = goal_etree.xpath('//ul[@class="member_info_list fn-clear"]/li/div/text()')
    print(education)
    print(username)
    print(age)
    print(marital_status)
    print(location)
    print(education)


    # 当前用户征友资料关闭
    if goal_etree.xpath('//div[@class="tip-mb"]/dl/dd[2]/text()') == ['抱歉，该用户的征友资料已关闭，谢谢关注。']:
        # 将注销用户的realuid进行写入
        with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/jiayuanBot/Pool/fail_uesr_pool.txt',
                  mode='a+') as wfup:
            wfup.write('"realUid":'+realuid)
            wfup.write('\n')
        fail_uesr_num += 1
        print('用户：%s已注销！已注销条目总数:%s' % (realuid, fail_uesr_num))
        continue

    # 连接数据库
    # con = pymysql.connect(user='root', password='woaini', host='localhost',
    #                       database='crawler', port=3306, charset='utf8')
    # # 创建数据库游标
    # sor = con.cursor()
    # sql = 'insert into jiayuan VALUES '
    # print(goal_res)
    # # 随机睡眠1～5秒
    # time.sleep(random.randint(1, 5))
    # print(realuid)
