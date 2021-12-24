from django import forms
from django.db import models
from django.forms import fields    
from .models import Property, Activity

class PropertyForm(forms.ModelForm):
    
    class Meta:
        model = Property
        fields = ('title','address','description','status','disableddate')
        labels = {
            'title' : 'Title Property',
            'address' : 'Address',
            'description' : 'Description',
            'status':'Status',
            'disbaleddate' : 'Disabled Date'
             }

    def __init__(self, *args, **kwargs ):
        super(PropertyForm,self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "Status"


class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ('title_activity','status_activity','property_id','schedule')
        
def __init__(self, *args, **kwargs ):
        super(PropertyForm,self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "Status"