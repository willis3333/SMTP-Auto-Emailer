import secretprod as sct
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

user = sct.user_sg
emailfrom = sct.email_from
p_w = sct.key_sg


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


# def sendmail_text_only(subject, tolist, message_text):
#     tolist.append(sct.email_from_mg)
#     return requests.post(
#         sct.url_mg,
#         auth=("api", sct.auth_mg),
#         data={"from": "Mailgun Sandbox <postmaster@sandboxa1ffddba4d854ce4ab7885d5b288cb70.mailgun.org>",
#               "to": ", ".join(tolist),
#               "subject": subject,
#               "text": message_text})
#
# sendmail_text_only('hello', ['matthewwillis55@gmail.com'], 'test')


def sendmail_text_only_sg(message_subject, tolist, message_body):
    tolist.append(sct.my_email)

    msg = MIMEMultipart()

    msg['To'] = ", ".join(tolist)
    msg['From'] = sct.email_from_mg
    msg['Subject'] = message_subject

    msg.attach(MIMEText(message_body, _subtype='html'))

    message_str_var = msg.as_string()

    with smtplib.SMTP(host=sct.host_mg, port=sct.port_mg) as connection:
        connection.starttls()
        connection.login(user=sct.user_mg, password=sct.key_mg)
        connection.sendmail(from_addr=emailfrom, to_addrs=", ".join(tolist), msg=message_str_var)
        connection.close()

