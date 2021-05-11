from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=64, verbose_name='제목'),
    content = models.TextField(verbose_name='내용'),
    views = models.PositiveIntegerField(default=0,verbose_name='조회수'),
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간'),
    top_fixed = models.BooleanField(default=0, verbose_name='상단고정'),#공지사항같은거, 페이지 넘겨도 상단 고정
    writer = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)#user.User 작성자 불러오기

    def __str__(self):
        return self.title

    class Meta:
        db_table = '게시글'
        verbose_name = '게시글'
        verbose_name_plural = '게시글'