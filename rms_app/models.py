from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse




class Food(models.Model):
    food_item = models.CharField(max_length=100)
    per_price = models.PositiveIntegerField()
    food_img = models.ImageField(default="default_food.jpg", upload_to="food_pics")

    def __str__(self):
        return self.food_item

    def save(self, *args, **kwargs):
        super(Food, self).save(*args, **kwargs)

        img = Image.open(self.food_img.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.food_img.path)


class Invoice(models.Model):
    invoice_number = models.BigAutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse('add_items_on_invoice', kwargs={'pk': self.pk})





class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="invoiceitem")
    item   = models.ForeignKey(Food, on_delete=models.PROTECT,null=True,blank=True)
    quantity = models.PositiveIntegerField()
    accumulated =  models.PositiveIntegerField(default=0)

    
    def __str__(self):
        return self.invoice.customer_name
    
    @property
    def price(self):
        return  self.item.per_price
    
    @property
    def currentitem(self):
        return  self.item

    @property
    def creator(self):
        return self.invoice.created_by

    @property
    def multiply(self):
        return (self.item.per_price)*(self.quantity)



    def save(self, *args, **kwargs):
        self.accumulated = (self.item.per_price)*(self.quantity) 
        super(InvoiceItem, self).save(*args, **kwargs)




