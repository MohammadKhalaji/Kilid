from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number', 'email_address')
        labels = {
            'phone_number': 'شماره تلفن',
            'email_address': 'پست الکترونیکی'
        }


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ('title', 'price', 'house_type', 'meters', 'bedrooms', 'parkings', 'location', 'locality', 'pic', 'estate')
        labels = {
            'title': 'عنوان',
            'price': 'قیمت',
            'house_type': 'نوع ملک',
            'meters': 'متراژ',
            'bedrooms': 'تعداد اتاق خواب',
            'parkings': 'تعداد پارکینگ',
            'location': 'شهر',
            'locality': 'محله',
            'pic': 'تصویر',
            'estate': 'بنگاه',
        }


class HouseAdminForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ('title', 'price', 'house_type', 'meters', 'bedrooms', 'parkings', 'location', 'locality', 'pic', 'estate', 'starred')
        labels = {
            'title': 'عنوان',
            'price': 'قیمت',
            'house_type': 'نوع ملک',
            'meters': 'متراژ',
            'bedrooms': 'تعداد اتاق خواب',
            'parkings': 'تعداد پارکینگ',
            'location': 'شهر',
            'locality': 'محله',
            'pic': 'تصویر',
            'estate': 'بنگاه',
            'starred': 'اکازیون'
        }

class HouseEditForm(forms.ModelForm):
    class Meta:
        model = House
        fields = (
        'title', 'price', 'house_type', 'meters', 'bedrooms', 'parkings', 'location', 'locality', 'estate')
        labels = {
            'title': 'عنوان',
            'price': 'قیمت',
            'house_type': 'نوع ملک',
            'meters': 'متراژ',
            'bedrooms': 'تعداد اتاق خواب',
            'parkings': 'تعداد پارکینگ',
            'location': 'شهر',
            'locality': 'محله',
            'estate': 'بنگاه',
        }


class HouseAdminEditForm(forms.ModelForm):
    class Meta:
        model = House
        fields = (
            'title', 'price', 'house_type', 'meters', 'bedrooms', 'parkings', 'location', 'locality', 'estate',
            'starred')
        labels = {
            'title': 'عنوان',
            'price': 'قیمت',
            'house_type': 'نوع ملک',
            'meters': 'متراژ',
            'bedrooms': 'تعداد اتاق خواب',
            'parkings': 'تعداد پارکینگ',
            'location': 'شهر',
            'locality': 'محله',
            'estate': 'بنگاه',
            'starred': 'اکازیون',
        }


class HouseImageForm(forms.ModelForm):
    class Meta:
        model = HouseImage
        fields = ('pic', )
        labels = {
            'pic': 'تصویر اضافی (اختیاری)'
        }

    def __init__(self, *args, **kwargs):
        super(HouseImageForm, self).__init__(*args, **kwargs)
        self.fields['pic'].required = False


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email_address', 'phone_number')
        labels = {
            'email_address': 'پست الکترونیکی',
            'phone_number': 'شماره تلفن'
        }

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['email_address'].required = False


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        labels = {
            'text': 'متن کامنت'
        }


class SearchForm(forms.Form):
    locality = forms.CharField(max_length=1000, label='محله')
