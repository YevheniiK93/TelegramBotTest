from django.shortcuts import render, redirect
from .models import UserSubmit
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.groups.filter(name='manager').exists())
def submit_list(request):
    lst = UserSubmit.objects.filter(is_processed=False)
    return render(request, 'submit_list.html', context={'lst': lst})


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.groups.filter(name='manager').exists())
def submit_update(request, pk):
    UserSubmit.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:submits')
