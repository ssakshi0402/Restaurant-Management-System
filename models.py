from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

STATE_CHOICES = (
('Andhra Praadesh','Andhra Pradesh'),
('Arunachal Pradesh','Arunachal Pradesh'),
('Assam','Assam'),
('Bihar','Bihar'),
('Chhattisgarh','Chhattisgarh'), 
('Goa','Goa'),
('Gujarat','Gujarat'),
('Haryana','Haryana'),
('Himachal Pradesh','Himachal Pradesh'),
('Jharkhand','Jharkhand'),
('Karnataka','Karnataka'),
('Kerala','Kerala'),
('Madhya Pradesh','Madhya Pradesh'),
('Maharashtra','Maharashtra'),
('Manipur','Manipur'),
('Meghalaya','Meghalaya'),
('Mizoram','Mizoram'),
('Nagaland','Nagaland'),
('Odisha','Odisha'),
('Punjab','Punjab'),
('Rajasthan','Rajasthan'),
('Sikkim','Sikkim'),
('Tamil Nadu','Tamil Nadu'),
('Telangana','Telangana'),
('Tripura','Tripura'),
('Uttarakhand','Uttarakhand'),
('Uttar Pradesh','Uttar Pradesh'),
('West Bengal','West Bengal'),
('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
('Chandigarh','Chandigarh'),
('Dadra and Nagar Haveli','Dadra and Nagar Haveli'),
('Daman & Diu','Daman & Diu'),
('Delhi','Delhi'),
('Jammu & Kashmir','Jammu & Kashmir'),
('Ladakh','Ladakh'),
('Lakshadweep','Lakshadweep'),
('Puducherry','Puducherry')
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=10, blank=True)
    locality = models.CharField(max_length=200)
    state = models.CharField(choices=STATE_CHOICES, max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=6)
    

    def __str__(self):
        return str(self.id)








CATEGORY_CHOICES = (
('Fine Dining','Fine Dining'),
('Casual Dining','Casual Dining'),
('Contemporary Casual','Contemporary Casual'),
('Family Style','Family Style'),
('Fast Casual','Fast Casual'),
('Fast Food','Fast Food'),
('Cafe','Cafe'),
('Buffet','Buffet'),
('Food Trucks and Concession Stands','Food Trucks and Concession Stands'),
('Pop-Up Restaurant','Pop-Up Restaurant')
)

class Restaurant(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    Restaurant_name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    state = models.CharField(choices=STATE_CHOICES, max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=6)
    Restaurant_category = models.CharField(choices = CATEGORY_CHOICES, max_length=100)
    Restaurant_image = models.ImageField(upload_to = 'restroimg')
    

    def __str__(self):
        return str(self.id)

class Restauranttype(models.Model):
    Restaurant_type = models.CharField(choices = CATEGORY_CHOICES, max_length=100)
    Restauranttype_image = models.ImageField(upload_to = 'restroimg')
    
    def __str__(self):
        return str(self.id)

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    selling_price = models.FloatField()
    disc_price = models.FloatField()
    category = models.CharField(choices = CATEGORY_CHOICES, max_length=100)
    Restro_name = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=6)
    product_image = models.ImageField(upload_to = 'productimg')

    def __str__(self):
        return str(self.id)

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.disc_price

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The way','On The way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,default='Pending') 

    @property
    def total_cost(self):
        return self.quantity * self.product.disc_price

    
