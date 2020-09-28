from django.shortcuts import render



# Create your views here.
def home(request):
	return render(request, 'home.html',{})

def contact(request):
	return render(request, 'contact.html',{})

def about(request):
	return render(request, 'about.html',{})

def services(request):
	return render(request, 'services.html',{})

def appointment(request):
	return render(request, 'appointment.html',{})

def referral(request):
	return render(request, 'referral.html',{})

def Personal_Care_Support(request):
	return render(request, 'Personal_Care_Support.html',{})

def Assistance_with_self_Care_activities(request):
	return render(request, 'Assistance_with_self_Care_activities.html',{})

def Cleaning_Gardening(request):
	return render(request, 'Cleaning_Gardening.html',{})

def Community_Participation(request):
	return render(request, 'Community_Participation.html',{})

def Travel_Transport_Assist(request):
	return render(request, 'Travel_Transport_Assist.html',{})

def Support_Coordination(request):
	return render(request, 'Support_Coordination.html',{})

def Supported_Independent_Living(request):
	return render(request, 'Supported_Independent_Living.html',{})

def Plan_Management(request):
	return render(request, 'Plan_Management.html',{})

def Respite_Care(request):
	return render(request, 'Respite_Care.html',{})

def Home_Modification(request):
	return render(request, 'Home_Modification.html',{})

def Accommodation(request):
	return render(request, 'Accommodation.html',{})

def Exercise_physiology_Fitness_Trainer(request):
	return render(request, 'Exercise_physiology_Fitness_Trainer.html',{})

def Allied_Health(request):
	return render(request, 'Allied_Health.html',{})

def Incontinence_Assessment(request):
	return render(request, 'Incontinence_Assessment.html',{})

def Specialized_Community_Nursing(request):
	return render(request, 'Specialized_Community_Nursing.html',{})


