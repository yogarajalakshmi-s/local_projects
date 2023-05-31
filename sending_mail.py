# DAY - 32: Sending email using smtplib

import smtplib

my_email = "python.test.googol@gmail.com"
password = "test1234"  # Password from custom app in App passwords section in Manage Accounts

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()  # Transfer Security Layer - encrypts message
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="pythontest.googol@yahoo.com",
        msg="Subject:Hello\n\nThis is the content of the email"
    )
connection.close()
