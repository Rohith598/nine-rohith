try:
    numerator=int(input("enter a number:"))
    denominator=int(input("enter a number:"))
    result=numerator/denominator
    print("result is:",result)
except ZeroDivisionError:
    print("division by zero is not allowed")
finally:
    print("execution completed")