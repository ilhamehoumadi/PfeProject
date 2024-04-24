from django.db import models

# Create your models here.
class Category(models.Model):

    
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    
    def __str__(self) :
        return self.name
    class Meta:
        #verbose_name = '',
        ordering =['name']
        