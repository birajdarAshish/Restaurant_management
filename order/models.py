from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class menu(models.Model):
	item_no=models.AutoField(primary_key=True)
	name=models.CharField(max_length=20)
	category=models.CharField(max_length=20)
	veg=models.CharField(max_length=2)
	price=models.IntegerField()


class bill(models.Model):
	b_id=models.AutoField(primary_key=True)
	amt=models.IntegerField()
	date=models.DateTimeField(default=timezone.now)
	
	class Meta:
		ordering = ['date']

	def __str__(self):
		return string(self.b_id)


class orders(models.Model):
   
    b_no=models.ForeignKey(bill, on_delete=models.CASCADE)	
    item=models.ForeignKey(menu,null=True,on_delete= models.PROTECT)
    qty=models.IntegerField()
    cost=models.IntegerField()

    def cost(self):
    	return self.item.price * self.qty
    



