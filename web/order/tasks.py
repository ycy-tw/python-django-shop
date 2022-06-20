from celery import shared_task
from django.core.mail import send_mail
from demo.settings import PRODUCTION
from .models import Order


@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'[Demo only]Order nr. {order.id}'
    message = f'Dear {order.name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.' \
              f'(This not a real order, only for demo purpose.)'

    if PRODUCTION:

        from demo.settings import EMAIL_HOST_USER
        sender = EMAIL_HOST_USER

    else:
        sender = 'demo@example.com'

    mail_sent = send_mail(subject,
                          message,
                          sender,
                          [order.email])
    return mail_sent
