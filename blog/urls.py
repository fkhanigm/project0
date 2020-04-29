from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list.as_view(), name='post_list'),
    path('post/<int:pk>/', views.post_detail.as_view(), name='post_detail'),
    path('post/new', views.post_new.as_view(), name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/<int:pk>/comment/', views.comment_new, name='comment_new'),
    
]
