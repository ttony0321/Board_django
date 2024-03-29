# Generated by Django 3.2.1 on 2021-05-27 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210527_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth',
            field=models.CharField(max_length=10, null=True, verbose_name='인증번호'),
        ),
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.CharField(choices=[('3', 'Lv3_미인증사용자'), ('2', 'Lv2_인증사용자'), ('1', 'Lv1_관리자'), ('0', 'Lv0_개발자')], default=3, max_length=18, verbose_name='등급'),
        ),
    ]
