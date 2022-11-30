from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Customer,Staff,Order

class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_no= forms.CharField(required=True)
    Cupmas = forms.CharField(required=True)
    section = forms.CharField(required=True)
    bulding_name = forms.CharField(required=True)
    office_no = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user =super().save(commit=False)
        user.is_customer=True
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name=self.cleaned_data.get('last_name')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_no=self.cleaned_data.get('phone_no')
        customer.Cupmas=self.cleaned_data.get('Cupmas')
        customer.section=self.cleaned_data.get('section')
        customer.bulding_name=self.cleaned_data.get('bulding_name')
        customer.office_no=self.cleaned_data.get('office_no')
        customer.save()
        return user

class staffSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_no= forms.CharField(required=True)
    cupmas = forms.CharField(required=True)
    bulding_name = forms.CharField(required=True)
    office_no = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def data_save(self):
        user =super().save(commit=False)
        user.is_staff=True
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name=self.cleaned_data.get('last_name')
        user.save()
        staff= Staff.objects.create(user=user)
        staff.phone_no=self.cleaned_data.get('phone_no')
        staff.cupmas=self.cleaned_data.get('cupmas')
        staff.bulding_name=self.cleaned_data.get('bulding_name')
        staff.office_no=self.cleaned_data.get('office_no')
        staff.save()
        return staff
class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['service','category','discription','quantity','status']