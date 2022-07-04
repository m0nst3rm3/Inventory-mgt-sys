from django.urls import path

from .views import signup_page, login_page, logout_page
urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('login/signup/', signup_page, name='signup'),
]
