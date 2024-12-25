from django import forms
from .models import Critique, Comment

class CritiqueForm(forms.ModelForm):
    class Meta:
        model = Critique
        fields = ("title", "content", "note", "film")
        
        def clean_note(self):
            note = self.cleaned_data.get('note')
            if note > 5:
                raise forms.ValidationError("La note ne doit pas depasser 5")
            return note

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['film'].widget.attrs.update({'class': 'form-control', 'style': 'background-color: #333; color: #fff;'})
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'style': 'background-color: #333; color: #fff;'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'style': 'background-color: #333; color: #fff;'})
        self.fields['note'].widget.attrs.update({'class': 'form-control', 'style': 'background-color: #333; color: #fff;'})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('critique', 'text')