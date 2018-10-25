import unittest
import time
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL
import os
discover=unittest.defaultTestLoader.discover(start_dir='case',pattern='login_case.py')
#发送邮箱服务器
smtpserver='smtp.qq.com'
#fa发送邮箱用户名,m密码
user="929336066@qq.com"
password="pothdiyhouexbdcg"
#接收邮箱
sender='929336066@qq.com'
reciever="3082236174@qq.com"
def send_mail(report):
    print(report)
    # report=open(report,'rb')
    # r=report.read()
    r=open(report,'rb').read()
    # report.close()
    # msg=MIMEText(r,'html','utf-8')
    msg=MIMEMultipart("related")
    subject="自动化测试报告"
    msg['subject']=Header(subject,'utf-8')
    msg['from']='may'
    msg['to']='老板'
    att=MIMEText(r,'base64',"utf-8")
    att['Content-Type']='application/octet-stream'
    att["Content-Disposion"]='attachment,filename=%s' % str.encode("utf-8")
    msg.attach(att)
    smtp=smtplib.SMTP_SSL()
    smtp.connect(smtpserver,465)
    smtp.login(user,password)
    # smtp=SMTP_SSL(smtpserver)
    # smtp.set_debuglevel(1)
    # smtp.ehlo(user)
    # smtp.login(user,password)
    smtp.sendmail(sender,reciever,msg.as_string())
    smtp.quit()
def find_newreport(report):
    lists=os.listdir(report)
    lists.sort(key=lambda fn: os.path.getmtime(report+fn))
    file_new=os.path.join(report,lists[-1])
    print("最新生成的文件是:" + lists[-1])
    print(file_new)

    f = open(file_new)
    while True:
        line = f.readline()
        if not line: break
        print(line)
    f.close()
    return file_new

if __name__=="__main__":
    time=time.strftime("%Y-%m-%d %H-%M-%S")
    print(time)
    filename='report/'+time+'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='自动化测试报告',tester='may')
    runner.run(discover)
    # f=open(filename,'rb')
    # mail_body=f.read()
    # msg=MIMEText(mail_body,'html','utf-8')
    # subject='测试流程邮件'
    # msg['subject']=Header(subject,"utf-8")
    # smtp=smtplib.SMTP()
    # smtp.connect(smtpserver)
    # smtp.login(user,password)
    # smtp.sendmail(user,reciever,msg.as_string())
    # print("已发送邮件")
    # smtp.quit()
    newfile=find_newreport('report/')
    sleep(5)
    send_mail("report/2018-10-10 17-22-23result.html")
    print(type(newfile))
    print(type("D:\\a.txt"))
    f = open("D:\\a.txt")
    while True:
        line = f.readline()
        if not line: break
        print(line)
    f.close()
    print("已发送邮件")