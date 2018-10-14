#1
def mul(x,y):
    return x*y

from functools import partial
mul_sum=partial(mul,2)
print(mul_sum(3))


#2
def add(x,y,z):
    return x+y+z
add_sum=partial(partial(add,1),2)
print(add_sum(3))


#3
import time
time_start=time.time()
while i<1000000:
    i=0
    i+=1
time_end=time.time()
print(time_end-time_start)
print('s')
