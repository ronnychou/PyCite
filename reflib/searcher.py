import requests
from bs4 import BeautifulSoup as bs
import urllib
import json
import re


#TODO add headers
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38'}

class BaiduScholar():
    def __init__(self, paper_name) -> None:
        self.paper_name = paper_name
    
    def __call__(self):
        return self.search_ref()
        
    def search_ref(self, debug=False):
        json_request = self.search_ref_json(self.paper_name, debug)
        if not json_request:
            return None
        if(debug): print('parser json')
        try:
            ref_json = json.loads(json_request.decode('gb2312'))['data']
            if(debug): print('regualr')
            refs={'APA':None, 'MLA':None, 'GBT7714':None}
            refs['APA'] = re.sub('#i{|}', '', ref_json['sc_APA']).replace('[1] ','').replace('[1]','')
            refs['GBT7714'] = re.sub('#i{|}', '', ref_json['sc_GBT7714']).replace('[1] ','').replace('[1]','')
            refs['MLA'] = re.sub('#i{|}', '', ref_json['sc_MLA']).replace('[1] ','').replace('[1]','')
        except Exception as e:
            # services.log("【异常】Json解析错误:"+str(ref_json))
            raise e
        if(debug): print('--------------')
        return refs

    def search_ref_json(self, debug=False):
        if(debug): print("request paper html")
        page = self.page_request(self.paper_name)
        if(debug): print("parser html")
        soup = bs(page, "lxml")
        tags = soup.find_all(name='meta')
        # TODO 筛选多个结果
        # 获取paper链接
        try:
            paper_url = ''.join(['https:',tags[-1]['content'].split(' ')[-1].replace('url=','')])
            paper_id = re.findall('paperid=(.*?)&', paper_url)[0]
            if(debug): print("request reference type json")
            refs = self.ref_request(paper_id)
            return refs
        except:
            print('Occur error when parsing html')
            return None

    def page_request(paper_name):
        params = urllib.parse.urlencode({
            "wd" : paper_name,                                  # 论文名称
            "tn" : "SE_baiduxueshu_c1gjeupa",                   # 百度学术搜索
            "ie" : "utf-8"})                                    # 编码格式
        url = "http://xueshu.baidu.com/s?{0}".format(params)    # GET参数拼接
        try:
            response = urllib.request.urlopen(url, timeout=2).read() # 读取二进制字节
            return response
        except:
            print('Occur error when opening url')
            return None

    def ref_request(paper_id):
        params = urllib.parse.urlencode({
            "type": "cite",
            "paperid": paper_id})                            
        url = "http://xueshu.baidu.com/u/citation?{0}".format(params)   # GET参数拼接
        try:
            response = urllib.request.urlopen(url, timeout=2).read() # 读取二进制字节
            return response
        except:
            print('Occur error when opening url')
            return None


class CNKI():
    pass


class GoogleScholar():
    pass