#-*- coding:utf-8 -*-

import smtplib, os  # smtplib: 메일 전송을 위한 패키지
from email import encoders  # 파일전송을 할 때 이미지나 문서 동영상 등의 파일을 문자열로 변환할 때 사용할 패키지
from email.mime.text import MIMEText   # 본문내용을 전송할 때 사용되는 모듈
from email.mime.multipart import MIMEMultipart   # 메시지를 보낼 때 메시지에 대한 모듈
from email.mime.base import MIMEBase     # 파일을 전송할 때 사용되는 모듈

toAddr = ["musicboy9@naver.com"]

email = "9thmusicboy@gmail.com"

smtp = smtplib.SMTP('smtp.gmail.com', 587)   # 587: 서버의 포트번호
smtp.ehlo()
smtp.starttls()   # tls방식으로 접속, 그 포트번호가 587
smtp.login('9thmusicboy', "Werwhogeni2255.")

msg = MIMEMultipart()    #msg obj.
msg['Subject'] = '오늘의 식단정보입니다.'
part = MIMEText('맛있는 돼김볶')
msg.attach(part)

for addr in toAddr:
    msg["To"] = addr
    smtp.sendmail("9thmusicboy@gmail.com", addr, msg.as_string())
        #msg는 object이기 때문에 전송을 위해 .as_string()으로 문자열로 바꿔야함(parsing)
    print(addr)