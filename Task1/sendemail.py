import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email content
email_from = 'moinalikhandevopser@gmail.com'
email_password = 'unhdjbkotyfzcbmx'
email_subject = 'Daily Goods Arrival Notification'
email_body = 'Hello,\n\nThis is to inform you that new goods have arrived in our store today.\n\nThank you for your continued patronage.\n\nBest regards,\nSender'

# Email recipients
recipients = ['meghumeghu3@gmail.com']
cc_recipients = ['afwaan3@gmail.com','meghumeghu3@gmail.com']

# Create email message
msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = ', '.join(recipients)
msg['Cc'] = ', '.join(cc_recipients)
msg['Subject'] = email_subject
msg.attach(MIMEText(email_body, 'plain'))

# SMTP server connection
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_from, email_password)

# Send email
server.sendmail(email_from, recipients + cc_recipients, msg.as_string())
print('Email notification sent successfully!')

# Close SMTP server connection
server.quit()
