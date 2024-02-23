from django import forms  #import django forms

CHART__CHOICES = (        #specify choices as a tuple
    ('#1', 'Bar chart'),  # when user selects "Bar chart", it is stored as "#1"
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

class RecipesSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=120)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)