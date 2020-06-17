from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Signup
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DetailView,ListView,DeleteView
from .models import employ
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def SignUp(request):
	if request.method=='POST':
	    form=Signup(request.POST)	
	    if form.is_valid():
	        form.save()
	        username=form.cleaned_data.get('username')
	        messages.success(request,f'Account created for {username}')
	        return  redirect('login')
	else:
		form = Signup()
	return render(request,'rests/Fp.html',{'form':form})

@login_required
def home(request):
	return render(request,'rests/Home.html')
@login_required
def Employee(request):
	return render(request,'rests/Employ.html')

class e_list(LoginRequiredMixin,ListView):
	model=employ
	template_name='rests/Employ.html'
	ordering=['d_no','name']
	context ={

        'emp':employ.objects.all()
	}
	context_object_name='emp'

class e_detail(LoginRequiredMixin,DetailView):
	model=employ
	template_name='rests/employ_detail.html'

class e_insert(LoginRequiredMixin,CreateView):
	model=employ
	fields=['name','age','salary','d_no','contact_no','address']
	template_name='rests/e_insert_form.html'

class e_update(LoginRequiredMixin,UpdateView):
	model=employ
	fields=['e_id','name','age','salary','d_no','contact_no','address']

class e_delete(LoginRequiredMixin,DeleteView):
	model=employ
	success_url='/Employee'
	


		




	

