def baidu_translate(content):
    import http
    import json
    import hashlib
    import urllib
    import random

    appid = '20211009000968381'  # 你的appid
    secretKey = 'hxiNivFiZjFYZXmGrCUd'  # 你的密钥
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content
    fromLang = 'zh'
    toLang = 'en'
    salt = random.randint(32768, 65536)
    sign = appid+q+str(salt)+secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")  # 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        return(dst) 
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()