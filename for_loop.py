'''
#5
for i in range(100,9,-10):
    print(i)

#1
for i in range(0,101,1):
    print(i)

#2
for i in range(1,11,1):
    print(i*5)
for i in range(5,51,5):
    print(i)

#3
for i in range(2,101,2):
    print(i)


#4
for i in range(1,100,2):
    print(i)
#6
for i in range (1,11,1):
    print('hello world')

# taking range from user

n= int(input('give a range :'))
for i in range(1,n,1):
    print(i)

#n to 1    
n1=int(input('give a range for nto1:'))
for i in range(n1,0,-1):
    print(i)

#even number in  range 1to n i/p from out
n= int(input('Give a Number for Even Range :\n'))

for i in range(1,n+1,1):
    if i%2==0 :
        print(i)

#odd number in 1 to n i/p from out
odd= int(input('Give number for odd:'))
for i in range(1,odd+1,1):
        if i%2==1:
            print(i)
            
#addition of even number in  range 1to n
n= int(input('Give a Number For Range:'))
s=0
for i in range(1,n+1,1):
        if i%2==0:
            s=s+i
print(s)

'''
#product of odd number in  range 1to n
n= int(input('Give A Number To Find Product:'))
s=1
for i in range(1,n+1,1):
    if i%2==1:
        s=s*i
print(s)

    



































