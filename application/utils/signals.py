import time

from django.core.signals import request_finished
from django.dispatch import receiver, Signal

some_signal = Signal()


@receiver(some_signal)
def some_signal_callback(sender, **kwargs):
    time.sleep(3)
    print("some_signal_callback finished!")



@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")
