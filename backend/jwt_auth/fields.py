from django.db import models
from django.conf import settings
from cryptography.fernet import Fernet, InvalidToken


class EncryptedField(models.TextField):
    def __init__(self, *args, **kwargs):
        super(EncryptedField, self).__init__(*args, **kwargs)
        self.cipher = Fernet(settings.DJANGO_ENCRYPTED_FIELD_KEY)

    def to_python(self, value):
        if not value:
            return None
        try:
            decrypted_data = self.cipher.decrypt(str(value).encode()).decode()
            return decrypted_data
        except InvalidToken:
            return value

    def from_db_value(self, value, expression, connection):
        if not value:
            return ''
        return self.to_python(value)

    def get_prep_value(self, value):
        if not value:
            return ''
        encrypted_data = self.cipher.encrypt(str(value).encode()).decode()
        return encrypted_data
