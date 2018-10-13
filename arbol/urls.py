from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('arbol/', views.AccountList.as_view()),
    path('arbol/<int:pk>/', views.AccountDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)