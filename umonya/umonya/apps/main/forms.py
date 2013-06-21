from django import forms
from models import Registration, Contact


class RegistrationForm(forms.Form):
    questions = Registration.objects.all().order_by("priority")
    for item in questions:
        required = ""
        if item.required:
            required = "required"

        if item.field_type == "CharField":
            vars()[item.name] = forms.CharField(label=item.text, required=item.required,
                                                widget=forms.TextInput(attrs={"class": required, required: ""}))
        elif item.field_type == "EmailField":
            vars()[item.name] = forms.EmailField(label=item.text, required=item.required,
                                                 widget=forms.TextInput(attrs={"class": required, required: "",
                                                                        "type": "email"}))
        elif item.field_type == "IntegerField":
            vars()[item.name] = forms.IntegerField(label=item.text, required=item.required,
                                                   widget=forms.TextInput(attrs={"class": required, required: ""}))
        elif item.field_type == "TextField":
            vars()[item.name] = forms.CharField(label=item.text, required=item.required,
                                                widget=forms.Textarea(attrs={"class": required, required: ""}))


class ContactForm(forms.Form):
    class Meta:
        model = Contact
