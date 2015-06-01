from django import forms
from models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('author', 'title',)

    def title_save(self):
        self.save()