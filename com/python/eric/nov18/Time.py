from time import *
from datetime import *

localtime = localtime()
asctime = asctime(localtime)
print(asctime)
print(time)
s = strftime("%Y%m%d-%H:%M:%S", localtime)
print("This is %s" % s)
print(ctime())  # Ctime == asctime

# clock sleep clock
print(clock())
sleep(1)
print(clock())

datetime_time = datetime.now()
# 两天前
days_ = datetime_time - timedelta(days=2)
print(days_)
print(datetime_time)
print(datetime_time.strftime("%Y%m%d-%H:%M:%S"))
print(datetime_time.strftime("%A"))
print(strptime("20171120-21:23:19", "%Y%m%d-%H:%M:%S"))
print(mktime(strptime("20171120-21:23:19", "%Y%m%d-%H:%M:%S")))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[::2])
print(a[:-2])
print(a[-2:])