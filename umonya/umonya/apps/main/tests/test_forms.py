from umonya.apps.main.forms import RegistrationForm
from django.test import TestCase
from umonya.apps.main.models import Registration, Dynamic_Section


class TestForms(TestCase):
    def test_form_rendering(self):
        Dynamic_Section.objects.create(section="registration", enabled=True)
        Registration.objects.create(name="name", field_type="CharField", text="What is Your Name?", priority=1, required=True)
        Registration.objects.create(name="age", field_type="IntegerField", text="How Old are you", priority=5, required=False)
        response = self.client.get("/registration/")
        self.assertTrue('form' in response.context)
        self.assertContains(response, "What is Your Name?")

    def test_empty_registration_form(self):
        # Testing the processing of the registration form in the views functionRegistration_Question.objects.create(name="name", field_type="CharField", text="What is Your Name?", priority=1, required=True)
        Registration.objects.create(name="name", field_type="CharField", text="What is Your Name?", priority=1, required=True)
        Registration.objects.create(name="age", field_type="IntegerField",
                                    text="How Old are you", priority=5, required=False)
        data = {"name": "", "age": ""}
        form = RegistrationForm(data=data)
        self.assertEqual(form["name"].errors, [u'This field is required.'])
        self.assertEqual(form["age"].errors, [u'This field is required.'])
