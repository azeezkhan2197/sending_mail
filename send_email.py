from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
host="smtp.gmail.com"
port=587

to_email_id=["abdulazeez2197@gmail.com"]
def send_mail(email_id,text):
    mail=MIMEMultipart()
    mail['subject']="testmsg"
    mail['from']=email_id
    mail['to']=to_email_id[0]
    msg=MIMEText(text)
    mail.attach(msg)
    obj=smtplib.SMTP(host,port)
    obj.ehlo()
    obj.starttls()
    obj.login(email_id,"karkbskkhk")
    obj.sendmail(email_id,to_email_id[0],mail.as_string())
    obj.quit()