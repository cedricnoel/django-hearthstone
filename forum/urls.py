from django.urls import path

from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.index, name="index"),

    path('subject/<int:pk>', views.SubjectDetailView.as_view(), name='subject-detail'),
    path('subject/new', views.new_subject, name='new-subject'),
    path('subject/store', views.store_subject, name='store-subject'),
    path('subject/<int:subject_id>/edit', views.edit_subject, name='edit-subject'),
    path('subject/<int:subject_id>/update', views.update_subject, name='update-subject'),
    path('subject/<int:subject_id>/delete', views.delete_subject, name='delete-subject'),

    path('comment/<int:comment_id>/answer', views.new_answer, name='new-answer'),
    path('answer/store', views.store_answer, name='store-answer'),
    path('answer/<int:answer_id>/delete', views.delete_answer, name='delete-answer'),

    path('subject/<int:subject_id>/comment', views.new_comment, name='new-comment'),
    path('comment/store', views.store_comment, name='store-comment'),
    path('comment/<int:comment_id>/delete', views.delete_comment, name='delete-comment')
]