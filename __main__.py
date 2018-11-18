import datetime
from read_template import get_template
from read_csv import read
from send_email import send_mail
context={}
context=read("file1.csv",1)
#print(context)
text=get_template()
#print(text)
today=datetime.date.today()
context["date"]=today.strftime("%d-%m-%y")
#print(context)
def email_text(text,context):
    return_email_text=text.format(**context)
    return return_email_text
email=email_text(text,context)
#print(email)
send_mail(context["email"],email)