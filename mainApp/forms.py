from django import forms


class LandingPageForm(forms.Form):
    csv_data = forms.FileField(widget=forms.FileInput(attrs={'accept': ".csv"}), label='Select a file')
