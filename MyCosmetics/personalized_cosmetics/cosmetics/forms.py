from django import forms

class CosmeticPreferenceForm(forms.Form):
    skin_type_choices = [
        ('oily', 'Oily'),
        ('dry', 'Dry'),
        ('combination', 'Combination'),
        ('normal', 'Normal'),
    ]
    
    skin_type = forms.ChoiceField(choices=skin_type_choices, label='Skin Type')
    age = forms.IntegerField(label='Age', min_value=0)
    concerns = forms.CharField(label='Concerns', max_length=200, widget=forms.Textarea)
    preferences = forms.CharField(label='Preferences', max_length=200, widget=forms.Textarea)