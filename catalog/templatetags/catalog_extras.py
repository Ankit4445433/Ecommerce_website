from django import template

register = template.Library()

@register.filter
def getProductTotal(obj):
    amount = (obj.product.price)*(obj.quantity)
    return amount

@register.filter
def getPayable(items):
    total=0
    for item in items :
        total= total+((item.product.price)*(item.quantity))
    return total

payment = {'0':'cash on delivery','1':'e-sewa'}
delivery = {'0':'Not Delivered'}

@register.filter
def get_payment_method(index):
    return payment[index]

@register.filter
def get_delivery_status(index):
    return delivery[index]