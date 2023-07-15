from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# creating a category table in our database
class Category(models.Model):
  name= models.CharField(max_length=255)

  class Meta:
    # ordering our data in table
    ordering =('name',)
    # changing name of our table in admin site
    verbose_name_plural ='Categories'

  # returning name of object 
  def __str__(self):
    return self.name


class Item(models.Model):
  
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True,null=True)
  price = models.FloatField()
  # upload_to will create a new folder to store images if no item_images folder is present
  image = models.ImageField(upload_to='item_images',blank=True,null=True)
  is_sold = models.BooleanField(default=False)
  created_at= models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User,related_name="items",on_delete=models.CASCADE)
  category = models.ForeignKey(Category,related_name="items",on_delete=models.CASCADE)  

  # returning name of object 
  def __str__(self):
    return self.name