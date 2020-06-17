from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class dept(models.Model):
    dname=models.CharField(max_length=15)
    d_no=models.IntegerField(primary_key=True)

    class Meta:
    	db_table='dept'
    	ordering=['d_no']
		
class employ(models.Model):
	name=models.CharField(max_length=20)
	age=models.IntegerField()
	e_id=models.AutoField(primary_key=True)
	salary=models.IntegerField()
	d_no=models.ForeignKey(dept,on_delete= models.CASCADE)
	contact_no=models.CharField(max_length=13)
	address=models.CharField(max_length=30)

	class Meta:
		db_table = 'employ'
		ordering=['d_no']

	def get_absolute_url(self):
		return reverse('Home')








    



	




		









