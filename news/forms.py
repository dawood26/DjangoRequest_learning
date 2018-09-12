from django.forms import ModelForm
from . models import Article,Reporter
class ReporterForm(ModelForm):
    class Meta:
        model = Reporter
        fields = ['full_name', 'contact', 'email']
