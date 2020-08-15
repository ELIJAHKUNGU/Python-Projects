result =None
a= float(input('Enter a Number'))
b = float(input("Enter  a number "))
try:
  result = a / b

except Exception as e:
     print("The Error is : ",type(e) )
except TypeError as e :
    print("The Error is : ", type(e))
else:
    print('__else__')
finally:
    print('__finally__')


print('Result : ' , result)
print('End')
