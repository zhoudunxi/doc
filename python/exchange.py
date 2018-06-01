#!/usr/bin/python
#encoding=utf-8
import re,requests,json,time,sys,os
dingding = 'https://oapi.dingtalk.com/robot/send?access_token=62399a3a4f8e4014cf4c7341613ce2992341b53933f17c14a9e245a27f74dae8'
def send_message(info):
    headers = {'Content-Type':'application/json'}
    message = {"msgtype": "text","text":{"content":info},"at":{"atMobiles":["18116208606","17773324033","15026402845"],"isAtAll":"FALSE"}}
    req = requests.post(url=dingding,data=json.dumps(message),headers=headers)
    req.status_code
    req.content
def LX(url):
    try:
        res =  json.loads(requests.get(url,params={}).text)
        result =  res["PriceItemList"][-1]["PriceDateTime"]
        results = re.split("T",result)
        result2 = results[1]
        result1 = results[0]
        result3 = result1 + ' ' +  result2
        result3 = time.mktime(time.strptime(result3,'%Y-%m-%d %H:%M:%S'))
        date = time.mktime(time.localtime())
        result4 = int(date) - int(result3)
        if result4 < 120:
            print "OKOKOK"
    except:
        print send_message("华凝交易所K线延迟@18116208606,@17773324033,@15026402845")
def ZJWL(url):
    try:
        res =  json.loads(requests.get(url,params={}).text)
        result =  res["PriceItemList"][-1]["PriceDateTime"]
        results = re.split("T",result)
        result2 = results[1]
        result1 = results[0]
        result3 = result1 + ' ' +  result2
        result3 = time.mktime(time.strptime(result3,'%Y-%m-%d %H:%M:%S'))
        date = time.mktime(time.localtime())
        result4 = int(date) - int(result3)
        if result4 < 120:
            print "OKOKOK"
    except:
        print send_message("中金交易所K线延迟@18116208606,@17773324033,@15026402845")

def ZJWLURL():
    try:
        res = requests.get("http://103.40.195.72/api/prices/kchart/get?goodsType=AG&chartType=1",timeout=10)
        code = res.status_code
    except:
        code = "请求中金交易所超时"
    if code == 200:
        ZJWL("http://103.40.195.72/api/prices/kchart/get?goodsType=AG&chartType=1")
    else:
         print send_message("中金交易所K线请求失败@18116208606,@17773324033,@15026402845")
def LXURL():
    try:
        res = requests.get("http://xiaoniu.zjcomex.com/api/prices/kchart/get?goodsType=AG&chartType=1",timeout=10)
        code = res.status_code
    except:
        code = "请求华凝交易所超时"
    if code == 200:
        LX("http://xiaoniu.zjcomex.com/api/prices/kchart/get?goodsType=AG&chartType=1")
    else:
         print send_message("中金交易所K线请求失败@18116208606")
    
        
    

if __name__ == '__main__':
    if sys.argv[1] == "ZJ":
        ZJWLURL()
    elif sys.argv[1] == "LX":
        LXURL()
    else:
        print "语法错误"
