from django.db import models
import string
import random
from django.contrib.auth.models import User

# Create your models here.





class cart_product(models.Model):
#  field = ArrayField(base_field=models.CharField(max_length=100), default=default_strings, blank=True, null=True)
#  tokens = models.JSONField(default=default_tokens(), blank=True, null=True)
 user = models.ForeignKey(User, on_delete=models.CASCADE)
#  user=models.CharField(max_length=150,default="vamsi")
 p_key=models.CharField(default='a', max_length=50)
 img = models.URLField(default='/') 
 name=models.TextField()
 description=models.TextField(default='jfjnj')
 price=models.IntegerField()
 discount=models.IntegerField(default=0)
 qty=models.IntegerField(default=1)
 
 def __str__(self):
        return self.name
 



class product(models.Model):
 p_key=models.CharField(default='a', max_length=50)
#  customer = models.ManyToManyField(cart_product)
 img = models.URLField(default='/') 
 name=models.TextField()
 description=models.TextField(default='ff')
 price=models.IntegerField()
 discount=models.IntegerField(default=0)
 #  incart=models.BooleanField(default=False)
 def save(self, *args, **kwargs):
        if not self.pk:  # Only generate a random key if the instance is being created (not updated)
            self.p_key = self.generate_random_key(50)
        super().save(*args, **kwargs)

 @staticmethod
 def generate_random_key(length):
        characters = string.ascii_letters + string.digits
        random_key = ''.join(random.choices(characters, k=length))
        return random_key
 def __str__(self):
        return self.name
