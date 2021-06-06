import smtplib, random
from random import randint

msg_2 = ["Error ","Error ","Error ","Error ","Error ","Error ","Error ","Error ","Error ","Error ","Error ","Error ","Err ","Decode ","Serialize ","EOF ","Fuct ","Err404 ","Not Found Code ","Code ","Talk Exception ","Reason "]
email_main = "xx@gmail.com"
email_to = "xx@gmail.com"
total_email=300-60
print("Ongoing send "+str(total_email)+" Emails")
count = 0

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
for x in range(total_email):
    msg = random.randint(0,500000000000)
    msg2 = random.choice(msg_2)
    server.login(email_main,"123456alif")
    server.sendmail(email_main,
                    email_to,
                    str(msg2)+str(msg))
    count +=1
    print("sending mail total: "+str(count)+"\nleft mail: "+str(total_email-count)+"\nMessage: "+msg2+str(msg))

server.quit()