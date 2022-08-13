import secretprod as sct
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


user = sct.user_sg
emailfrom = sct.email_from
p_w = sct.key_sg2


def sendmail_text_only(message_subject, tolist, message_body):
    tolist.append(emailfrom)

    msg = MIMEMultipart()

    msg['To'] = ", ".join(tolist)
    msg['From'] = emailfrom
    msg['Subject'] = message_subject

    msg.attach(MIMEText(message_body, _subtype='html'))

    message_str_var = msg.as_string()

    with smtplib.SMTP(host=sct.host_sg, port=sct.port_sg) as connection:
        connection.starttls()
        connection.login(user=user, password=p_w)
        connection.sendmail(from_addr=emailfrom, to_addrs=", ".join(tolist), msg=message_str_var)
        connection.close()




