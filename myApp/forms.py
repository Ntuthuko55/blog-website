from django import forms
from myApp.models import destination,comments

class ArticleForm(forms.ModelForm):
    class Meta():
        model = destination
        exclude =['id','createdAt',]
        #fields = '__all__'

class CommentsForm(forms.ModelForm):
    class Meta():
        model=comments
        exclude =['id','date_added',]
        