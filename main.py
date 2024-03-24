print("This is an amazing calculator to perfrom between two numbers")
print("'+' for addition\n"
      "'-' for subtraction\n"
     "'*' for multiplication\n"
     "'/' for division\n"
     "'%' for reminder\n")
n1 = complex(input("Enter 1st number : "))
n2 = complex(input("Enter 2nd number : "))
opr = str(input("Enter the operator : "))
if  opr == "+":
    print("Result :",n1+n2)
elif opr == '-':
    print("Result :",n1-n2)
elif opr == '*':
    print("Result :",n1*n2)
elif opr == '/':
    if n2 != 0 :
     print("Result :",n1/n2)
    else :
     print("Result : value can not be determined")
elif opr == '%':
  print ("Result :", n1%n2)
  if isinstance(result,int):
     result = int(result)
    print("Result :" , result)
  elif isinstance(result,float):
    print("Result :",{".2f"}.format(result))
  
  print("This calculator is not yet trained to calculate it")
  
