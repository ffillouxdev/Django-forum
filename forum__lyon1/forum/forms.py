from django import forms
from django.contrib.auth import get_user_model
from .models import Topic
from .models import Reply


User = get_user_model()

"""
class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']
"""
class CreateTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description', 'section'] 


class ReplyTopicForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5, 'placeholder': 'Your message'}))
    
class ReplyTopicForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'placeholder': 'Enter your reply here...'}), max_length=4000)

    class Meta:
        model = Reply
        fields = ['text']

    def save(self, commit=True, **kwargs):
        instance = super(ReplyTopicForm, self).save(commit=False)
        instance.author = kwargs.get('author')
        instance.topic = kwargs.get('topic')
        if commit:
            instance.save()
        return instance
