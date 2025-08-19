from django import forms
from .models import Photo, Video, KeyInfo, OrganizationContent, Notice, Notice
from ckeditor.widgets import CKEditorWidget

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name',
            'id': 'name',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Email',
            'id': 'email',
        })
    )
    subject = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Subject',
            'id': 'subject',
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Leave a message here',
            'id': 'message',
            'style': 'height: 150px;',
        })
    )



class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'youtube_url']   



class KeyInfoForm(forms.ModelForm):
    class Meta:
        model = KeyInfo
        fields = ['key_strategy', 'key_achievement']



class OrganizationContentForm(forms.ModelForm):
    class Meta:
        model = OrganizationContent
        fields = '__all__'
        widgets = {
            'mission': CKEditorWidget(),
            'vision': CKEditorWidget(),
            'goal': CKEditorWidget(),
            'objective': CKEditorWidget(),
            'value': CKEditorWidget(),
            'geo_area': CKEditorWidget(),
            'theme_area': CKEditorWidget(),
        }        

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'content', 'attachment', 'is_active']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        help_texts = {
            'attachment': 'Upload a file (PDF, DOC, etc.) related to this notice (optional)',
            'is_active': 'Uncheck to hide this notice from the website',
        }
