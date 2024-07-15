import random
from django.core.mail import send_mail
from django.conf import settings
from django.utils.timezone import now
from datetime import timedelta

def send_verification_code(email, name):
    # Генерация 8-значного кода
    code = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    code_validity = now() + timedelta(minutes=30)

    subject = 'Подтверждающий код'
    message = f'Здравствуйте {name}, вот код, подтверждающий ваш почтовый адрес: {code}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
    return code, code_validity
