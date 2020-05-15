from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Signup,Employee
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DetailView,ListView
from .models import employee
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
	return render(request,'rest/Fp.html',{'form':form})

@login_required
def home(request):
	return render(request,'rest/Home.html')
@login_required
def Employee(request):
	return render(request,'rest/Employee.html')

class e_list(LoginRequiredMixin,ListView):
	model=employee
	template_name='rest/Employee.html'
	ordering=['d_no','name']
	context ={

        'emp':employee.objects.all()
	}
	context_object_name='emp'

class e_detail(LoginRequiredMixin,DetailView):
	model=employee
	template_name='rest/employee_detail.html'

class e_insert(LoginRequiredMixin,CreateView):
	model=employee
	fields=['name','age','salary','d_no','contact_no','address']
	template_name='rest/e_insert_form.html'

class e_update(LoginRequiredMixin,UpdateView):
	model=employee
	fields=['e_id','name','age','salary','d_no','contact_no','address']


		




	

