from django.shortcuts import render
from django.http import HttpResponse
from appvahed.models import mdl_vahed
from appvahed.forms import frm_vahed

# Create your views here.

def vw_home(request):
    vahedha=mdl_vahed.objects.all()
    return render(request,"about.html",{"vahedha":vahedha,"frm_vahed":frm_vahed()})
	
	#return HttpResponse("ok")
def vw_login(request):
    return render(request,"login.html",)
    

	
def vw_sabtvahed(request):
    print request.POST
    cur_frm=frm_vahed(request.POST)
    if cur_frm.is_valid():
        cur_frm.save()    
        return HttpResponse("ok")		
    return render(request,"about.html",{"frm_vahed":cur_frm})