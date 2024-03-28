from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from  aboutus.models import AboutUs
from education.models import Education
from skills.models import Skills
from experience.models import Experience
from project.models import Project
import plotly.express as px
import base64,urllib
from io import BytesIO

def education(request):
    education_data=Education.objects.all()
    data={
        'education_data':education_data
    }
    return render(request,"education.html",data)



def aboutus(request):
    aboutus_data=AboutUs.objects.all()
   
    data={
        'aboutus_data':aboutus_data
    }
    return render(request,"index.html",data)

def contact(request):
    contact_data=AboutUs.objects.all()
    data={
        'contact_data':contact_data
    }
    return render(request,"contact.html",data)

def experience(request):
    experience_data=Experience.objects.all()
    
    data={
        'experience_data': experience_data
    }
    return render(request,"experience.html",data)

def skills(request):
    skills_data=Skills.objects.all()
    
   
    fig=px.bar(
        x=[i.skills_name for i in skills_data],
        y=[i.rating for i in skills_data],
        title="Skills and Respective Rating",
        labels={'x':'Skills Name','y':'Rating'}
    )
    chart=fig.to_html()
    data={
        'chart':chart,
        'skills_data':skills_data
    }
    
    return render(request,"skills.html",data)

def projects(request):
    project_data=Project.objects.all()
    data={
        'project_data':project_data
    }
    return render(request,"projects.html",data)

