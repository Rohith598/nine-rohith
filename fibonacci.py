def is_fibonacci(n):
    a,b=0,1
    count=0
    if n<=0:
        print("enter an positive integer")
    elif n==1:
        print("fibonacci sequence:")
        print(a)
    else:
        print("fibonaci sequence:")
        while count<n:
            print(a,end='')
            a,b=b,a+b
            count+=1
n=int(input("enter anumber:"))
is_fibonacci(n)