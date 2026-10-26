import datetime
from django import template

#Constants
LOW_STOCK_THRESHOLD = 10

register = template.Library()

@register.filter
def expiry_status(expiry_date):
    if expiry_date is None:
        return 'No expiry date'

    today = datetime.date.today()
    if expiry_date > datetime.date.today():
        status = f'Expires in {(expiry_date - today).days} days'
    elif expiry_date == datetime.date.today():
        status = 'Expires today'
    else:
        status = 'Expired'
    return status


@register.filter
def stock_level(product_qty):
    if product_qty is None:
        return 'No stock level'

    if product_qty == 0:
        status = 'Out of stock'
    elif product_qty < LOW_STOCK_THRESHOLD:
        status = 'Low stock'
    else:
        status = 'In stock'

    return status
