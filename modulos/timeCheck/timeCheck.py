import time

hours = time.strftime('%H') 
minutes = time.strftime('%M') 

def hoursLeft():
    return 18- int(hours)

def minutesLeft():
    return 59-int(minutes)

def checkTime():
    if int(hours) >= 19:
        print ("Es hora de irse a casa") 
    else:
        print ("Quedan", hoursLeft(), "horas y", minutesLeft(), "minutos para irnos a casa")
        
checkTime()