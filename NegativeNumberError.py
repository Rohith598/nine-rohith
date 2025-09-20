class NegativeNumberError(Exception):
    pass
def check_num(num):
    if num<0:
        raise NegativeNumberError("Negative numbers are not allowed")
    else:
        print("valid number",num)
try:
    n=int(input("enter a number:"))
    check_num(n)
except NegativeNumberError as e:
    print("error:",e)