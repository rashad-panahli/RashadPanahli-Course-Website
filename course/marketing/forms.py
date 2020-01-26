from django import forms
from .models  import Signup


class SignupForm(forms.ModelForm):
    email = forms.EmailField(label='')
    class Meta:
        model = Signup
        fields = ['email']
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        print(email)
        qs = Signup.objects.filter(email__iexact=email)
        if qs.exists():
            print('exists')
            raise forms.ValidationError("Bu email mövcuddur")
        return email