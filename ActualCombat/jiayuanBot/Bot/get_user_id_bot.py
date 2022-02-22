# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests
import copy


# 页面数
numberofpages = 1
# 库内所有user_id条目
all_user_id_num = 0
# cookies内容
cookie = {
    'Cookies': 'guider_quick_search=on; accessID=20210916190140167327; myuid=293241775; PHPSESSID=961a6a1bcb914fcb1c8cd6d42958a6b5; main_search:294241775=|||00; is_searchv2=1; SESSION_HASH=392ee6f402761cdbe32543e0faa28e4a972d31e8; pop_time=1631925445832; save_jy_login_name=19834523498; stadate1=293241775; myloc=12|1201; myage=39; PROFILE=294241775:%E5%AD%A4%E7%8B%AC%E7%9A%84%E7%8B%BC:m:images1.jyimg.com/w4/global/i:0::1:zwzp_m.jpg:1:1:50:10:3; mysex=m; myincome=60; COMMON_HASH=6baecf9a6d747da235d017ed9035956d; sl_jumper=&cou=17&omsg=0&dia=0&lst=2021-09-17; last_login_time=1631925445; upt=-mni9lJ5d-nmSDgP2yfKDT7GP2I*2dp4DoGZcHFbxgPktsy3hYnz2j68RDnlQjt5DrIJHxPijlgva30aGpXKFig.; user_attr=000000; user_access=1; pop_avatar=1; RAW_HASH=JXSOL7Sa3mPg-u9Go9J8Hgw-PglQxWABaaluB8deQvSn88zVMN8qN6*WeRTjAc9Wj-6wSBNm5mqa0UrWm5bJnHNXx16VSXReBZlLw9zxP4Mc38w.'
}
# data内容
data = {
    'sex': 'f',
    'sn': 'default',
    'sv': '1',
    'p': '1',
    'stc': '2:18.25',
    'f': 'select',
    'listStyle': 'bigPhoto',
    'pri_uid': '294241775',
    'jsversion': 'v5'
}
# headers内容
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Referer': 'https://search.jiayuan.com/v2/index.php?key=&sex=f&stc=2:18.25&sn=default&sv=1&p=1&pt=106683&ft=off&f=select&mt=d'
}

while True:
    # 修改页数
    data['p'] = str(numberofpages)
    # 爬取页数内容
    url = 'https://search.jiayuan.com/v2/search_v2.php'
    # 页面访问计数
    url_count = 1
    while True:
        try:
            if url_count == 5:
                break
            res = requests.post(url, headers=headers, cookies=cookie, data=data, timeout=5)
            break
        # 出现错误
        except:
            url_count += 1
    # 如果访问超过5次，则跳过
    if url_count == 5:
        print('第%s页访问错误，已跳过！' % numberofpages)
        continue
    # 对爬取对数据进行处理
    res = res.text.split(',')
    # 深拷贝
    goal = copy.deepcopy(res)
    # 获取用户realUid
    for i in res:
        if 'realUid' not in i:
            goal.remove(i)
    print(goal)
    # 第一页包含用户本身realUid进行处理
    if numberofpages == 1:
        res = goal[1:]
    else:
        res = goal
    # 当前库内总共条目
    all_user_id_num += len(res)
    # 进行写入文件
    with open('/Users/tempuser/PycharmProjects/python爬虫/ActualCombat/jiayuanBot/Pool/all_user_id_pool.txt',
              mode='a+') as waui :
        for i in res:
            waui.write(i)
            waui.write('\n')
        print('写入成功第%s页的user_id,共%s位用户！当前库内共有%s条user_id!' % (numberofpages, len(res), all_user_id_num))
    # 跳转下一搜索页面
    numberofpages += 1
