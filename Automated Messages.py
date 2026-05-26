import smtplib
from email.message import EmailMessage

a = EmailMessage()
a["Subject"] = "Automated Messages"
a["From"] = ("456@gmail.com")
a["To"] = "123@gmail.com"
a.set_content("Hi , this mail is sent automatically by using Python")
b = smtplib.SMTP("smtp.gmail.com", 587)
b.starttls()
b.login("123" , "")
b.send_message(a)
b.quit()

