from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_customer =models.BooleanField(default=False)
    is_staff =models.BooleanField(default=False)
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)

class Customer(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    phone_no=models.CharField(max_length=20)
    Cupmas = models.CharField(max_length=20,null=True)
    section=models.CharField(max_length=20,null=True)
    bulding_name=models.CharField(max_length=20,null=True)
    office_no =models.CharField(max_length=3,null=True)
    date_created =models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        
        return self.user.first_name

class Staff(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    phone_no=models.CharField(max_length=20)
    Cupmas = models.CharField(max_length=20,null=True)
    section=models.CharField(max_length=20,null=True)
    bulding_name=models.CharField(max_length=20,null=True)
    office_no =models.CharField(max_length=3,null=True)
    date_created =models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        
        return self.user.first_name

CATEGORY = (
              ('Ict Equipmaint','Ict Equipmaint'),
              ('Networking','Networking'),
              )


class Service(models.Model):
    
    name =models.CharField(max_length=20,null=True)
    category=models.CharField(max_length=20,null=True ,choices=CATEGORY)
    discription=models.TextField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
            return self.name
class Order(models.Model):
    STATUS = (
           ('pending','pending'),
           ('fixed','fixed'),
           ('not fixed','not fixed')
           )
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    service = models.ForeignKey(Service,on_delete=models.CASCADE,null=True)
    category=models.CharField(max_length=20,null=True ,choices=CATEGORY)
    discription=models.TextField(max_length=200,null=True)
    quantity =models.CharField(max_length=3,null=True)
    status=models.CharField(max_length=20,null=True,default='pending',choices=STATUS)
    date_created=models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return f'Name of Order: {self.service.name}'
    class Meta:
        ordering =['status']

class Post(models.Model):
    title = models.CharField(max_length=100,null=True)
    body = models.TextField()
    created =models.DateTimeField(auto_now_add=True,null=True)
    update =models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return self.title
    
