import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方SMTP服务
mail_host = "smtp.163.com"  # 服务器
mail_user = "18895341711@163.com"
mail_pwd = "Tt19950305"

sender = "18895341711@163.com"  # 发送的邮件地址
receivers = ['237932061@qq.com']  # 接受的邮件地址

message = MIMEText('Python发送邮件demo..', 'text/html', 'utf-8')
message['From'] = Header('来自Python发送', 'utf-8')
message['To'] = Header('随机邮件地址', 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 进行邮件的发送
smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
smtpObj.login(mail_user, mail_pwd)
smtpObj.sendmail(sender, receivers, message.as_string())
print("邮件发送成功")

