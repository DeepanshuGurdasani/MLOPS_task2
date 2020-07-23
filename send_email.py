import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MESSAGE = MIMEMultipart('alternative')
subject="Error in Your Code"
MESSAGE['subject'] = subject
MESSAGE['To'] = "deepanshugurdasani@gmail.com"
MESSAGE['From'] = "deepanshugurdasani@gmail.com"
body="""
Hello Developer There is an <b>Issue in Your code</b> that you've Pushed to <b>Github</b> Last Time<br>
Please, Correct it and <b>Re Push it to Github Again</b>, for further processing.
"""
HTML_BODY = MIMEText(body, 'html')
MESSAGE.attach(HTML_BODY)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('deepanshugurdasani@gmail.com','Soni@Family123')
server.sendmail(
        'deepanshugurdasani@gmail.com',
        "deepanshugurdasani@gmail.com",
        MESSAGE.as_string()
    )
server.quit()
