from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

# CLASSES THAT DEFINE THE TYPE OF DATE WE WANT IN THE DBMS
class City(models.Model):
    # if foreign key : models.ForeignKey(TableY, on_delete=models.CASCADE, related_name='attributeInTableY')
    name = models.CharField(max_length=64, default='City')
    image = models.URLField(default='https://images.pexels.com/photos/139229/pexels-photo-139229.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260')
    price = models.FloatField(default=0.0)
    dpt = models.TextField(default='Colombia')
    iata = models.CharField(max_length=3, default='COL')
    # if many to many relation
    # x = models.ManyToManyField( TableY, blank=True, related_name="attributeInTableY"  )

    def __str__(self):
        return f'{self.name} ({self.iata}) - $ {self.price} - {self.dpt} '

