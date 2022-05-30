from django.db import models
from django.forms import CharField

# Create your models here.

#class Products(models.Model):
    # product_name=models.CharField(max_length=200)
    # product_price=models.FloatField()
    # product_quantity=models.PositiveIntegerField()

# class Order(models.Model):
#     product_name=models.CharField(max_length=200)
#     Invoice_ID=models.CharField(max_length=200)
#     product_price=models.FloatField()
#     product_quantity=models.PositiveIntegerField()
#     date_of_insertion=models.DateField(auto_now_add=True)
#     user_name=models.CharField(max_length=200)
#     user_consumer=models.CharField(max_length=200)
#     class Meta:
#         db_table = "orders"

class Candidate(models.Model):
    candidate_ID=models.CharField(max_length=10)
    start_time=models.PositiveIntegerField()
    end_time=models.PositiveIntegerField()
    candidate_name=models.CharField(max_length=40)
    class Meta:
        db_table = "candidate"

class Interviewer(models.Model):
    interviewer_ID=models.CharField(max_length=10)
    start_time=models.PositiveIntegerField()
    end_time=models.PositiveIntegerField()
    interviewer_name=models.CharField(max_length=10)
    class Meta:
        db_table = "interviewer"


























































