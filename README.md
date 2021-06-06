# spam-email-with-smtplib

spam email with smtplib with Gmail

setting your gmail first.

We are using Google's Gmail service to send mail. So we need some settings (if required) for google's security purposes. If those settings are not set up, then the following code may not work, if the google doesnot support the access from third-party app.

To allow the access, we need to set 'Less Secure App Access' settings in the google account. If the two step verification is on, we cannot use the less secure access.

To complete this setup, go to the Google's Admin Console, and search for the Less Secure App setup.

![send_mail](https://user-images.githubusercontent.com/82330418/120917747-18bb5600-c6db-11eb-90e3-5878e1c4d5be.jpg)

open spamerssmtplib.py with your favorite code writers
and imput data in script

1. Imput your message, you can imput multiple message in list format ["1","2","3"]
>> msg_2 = ["write your message here","you can write another message"]#<< write your message here

2. Imput your email, dont forget to active Less Secure App Access
>> email_main = "xx@gmail.com"#<< imput your gmail here

3. Imput your reciver, you can imput multiple email in list format ["email@email.com","email2@email.com","email3@email.com"]
>> email_to = ["xx@gmail.com"]#<< imput your email direction here, you can imput multiple image

4. imput total spams wint format int

>> total_email=300#<< total email you want to send / spams


if alredy done, run the script

# how to run
python3 spamerssmtplib.py
