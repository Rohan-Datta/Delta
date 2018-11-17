from django.db import models
from django.utils import timezone
from datetime import date
from django.db import models
from django import forms

#Item Category Variable Names
LAPTOP = "Laptops"
DESKTOP = "Desktops"
WORKSTATION = "Workstations"
SERVER = "Servers"
PROCESSOR = "Processors"
GPU = "GPU"
ACCESSORIES = "Accessories"

#Accessories Category Variable Names
ADAPTER = "Adapters"
BAG = "Bags"
MOUSE = "Mouse"
KEYBOARD = "Keyboards"
HEADPHONES = "Headphones"

#Item Choices
ITEMS_TYPES = ((ADAPTER, "Laptops"), (DESKTOP, "Desktops"), (WORKSTATION, "Workstations"), (SERVER, "Servers"), (PROCESSOR, "Processors"), (GPU, "GPU"), (ACCESSORIES, "Accessories"))

#Accessory Choices
ACCESSORY_TYPES = ((ADAPTER, "Adapters"), (BAG, "Bags"), (MOUSE, "Mouse"), (KEYBOARD, "Keyboards"), (HEADPHONES, "Headphones"))

# Entry model
class Item(models.Model):
    name = models.CharField(max_length=200)
    item_type = models.CharField(max_length=10, choices=ITEMS_TYPES, null=False)
    
    def __str__(self):
        return '{} - {}'.format(self.name, self.posted_by)

class Laptop(models.Model):
    index = models.IntegerField(primary_key=True)
    company = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    type_name = models.CharField(max_length=200)
    inches = models.FloatField()
    screen_resolution = models.CharField(max_length=200)
    cpu = models.CharField(max_length=200)
    ram = models.CharField(max_length=200)
    Memory = models.CharField(max_length=200)
    gpu = models.CharField(max_length=200)
    operating_system = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    price_euros = models.FloatField()
    photo_url = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.company, self.product, self.type_name)

    
# Desktops - Show Laptops Only

# Workstations - Show Laptops Only

class Server(models.Model):    
    index = models.IntegerField(primary_key=True)
    company = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=1000)

class GPU(models.Model):
    index = models.IntegerField(primary_key=True)
    company = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=1000)

class Accessory(models.Model):
    index = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    accessory_type = models.CharField(max_length=10, choices=ACCESSORY_TYPES, null=False)
    company = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=1000)

