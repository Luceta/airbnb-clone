from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    """ Time Stamped Model """

    # autonow_add 모델 생성 날짜  auto_now 수시 업데이트
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
