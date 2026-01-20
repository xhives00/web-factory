from django import forms

class PbTimeForm(forms.Form):
    U = forms.FloatField(label="U (g)", min_value=0)
    Th = forms.FloatField(label="Th (g)", min_value=0)
    Pb = forms.FloatField(label="Pb (g)", min_value=0)
