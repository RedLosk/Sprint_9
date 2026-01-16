import pathlib
import random
import string


class Helpers:

    @staticmethod
    def generate_random_string(length, name=False):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        if name:
            random_string = random_string[0].upper() + random_string[1:]
        return random_string

    @staticmethod
    def generate_random_user():
        first_name = Helpers.generate_random_string(6, True)
        last_name = Helpers.generate_random_string(6, True)
        username = f"{first_name}{last_name}"
        user = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username ,
            'email': f"{username}@{random.choice(['mail.ru', 'rambler.ru', 'yandex.ru'])}",
            'password': Helpers.generate_random_string(8),
        }
        return user

    @staticmethod
    def get_root_dir():
        root_dir = pathlib.Path(__file__).parent
        return str(root_dir).replace('\\', '/')
