from lingcod.features.forms import FeatureForm
from django import forms
from models import *

class FolderForm(FeatureForm):
    name = forms.CharField(label='Folder Name')
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}), required=False)
    class Meta(FeatureForm.Meta):
        model = Folder

class UserKmlForm(FeatureForm):
    class Meta(FeatureForm.Meta):
        model = UserKml
