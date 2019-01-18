from django.views import generic
from django.shortcuts import render, redirect
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
from .models import Subject, Comment, Answer, Action
from .forms import SubjectForm, CommentForm, AnswerForm

def index(request):
    current_user = get_current_authenticated_user()
    subjects = Subject.objects.all()

    return render(request, 'forum/index.html', {
        'current_user': current_user, # Pour vérifier l'auteur
        'subjects': subjects
    })

def new_subject(request):
    if request.user.is_authenticated:
        form = SubjectForm()

        return render(request, 'forum/new_subject.html', {
            'form': form
        })
    else:
        return redirect('user:login')

def store_subject(request):
    if request.user.is_authenticated and request.method == 'POST':
        form = SubjectForm(request.POST)
        current_user = get_current_authenticated_user()

        if form.is_valid():
            subject = Subject(
                title=request.POST['title'],
                subtitle=request.POST['subtitle'],
                author=current_user,
                content=request.POST['content']
            )
            subject.save()
            action = Action(
                author=current_user,
                content=current_user.username + ' a posté un nouveau sujet'
            )
            action.save()

            return redirect('forum:subject-detail', pk=subject.id)

        return redirect('forum:index')

def edit_subject(request, subject_id):
    if request.user.is_authenticated:
        subject = Subject.objects.get(pk=subject_id)

        if request.user.id == subject.author.id:
            form = SubjectForm(instance=subject)

            return render(request, 'forum/edit_subject.html', {
                'subject_id': subject_id,
                'form': form
            })

def update_subject(request, subject_id):
    if request.user.is_authenticated and request.method == 'POST':
        subject = Subject.objects.get(pk=subject_id)
        form = SubjectForm(request.POST, instance=subject)

        if form.is_valid():
            form.save()

            return redirect('forum:subject-detail', pk=subject.id)

        return redirect('forum:index')

def delete_subject(request, subject_id):
    if request.user.is_authenticated:
        subject = Subject.objects.get(pk=subject_id)

        if request.user.id == subject.author.id:
            subject.delete()

            return redirect('forum:index')

        return redirect('forum:index')

def new_comment(request, subject_id):
    if request.user.is_authenticated:
        subject = Subject.objects.get(pk=subject_id)
        form = CommentForm()

        return render(request, 'forum/new_comment.html', {
            'form': form,
            'subject': subject
        })

def store_comment(request):
    if request.user.is_authenticated and request.method == 'POST':
        form = CommentForm(request.POST)
        current_user = get_current_authenticated_user()

        if form.is_valid():
            subject = Subject.objects.get(pk=request.POST['subject'])
            comment = Comment(author=current_user, content=request.POST['content'], subject=subject)
            comment.save()

            action = Action(
                author=current_user,
                content=current_user.username + ' a posté un nouveau commentaire'
            )
            action.save()

            return redirect('forum:subject-detail', pk=subject.id)

        return redirect('forum:index')

def delete_comment(request, comment_id):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_id)

        if comment.subject.author.id == request.user.id:
            comment.delete()

            return redirect('forum:index')

        return redirect('forum:index')

def new_answer(request, comment_id):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_id)
        form = AnswerForm()

        return render(request, 'forum/new_answer.html', {
            'form': form,
            'comment': comment
        })

def store_answer(request):
    if request.user.is_authenticated and request.method == 'POST':
        form = AnswerForm(request.POST)
        current_user = get_current_authenticated_user()

        if form.is_valid():
            comment = Comment.objects.get(pk=request.POST['comment'])
            answer = Answer(author=current_user, content=request.POST['content'], comment=comment)
            answer.save()

            action = Action(
                author=current_user,
                content=current_user.username + ' a répondu à un commentaire'
            )
            action.save()

            return redirect('forum:subject-detail', pk=comment.subject.id)

        return redirect('forum:index')


def delete_answer(request, answer_id):
    if request.user.is_authenticated:
        answer = Answer.objects.get(pk=answer_id)

        if answer.comment.subject.author.id == request.user.id or answer.author.id == request.user.id:
            answer.delete()

            return redirect('forum:subject-detail', pk=comment.subject.id)            

        return redirect('forum:index')

class SubjectDetailView(generic.DetailView):
    model = Subject
    template_name = 'forum/subject-detail.html'
