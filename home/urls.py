from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('post', views.post),
    path('show/<int:post_id>', views.post),
    path('comment/<int:post_id>',views.comment)
]