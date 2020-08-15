result =None
a= float(input('Enter a Number'))
b = float(input("Enter  a number "))
try:
  result = a / b

except Exception as e:
     print("The Error is : ",type(e) )


print('Result : ' , result)
print('End')
