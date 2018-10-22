from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import CollegeDetails,Facilites,Admissions,Approvals
from .forms import CollegeDetailForm,Facilityform,Admissionform,Approvalform,Aluminiform
from django.urls import reverse

def college(request,pk=None):

	try:

		college = CollegeDetailForm()

		h=CollegeDetails.objects.get(pk=pk)

		college = CollegeDetailForm(request.POST or None, instance=h)
	
	except:

		college =  CollegeDetailForm(data=request.POST)

	if 'save' in request.POST:
		
		if college.is_valid():

			a = college.save()
			
			ids = a.id

			print(a.id)

			return HttpResponseRedirect(reverse('facility',args=(a.id,)))		

	return render(request,"collegedetail.html",{"college":college})

def facility(request,pk=None):
	
	try: 

		facilities  = Facilityform()

		h=Facilites.objects.get(college_facility_id=pk)

		facilities = Facilityform(request.POST or None, instance=h)
	
	except:

		facilities = Facilityform(data=request.POST)

	if 'next' in request.POST:

		if facilities.is_valid():

			k = facilities.save(commit=False)

			k.college_facility_id = pk

			k.save()

			ids = k.id

			return HttpResponseRedirect(reverse('admission',args=(pk,)))

	elif 'prev' in request.POST:

		return HttpResponseRedirect(reverse('college',args=(pk,)))

	return render(request,"facility.html",{"facilities":facilities,'ids':pk})

def Admission_view(request,pk):

	try: 

		admission  = Admissionform()

		h=Admissions.objects.get(college_admission_id=pk)

		admission = Admissionform(request.POST or None, instance=h)
	
	except:

		admission = Admissionform(data=request.POST)

	if 'next' in request.POST:

		if admission.is_valid():

		    h = admission.save(commit=False)

		    h.college_admission_id = pk

		    h.save()

		    return HttpResponseRedirect(reverse('approval',args=(pk,)))

	if 'prev' in request.POST:

		return HttpResponseRedirect(reverse('facility',args=(pk,)))

	return render(request,"admission.html",{"admission":admission,'ids':pk})



def approval(request,pk):

	try:

		approval = Approvalform()

		h=Approvals.objects.get(college_approval_id=pk)

		approval = Approvalform(request.POST or None, instance=h)
	
	except:

		approval = Approvalform(data=request.POST)

	if 'next' in request.POST:
		
		if approval.is_valid():

			m= approval.save(commit=False)

			m.college_approval_id = pk

			m.save()

	if 'prev' in request.POST:

		return HttpResponseRedirect(reverse('admission',args=(pk,)))


	return render(request,"approval.html",{"approval":approval,'ids':pk})































# def Alumini(request):

# 	if request.method=="POST":

# 		alumini = Aluminiform(dtaa=request.POST)

# 		if alumini.is_valid():

# 			alumini.save()

# 	else:

# 		alumini = Aluminiform()

# 	return render(request,'Alumini.html',{'alumini':alumini})


