import smtplib
from email.message import EmailMessage

def send_mail(receiver_email, job_role):
    msg = EmailMessage()
    msg['Subject'] = f'Interview for {job_role}'
    msg['From'] = 'chhavijain2264@gmail.com'
    msg['To'] = receiver_email
    msg.set_content(f'You have been shortlisted for {job_role}. Please reply to confirm.')

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('your-email@gmail.com', 'your-app-password')  # Use App Password
        smtp.send_message(msg)
