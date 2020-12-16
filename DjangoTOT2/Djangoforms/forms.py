from django import forms

gender_choice = [('Male','Male'),('Female',"Female")]
langs = [('python','python'),('java','java')]
branches = [('CSE','CSE'),('ECE','ECE'),('EEE','EEE'),('CIVIL','CIVIL')]
class DynamicHtmlFormGen(forms.Form):
	firstname = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter your FirstName','name':'firstname','class':'form-control'}))
	lastname = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter your lastname','name':'lastname','class':'form-control'}))
	age = forms.CharField(widget = forms.NumberInput(attrs={'placeholder':'Enter your Age','name':'age','class':'form-control'}))
	email = forms.CharField(widget = forms.EmailInput(attrs={'placeholder':'Enter your Email Id','name':'email','class':'form-control'}))
	gender = forms.ChoiceField(widget = forms.RadioSelect(attrs={'name':'gender'}),choices=gender_choice)
	select_branch = forms.ChoiceField(widget = forms.Select(attrs={'class':'custom-select','name':'branch'}),choices=branches)
	language = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple(attrs={'name':'language'}),choices=langs)


	# """docstring for DynamicHtmlFormGen"""
	# def __init__(self, arg):
	# 	super(DynamicHtmlFormGen, self).__init__()
	# 	self.arg = arg
