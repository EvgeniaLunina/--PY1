import random
import string


def get_random_password() -> str:
    symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = random.sample(symbols, 8)
    password_str = "".join(password)
    return password_str
    ...  # TODO написать функцию генерации случайных паролей


print(get_random_password())
