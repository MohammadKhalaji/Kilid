from django.shortcuts import render, redirect, render_to_response
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.core.files.storage import FileSystemStorage
from . import forms
from django.utils.http import urlencode
import datetime
from .models import *
# Create your views here.


def myfloat(string):
    try:
        return float(string)
    except:
        return None

def index(request):
    return render(request, 'kilidapp/index.html')


def usermgmt(request, errors=None):
    print('errors', errors)
    if not request.user.is_authenticated:
        return render(request, 'kilidapp/usermgmt.html')
    else:
        return redirect('index')


@csrf_exempt
def my_login(request):
    if request.method == 'POST':
        auth_form = AuthenticationForm(data=request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data.get('username')
            password = auth_form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('/usermgmt?login=true&error=true')
        else:
            return redirect('/usermgmt?login=true&error=true')
    else:
        return redirect('index')


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = forms.ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save()
            profile.user = user
            profile.save()
            user.email = profile.email_address
            user.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            errors = dict(user_form.errors)
            res = ''
            for key, item in errors.items():
                res += 'XXX'.join(item)
                res += 'XXX'
            return redirect('/usermgmt?signupError=true&text=' + res)
    else:
        return redirect('index')


def my_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/usermgmt?login=true')
    else:
        return redirect('index')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/usermgmt?login=true')

    user = request.user
    profile = user.profile
    queryset = profile.house_set.all()
    if request.user.profile.is_admin:
        queryset = House.objects.all()

    return render(request, 'kilidapp/dashboard.html', {'houses': queryset})


@csrf_exempt
def add_house(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.user.profile.is_admin:
        form = forms.HouseAdminForm(request.POST or None, request.FILES or None)

    else:
        form = forms.HouseForm(request.POST or None, request.FILES or None)
        
    if request.method == 'POST':
        if form.is_valid():
            print('form is valid')
            house = form.save()
            house.created_at = datetime.datetime.now()
            house.profile = request.user.profile
            house.save()
            return redirect('dashboard')
    return render_to_response('kilidapp/add_house.html', {'form': form})

@csrf_exempt
def edit_house(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    profile = user.profile
    house = House.objects.get(pk=pk)
    if house not in profile.house_set.all() and not profile.is_admin:
        return redirect('dashboard')

    form = forms.HouseEditForm(request.POST or None, request.FILES or None, instance=house)

    if profile.is_admin:
        form = forms.HouseAdminEditForm(request.POST or None, request.FILES or None, instance=house)

    imageform = forms.HouseImageForm(request.POST or None, request.FILES or None)


    if request.method == 'POST':
        if form.is_valid():
            form.save()
            if imageform.is_valid() and len(request.FILES) > 0:
                # img = imageform.save()
                imageform.instance.house = house
                imageform.instance.save()
            return redirect('dashboard')
    return render_to_response('kilidapp/edit_house.html', {'form': form, 'pk': pk, 'imageform': imageform})


def delete_house(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    user = request.user
    profile = user.profile
    house = House.objects.get(pk=pk)
    if house not in profile.house_set.all() and not request.user.profile.is_admin:
        return redirect('dashboard')

    if house in profile.house_set.all():
        profile.house_set.remove(house)
        profile.save()
    house.delete()
    return redirect('dashboard')


def delete_house_ajax(request, pk):
    if not request.user.is_authenticated:
        data = {
            'status': 'not authenticated'
        }
        return JsonResponse(data)

    user = request.user
    profile = user.profile
    house = House.objects.get(pk=pk)
    if house not in profile.house_set.all() and not request.user.profile.is_admin:
        data = {
            'status': 'not authorized'
        }
        return JsonResponse(data)

    if house in profile.house_set.all():
        profile.house_set.remove(house)
        profile.save()
    house.delete()

    data = {
        'status': 'ok'
    }

    return JsonResponse(data)




@csrf_exempt
def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    profile = user.profile

    form = forms.ProfileEditForm(request.POST or None, request.FILES or None, instance=profile)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render_to_response('kilidapp/edit_profile.html', {'form': form})


@csrf_exempt
def admin_panel(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.profile.is_admin:
        return redirect('dashboard')

    users = User.objects.all()
    # users = [user for user in users if user is not request.user]

    return render(request, 'kilidapp/admin_panel.html', {'users': users})


def promote_user(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.profile.is_admin:
        return redirect('dashboard')

    iuser = User.objects.get(pk=pk)

    iuser.profile.is_admin = True
    iuser.profile.save()

    return redirect('admin_panel')


def promote_user_ajax(request, pk):
    if not request.user.is_authenticated:
        data = {
            'status': 'not authenticated'
        }
        return JsonResponse(data)

    if not request.user.profile.is_admin:
        data = {
            'status': 'not authorized'
        }
        return JsonResponse(data)

    iuser = User.objects.get(pk=pk)

    iuser.profile.is_admin = True
    iuser.profile.save()

    data = {
        'status': 'ok'
    }
    return JsonResponse(data)


def delete_user(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.profile.is_admin:
        return redirect('dashboard')

    iuser = User.objects.get(pk=pk)

    if iuser is request.user:
        return redirect('admin_panel')

    iuser.delete()

    return redirect('admin_panel')


def delete_user_ajax(request, pk):
    if not request.user.is_authenticated:
        data = {
            'status': 'not authenticated'
        }
        return JsonResponse(data)

    if not request.user.profile.is_admin:
        data = {
            'status': 'not authorized'
        }
        return JsonResponse(data)

    iuser = User.objects.get(pk=pk)

    if iuser is request.user:
        data = {
            'status': "can't delete yourself"
        }
        return JsonResponse(data)

    iuser.delete()

    data = {
        'status': 'ok'
    }
    return JsonResponse(data)


def all_houses(request):
    houses = House.objects.all()
    userbookmarks = None
    long = False

    if request.user.is_authenticated:
        userbookmarks = request.user.profile.bookmarks.all()

    if len(houses) > 4:
        long = True
        houses = houses[:4]

    return render(request, 'kilidapp/all_houses.html', {'houses': houses, 'title': 'همه خانه ها', 'userbookmarks': userbookmarks, 'long': long})


def bookmark_ajax(request, pk):
    print('this this this')
    if not request.user.is_authenticated:
        data = {
            'status': 'not authenticated'
        }
        return JsonResponse(data)

    house = House.objects.get(pk=pk)
    user = request.user
    profile = user.profile
    profile.bookmarks.add(house)
    profile.save()

    data = {
        'status': 'ok'
    }
    return JsonResponse(data)


def unbookmark_ajax(request, pk):
    if not request.user.is_authenticated:
        data = {
            'status': 'not authenticated'
        }
        return JsonResponse(data)

    house = House.objects.get(pk=pk)
    user = request.user
    profile = user.profile
    profile.bookmarks.remove(house)
    profile.save()

    data = {
        'status': 'ok'
    }
    return JsonResponse(data)


def my_bookmarks(request):
    if not request.user.is_authenticated:
        return redirect('login')

    houses = request.user.profile.bookmarks.all()
    userbookmarks = request.user.profile.bookmarks.all()

    return render(request, 'kilidapp/all_houses.html',
                  {'houses': houses, 'title': 'بوکمارک های من', 'userbookmarks': userbookmarks, 'long': False})


def load_all_ajax(request):
    houses = House.objects.all()
    userbookmarks = None

    if request.user.is_authenticated:
        userbookmarks = request.user.profile.bookmarks.all()
    print(userbookmarks)
    string = render_to_string('kilidapp/housestemplate.html', {'houses': houses, 'userbookmarks': userbookmarks, 'title': 'همه خانه ها', 'user': request.user})
    return JsonResponse({'data': string, 'status': 'ok'})


@csrf_exempt
def house(request, pk):
    house = House.objects.get(pk=pk)
    if house is None:
        return redirect('all_houses')

    comments = house.comment_set.all()
    images = [house.pic]
    for housepic in house.houseimage_set.all():
        images.append(housepic.pic)

    form = forms.CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save()
            comment.house = house
            comment.created_at = datetime.datetime.now()
            comment.save()
            house.save()

    return render(request, 'kilidapp/house.html', {'house': house, 'comments': comments, 'images': images, 'form': form})


@csrf_exempt
def search(request):
    post = request.POST
    location = post['location']
    locality = post['locality']
    min_meters = myfloat(post['minMeters']) or 0
    max_meters = myfloat(post['maxMeters']) or 99999999999999999999999999
    min_price = myfloat(post['minPrice']) or 0
    max_price = myfloat(post['maxPrice']) or 999999999999999999999999999

    houses = House.objects.filter(
        price__gte=min_price,
        price__lte=max_price,
        meters__gte=min_meters,
        meters__lte=max_meters,
        location__contains=location,
        locality__contains=locality
    )

    userbookmarks = None
    if request.user.is_authenticated:
        userbookmarks = request.user.profile.bookmarks.all()

    return render(request, 'kilidapp/all_houses.html', {'houses': houses, 'title': 'نتایج جستجو', 'userbookmarks': userbookmarks, 'long': False})
