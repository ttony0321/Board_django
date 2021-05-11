from django.db import models

# Create your models here.

class User(models.Model):
    userid = models.CharField(max_length=32,
                              verbose_name='사용자 ID')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    nickname = models.CharField(max_length=64,
                                verbose_name='닉네임', default='')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')

    def __str__(self):
        return self.userid

    class Meta:
        db_table = 'board_user'
        verbose_name = "게시판 사용자"
        verbose_name_plural = "게시판 사용자"