from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('arbol/', views.AccountList.as_view()),
    path('arbol/<int:pk>/', views.AccountDetail.as_view()),
    path('users/', views.UserList.as_view()), # new
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)