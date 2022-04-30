from.models import Post,User
from django.forms import ModelForm,TextInput,Textarea,DateTimeInput
from django import forms

class PostForm(ModelForm):
     class Meta:
        model = Post
        fields = ['title','text', 'author','dateCreation']
        labels = {'title': 'Заголовок',
                  'text' : 'Текст статьи',
                  'author': 'Автор',
                  'dateCreation': 'Дата',
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

