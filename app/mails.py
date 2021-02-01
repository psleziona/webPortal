from flask_mail import Message
from app import mail


def send_auth_msg(link, user):
    msg = Message(
        subject='User confirm message',
        body=f'Here is your activate url if href doesn\'t work copy and past in browser url field {link}',
        html=f'<p>To confirm click</p><a href={link}>Confirm link</a>',
        recipients=[user],
        sender='god@god.heaven'
    )
    print(msg)
    mail.send(msg)