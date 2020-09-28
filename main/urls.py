"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    path( '', views.home, name="home"),
    path( 'home.html', views.home, name="home"),
    path( 'contact.html', views.contact, name="contact"),
    path( 'about.html', views.about, name="about"),
    path( 'services.html', views.services, name="services"),
    path( 'appointment.html', views.appointment, name="appointment"),
    path( 'referral.html', views.referral, name="referral"),
    path( 'Personal_Care_Support.html', views.Personal_Care_Support, name="Personal_Care_Support"),
    path( 'Assistance_with_self_Care_activities.html', views.Assistance_with_self_Care_activities, name="Assistance_with_self_Care_activities"),
    path( 'Cleaning_Gardening.html', views.Cleaning_Gardening, name="Cleaning_Gardening"),
    path( 'Community_Participation.html', views.Community_Participation, name="Community_Participation"),
    path( 'Travel_Transport_Assist.html', views.Travel_Transport_Assist, name="Travel_Transport_Assist"),
    path( 'Support_Coordination.html', views.Support_Coordination, name="Support_Coordination"),
    path( 'Supported_Independent_Living.html', views.Supported_Independent_Living, name="Supported_Independent_Living"),
    path( 'Plan_Management.html', views.Plan_Management, name="Plan_Management"),
    path( 'Respite_Care.html', views.Respite_Care, name="Respite_Care"),
    path( 'Home_Modification.html', views.Home_Modification, name="Home_Modification"),
    path( 'Accommodation.html', views.Accommodation, name="Accommodation"),
    path( 'Exercise_physiology_Fitness_Trainer.html', views.Exercise_physiology_Fitness_Trainer, name="Exercise_physiology_Fitness_Trainer"),
    path( 'Allied_Health.html', views.Allied_Health, name="Allied_Health"),
    path( 'Incontinence_Assessment.html', views.Incontinence_Assessment, name="Incontinence_Assessment"),
    path( 'Specialized_Community_Nursing.html', views.Specialized_Community_Nursing, name="Specialized_Community_Nursing"),
    
]
