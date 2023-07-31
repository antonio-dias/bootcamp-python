import smtplib

my_email = "my_email@gmail.com"
MY_EMAIL = "my_email@gmail.com"
password = "mypassword"  # change to your password

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="my_email@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )
    # connection.close()
