from django import forms
from .models import Post,Comment
from captcha.fields import CaptchaField




class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["title","content","image"]

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["author","text"]

class ContactForm(forms.Form):
    from_email=forms.EmailField(max_length=255)
    subject = forms.CharField()
    message=forms.CharField(widget=forms.Textarea)
class CaptchaForm(forms.Form):
    captcha = CaptchaField()