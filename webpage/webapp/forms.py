from django import forms
from webapp.models import CollegeDetails,Facilites,Admissions,Approvals,Aluminis

class CollegeDetailForm(forms.ModelForm):

    Type_entity = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    Entity_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    College_website = forms.URLField(widget=forms.URLInput(attrs={"class":"form-control"}))

    Contactno = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    Contactno2 = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    Email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))

    Location = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))



    class Meta():

	    model = CollegeDetails
		
	    fields = "__all__"
	    

class Facilityform(forms.ModelForm):

	ownership_choice = (('Please choose','Please choose'),('Public','Public'),('Private','Private'))

	gender_choice = (('Please choose','Please choose'),('Male','Male'),('Female','Female'))

	ownership = forms.ChoiceField(choices=ownership_choice,initial='Please choose')

	gender = forms.ChoiceField(choices=gender_choice,initial='Please choose')

	year = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))

	campus_size = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

	total_faculty = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

	class Meta():

		model = Facilites

		fields = ('ownership','gender','year','campus_size','total_faculty')

class Admissionform(forms.ModelForm):

	Exam = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

	choice1 = (('Please choose','Please choose'),('Yes','Yes'),('No','No'))

	choice2 = (('Please choose','Please choose'),('Yes','Yes'),('No','No'))
 
	Seat_reservation = forms.CharField( widget=forms.Textarea(attrs={"class":"md-textarea form-control"}))

	Admisson_process = forms.CharField(widget=forms.Textarea(attrs={"class":"md-textarea form-control"}))

	Quota = forms.ChoiceField(choices=choice1,initial='Please choose')

	Cut_off = forms.ChoiceField(choices=choice2,initial='Please choose')

	class Meta():

		model = Admissions

		fields = ('Exam','Quota','Cut_off','Seat_reservation','Admisson_process')



class Approvalform(forms.ModelForm):

	choice = (('Please choose','Please choose'),('Standalone institute','Standalone institute'),('Approved institute','Approved institute'),('Autonomous','Autonomous'))
	
	choice2 = (('Please choose','Please choose'),('NAAC','NAAC'),('NABH','NABH'))

	Accreditations = forms.ChoiceField(choices=choice2,initial='Please choose')

	approvals = forms.ChoiceField(choices=choice,initial='Please choose',widget=forms.Select(attrs={'class':'mdb-select md-form'}))

	other_approval = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

	class Meta():

		model = Approvals

		fields = ('approvals','other_approval','Accreditations')

class Aluminiform(forms.ModelForm):


	Name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

	Current_designation =forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
	
	Comapany = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
	
	Sort_order = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

	College =  forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

	Course = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

	class Meta():

		model = Aluminis

		fields = '__all__'

