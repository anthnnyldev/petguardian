from django import forms
from .models import Report, Comment

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['pet_description', 'post_description', 'media', 'latitude', 'longitude']
        widgets = {
            'pet_description': forms.Textarea(attrs={'rows': 3, 'class': 'w-full border rounded-md p-2'}),
            'post_description': forms.Textarea(attrs={'rows': 3, 'class': 'w-full border rounded-md p-2'}),
            'media': forms.ClearableFileInput(attrs={'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

class ReportDeleteForm(forms.Form):
    confirm_delete = forms.BooleanField(label='Confirmar eliminación', required=True)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2, 'class': 'w-full border rounded-md p-2'}),
        }