import smtplib

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login('georgia.davis@girlswhocode.com', 'Colbrook2')

sender = 'georgia.davis@girlswhocode.com'
recipient = ['gyang925@gmail.com']
msg = """From: %s
To: %s
Subject: Hello from Your Girls Who Code Site Manager!
This is a test email.""" % (sender, ', '.join(recipient))

smtp.sendmail(sender, recipient, msg)

smtp.quit()
