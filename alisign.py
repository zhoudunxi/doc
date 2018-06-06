# coding=utf-8
import base64
import hmac,time
from hashlib import sha1
import urllib
import sys,uuid
import urllib2
from config import ACCESS_KEY_ID,ACCESS_KEY_SECRET,dictionary
class AliyunMonitor():
    def __init__(self,url):
        self.access_id=ACCESS_KEY_ID
        self.access_secret=ACCESS_KEY_SECRET
        self.url=url
    #定义生成签名的方法
    def sign(self,accessKeySecret,dictionary):
        sortdDictionary=sorted(dictionary.items(),key=lambda x:x[0])
        a=''
        for (k,v) in sortdDictionary:
            a += '&' + self.percentEncode(k) + '=' + self.percentEncode(v)
        stringToSign= 'GET&%2F&' +self.percentEncode(a[1:])
        #利用hmac加密
        h = hmac.new(accessKeySecret + '&',stringToSign,sha1)
        signature = base64.encodestring(h.digest()).strip()
        return signature
    def percentEncode(self,encodeStr):
        encodeStr = str(encodeStr)
        res = urllib.quote(encodeStr.decode('utf8').encode('utf8'),'')
        res = res.replace('+','%20')
        res = res.replace('*','%2A')
        res = res.replace('%7E','~')
        return res
    def get_url(self,dicts):
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        dictionary['Timestamp']=timestamp
        dictionary['SignatureNonce']=str(uuid.uuid1())
        for key in dicts:
            dictionary[key] = dicts[key]
        #获得签名
        signature = self.sign(ACCESS_KEY_SECRET,dictionary=dictionary)
        dictionary['Signature'] = signature
        #print signature
        #print dictionary
        #print urllib.urlencode(dictionary)
        url = self.url + "/?" + urllib.urlencode(dictionary)
        return url



##测试
if __name__ == '__main__':
    a=AliyunMonitor('http://metrics.cn-shanghai.aliyuncs.com')
    b={'Action':'QueryMetricList',
       'Project':'acs_bandwidth_package',
       'Metric':'net_rx.rate',
       'Dimensions':'[{"instanceld":"cbwp-uf620gbirormb01i7jcdu"}]',
       'Period':300
       }

    c = a.get_url(b)
    #print c
    print urllib.urlopen(c).readlines()
