num1=input("enter the num1 : ")
num2=input("enter the num2 : ")
op=input('enter the operation: ')

try : 
    if num1.isdigit() and num2.isdigit() and op.isalpha():
        num1 = int(num1)
        num2 = int(num2)
        match op:
            case "add":
                print("ans : ",num1+num2)
            case "sub":
                print("ans : ",num1-num2)
            case 'mul':
                print("ans : ",num1*num2)    
            case 'div':
                print('ans',num1/num2)    
    else:
        raise ValueError("input are not valid ")    
except ValueError as e:
    print(e)                

