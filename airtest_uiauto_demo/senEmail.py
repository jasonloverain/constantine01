import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def sendmail(toaddr):
    fromaddr = '18602829297@163.com'
    password = 'test1234'
    toaddrs = [toaddr]
    content = 'HELLO,THIS IS A TESTREPORT'
    textApart = MIMEText(content)

    zipFile = 'D:\\multireport.zip'
    zipApart = MIMEApplication(open(zipFile, 'rb').read())
    zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

    m = MIMEMultipart()
    m.attach(textApart)
    m.attach(zipApart)
    m['Subject'] = 'title'

    try:
        server = smtplib.SMTP('smtp.163.com')
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:', e)  # 打印错误

if __name__ == '__main__':
    sendmail("wx-zhangyl@dtdream.com")