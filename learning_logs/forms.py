from django import forms

from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        # field = ['text']
        fields = '__all__'
        labels = {'text': ""}
