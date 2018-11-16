from django.urls import path

from . import views

app_name = 'decks'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:deck_id>/', views.details, name='detail'),
    path('new/', views.new, name='new'),
    path('store/', views.store, name='store'),
    path('<int:deck_id>/edit', views.edit, name='edit'),
    path('<int:deck_id>/update', views.update, name='update'),
    path('<int:deck_id>/delete', views.delete, name='delete'),
]