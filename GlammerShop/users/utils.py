import random
from django.utils import timezone

def generate_verification_code():
    """
    Генерирует случайный код подтверждения длиной 8 цифр.
    """
    return ''.join([str(random.randint(0, 9)) for _ in range(8)])

def is_code_valid(code_created_at, expiration_minutes=15):
    """
    Проверяет, действителен ли код подтверждения.
    Код считается действительным, если он был создан не более чем
    через указанное количество минут.
    
    :param code_created_at: Время создания кода
    :type code_created_at: datetime
    :param expiration_minutes: Время истечения срока действия кода в минутах
    :type expiration_minutes: int
    :return: True, если код действителен, иначе False
    :rtype: bool
    """
    if code_created_at:
        expiration_time = timezone.now() - timezone.timedelta(minutes=expiration_minutes)
        return code_created_at > expiration_time
    return False
