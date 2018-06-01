#coding=utf-8
import pymysql,time
import Excel
import csv
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from send_email import send_mail
from datetime import datetime,timedelta
#建立连接
def conn():
    conn = pymysql.connect(host='rr-uf6i306n7l8gxl71g.mysql.rds.aliyuncs.com',user='mysqlroot',passwd='MZi7fKWWC5F7Br6',port=3306,db='housekeeper',charset='utf8')
    return conn
def __select__(sql,conn):
    cursor = conn.cursor()
    count = cursor.execute(sql)
    restults = cursor.fetchall()
    cursor.close()
    conn.close()
    return restults

def __insert__(sql,conn):
    cursor = conn.cursor()
    count = cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return

if __name__ == '__main__': 
    d=datetime.now()+timedelta(-1)
    d1=datetime.now()+timedelta(-2)
    d2 = d.strftime('%Y-%m-%d')
    d3 = d1.strftime('%Y-%m-%d')
    sql='''select phone_num from account WHERE LEFT(create_time,10)='%s' 
    ''' % d2
    sql1='''#市场要管家数据
    SELECT COUNT(*), '注册数',LEFT(create_time,10),app_channel_name
    from  account where LEFT(create_time,10) ='%s'
    GROUP BY  app_channel_name,LEFT(create_time,10)
    UNION ALL
    SELECT COUNT(*), '激活数',LEFT(create_time,10),app_channel_name
    from  app_channel where LEFT(create_time,10) ='%s'
     GROUP BY  app_channel_name,LEFT(create_time,10)
    ''' % (d2,d2)
    sql2='''SELECT COUNT(*), '注册数',LEFT(create_time,10),app_channel_name
    from  account where LEFT(create_time,10) >'%s'  and app_channel_name='hy10'
    GROUP BY  app_channel_name,LEFT(create_time,10)
    UNION ALL
    SELECT COUNT(*), '激活数',LEFT(create_time,10),app_channel_name
    from  app_channel where LEFT(create_time,10)  >'%s'  and app_channel_name='hy10'
     GROUP BY  app_channel_name,LEFT(create_time,10)
    ''' % (d3,d3)
    s = [sql,sql1,sql2]
    sql4='''SELECT phone_num  from account    
    '''
    
    weekbook = Excel.__getWorkbook__()
    for i in xrange(len(s)):
        
        sheet = weekbook.add_sheet('gj'+str(i),cell_overwrite_ok=True)
        restults=__select__(s[i],conn())
        Excel.__writeExcel__(restults,sheet)
        
    weekbook.save('scshuju&gjshuju.xls')
    with open('gjzhuce.csv','wb') as csvfile:
        writer = csv.writer(csvfile,dialect='excel')
        restults=__select__(sql4,conn())
        writer.writerows(restults)
        csvfile.close()
    send_mail('scshuju&gjshuju.xls','gjzhuce.csv.zip')
    #send_mail('gjzhuce.csv.zip')
