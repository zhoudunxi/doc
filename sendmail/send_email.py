#coding=utf8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

username = 'hfyangjun@163.com'
password = '123jun123'
#to='nana.huang@xiaoniutaojin.com'
to = ['ni.chen@xiaoniutaojin5.com','ping.wang@xiaoniutaojin.com','jianping.li@xiaoniutaojin.com','nana.huang@xiaoniutaojin.com','845274594@qq.com']
#to = ['845274594@qq.com']
#to = '845274594@qq.com'
#msg = MIMEMultipart()
#msg['Subject'] = 'yunying data'
#msg['From'] = username
#msg['To'] =to

# 首先是xls类型的附件
def send_mail(url,url1):
    msg = MIMEMultipart()
    msg['Subject'] = 'yunying data'
    msg['From'] = username
    msg['To'] =",".join(to)
    xlsxpart = MIMEApplication(open(url, 'rb').read())
    xlsxpart.add_header('Content-Disposition', 'attachment', filename=url)
    msg.attach(xlsxpart)
    xlsxpart1 = MIMEApplication(open(url1, 'rb').read())
    xlsxpart1.add_header('Content-Disposition', 'attachment', filename=url1)
    msg.attach(xlsxpart1)
    try:
        client = smtplib.SMTP_SSL('smtp.163.com',465)
        #client.connect('smtp.163.com',465)
        client.ehlo()
        client.login(username, password)
        client.sendmail(username, to, msg.as_string())
        client.quit()
        #print '发送成功！'
    except smtplib.SMTPRecipientsRefused as e:
        print 'Recipient refused',e
    except smtplib.SMTPAuthenticationError as e:
        print 'Auth error',e
    except smtplib.SMTPSenderRefused as e:
        print 'Sender refused',e
    except smtplib.SMTPException as e:
        send_mail(url)
        print '123456',e


#print smtplib.SMTP_SSL().connect('smtp.163.com',465)
