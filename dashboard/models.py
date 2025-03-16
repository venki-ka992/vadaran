from django.db import models

class PlantVariety(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class CultureBatch(models.Model):
    batch_id = models.CharField(max_length=50, unique=True)
    plant_variety = models.ForeignKey(PlantVariety, on_delete=models.CASCADE)
    start_date = models.DateField()
    expected_harvest_date = models.DateField()
    No_of_bottles = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    
    STATUS_CHOICES = [
        ('Incubation', 'Incubation'),
        ('Growth', 'Growth'),
        ('Ready', 'Ready'),
        ('Harvested', 'Harvested'),
    ]
    
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Incubation')

    def __str__(self):
        return f"{self.batch_id} - {self.plant_variety.name}"

from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    purchase_date = models.DateField()
    
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('In Use', 'In Use'),
        ('Under Maintenance', 'Under Maintenance'),
        ('Decommissioned', 'Decommissioned'),
    ]
    
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Available')

    def __str__(self):
        return self.name

class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="General") 
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=100, default="kgs")
    last_updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f"{self.item_name} ({self.quantity} {self.unit})"

from django.db import models

from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=100)
    order_date = models.DateField()
    plant_type = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    advance_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    pending_amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def save(self, *args, **kwargs):
        
        self.total_amount = self.quantity * self.price
        self.pending_amount = self.total_amount - self.advance_paid

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_id} - {self.customer_name}"

class Employee(models.Model):
    EMPLOYEE_ROLES = [
        ('Manager', 'Manager'),
        ('Technician', 'Technician'),
        ('Laborer', 'Laborer'),
        ('Supervisor', 'Supervisor'),
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=EMPLOYEE_ROLES)
    hire_date = models.DateField()
    contact_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.role}"


