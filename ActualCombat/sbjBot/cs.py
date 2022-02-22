import requests

cookies = {
    'UM_distinctid': '17bf277bf8e763-0ffbad3484099a-113f6757-129790-17bf277bf8f5fa',
    'goN9uW4i0iKzS': '54p9Oh5.nujnJ0R0cPqirtGqmxM8Pw5PubKqi_THKJH_OkYtSJAecv2MWdHnLwvB70xqjh1dClvFUFeiso93Biq',
    'tmas_cookie': '2272.7689.15400.0000',
    '018f9ebcc3834ce269': '2efc18aea4fa1734db221a2d03a37f68',
    'JSESSIONID': '0000IgEeETt6p3tu_27dqd_tvLp:1bm104mv1',
    'goN9uW4i0iKzT': '53VvthbmxngaqqqmZck6htAxC4e.tVnVKVpwJZbMKn.7FM4Dset8SHmPsCv97mNQ_oAp727gQjsZq29KKd7jfrkxRTUG2Tx930BOc5Uoh14Tjk_WyH104zgcB27Ljg6NYdS3KeNEtgfE4p58mzVkohcgxg9SpZxnthyqGYb.JxX0kLL7EAWyNjlI9bolZF3608ILseoXV2i.HuY60.9mZH_vPTnZu8ZfK87fbKoQ8FF6IJrkOcVvlOqu.KE4DdhIuBOgQohXyrXZrBvw5atUVzbFEMXfrA9wP0tXDfRqRmEXa',
}

headers = {
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://wsgg.sbj.cnipa.gov.cn:9080',
    'Referer': 'http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=1757',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-HK;q=0.6',
}

params = (
    ('O56fzBVE', '5aeuThTFZbFU4Iz4M4cm5GOqF.vmXcfwgD74iB21XandDsUeUFEja1OVYPV5ZF2lrIQsTIvKSQfuvkwWnyCQXPxy.KAyj8lH8Z7BRcP7gRxi0tJhR95IT5h8NW9aMHHoBrddkwOFPwdpfpgi1Ejhfu1n.gn3gsxLBQey3FRi.Tdvi9nyKeDFHNNrniF2S.FqjKMwvuZGkNGjP2om2d_W2RO_GKByhn11G5TLbQ3tMTqO06QeuF0vUAlT5nK4NZH2X9_CwMI30fLsZcgyoQj4qj4B_OT8Da.uPlRKauvXCB0T5XCTvKb0Wvpsrrrm1flN2CqaL1b4cKa.NY.hXiHtL1xu_Vx9n18IWtjF0LIF35aW'),
)

data = {
  'annNum': '1757'
}

response = requests.post('http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=1757', headers=headers, params=params, cookies=cookies, data=data, verify=False)
print(response.text)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/getAnnType.html?O56fzBVE=5aeuThTFZbFU4Iz4M4cm5GOqF.vmXcfwgD74iB21XandDsUeUFEja1OVYPV5ZF2lrIQsTIvKSQfuvkwWnyCQXPxy.KAyj8lH8Z7BRcP7gRxi0tJhR95IT5h8NW9aMHHoBrddkwOFPwdpfpgi1Ejhfu1n.gn3gsxLBQey3FRi.Tdvi9nyKeDFHNNrniF2S.FqjKMwvuZGkNGjP2om2d_W2RO_GKByhn11G5TLbQ3tMTqO06QeuF0vUAlT5nK4NZH2X9_CwMI30fLsZcgyoQj4qj4B_OT8Da.uPlRKauvXCB0T5XCTvKb0Wvpsrrrm1flN2CqaL1b4cKa.NY.hXiHtL1xu_Vx9n18IWtjF0LIF35aW', headers=headers, cookies=cookies, data=data, verify=False)
