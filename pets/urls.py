from django.contrib.auth.decorators import login_required
from django.urls import path, re_path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'api/v1/articles', APIArticle, basename='article')


urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('cats/', CatsPage.as_view(), name='cats'),
    path('dogs/', DogsPage.as_view(), name='dogs'),
    path('add-post', login_required(AddPost.as_view()), name='add-post'),
    path('join/', JoinPage.as_view(), name='join'),
    path('sign-in/', LoginUser.as_view(), name='sign-in'),
    path('sign-out/', logout_user, name='sign-out'),
    path('search/', search_page, name='search'),
    path('terms-of-service/', TermsPage.as_view(), name='terms'),
    path('comment/', comment_receiver, name='add_comment'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('contact-receiver/', contact_receiver, name='contact_receiver'),
    path('<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
urlpatterns += router.urls

