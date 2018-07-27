# _*_ encoding:utf-8 _*_
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    birthday = models.DateTimeField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=50, choices=(("male", u"男"), ("female", u"女")), default="female")
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    images = models.ImageField(upload_to="images/%Y/%m", default=u"images/default.png", max_length=100)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
