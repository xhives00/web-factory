from django import forms

class PbTimeForm(forms.Form):
    U = forms.FloatField(label="U (ppm)", min_value=0)
    Th = forms.FloatField(label="Th (ppm)", min_value=0)
    Pb = forms.FloatField(label="Pb (ppm)", min_value=0)
