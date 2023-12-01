from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Video
from .models import MentorshipApplication


class Video_form(forms.ModelForm):
  class Meta:
    model=Video
    fields=("caption","video")

class MentorshipApplicationForm(forms.ModelForm):
    class Meta:
        model = MentorshipApplication
        fields = ('field1', 'field2')
