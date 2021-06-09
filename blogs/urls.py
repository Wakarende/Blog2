from django.urls import path
from .views import ArticleView,singleArticleView


urlpatterns=[
  path('blogs/', ArticleView.as_view()),
  path('blogs/<int:pk>/',singleArticleView.as_view()),
  # path('blogs/get/<int:pk>/',singleArticleView.as_view()),
  path('blogs/update/<int:pk>/', ArticleView.as_view()),
  path('blogs/delete/<int:pk>/', ArticleView.as_view()),
]



