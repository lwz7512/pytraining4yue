# qq email check and send
# @2021/04/25
# 
# for python smtp module reference:
# https://docs.python.org/zh-cn/3/library/smtplib.html
# form smtp concept:
# https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol


from smtplib import SMTP_SSL

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# before use your own email account to send email, 
# active your qq smtp service, and generate your own auth code,
# according to this tutorial:
# https://www.cnblogs.com/givemelove/p/11097778.html


# personal mail info
my_email = 'lwz7512@qq.com'    # 1. your own qq email
auth_code = '???' # 2. generate your own auth code
to_emails = ['lwz7512@qq.com', 'lwz7512@gmail.com'] # could be multipal email address
# email content
message = MIMEMultipart()
message['From'] = my_email
message['To'] = ','.join(to_emails)
message['subject'] = 'Greeting email from Python'
body = 'Hi, this is python e-mail sender, how are you?'
message.attach(MIMEText(body,'plain'))


def sendEmailBy(smtp_user, smtp_password, from_email, to_emails, msg):
  print('>>> create qq mail client...')
  smtp = SMTP_SSL('smtp.qq.com', 465)
  print('>>> login qq mail server...')
  smtp.login(smtp_user, smtp_password)
  print('>>> sending ...')
  smtp.sendmail(from_email, to_emails, msg.as_string())
  print('>>> send completed!')
  smtp.quit()


def test_qqmail_open():
  print('>>> trying to connect qq mail server...')
  try:
    with SMTP_SSL('smtp.qq.com', 465) as conn:
      status = conn.noop()[0]
  except:  # smtplib.SMTPServerDisconnected
      status = -1
  result = True if status == 250 else False
  print('<<< connection success!') if result else print('<<< connection failed!')
  return result

# test
# test_qqmail_open()

# call function
sendEmailBy(my_email, auth_code, my_email, to_emails, message)

