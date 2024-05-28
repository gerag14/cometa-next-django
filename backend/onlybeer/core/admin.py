from django.contrib import admin

from .models import Customer, Invoice, Order, OrderDetail, Product


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("uuid", "name", "email", "created_on", "updated_at")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("uuid", "name", "price", "stock", "created_on", "updated_at")


class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 1
    readonly_fields = ("total", "price")

    def total(self, obj):
        return obj.total

    total.short_description = "Total"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "customer",
        "status",
        "created_on",
        "updated_at",
    )
    readonly_fields = ("total",)

    inlines = [OrderDetailInline]

    def total(self, obj):
        return obj.total

    total.short_description = "Total"


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "order",
        "invoice_date",
        "amount",
        "status",
        "created_on",
        "updated_at",
    )
