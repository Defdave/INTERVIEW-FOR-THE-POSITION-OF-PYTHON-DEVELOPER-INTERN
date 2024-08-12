from django import forms
from .models import AnnouncedPUResults, PollingUnit, State, LGA, Ward
from datetime import datetime

class PollingUnitForm(forms.Form):
    polling_unit_id = forms.IntegerField(label='Polling Unit ID', min_value=1)


class ResultForm(forms.ModelForm):
    class Meta:
        model = AnnouncedPUResults
        fields = ['polling_unit_uniqueid', 'party_abbreviation', 'party_score', 'entered_by_user']

    def __init__(self, *args, **kwargs):
        super(ResultForm, self).__init__(*args, **kwargs)
        self.fields['polling_unit_uniqueid'].queryset = PollingUnit.objects.none()  # Start with empty queryset

        if 'ward' in self.data:
            try:
                ward_id = int(self.data.get('ward'))
                self.fields['polling_unit_uniqueid'].queryset = PollingUnit.objects.filter(ward_id=ward_id).order_by('polling_unit_uniqueid')
            except (ValueError, TypeError):
                pass