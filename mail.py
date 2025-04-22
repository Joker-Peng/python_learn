import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# 配置你的腾讯企业邮箱账户信息
smtp_server = 'smtp.exmail.qq.com'  # 腾讯企业邮箱的SMTP服务器
smtp_port = 465  # SMTP服务器端口，465为SSL端口，587为TLS端口
username = 'penglang@xun-ao.com'  # 你的邮箱账号
password = 'Qweasd11'  # 你的邮箱密码或授权码（建议使用授权码）

# 收件人信息
to_email = 'xiongxing@xun-ao.com'
to_name = '熊星'

# 邮件内容
subject = 'Test Email from Tencent Enterprise Email'
body = 'This is a test email sent from Python using Tencent Enterprise Email.'

# 创建MIMEMultipart对象
msg = MIMEMultipart()
msg['From'] = Header(f'彭朗', 'utf-8')
msg['To'] = Header(f'{to_name} <{to_email}>', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

# 添加邮件正文
msg.attach(MIMEText(body, 'plain', 'utf-8'))

try:
    # 连接到SMTP服务器并发送邮件
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)  # 使用SSL加密连接
    server.login(username, password)  # 登录邮箱账户
    server.sendmail(username, [to_email], msg.as_string())  # 发送邮件
    server.quit()  # 关闭连接
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")