from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Portraits
from .forms import PortraitsForm, CommentaireForm, UserProfileForm
from django.shortcuts import redirect

def portraits_list(request):
    portraits = Portraits.objects.filter(date_publication__lte=timezone.now()).order_by('date_publication')
    return render(request, 'roots/portraits_list.html', {'portraits': portraits})

def portraits_detail(request, pk):
    portraits = get_object_or_404(Portraits, pk=pk)
    return render(request, 'roots/portraits_detail.html', {'portraits': portraits})

def portraits_new(request):
    if request.method == "POST":
        form = PortraitsForm(request.POST)
        if form.is_valid():
            portraits = form.save(commit=False)
            portraits.ajouteePar = request.user
            portraits.date_publication = timezone.now()
            portraits.save()
            return redirect('roots.views.portraits_detail', pk=portraits.pk)
    else:
        form = PortraitsForm()
    return render(request, 'roots/portraits_edit.html', {'form': form})

def add_commentaire_to_portraits(request, pk):
    portraits = get_object_or_404(Portraits, pk=pk)
    if request.method == "POST":
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.auteur = request.user
            commentaire.portraits = portraits
            commentaire.save()
            return redirect('roots.views.portraits_detail', pk=portraits.pk)
    else:
        form = CommentaireForm()
    return render(request, 'roots/add_commentaire_to_portraits.html', {'form': form})

def user_detail(request, pk):
    user_profile = get_object_or_404(User, pk=pk)
    return render(request, 'roots/user_detail.html', {'user_profile': user_profile})

def user_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.save()
            return redirect('roots.views.user_detail', pk=user_profile.pk)
    else:
        form = UserProfileForm()
    return render(request, 'roots/user_profile.html', {'form': form})

def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('roots.views.post_detail', pk=comment.post.pk)

def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('roots.views.post_detail', pk=post_pk)
