from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    summary = models.TextField(blank=True, null=False)
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        #return "/product/{}".format(self.id)
        return reverse('product:product_detail',kwargs={"my_id": self.id})