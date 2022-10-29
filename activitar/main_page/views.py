from django.shortcuts import render, redirect
from .models import *
from .forms import UserSubmitForm


def main_page_view(request):
    if request.method == 'POST':
        user_submit = UserSubmitForm(request.POST)
        if user_submit.is_valid():
            user_submit.save()
            return redirect('/')
    hero = Hero.objects.filter(hero_access=True)
    feature = Feature.objects.all()
    about = About.objects.all()
    classes = Classes.objects.all()
    plan = Plan.objects.filter(is_visible=True)
    whyus = Whyus.objects.filter(is_visible=True)
    user_submit = UserSubmitForm()

    return render(request, 'main_page.html', context={
        "hero": hero,
        "feature": feature,
        "about": about,
        "classes": classes,
        "plan": plan,
        "whyus": whyus,
        'form_submit': user_submit,
    })
