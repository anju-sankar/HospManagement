from django.db import models

# Create your models here.
class dept_tbl(models.Model):
    name = models.CharField(max_length= 50)
    des = models.CharField(max_length= 100)
    def __str__(self):
        return self.name

class doc_tbl(models.Model):
    doc_name = models.CharField(max_length= 50)
    doc_img = models.FileField(upload_to="pictures")
    dept_name = models.ForeignKey(dept_tbl,on_delete=models.CASCADE)
    def __str__(self):
        return self.doc_name

class reg_tbl(models.Model):
    name = models.CharField(max_length= 5)
    mob = models.IntegerField()
    email = models.EmailField()
    password= models.CharField(max_length=100)
    user_type = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class book_appt_tbl(models.Model):
    name = models.CharField(max_length= 5)
    mob = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=40)
    district = models.CharField(max_length=40)
    date = models.DateField()
    test = models.CharField(max_length=40)
    doc_name = models.CharField(max_length=50)
    user = models.ForeignKey(reg_tbl,on_delete=models.CASCADE)
    def __str__(self):
        return self.name