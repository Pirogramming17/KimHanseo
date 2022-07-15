from django.db import models



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 100, default='', verbose_name="제목")
    year = models.CharField(max_length= 50, default='', verbose_name="개봉년도")
    genre = models.CharField(max_length= 50, default='', verbose_name="장르")
    star = models.FloatField(verbose_name="별점", default = 0)
    content = models.TextField(max_length= 500, default='', verbose_name="리뷰내용")
    director = models.CharField(max_length= 80, default='', verbose_name="감독")
    actor = models.CharField(max_length= 150, default='', verbose_name="주연")
    time = models.IntegerField(verbose_name="러닝타임", default = 0)
