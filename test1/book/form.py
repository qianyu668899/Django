from django import forms
from models import Publisher
from django.forms import ModelForm


class PublisherForm(ModelForm):
    class Meta:				
        model = Publisher

TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestion'),
)

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=False)


    def clean_message(self):
		message = self.cleaned_data.get('message', '')
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError("Not Enough Words!")
		return message