from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /cards/5/
    path('<int:question_id>/', views.detail, name='detail'),
]