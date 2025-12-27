import os
import smtplib

from dotenv import load_dotenv
load_dotenv()

class NotificationManager:
    def __init__(self):
        self.smtp_sender = os.environ.get("SMTP_EMAIL_SENDER")
        self.smtp_password = os.environ.get("SMTP_PASSWORD")
        self.smtp_host = os.environ.get("SMTP_HOST")

    def send_emails(self, customer_emails, message):
        with smtplib.SMTP(host=self.smtp_host) as connection:
            connection.starttls()
            connection.login(user=self.smtp_sender, password=self.smtp_password)

            for cust in customer_emails:
                connection.sendmail(
                    from_addr=self.smtp_sender,
                    to_addrs=cust,
                    msg=message
                )