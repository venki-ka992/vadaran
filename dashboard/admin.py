from django.contrib import admin
from .models import PlantVariety, CultureBatch, Equipment, Inventory, Order,Employee

# Unregister the model first if it's already registered
if admin.site.is_registered(Inventory):
    admin.site.unregister(Inventory)

@admin.register(PlantVariety)
class PlantVarietyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  
    search_fields = ('name',) 
    ordering = ('name',)  

@admin.register(CultureBatch)
class CultureBatchAdmin(admin.ModelAdmin):
    list_display = ('batch_id', 'plant_variety', 'start_date', 'expected_harvest_date', 'status')
    search_fields = ('batch_id', 'plant_variety__name')  
    list_filter = ('status', 'plant_variety')  
    ordering = ('-start_date',)  

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'purchase_date', 'status') 
    search_fields = ('name',)  
    list_filter = ('status',)  
    ordering = ('-purchase_date',)  

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'category', 'quantity', 'unit', 'last_updated')
    search_fields = ('item_name', 'category')
    list_filter = ('category', 'unit')
    ordering = ('-last_updated',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer_name', 'plant_type', 'order_date', 'quantity', 'price', 'total_amount', 'advance_paid', 'pending_amount', 'status')
    search_fields = ('order_id', 'customer_name', 'plant_type')
    list_filter = ('status', 'order_date')
    ordering = ('-order_date',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'hire_date', 'contact_number', 'email', 'salary')
    list_filter = ('role', 'hire_date')
    search_fields = ('name', 'contact_number', 'email')



    

admin.site.site_header = "VADARAN BIO PLANTS PVT LTD"
admin.site.site_title = "Lab Admin Panel"
admin.site.index_title = "Welcome to Lab Management Dashboard"
