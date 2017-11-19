from time import *
from datetime import *

localtime = localtime()
asctime = asctime(localtime)
print(asctime)
s = strftime("%Y%m%d-%H:%M:%S", localtime)
print("This is %s" % s)
print(ctime())   #Ctime == asctime

# clock sleep clock
print(clock())
sleep(5)
print(clock())

datetime_time = datetime.now()
print(datetime_time)
print(datetime_time.strftime("%Y%m%d-%H:%M:%S"))
