from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Form
from .forms import ReqForm
from .filters import FormFilter

def form(request):
    return render(request,'form.html')
def status(request):
    return render(request,'status.html')
def about(request):
    return render(request,'about.html')
def index(request):
    return render(request,'index.html')
#fields=['id','email','ClubName','RepresentativeName','Contact','req_date_from','req_date_to',
# 'req_type','req_purpose','req_purpose','formtime']
def showformdata(request):
    if request.method=='POST':
        fm=ReqForm(request.POST)
        if fm.is_valid():
            em=fm.cleaned_data['email']
            cn=fm.cleaned_data['ClubName']
            rn=fm.cleaned_data['RepresentativeName']
            cn=fm.cleaned_data['Contact']
            df=fm.cleaned_data['req_date_from']
            dt=fm.cleaned_data['req_date_to']
            rt=fm.cleaned_data['req_type']
            rp=fm.cleaned_data['req_purpose']
            profile = fm.save(commit=False)
            profile.user = request.user
            profile.save()
            fm.save()    
            fm=ReqForm()   
            print(em)    
            print(rn) 
    else:
        fm=ReqForm()
    return render(request,'form.html',{'frm':fm})
    
def reqInfo(request):
    u=request.user
    req = Form.objects.filter(user=request.user)
    print(req)
    context={
        'form':form,
        'req': req
    }
    return render(request,'status.html',context)
#  active_orders = MyModel.objects.filter(user=request.user)
#     context = {
#        'form': form,
#        'active_orders': active_orders
#     }
#     return render(request, "main/mytemplate.html", context)