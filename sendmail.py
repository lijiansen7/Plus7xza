# coding=utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

host = 'smtp.qq.com'
user = '邮箱'
pwd = '授权码' 

def send_mail(recv,message):
    """
    :param message:
    :param recv: # 接收者账号列表
    :return:
    """
    msg = MIMEMultipart()
    msg.attach(MIMEText(message))  
    msg['Subject'] = '恩兔'  
    msg['From'] = user  
    msg['To'] = ','.join(recv)  


    server = smtplib.SMTP()
    server.connect(host)
    server.login(user, pwd)
    server.sendmail(user, recv, msg.as_string())
    server.close()
    return True
    
ip = os.getenv('LOGIN_IP')
send_mail(user,"服务器登录成功ip来自"+ip)
