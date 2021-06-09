from django.urls import path
from .views import ArticleView,singleArticleView,CommentView,singleCommentView


urlpatterns=[
  path('blogs/', ArticleView.as_view()),
  path('blogs/<int:pk>/',singleArticleView.as_view()),
  # path('blogs/get/<int:pk>/',singleArticleView.as_view()),
  path('blogs/update/<int:pk>/', ArticleView.as_view()),
  path('blogs/delete/<int:pk>/', ArticleView.as_view()),
  path('comments/', CommentView.as_view()),
  path('comments/<int:pk>/', singleCommentView.as_view()),
  path('comments/update/<int:pk>/', CommentView.as_view()),
  path('comments/delete/<int:pk>/', CommentView.as_view()),
]



