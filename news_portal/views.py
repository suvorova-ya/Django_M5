from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import View
from .models import Post,User
from django.views.generic import ListView, UpdateView, CreateView, DetailView,DeleteView,TemplateView
from .filters import PostFilter
from .forms import PostForm,UserForm
from django.http import  HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic.edit import CreateView



class news(ListView):
    model = Post
    template_name = 'news_portal/news.html'
    context_object_name = 'news'
    ordering = ['-dateCreation']
    paginate_by = 1  # поставим постраничный вывод в один элемент



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый пост
            form.save()

        return super().get(request, *args, **kwargs)

class NewsDetail(DetailView):
    model = Post
    template_name = 'news_portal/details_view.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data



def PostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('details_view', args=[str(pk)]))

class PostCreateView(PermissionRequiredMixin,CreateView):
    model = Post
    template_name = 'news_portal/news_create.html'
    form_class = PostForm
    permission_required = 'news_portal.add_post'



class PostUpdateView(PermissionRequiredMixin,UpdateView):
    model = Post
    template_name = 'news_portal/news_create.html'
    form_class = PostForm
    permission_required = 'news_portal.change_post'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)



# дженерик для удаления статьи
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'news_portal/news_delete.html'
    success_url = '/news/'

def about(request):
    return render(request,'news_portal/about.html')

# дженерик для редактирования профиля

class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    template_name = 'news_portal/user_update.html'
    form_class = UserForm
    success_url = '/news/'

    def get_object(self, **kwargs):
        return self.request.user


