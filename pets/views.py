from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, TemplateView, CreateView
from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
import rest_framework.permissions as permissions
from .serializers import *
from .mixins import BaseMixin
from .models import *
from .forms import *
from .permissions import IsOwnerOrReadOnly


class MainPage(BaseMixin, TemplateView):
    template_name = 'templates/index.html'
    context_object_name = 'menu'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(**kwargs)
        context.update(base_context)
        latest_articles = Article.objects.all().exclude(is_published=False).order_by('-time_create')[:5]
        context['latest_articles'] = latest_articles
        return context


class CatsPage(BaseMixin, ListView):
    paginate_by = 5
    template_name = 'templates/cats.html'
    context_object_name = 'menu'
    queryset = Article.objects.filter(cat_id__slug='cats').exclude(is_published=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(**kwargs)
        context.update(base_context)
        context['title'] = 'Cats'
        return context


class DogsPage(BaseMixin, ListView):
    paginate_by = 5
    template_name = 'templates/dogs.html'
    context_object_name = 'menu'
    queryset = Article.objects.filter(cat_id__slug='dogs').exclude(is_published=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(**kwargs)
        context.update(base_context)
        context['title'] = 'Dogs'
        return context


class AddPost(BaseMixin, CreateView):
    model = Article
    template_name = 'templates/add-article.html'
    form_class = AddPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(**kwargs)
        context.update(base_context)
        context['title'] = 'Add Post'
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        # print(self.request.__dict__)
        post.slug = slugify(post.title)

        post.save()
        return redirect(self.request.META['HTTP_REFERER'])


class JoinPage(BaseMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'templates/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(**kwargs)
        context.update(base_context)
        context['title'] = 'Join'
        return context


class LoginUser(BaseMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'templates/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(**kwargs)
        context.update(base_context)
        context['title'] = 'Login'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


def search_page(request):
    if request.method == 'POST':
        query = request.POST.get("search_query")
        if not query:
            return render(request, 'templates/search.html', BaseMixin.get_user_context_func())
        search_result = Article.objects.filter(title__icontains=query)
        context = BaseMixin.get_user_context_func()
        if not search_result:
            context['empty_result'] = True
        context['search_result'] = search_result

        return render(request, 'templates/search.html', context=context)

    return render(request, 'templates/search.html', BaseMixin.get_user_context_func())


class ShowPost(BaseMixin, TemplateView):
    template_name = 'templates/post.html'
    slug_url_kwarg = 'post_slug'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(**kwargs)
        context.update(base_context)
        context['article'] = Article.objects.get(slug=context['post_slug'])
        context['comments'] = Comment.objects.filter(article_id=context['article'].id)
        return context


def comment_receiver(request):
    if request.method == 'POST':
        cf = CommentForm(request.POST or None)
        if cf.is_valid():
            cf.save()
            return redirect(request.META['HTTP_REFERER'])
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect('home')


class TermsPage(BaseMixin, TemplateView):
    template_name = 'templates/terms.html'
    context_object_name = 'menu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(**kwargs)
        context.update(base_context)
        return context


class ContactPage(BaseMixin, TemplateView):
    template_name = 'templates/contact.html'
    context_object_name = 'menu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(**kwargs)
        context.update(base_context)
        context['title'] = 'Contact'
        return context


class CatsAPIPaginator(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class APIArticle(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = CatsAPIPaginator
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


def contact_receiver(request):
    if request.method == 'POST':
        cf = ContactForm(request.POST or None)
        if cf.is_valid():
            cf.save()
            return redirect('contact')
        return redirect('contact')


def page_not(request):
    return HttpResponseServerError('<h1>Sorry, page not found</h1>')
