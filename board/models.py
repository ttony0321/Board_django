from django.db import models
from uuid import uuid4
import os
from django.conf import settings
from datetime import datetime
# Create your models here.

def get_file_path(instance, filename):
    date_path = datetime.now().strftime('%Y/%m/%d')
    uuidname = uuid4().hex
    return '/'.join(['upload_file/', date_path, uuidname])


class Board(models.Model):
    title = models.CharField(max_length=64, verbose_name='제목', null=True)
    content = models.TextField(verbose_name='내용')
    views = models.PositiveIntegerField(default=0,verbose_name='조회수')
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    top_fixed = models.BooleanField(default=0, verbose_name='상단고정')#공지사항같은거, 페이지 넘겨도 상단 고정
    writer = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)#user.User 작성자 불러오기
    upload_files = models.FileField(upload_to=get_file_path, null=True, blank=True, verbose_name='파일')
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')


    def __str__(self):
        return self.title

    class Meta:
        db_table = '게시글'
        verbose_name = '게시글'
        verbose_name_plural = '게시글'

    def delete(self, *args, **kargs):
        if self.upload_files:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.upload_files.path))
        super(Board, self).delete(*args, **kargs)