import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from_addr = "xx@mail.com"
sslcode = "xxx"    # QQ code for SMTP
smtp_server = 'smtp.qq.com'     # set the server

def SendEmail(to_list):
    msg = MIMEMultipart()
    msg["Subject"] = "XX"   # Title
    msg["From"] = from_addr
    msg["To"] = ",".join(to_list)

    # Insert the content of email
    part = MIMEText('<html><body>'
                    '<h3>Hello</h3>'        # Head Line
                    +'<p>Goodbye</p>' +     # Content
                    '</body></html>', 'html', 'utf-8')
    msg.attach(part)

    # Insert the attachment
    part = MIMEApplication(open('1.doc', 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=u"1.doc")
    msg.attach(part)

    try:
        s = smtplib.SMTP_SSL(smtp_server, 465)
        s.login(from_addr, sslcode)
        s.sendmail(from_addr, to_list, msg.as_string())
        s.quit()
        return "Success!"

    except smtplib.SMTPException as e:
        return "Failed, %s" % e


if __name__ == '__main__':
    email_list = []     # receive list
    with open('email.txt', 'r', encoding='utf-8') as f:
        # Insert the email address into email_list
        for line in f.readlines():
            email_list.append(line)
        f.close()
    # print(len(email_list),email_list)   # check the mail list
    re = SendEmail(email_list)
    print(re)
