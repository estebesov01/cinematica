from django.contrib import admin
from .models import Order, Ticket
# Register your models here.
admin.site.register(Order)
admin.site.register(Ticket)

# def create(self, request, *args, **kwargs):
#     order = OrderListSerializer(data=request.data)
#     if order.is_valid():
#         if CartItem.objects.filter(user=self.request.user).count() == 0:
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         order.save(user=self.request.user)
#         for item in CartItem.objects.filter(user=self.request.user):
#             OrderItem.objects.create(order_id=order.instance.id,
#                                      user_id=item.user_id,
#                                      quantity=item.quantity,
#                                      product_id=item.product_id
#                                      )
#         CartItem.objects.filter(user=request.user).delete()
#         return Response(status=status.HTTP_201_CREATED)
#     return Response(order.errors, status=status.HTTP_400_BAD_REQUEST)