from django.contrib import admin

from .models import Customer, Invoice, Order, OrderDetail, Product


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("uuid", "name", "email", "created_at", "updated_at")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("uuid", "name", "price", "stock", "created_at", "updated_at")


class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 1
    readonly_fields = ("total",)

    def total(self, obj):
        return obj.total

    total.short_description = "Total"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "customer",
        "order_date",
        "status",
        "created_at",
        "updated_at",
    )
    inlines = [OrderDetailInline]


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "order",
        "invoice_date",
        "amount",
        "status",
        "created_at",
        "updated_at",
    )
