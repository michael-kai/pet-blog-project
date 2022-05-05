from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('cats/', CatsPage.as_view(), name='cats'),
    path('dogs/', DogsPage.as_view(), name='dogs'),
    path('join/', JoinPage.as_view(), name='join'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('search/', search_page, name='search'),
    path('terms-of-service/', TermsPage.as_view(), name='terms'),
    path('comment/', comment_receiver, name='add_comment'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('contact-receiver/', contact_receiver, name='contact_receiver'),
    path('<slug:post_slug>/', ShowPost.as_view(), name='post'),
]
