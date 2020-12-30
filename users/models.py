from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """custom user model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "Other"),
    )
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "english"), (LANGUAGE_KOREAN, "korean"))

    CURRENCY_USE = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USE, "usd"), (CURRENCY_KRW, "krw"))

    profile_pic = models.ImageField(null=True, blank=True)
    bio = models.TextField(default="", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)