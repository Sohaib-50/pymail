import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr


def send_email(subject, body, sender, password, recipients):
    msg = MIMEMultipart()
    msg['From'] = formataddr(('Python', sender))
    msg['To'] = ','.join(recipients)
    msg['Subject'] = Header(subject, 'utf-8')

    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, 'Henlo123123')
    server.sendmail(sender, recipients, msg.as_string())
    server.quit()

password = input("Password: ")
send_email("Yo", "Heyy", "sohaibahmedabbasi0@gmail.com", password, ["sohaibahmedabbasi2@gmail.com"])
