from django.db import models

# Create your models here.
class Product_category(models.Model):
    pcid=models.IntegerField()
    pcname=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.pcname
class Product(models.Model):
    pcname=models.ForeignKey(Product_category,on_delete=models.CASCADE)
    pid=models.IntegerField()
    pname=models.CharField(max_length=20)
    pprice=models.IntegerField()
    pdescription=models.TextField()

    pdate=models.DateField()