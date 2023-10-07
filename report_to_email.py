import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

fromaddr = "epam.2@mail.ru"
toaddr = "epam.2@mail.ru"
mypass = "CNZfmnGCULUvgaQ3ekSA"
reportname = "my_log.log"


def send_message(messege: str) -> None:
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = messege

    with open(reportname, 'rb') as f:
        part = MIMEApplication(f.read(), Name=basename(reportname))
        part['Content-Disposition'] = 'attachment; filename="%s' % basename(reportname)
        msg.attach(part)

        body = 'Error when starting a project on Python "PageObject"'
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        server.login(fromaddr, mypass)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

#     def sendmail(email=fromaddr, password=mypass, message='Hello world'):
#
#         server = smtplib.SMTP(host="smtp.mail.ru", port=587)
#         server.starttls()
#         server.login(email, password)
#         server.sendmail(email, email, message)
#         server.quit()
#         return None
#
#
# if __name__ == '__main__':
#     send_message()
