from django import forms

class contact_form(forms.Form):
    Vorname = forms.CharField( max_length=100, label='Vorname*')
    Nachname = forms.CharField(max_length=100, label='Nachname*')
    EMail_Adresse = forms.EmailField(widget=forms.TextInput(
    attrs={'type': 'email', 'placeholder': ('E-mail Adresse einfügen*')}),label="E-Mail Adresse")
    Beschreibung = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Beschreiben Sie worum es geht.*'}), label="Beschreibung*")
    AGB_akzeptiert_und_verstanden= forms.BooleanField(required=True, label='AGB Akzeptiert und verstanden?*')