# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests

# cookie = {
#     'accessID': '20210921101217373657',
#     'user_access': '1',
#     'SESSION_HASH': '7b16ee1652404d69d791ca82b1e01aa87b015ac8',
#     'PHPSESSID': 'f89bd8f458cdf9fe3d26ae83cccab533'
# }
# cookies内容
cookie = {
    'Cookies':'accessID=20210916190140167327; myuid=293241775; save_jy_login_name=19834523498; SESSION_HASH=19aa0eb830569de2e036e2d61176424b97491d1c; PHPSESSID=06b355f2a8f520199975ef83058560fc; main_search:294241775=|||00; user_access=1; stadate1=293241775; myloc=12|1201; myage=39; PROFILE=294241775:%E5%AD%A4%E7%8B%AC%E7%9A%84%E7%8B%BC:m:images1.jyimg.com/w4/global/i:0::1:zwzp_m.jpg:1:1:50:10:3.0; mysex=m; myincome=60; COMMON_HASH=6baecf9a6d747da235d017ed9035956d; sl_jumper=&cou=17&omsg=0&dia=0&lst=2021-09-21; last_login_time=1632191006; upt=USFBJSwm7f4Pj6K2Aq7iVC10i-xhF81sVOf0UxLL-SxLV7SOnWujyKeaJIjoe3bCQp*wRl0n-gTt0PAplOIiS8M.; user_attr=000000; jy_safe_tips_new=xingfu; pop_avatar=1; RAW_HASH=f*7QuzAEM-xYizywII7xWIES81LZKYOc1rCGC-vbY8KF75GygBars7kfDkQMtR*rI4ZUR3fuV5bLKGHFkVrkszES3I95WIhQNU-XDk7yl-UHutA.; pop_time=1632191741175'
   # 'Cookies': 'guider_quick_search=on; accessID=20210916190140167327; myuid=293241775; PHPSESSID=961a6a1bcb914fcb1c8cd6d42958a6b5; main_search:294241775=|||00; is_searchv2=1; save_jy_login_name=19834523498; stadate1=293241775; myloc=12|1201; myage=39; mysex=m; myincome=60; COMMON_HASH=6baecf9a6d747da235d017ed9035956d; last_login_time=1631925445; upt=-mni9lJ5d-nmSDgP2yfKDT7GP2I*2dp4DoGZcHFbxgPktsy3hYnz2j68RDnlQjt5DrIJHxPijlgva30aGpXKFig.; user_attr=000000; user_access=1; SESSION_HASH=1ab4aa8d0e18f6fd2441b35b53dd8ba2cdd310c8; pop_time=1631962117397; pop_avatar=1; PROFILE=294241775:%E5%AD%A4%E7%8B%AC%E7%9A%84%E7%8B%BC:m:images1.jyimg.com/w4/global/i:0::1:zwzp_m.jpg:1:1:50:10:3; RAW_HASH=RuCT39Jv*hMuewpyMpQbIQcH-Hv4N5S2FMdkTMpOKGVCPM5uoF34PUvsbR4T-Aq9e1R4quPtp33GjozX9HkzWRSAFCDsHCc69f*bITPUzgow6JY.'
    # 'Cookies': 'guider_quick_search=on; accessID=20210916190140167327; myuid=293241775; PHPSESSID=961a6a1bcb914fcb1c8cd6d42958a6b5; main_search:294241775=|||00; is_searchv2=1; SESSION_HASH=392ee6f402761cdbe32543e0faa28e4a972d31e8; pop_time=1631925445832; save_jy_login_name=19834523498; stadate1=293241775; myloc=12|1201; myage=39; PROFILE=294241775:%E5%AD%A4%E7%8B%AC%E7%9A%84%E7%8B%BC:m:images1.jyimg.com/w4/global/i:0::1:zwzp_m.jpg:1:1:50:10:3; mysex=m; myincome=60; COMMON_HASH=6baecf9a6d747da235d017ed9035956d; sl_jumper=&cou=17&omsg=0&dia=0&lst=2021-09-17; last_login_time=1631925445;upt=-mni9lJ5d-nmSDgP2yfKDT7GP2I*2dp4DoGZcHFbxgPktsy3hYnz2j68RDnlQjt5DrIJHxPijlgva30aGpXKFig.;user_attr=000000; user_access=1; pop_avatar=1;RAW_HASH=JXSOL7Sa3mPg-u9Go9J8Hgw-PglQxWABaaluB8deQvSn88zVMN8qN6*WeRTjAc9Wj-6wSBNm5mqa0UrWm5bJnHNXx16VSXReBZlLw9zxP4Mc38w.'
}
# headers内容
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Referer': 'https://search.jiayuan.com/v2/index.php?key=&sex=f&stc=2:18.25&sn=default&sv=1&p=1&pt=106683&ft=off&f=select&mt=d'
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
url = 'https://usercp.jiayuan.com/v2/'
res = requests.get(url=url,headers=headers,cookies=cookie)
print(res.text)