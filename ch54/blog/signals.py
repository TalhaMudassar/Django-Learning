from django.dispatch import Signal,receiver

#creating signals.
notification = Signal()


#Rec Function
@receiver(notification)
def show_notification(sender,**kwargs):
    # here we write our logic 
    print("--------------------")
    print(sender)
    print(f"{kwargs}")