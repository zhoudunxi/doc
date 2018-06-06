#coding=utf-8
import uuid
from datetime import datetime,timedelta
startTime=(datetime.now()+timedelta(minutes=-5)).strftime('%Y-%m-%d %H:%M:%S')
endTime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

ACCESS_KEY_ID="LTAI9lIUCK2AF0rU"
ACCESS_KEY_SECRET="VX0MJYNb3Jxiei2iHZ6Z1HhzrwH6fl"
dictionary = {
    'Format':'Json',
    'Version':'2017-03-01',
    'AccessKeyId':ACCESS_KEY_ID,
    'SignatureVersion':'1.0',
    'SignatureMethod': 'HMAC-SHA1',
    'StartTime':startTime,
    'EndTime':endTime
}
