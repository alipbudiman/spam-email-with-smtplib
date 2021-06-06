import smtplib, random
from random import randint

msg_2 = ["write your message here","you can write another message"]#<< write your message here
email_main = "xx@gmail.com"#<< imput your gmail here
email_to = ["xx@gmail.com"]#<< imput your email direction here, you can imput multiple image
total_email=300#<< total email you want to send / spams
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
