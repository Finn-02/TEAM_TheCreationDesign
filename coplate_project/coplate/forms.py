from django import forms
from .models import User, Notice, Community, Adboard, Taxi

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname", "department"]

    def signup(self, request, user):
        user.nickname = self.cleaned_data["nickname"]
        user.department = self.cleaned_data["department"]
        user.save()

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'content']

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['title', 'content']

class AdboardForm(forms.ModelForm):
    class Meta:
        model = Adboard
        fields = ['title', 'content']

class TaxiForm(forms.ModelForm):
    class Meta:
        model = Taxi
        fields = ['title', 'content']