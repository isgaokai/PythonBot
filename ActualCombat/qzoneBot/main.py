# -*- encoding : utf-8 -*-
# @Author : Fenglchen
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
    'cookie': 'pgv_pvid=869341858; pgv_info=ssid=s9238697591; uin=o1143552064; skey=@qvapHogG0; RK=E5AV1VqKF9; ptcz=ca2f54d1db76766ae320e4fb6f912fdf11d0728979d778832de71b500fefa80b; p_uin=o1143552064; pt4_token=P1C-9TfnDKxIOUDaPnNESOD1El2Al8WzuOBz-l2GDLs_; p_skey=cukwLoNHOtCA*BcqT3wfxCcVZYxmf47fePg3*4CTvAc_; Loading=Yes; qz_screen=1680x1050; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=0',
    'if-modified-since': 'Mon, 20 Sep 2021 14:50:37 GMT',
}
cookie = {"p_skey": "tKw8caBdVb75vdbh6N7-dGz6tveYqWNMuSyKBMVCOOY_", "Loading": "Yes", "pt4_token": "2XEZnDgQ9vht0Xh31s0dlaHzw69YtlRe9qix0Z2bP2g_", "p_uin": "o1143552064", "RK": "75BV13q6Fd", "skey": "@PLF2AuB3u", "ptcz": "6251ee30ea59a9a41161cc1e793f6447e27784de6a3292f8a070fda9fe1d6a92", "uin": "o1143552064", "ptui_loginuin": "1143552064", "pgv_info": "ssid=s9851645207", "pgv_pvid": "4179237676"}
params = (
    ('_t_', '0.6654701684628401'),
)

response = requests.get('https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi?uin=1143552064&do=1&rd=0.6764372107767516&fupdate=1&clean=1&g_tk=1923171194&g_tk=1923171194', headers=headers,cookies=cookie)
response = response.text
response
print(response)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://user.qzone.qq.com/1143552064?_t_=0.6654701684628401', headers=headers)
