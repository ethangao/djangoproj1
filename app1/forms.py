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

class AddTopic(forms.Form):
    topicTitle = forms.CharField(max_length=512, widget=forms.TextInput(attrs={'name': 'topicTitle'}))
    topicContent = forms.CharField(widget=forms.Textarea(attrs={'name': 'editor1', 'id':'editor1'}) )
    topicTags = forms.CharField(max_length=1024, widget=forms.TextInput(attrs={'name': 'topicTags'}))

    def save(self, userId):
        topicTitle = self.cleaned_data['topicTitle']
        topicContent = self.cleaned_data['topicContent']
        topicTags = self.cleaned_data['topicTags']
        return mongodb.addTopic(userId, topicTitle, topicContent, topicTags)