#swapping with third variable

a=int(input("enter the value of a  "))
b=int(input('enter the value of b  '))
c=a
a=b
b=c

print('values after swapping')
print('value of a =  ',a)
print('value of b  ', b)






#swaping program without third variable

a=int(input("enter the value of a  "))
b=int(input('enter the value of b  '))
a= a+b
b= a-b
a= a-b

print('values after swapping')
print('value of a =  ',a)
print('value of b  ', b)