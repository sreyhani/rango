from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from edusys.models import Course


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class ContactUs(forms.Form):
    title = forms.CharField(max_length=30, required=True, label='title')
    email = forms.EmailField(max_length=30, required=True, label='email')
    text = forms.CharField(min_length=10, max_length=250, required=True, widget=forms.Textarea, label='text')


class CourseForm(forms.ModelForm):
    exam_date = forms.DateField(input_formats='%Y-%m-%d')
    class Meta:
        model = Course
        fields = "__all__"

#
# class ImageUploadForm(forms.Form):
#     image = forms.ImageField()


class SearchCourse(forms.Form):
    search_query = forms.CharField(max_length=50, required=True, label="search_query")
    department = forms.BooleanField(required=False)
    teacher = forms.BooleanField(required=False)
    course = forms.BooleanField(required=False)
