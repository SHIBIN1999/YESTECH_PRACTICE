from django.db import models

# Create your models here.
class department(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()


class doctors(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_spec=models.CharField(max_length=100)
    dep_name=models.ForeignKey(department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors')