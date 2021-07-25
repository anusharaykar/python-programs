import time
def fibdeco(func):
    def wrapper():
        starttime=time.perf_counter()
        value=func()
        endtime=time.perf_counter()
        runtime=endtime-starttime
        return value,starttime,endtime,runtime
    return wrapper
@fibdeco
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b


f,starttime,endtime,runtime=fib()
n=int(input("Enter the number to generate fibonacci series"))
for i in range(0,n):
    print(next(f))
print("Start time:",starttime)
print("Endtime",endtime)
print("run time",runtime)
