from django.db import models
class Emp(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    sal=models.IntegerField()
    img=models.ImageField(upload_to='pic')
    def __str__(self) -> str:
        return self.name+' '+self.email