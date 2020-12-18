from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db import models
# Create your models here.
from account.validators import phone_validator


class User(AbstractUser):
    country = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f'{self.username}'

class Phone(models.Model):
    phone = models.CharField(verbose_name=_("phone_number"), validators=[phone_validator()], max_length=17, blank=True,
                             help_text="Enter valid phone number because it'll send you a message at once")
    owner = models.ForeignKey(
        verbose_name=_('owner'),
        to=User,
        related_name='phone',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'owner:{self.owner} and phone_number:{self.phone}'