# -*- encoding : utf-8 -*-
# @Author : Fenglchen
# cookie = {"pgv_pvid": "8825877546", "p_skey": "-w1kW2KG76l8wpBEMLvKjAjX3A2M3nNYa1B*5HnQPz4_", "Loading": "Yes", "pt4_token": "O47EervpLXyZApjLViYp0DumuJOD0uQLartwA3*c1so_", "qz_screen": "1680x1050", "p_uin": "o1143552064", "RK": "75BV13q6Fd", "skey": "@PLF2AuB3u", "ptcz": "82e8d61f78eac9e3ffd65b40c5585e9182468f2aed87fb87fafabb4c397dc9dd", "uin": "o1143552064", "ptui_loginuin": "1143552064", "pgv_info": "ssid=s4542493751"}
# url = 'https://user.qzone.qq.com/1143552064'
import requests

headers = {
    'authority': 'user.qzone.qq.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://i.qq.com/',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'pgv_pvid=8825877546; pgv_info=ssid=s4542493751; ptui_loginuin=1143552064; uin=o1143552064; skey=@PLF2AuB3u; RK=75BV13q6Fd; ptcz=82e8d61f78eac9e3ffd65b40c5585e9182468f2aed87fb87fafabb4c397dc9dd; p_uin=o1143552064; pt4_token=O47EervpLXyZApjLViYp0DumuJOD0uQLartwA3*c1so_; p_skey=-w1kW2KG76l8wpBEMLvKjAjX3A2M3nNYa1B*5HnQPz4_; Loading=Yes; qz_screen=1680x1050; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=0',
    'if-modified-since': 'Tue, 21 Sep 2021 02:41:30 GMT',
}

response = requests.get('https://user.qzone.qq.com/1143552064', headers=headers)
print(response.text)