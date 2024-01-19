from django.shortcuts import render, redirect, get_object_or_404
from .models import Notice, Community, Adboard, Taxi, ClubApplication
from .forms import NoticeForm, CommunityForm, AdboardForm, TaxiForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def index(request):
    latest_two_notices = Notice.objects.all().order_by('-created_at')[:2]
    return render(request, "coplate/index.html", {'notices': latest_two_notices})

def apply_club(request):
    return render(request, "JoinClub.html")

def apply_activity(request):
    return render(request, "JoinActivity.html")

#Community---------------------------------------------------------------------------------------------------
def community(request):
    posts = Community.objects.all().order_by('-created_at')
    return render(request, 'Community.html', {'posts': posts})

def add_community(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community')
    else:
        form = CommunityForm()
    return render(request, 'add_notice.html', {'form': form})

def community_detail(request, post_id):
    post = get_object_or_404(Community, pk=post_id)
    return render(request, 'Community_detail.html', {'notice': post})

def community_update(request, post_id):
    # 특정 게시물을 수정하고 상세 페이지로 이동합니다.
    post = Community.objects.get(id=post_id)
    if request.method == 'POST':
        post_form = CommunityForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('community_detail', post_id=post.id)
    else:
        # GET 요청이 오면 해당 게시물의 정보를 채운 폼을 사용하여 post_form.html을 렌더링합니다.
        post_form = CommunityForm(instance=post)
    return render(request, 'add_notice.html', {'form': post_form})

def community_delete(request, post_id):
    # 특정 게시물을 삭제하고 게시물 목록으로 이동합니다.
    post = Community.objects.get(id=post_id)
    post.delete()
    return redirect('community')    

#adboard---------------------------------------------------------------------------------------------------
def adboard(request):
    posts = Adboard.objects.all().order_by('-created_at')
    return render(request, 'Adboard.html', {'posts': posts})

def add_adboard(request):
    if request.method == 'POST':
        form = AdboardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adboard')
    else:
        form = AdboardForm()
    return render(request, 'add_notice.html', {'form': form})

def adboard_detail(request, post_id):
    post = get_object_or_404(Adboard, pk=post_id)
    return render(request, 'Adboard_detail.html', {'notice': post})

def adboard_update(request, post_id):
    # 특정 게시물을 수정하고 상세 페이지로 이동합니다.
    post = Adboard.objects.get(id=post_id)
    if request.method == 'POST':
        post_form = AdboardForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('adboard_detail', post_id=post.id)
    else:
        # GET 요청이 오면 해당 게시물의 정보를 채운 폼을 사용하여 post_form.html을 렌더링합니다.
        post_form = AdboardForm(instance=post)
    return render(request, 'add_notice.html', {'form': post_form})

def adboard_delete(request, post_id):
    # 특정 게시물을 삭제하고 게시물 목록으로 이동합니다.
    post = Adboard.objects.get(id=post_id)
    post.delete()
    return redirect('adboard')    

#taxi---------------------------------------------------------------------------------------------------
def taxi(request):
    posts = Taxi.objects.all().order_by('-created_at')
    return render(request, 'Taxi.html', {'posts': posts})

def add_taxi(request):
    if request.method == 'POST':
        form = TaxiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taxi')
    else:
        form = TaxiForm()
    return render(request, 'add_notice.html', {'form': form})

def taxi_detail(request, post_id):
    post = get_object_or_404(Taxi, pk=post_id)
    return render(request, 'Taxi_detail.html', {'notice': post})

def taxi_update(request, post_id):
    # 특정 게시물을 수정하고 상세 페이지로 이동합니다.
    post = Taxi.objects.get(id=post_id)
    if request.method == 'POST':
        post_form = TaxiForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('taxi_detail', post_id=post.id)
    else:
        # GET 요청이 오면 해당 게시물의 정보를 채운 폼을 사용하여 post_form.html을 렌더링합니다.
        post_form = TaxiForm(instance=post)
    return render(request, 'add_notice.html', {'form': post_form})

def taxi_delete(request, post_id):
    # 특정 게시물을 삭제하고 게시물 목록으로 이동합니다.
    post = Taxi.objects.get(id=post_id)
    post.delete()
    return redirect('taxi')    

#notice---------------------------------------------------------------------------------------------------
def notice(request):
    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'Notice.html', {'notices': notices})

def add_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notice')
    else:
        form = NoticeForm()
    return render(request, 'add_notice.html', {'form': form})

def post_detail(request, post_id):
    post = get_object_or_404(Notice, pk=post_id)
    return render(request, 'Notice_detail.html', {'notice': post})

def post_update(request, post_id):
    # 특정 게시물을 수정하고 상세 페이지로 이동합니다.
    post = Notice.objects.get(id=post_id)
    if request.method == 'POST':
        post_form = NoticeForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        # GET 요청이 오면 해당 게시물의 정보를 채운 폼을 사용하여 post_form.html을 렌더링합니다.
        post_form = NoticeForm(instance=post)
    return render(request, 'add_notice.html', {'form': post_form})

def post_delete(request, post_id):
    # 특정 게시물을 삭제하고 게시물 목록으로 이동합니다.
    post = Notice.objects.get(id=post_id)
    post.delete()
    return redirect('notice')    

#notice---------------------------------------------------------------------------------------------------

@login_required
def apply_club_a(request):
    if request.method == 'POST':
        club_name = request.POST.get('club_name')

        if ClubApplication.objects.filter(user=request.user, club_name=club_name).exists():
            messages.error(request, '이미 신청하셨습니다.')

        application = ClubApplication(user=request.user, club_name=club_name)
        application.save()
        messages.success(request, '신청 완료되었습니다.')

    return redirect('apply_club')