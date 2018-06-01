#!/usr/bin/python
#coding=utf8
"""
# Author: huanghan
# Created Time : 2018-04-10 01:13:01

# File Name: url2.py
# Description:

"""
# Create your tests here.
#encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests,MySQLdb


def test():
    f = open("/data/python/aa.txt","r")
    str = f.readlines()
    f.close()
    return(str)
def sel(a):
    db = MySQLdb.connect("10.23.65.73","root","AAAaaa111!","datav",use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql="select mobile from account where mobile=%s" % a 
    print sql
    cursor.execute(sql)
    data1 = cursor.fetchone()
    db.close()
    return  data1

def url():
    aa = test()
    bb = len(aa)
    cc =int(bb-1)
    for i in aa[0:cc]:
        res = requests.get(url="http://tcc.taobao.com/cc/json/mobile_tel_segment.htm?", params=dict(tel = i))
        ress = res.text.split("=")[1].split(",")
        if ress is None:
            continue
        else:
            a,b,c = ress[1].strip().split(":")[1],ress[2].strip().split(":")[1],ress[3].strip().split(":")[1]
            bb = sel(c)
            print bb
            if ( bb == None ):
                db = MySQLdb.connect("10.23.65.73","root","AAAaaa111!","datav",use_unicode=True, charset="utf8")
                cursor = db.cursor()
                sql = "insert into account (mobile,postion,mobilepostion) values (%s,%s,%s)"  %(c,a,b)
                cursor.execute(sql)
                db.commit()
                db.close()
            else:
                continue
if __name__ == "__main__":
    try:
        url()
    except KeyboardInterrupt:  
        pass