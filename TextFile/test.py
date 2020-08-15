fh = open("demo.txt" , 'w')
try:
     for i in range(10):
            fh.write('this is line no %d\n' % (i+1))
finally:
     fh.close()


     #same code
with open("demo.txt" , 'w') as fh:
    for i in range(10):
        fh.write('this is line no %d\n' % (i + 1))
