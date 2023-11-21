from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)
