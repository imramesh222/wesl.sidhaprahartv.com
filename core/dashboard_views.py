from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Notice
from .forms import NoticeForm

@login_required
def notice_list(request):
    notices = Notice.objects.all().order_by('-published_at')
    return render(request, 'dashboard/notice_list.html', {'notices': notices})

@login_required
def add_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.save()
            messages.success(request, 'Notice added successfully!')
            return redirect('notice_list')
    else:
        form = NoticeForm()
    
    return render(request, 'dashboard/notice_form.html', {
        'title': 'Add New Notice',
        'form': form
    })

@login_required
def edit_notice(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            form.save()
            messages.success(request, 'Notice updated successfully!')
            return redirect('notice_list')
    else:
        form = NoticeForm(instance=notice)
    
    return render(request, 'dashboard/notice_form.html', {
        'title': 'Edit Notice',
        'form': form
    })

@login_required
def delete_notice(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == 'POST':
        notice.delete()
        messages.success(request, 'Notice deleted successfully!')
        return redirect('notice_list')
    
    return render(request, 'dashboard/confirm_delete.html', {
        'title': 'Delete Notice',
        'object': notice,
        'cancel_url': 'notice_list'
    })
