import smtplib
import random
import datetime as dt

now = dt.datetime.now()
day = now.strftime('%A')

if now.weekday() == 6:
    with open('quotes.txt') as file:
        data = file.readlines()
    quote = random.choice(data)

    my_email = "python.test.googol@gmail.com"
    password = "cpvknapqgkioamei"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="pythontest.googol@yahoo.com",
            msg=f"Subject: {day} Motivations\n\n{quote}"
        )
