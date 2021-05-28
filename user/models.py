from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .choice import *


# Create your models here.
###level: 사용권한
###auth: 인증번호
class UserManager(BaseUserManager):
    def create_user(self, userid, password, email, **extra):
        if not userid:
            raise ValueError("User must have an userid")
        if not password:
            raise ValueError("User must have an password")

        user = self.model(
            userid= userid,
            password=password,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    #admin 관리자 계정 만들기
    def create_superuser(self, userid, password, email=None):
        user = self.create_user(userid, password, email)

        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.level = 0

        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    userid = models.CharField(max_length=32,
                              verbose_name='사용자 ID', unique=True)
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    email = models.EmailField(max_length=64,
                                verbose_name='이메일', unique=True, null=True)
    level = models.CharField(max_length= 18,
                             verbose_name='등급', choices=LEVEL_CHOICES, default=2)
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'userid'
    REQUIRED_FIELDS = ['email']
    def __str__(self):
        return self.userid

    class Meta:
        db_table = 'board_user'
        verbose_name = "게시판 사용자"
        verbose_name_plural = "게시판 사용자"