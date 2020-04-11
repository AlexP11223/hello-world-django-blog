from django.urls import path
from .views import PostCreateView, PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<int:pk>/', PostDetailView.as_view(), name='show'),
]
