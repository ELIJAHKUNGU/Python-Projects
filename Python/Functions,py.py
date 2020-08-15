def sum(x,y):
    print(x +y)
sum(14,23)


#default value 

def student(name='Unknown name' ,age=0 ,**marks):
    print('Name:' , name)
    print('Age' ,age)
    print('Marks' ,marks) #print in form of tuple
    for key ,value in marks.items():
        print(key ," " ,value)   

student("Start" , 78,english=98,math=90,biology=70,pyhic=68)


