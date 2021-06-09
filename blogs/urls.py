from django.urls import path
from . import views

urlpatterns=[
  path('', ArticleView.as_view()),
  path('<int:pk>/',ArticleView.as_view()),
  path('get/<int:pk>/',singleArticleView.as_view()),
  path('update/<int:pk>/', ArticleView.as_view()),
  path('delete/<int:pk>/', ArticleView.as_view()),
]



