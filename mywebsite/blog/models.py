from django.db import models
from django.urls import reverse

# Create your models here.
# 글의 분류(일상, 유머, 정보)

class Category(models.Model):
    name = models.CharField(max_length=50, help_text="블로그 글 분류 입력")

    def __str__(self):
        return self.name

# 블로그 글 (제목, 작성일, 대표 이미지, 내용, 분류)
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)
    # 하나의 글을 여러가지의 분류에 해당 될 수 있다.
    category = models.ManyToManyField(Category, help_text="글의 분류를 설정")

    def __str__(self):
        return self.title

    # 1번 글의 경우 -> single/1
    def get_absolute_url(self):
        return reverse("single", args=[str(self.id)])