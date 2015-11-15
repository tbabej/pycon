from django.db import models
import hashlib
import bcrypt

BCRYPT_SALT = '$2b$12$06lamu2xCWRwgTFASwWUx.'

class User(models.Model):

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    md5 = models.CharField(max_length=1000, blank=True)
    sha1 = models.CharField(max_length=1000, blank=True)
    sha2 = models.CharField(max_length=1000, blank=True)
    bcrypt = models.CharField(max_length=1000, blank=True)

    def save(self, *args, **kwargs):
        self.md5 = hashlib.md5(str(self.password)).hexdigest()
        self.sha1 = hashlib.sha1(str(self.password)).hexdigest()
        self.sha2 = hashlib.sha256(str(self.password)).hexdigest()
        self.bcrypt = bcrypt.hashpw(str(self.password), BCRYPT_SALT)

        super(User, self).save(*args, **kwargs)
