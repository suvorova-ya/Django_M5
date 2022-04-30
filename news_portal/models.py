from django.db import models
from django.contrib.auth.models import User



class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.authorUser.username


    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автор"


class Category(models.Model):
    name = models.CharField(max_length = 255,unique = True)


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE,related_name='autor')
    ARTICLE = 'AR'
    NEWS = 'NW'
    CATEGORY_CHOICES = (
        (ARTICLE, 'Статья'),
        (NEWS, 'Новость')
    )
    categoryType = models.CharField(max_length=2,choices=CATEGORY_CHOICES,default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add=False)
    postCategory = models.ManyToManyField(Category,through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    likes = models.ManyToManyField(User,related_name='post_like')

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title} {self.likes}"

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с новостями
        return f'/news/{self.id}'


    def preview(self):
      return self.text[0:123] +'...'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f"{self.user} liked {self.post}"

class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dataCreation = models.DateTimeField(auto_now_add=True)






