# from django import forms
# from .models import BlogPost


# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ['title', 'body', 'image', 'active']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
#             'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
#             'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#         }


from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

