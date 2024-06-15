
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, receiver_email, subject, body, password):
    # Create the container email message.
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    # Attempt to send the email.
    try:
        # Create server object with SMTP server details.
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, password)  # Login to the email server
        server.send_message(msg)  # Send the email
        server.quit()  # Logout from the server
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage (replace placeholders with actual values)
send_email('your_email@gmail.com', 'recipient_email@example.com', 'Subject Here', 'Email body here', 'YourPasswordHere')
