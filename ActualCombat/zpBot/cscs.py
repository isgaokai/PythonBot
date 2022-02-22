import requests

cookies = {
    'UM_distinctid': '17c17965f6c28b-0ee9656c47f749-1c3b6650-1aeaa0-17c17965f6d1c7',
    'bfWin007FirstMatchTime': '2021,8,25,08,00,00',
    'win007BfCookie': '2^0^1^1^1^1^1^0^0^0^0^0^1^2^1^1^0^1^1^0',
    'fAnalyCookie': 'null',
    'CNZZDATA1831853': 'cnzz_eid%3D477822909-1632571510-http%253A%252F%252Fjc.win007.com%252F%26ntime%3D1632571510',
    'CNZZDATA1261430177': '1455678091-1632483163-%7C1632569563',
}

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'http://zq.win007.com/cn/League/2005-2006/36.html',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-HK;q=0.6',
}

params = (
    ('sclassId', '36'),
    ('subSclassId', '0'),
    ('matchSeason', '2005-2006'),
    ('round', '22'),
    ('flesh', '0.3403480745624434'),
)

response = requests.get('http://zq.win007.com/League/LeagueOddsAjax', headers=headers, params=params, cookies=cookies, verify=False)
print(response.text)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('http://zq.win007.com/League/LeagueOddsAjax?sclassId=36&subSclassId=0&matchSeason=2005-2006&round=22&flesh=0.3403480745624434', headers=headers, cookies=cookies, verify=False)
