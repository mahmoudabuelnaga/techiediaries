from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    sku         = models.CharField(max_length=13, help_text='enter product stock keeping unit')
    barcode     = models.CharField(max_length=13, help_text='enter product barcode (ISBN, UPC.....)')
    title       = models.CharField(max_length=200, help_text='Enter Product Title')
    description = models.TextField(help_text='Enter Product Description')
    unitCost    = models.FloatField(help_text='Enter Product Unit Cost')
    unit        = models.CharField(max_length=10, help_text='Enter Product Unit')
    quentity    = models.FloatField(help_text='Enter Product Quentity')
    minQuentity = models.FloatField(help_text='Enter Product Min Quentity')
    family      = models.ForeignKey('Family', on_delete=models.CASCADE)
    location    = models.ForeignKey('Location', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('product-detail-view', args[str(self.id)])
    
    def __str__(self):
        return self.title

class Family(models.Model):
    reference   = models.CharField(max_length=13, help_text='Enter Family Reference')
    title       = models.CharField(max_length=200, help_text='Enter Family Title')
    description = models.TextField(help_text='Enter Family Description')
    unit        = models.CharField(max_length=13, help_text='Enter Family Unit')
    minQuentity = models.FloatField(help_text='Enter Family Min Quentity')

    def get_absolute_url(self):
        return reverse('family-detail-view', args[str(self.id)])

    def __str__(self):
        return self.title



class Location(models.Model):
    reference = models.CharField(max_length=20, help_text="Enter Location Reference")
    title = models.CharField(max_length=200, help_text='Enter Location Title')
    description = models.TextField(help_text='Enter Location Description')

    def get_absolute_url(slef):
        return reverse('location-detail-view', args[str(self.id)])
    
    def __str__(self):
        return self.title

class Transaction(models.Model):
    sku = models.CharField(max_length=13, help_text="Enter Product Stock Keeping Unit")
    barcode = models.CharField(max_length=13, help_text="Enter Product Barcode (ISBN, UPC....)")
    comment = models.TextField(help_text="Enter Product Comment")
    unitCost = models.FloatField(help_text="Enter Product Unit Cost")
    quentity = models.FloatField(help_text="Enter Product Quentity")
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    date     = models.DateField(blank=True, null=True)
    REASONS = (
        ('ns', 'New Stock'),
        ('ur', 'Usable Return'),
        ('nr', 'Unusable Return'),
    )
    reasons = models.CharField(max_length=2, default='ns', choices=REASONS, help_text='Reasons for transation')

    def get_absolute_url(self):
        return reverse('transaction-detail-view', args[str(self.id)])
    
    def __str__(self):
        return self.id