from django import forms
from django.core import validators

from blog.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'description', 'text',)

        widgets = {
            'title':forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True,
                                   widget=forms.TextInput(attrs={'placeholder':'Name' }))
    contact_email = forms.EmailField(required=True,
                                     widget=forms.TextInput(attrs={'type':'email','placeholder':'Email' }))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder':'Message'})
    )
    bot_catcher = forms.CharField(required=False,
                                  widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"
