from django import forms
from .models import Post
from .models import Contact

class AddPost(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['text',]
        
        
class AddForm(forms.Form):
    
    class Meta:
        model = Contact
        fields = ('name',)