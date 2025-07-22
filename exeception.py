a=input("enter the number")

try :
    if not a.isdigit:
        raise ValueError("input is not valid")
    else:
        print("it is num")
        

except ValueError as e :
    print(e)
    