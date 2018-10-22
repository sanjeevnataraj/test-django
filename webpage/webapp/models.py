from django.db import models

class CollegeDetails(models.Model):

	Type_entity = models.CharField(max_length=100)

	Entity_name = models.CharField(max_length=100)

	College_website = models.URLField(max_length=100)

	Contactno = models.PositiveIntegerField()
	
	Contactno2 = models.PositiveIntegerField()

	Email = models.EmailField(max_length=100)

	Location = models.CharField(max_length=100)

	Publish = models.BooleanField(default=True)

class Facilites(models.Model):

	college_facility = models.ForeignKey(CollegeDetails, on_delete=models.CASCADE)

	ownership = models.CharField(max_length=100)

	gender = models.CharField(max_length=100)

	year = models.CharField(max_length=4)

	campus_size = models.PositiveIntegerField()

	total_faculty = models.PositiveIntegerField()

class Admissions(models.Model):

	college_admission = models.ForeignKey(CollegeDetails, on_delete=models.CASCADE)

	Exam = models.CharField(max_length=100)

	Quota = models.CharField(max_length=100)

	Cut_off = models.CharField(max_length=100)

	Seat_reservation = models.CharField(max_length=100)

	Admisson_process = models.CharField(max_length=100)

class Approvals(models.Model):

	college_approval = models.ForeignKey(CollegeDetails, on_delete=models.CASCADE)

	approvals = models.CharField(max_length=100)

	other_approval = models.CharField(max_length=100)

	Accreditations = models.CharField(max_length=100)


class Aluminis(models.Model):

	Name = models.CharField(max_length=100)

	Current_designation = models.CharField(max_length=100)

	Comapany = models.CharField(max_length=100)

	Sort_order = models.CharField(max_length=100)

	College =  models.CharField(max_length=100)

	Course = models.CharField(max_length=122)
	