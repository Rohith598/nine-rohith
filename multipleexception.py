try:
    x=int(input("enter a number:"))
    y=int(input("enter a number:"))
    print("result:",x/y)
except ZeroDivisionError:
    print("division is not occured by zero")
except ValueError:
    print("invalid error")
except Exception as e:
    print("caught error:",e)
else:
    print("no error")
finally:
    print("execution completed")
