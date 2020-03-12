from django import forms
from discipline_journal.models import Profile, Punishment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'surname',
            'name',
            'middle_name',
            'department',
            'position',
            'photo'
        ]

class PunishmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs): 
        super(PunishmentForm, self).__init__(*args, **kwargs)                       
        self.fields['profile'].disabled = True

    class Meta:
        model = Punishment
        fields = '__all__'
        widgets = {
        'date': forms.DateInput(attrs={'class': 'date-input'}),
    }
    