from django.contrib.auth.forms import UserCreationForm
from django import forms
from djangoproj1.app1 import mongodb

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class AddDiscuss(forms.Form):
    discussContent = forms.CharField(label='Discuss Content', widget=forms.Textarea)
    topicId = forms.CharField(widget=forms.HiddenInput)

    def save(self, userId):
        discussContent = self.cleaned_data['discussContent']
        topicId = self.cleaned_data['topicId']
        return mongodb.addDiscuss(userId, topicId, discussContent)


