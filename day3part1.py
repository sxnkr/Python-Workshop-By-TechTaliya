#Python modules

#dates

from datetime import datetime,timedelta
#Tp print the current date and time
current  = datetime.now()
print(current)
print(type(current))

print(datetime.strftime(current, "%m-%d-%Y" ))
print(datetime.now().month)
tomorrow=current+timedelta(days=1)
print(f"tomorrow is {tomorrow}")
