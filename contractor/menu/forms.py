from django import forms
from menu.models import MenuItem


class PageForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta():
        model = MenuItem
        fields = ['name','description', 'price']
