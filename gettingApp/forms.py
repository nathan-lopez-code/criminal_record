from django import forms



class SeachbynameForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control bg-light border-0 small',
        'placeholder': 'Rechercher un casier par nom...',
        'aria-label': 'search',
        'aria-describedby': 'basic-addon2',
    }), error_messages={'required': 'Please enter your name'})


class Searhcbyimage(forms.Form):
    image = forms.FileField()
    image.widget.attrs.update(
        {
            'class': 'file-drop-input',
            'accept': '.png, .jpg, .jpeg',
        }
    )
