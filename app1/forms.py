from django.contrib.auth.forms import UserCreationForm
from django import forms
from app1 import mongodb

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class AddTopic(forms.Form):
    topicTitle = forms.CharField(max_length=512)
    topicContent = forms.CharField()

    def save(self, userId):
        topicTitle = self.cleaned_data['topicTitle']
        topicContent = self.cleaned_data['topicContent']
        mongodb.addTopic(userId, topicTitle, topicContent)

class AddDiscuss(forms.Form):
    discussContent = forms.CharField()
    topicId = forms.CharField(widget=forms.HiddenInput)

    def save(self, userId):
        discussContent = self.cleaned_data['discussContent']
        topicId = self.cleaned_data['topicId']
        mongodb.addDiscuss(userId, discussContent)


