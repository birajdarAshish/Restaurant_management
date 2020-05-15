from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import menu,bill,orders
from django.forms.models import model_to_dict

# Create your views here.
@login_required
def order(request):
	context ={

        'menus':menu.objects.all()

	}
	me = menu.objects.all()
	if request.method =='POST':
		bills= bill()
		bills.amt=0
		bills.save()
		print(request.POST.get(6))
		for men in me:
			i=men.item_no
			if request.POST.get(str(i))!='0':
				obj = menu.objects.get(name=men.name)
				order = orders()
				order.b_no=bills
				order.item= obj
				order.qty=int(request.POST.get(str(i)))
				order.save()
				costs =men.price * order.qty

				bills.amt =costs+bills.amt
				bills.save()
				i=i+1
		return redirect('Home')
	else:
		return render(request,'order/orderz.html',context)
@login_required
def menus(request):
	context ={

        'menus':menu.objects.all()
	}

	return render(request,'order/menu.html',context)

	

