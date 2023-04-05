from dataclasses import fields
from pyexpat import model
from unicodedata import name
from django import forms
from matplotlib import widgets
from matplotlib.rcsetup import all_backends

from tuition.models import Contact
from .models import Contact,Post

class ContactForm(forms.ModelForm):
    name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Name'}), label='My Name')
    class Meta:
        model  = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'My Name'
        self.fields['name'].initial = 'My Name '
        self.fields['phone'].initial = '+880'
        

    def clean_name(self):
        value =self.cleaned_data.get('name')
        num_of_w = value.split(' ')
        if len(num_of_w) > 3:
            self.add_error('name', 'Name can have maximum of 3 words')
        else:
            return value
        """widgets ={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Phone Number'}),
            'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Say Something','rows':5})
        }

        labels = {
            'name':'Your Name',
            'phone':'Your Phone Number',
            'content':'Your Words'
        
        }

        help_texts = {
            'name':'Your Name',
            'phone':'Your Phone Number',
            'contact':'Your Words',
        }"""


class ContactFormTwo(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

from .fields import ListTextWidget
class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        exclude = ['user','id','created_at','slug','likes','views']
        widgets = {
            'class_in':forms.CheckboxSelectMultiple(attrs={
                'multiple':True,
            }),
            'subject':forms.CheckboxSelectMultiple(attrs={
                'multiple':True,
            })
        }
    def __init__(self, *args, **kwargs):
        _district_set=kwargs.pop('district_set',None)
        super(PostForm,self).__init__(*args, **kwargs)
        self.fields['district'].widget=ListTextWidget(data_list=_district_set, name='district-set')

from .models import PostFile
class FileModelForm(forms.ModelForm):
    class Meta:
        model=PostFile
        fields=['image']


