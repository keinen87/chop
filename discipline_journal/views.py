from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from discipline_journal.models import Profile, Punishment
from discipline_journal.forms import ProfileForm, PunishmentForm
from django.http import HttpResponse

def profile_list(request):
    searchtext = request.GET.get('searchtext')
    profiles = Profile.objects.all()
    if searchtext:
        profiles = Profile.objects.filter(
            Q(surname__startswith=searchtext.capitalize()) | \
            Q(name__startswith=searchtext.capitalize()) | \
            Q(middle_name__startswith=searchtext.capitalize())
            )
    paginator = Paginator(profiles, 5)
    page = 1
    if 'page' in request.GET:
        page = int(request.GET['page'])
    try:
        profiles = paginator.page(page)
    except EmptyPage:
       profiles = paginator.page(paginator.num_pages)
    context = {
        'profiles': profiles
    }
    return render(request, 'index.html', context)

def profile_detail(request, slug):
    profile = Profile.objects.get(slug=slug)
    punishments = Punishment.objects.filter(profile=profile)
    context = {
        'profile': profile,
        'punishments': punishments
    }
    return render(request, 'profile_detail.html', context)

def profile_new(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            new_form = form.save()
            return redirect(f'/profile/{new_form.slug}/detail')
        else:
            context = {
                'form': form
            }
            return render(request, 'profile_new.html', context)
    else:
        form_class = ProfileForm
        context = {
            'form': form_class
        }
        return render(request, 'profile_new.html', context)

def profile_update(request, slug):
    try:
        profile = Profile.objects.get(slug=slug)
    except Profile.DoesNotExist:
        return redirect('/')
    if request.method == 'POST':
        form = ProfileForm(request.POST or None, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(f'/profile/{profile.slug}/detail')
        else:
            form_class = ProfileForm
            context = {
                'form': form_class,
                'profile': profile
            }
            return render(request, 'profile_update.html', context)
    else:
        form = ProfileForm(request.POST or None, instance=profile)
        context = {
            'profile': profile,
            'form': form
        }
        return render(request, 'profile_update.html', context)       

def profile_delete(request, slug):
    try:
        profile = Profile.objects.get(slug=slug)
        profile.delete()
        return redirect('/')
    except Profile.DoesNotExist:
        return redirect('/')

def punishment_new(request,slug):
    try:
        profile = Profile.objects.get(slug=slug)
    except Profile.DoesNotExist:
        return redirect('/')
    if request.method == 'POST':
        form = PunishmentForm(request.POST or None, initial={'profile':profile.id})
        if form.is_valid():
            form.save()
            return redirect(f'/profile/{profile.slug}/detail')
        else:
            form = PunishmentForm(initial={'profile':profile.id})
            context = {
                'form': form
            }
            return render(request, 'punishment_new.html', context)   
    else:
        form = PunishmentForm(initial={'profile':profile.id})
        context = {
            'form': form
        }
        return render(request, 'punishment_new.html', context)

def punishment_update(request, slug, id):
    try:
        profile = Profile.objects.get(slug=slug)
    except Profile.DoesNotExist:
        return redirect(f'/profile/{profile.slug}/detail')
    try:    
        punishment = Punishment.objects.get(profile=profile, id=id)
    except Punishment.DoesNotExist:
        return redirect(f'/profile/{profile.slug}/detail')
    form = PunishmentForm(request.POST or None,instance=punishment) #TODO
    context = {
                'form': form
            }        
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(f'/profile/{profile.slug}/detail')
        else:
            return render(request, 'punishment_new.html', context)   
    else:
        return render(request, 'punishment_new.html', context)

def punishment_delete(request, slug, id):
    try:
        profile = Profile.objects.get(slug=slug)
    except Profile.DoesNotExist:
        return redirect(f'/profile/{profile.slug}/detail')
    try:    
        punishment = Punishment.objects.get(profile=profile, id=id)
    except Punishment.DoesNotExist:
        return redirect(f'/profile/{profile.slug}/detail')    
    punishment.delete()
    return redirect(f'/profile/{profile.slug}/detail') 
                