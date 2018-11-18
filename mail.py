from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
host="smtp.gmail.com"
port=587
from_mail="abdulazeez2197@gmail.com"
password="karkbskkhk"
to_mail="abdulazeez2197@gmail.com"
hello="""sdahkjgd
sakhdkjashdkj"""
msg=MIMEMultipart()
msg["subject"]="test"
text=MIMEText(hello)
msg.attach(text)


email_conn=smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(from_mail,password)
email_conn.sendmail(from_mail,to_mail,msg.as_string())
email_conn.quit()