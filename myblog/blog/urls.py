from django.urls import path
from . import views
urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDetail.as_view()),
               path('rewiew/<int:pk>/', views.AddComments.as_view(), name='add_comments')]
