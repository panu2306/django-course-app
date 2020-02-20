from django import forms

class NameForm(forms.Form):
    name = forms.CharField(max_length=64)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_botcatcher(self):
        botcatcher_field = self.cleaned_data['botcatcher']
        
        if(len(botcatcher_field) > 0):
            raise forms.ValidationError("Gotcha Bot")        
        return botcatcher_field

    