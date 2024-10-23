from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse
def form(request):
    return render(request,'form.html')
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        to=Topic.objects.get_or_create(topic_name=tn)
        return HttpResponse(f'{tn} is created')
    
    return render(request,'insert_topic.html')
def insert_webpages(request):
    To=Topic.objects.all()
    d={'topics':To}
    if request.method=='POST':
        tn=request.POST['topic']
        to=Topic.objects.get(topic_name=tn)
        n=request.POST['n']
        u=request.POST['u']
        e=request.POST['e']
        wo=Webpages.objects.get_or_create(topic_name=to,name=n,url=u,email=e)
        return HttpResponse('data is inserted')
    return render(request,'insert_webpages.html',d)
def select_multiple(request):
    TO=Topic.objects.all()
    d={'TO':TO}
    if request.method=='POST':
        MTN=request.POST.getlist('tn')
        EQST=Webpages.objects.none()
        for i in MTN:
            EQST=EQST|Webpages.objects.filter(topic_name=i)
        d1={'EQST':EQST}
        return render(request,'display_webpages.html',d1)
            
        
    return render(request,'select_multiple.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        MTN=request.POST.getlist('tn')
        EQST=Webpages.objects.none()
        for i in MTN:
            EQST=EQST|Webpages.objects.filter(topic_name=i)
        d1={'EQST':EQST}
        return render(request,'display_webpages.html',d1)
            
    return render(request,'checkbox.html',d)
