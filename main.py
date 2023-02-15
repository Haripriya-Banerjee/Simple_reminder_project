import time
from plyer import notification

# creating a function for notification which takes time_out as variable 
def notify_func(time_out):  
    notification.notify(
        title = "**Please Drink Water now !",
        message ="Water is your body's principal chemical component and makes up about "\
            "50% to 70% of your body weight. Your body depends on water to survive.",
        app_icon="E:\PYTHON_PROJECT\inoc.ico.ico",
        timeout=time_out
    )
   

if __name__ == "__main__":
    while True:
        # calling notify_func 
        notify_func(10)
        time.sleep(60*60)
        
    


