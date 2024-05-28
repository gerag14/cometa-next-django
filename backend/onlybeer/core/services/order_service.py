from onlybeer.core.models import Order, OrderDetail


class OrderService:
    def __init__(self, order=None):
        self.order = order

    def create_order(self, validated_data):
        items_data = validated_data.pop("items", [])
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderDetail.objects.create(order=order, **item_data)
        return order

    def update_order(self, validated_data):
        items_data = validated_data.pop("items", [])
        instance = self.order
        instance.customer = validated_data.get("customer", instance.customer)
        instance.status = validated_data.get("status", instance.status)
        instance.save()

        for item_data in items_data:
            item_id = item_data.get("id")
            if item_id:
                item = OrderDetail.objects.get(id=item_id, order=instance)
                item.quantity = item_data.get("quantity", item.quantity)
                item.price = item_data.get("price", item.price)
                item.save()
            else:
                OrderDetail.objects.create(order=instance, **item_data)

        return instance
