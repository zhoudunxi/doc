#coding=utf-8
import urllib,urllib2,sys,json,time
from alisign import AliyunMonitor
#band=['net_rx.rate','net_tx.rate','net_rx.Pkgs','net_tx.Pkgs','net_tx.ratePercent']
def getResults(name):
    a=AliyunMonitor('http://metrics.cn-shanghai.aliyuncs.com')
    b={'Action':'QueryMetricList',
       'Project':'acs_bandwidth_package',
       'Metric':name,
       'Dimensions':'[{"instanceld":"cbwp-uf620gbirormb01i7jcdu"}]',
       'Period':300
       }   
    url = a.get_url(b)
    try:
       req = urllib2.Request(url)
       response = urllib2.urlopen(req)
    except urllib2.HTTPError, e:  
        print e.code  
        print e.read()
    html = json.loads(response.read())
    if "Pkgs" in name:
        return html['Datapoints'][0]['Value']
    elif "ratePercent"  in name:
        return float("%.3f" % float(html['Datapoints'][0]['Value'])) 
    else:
        return ("%.5f" % float(html['Datapoints'][0]['Value']/8388608))

if __name__ == '__main__':
    #band=['net_rx.rate','net_tx.rate','net_rx.Pkgs','net_tx.Pkgs','net_tx.ratePercent']
    print getResults(sys.argv[1])
