import random
import smtplib
import datetime as dt
import pandas

PLACEHOLDER = "[NAME]"
EMAIL = "python.test.googol@gmail.com"
PASSWORD = "nrvtagipjcldjmbm"

# Solution - 1:
# data = pandas.read_csv('birthdays.csv')
# names = {}
# emails = {}
# for (key, value) in data.iterrows():
#     names[f"{value.month}-{value.day}"] = value.name
#     emails[f"{value.month}-{value.day}"] = value.email
#
# now = dt.datetime.now()
# today = f"{now.month}-{now.day}"
# if today in names.keys():
#     with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
#         content = letter.read()
#         content.replace(PLACEHOLDER, str(names[today]))
#
#         with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#             connection.starttls()
#             connection.login(user=EMAIL, password=PASSWORD)
#             connection.sendmail(
#                 from_addr=EMAIL,
#                 to_addrs=emails[today],
#                 msg=f"Subject: HAPPY BIRTHDAY!!\n\n{content}"
#             )


# Solution - 2:
now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv('birthdays.csv')
birthday = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today in birthday:
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        content = letter.read()
        updated_content = content.replace(PLACEHOLDER, birthday[today]['name'])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=birthday[today]['email'],
            msg=f"Subject: HAPPY BIRTHDAY!!\n\n{updated_content}"
        )
