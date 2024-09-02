# calculator mini project
def add(a,b):
    ans=a+b
    print('addition=',ans)
def sub(a,b):
    ans=a-b
    print('sun =',ans)
def mul(a,b):
    ans=a*b
    print('mul is =',ans)
def div(a,b):
    ans=a/b
    print('div =',ans)
def expo(a,b):
    ans=a**b
    print('expo =',ans)
def rem(a,b):
    ans=a%b
    print(ans)
def flo(a,b):
    ans=a//b
    print('floor=',ans)

while True :
    ch = int(input('\n\n Enter a choice :\n 1.ADD \t 2.sub \n 3.mul \t 4.div \n 5.exp \t 6.rem \n 7.flo\t 8.exit\n '))
    if ch == 1:
        print('----> 1.Add')
        fn= int(input('Give first number :'))
        sn= int(input('Give second number :'))
        add(fn,sn)
    elif ch == 2:
        print('----> 2.Sub')
        fn = int(input('Give first number :'))
        sn = int(input('give second number :'))
        sub(fn,sn)
    elif  ch==3 :
        print('----> 3.mul ')
        fn = int(input('Give first number :'))
        sn = int(input('Give second number :'))
        mul(fn,sn)
    elif ch==4 :
        print('----> 4.div')
        fn= int(input('Give first number:'))
        sn = int(input('Give second number :'))
        div(fn,sn)
    elif ch == 5:
        print('----> 5.expo')
        fn = int(input('Give First number :'))
        sn = int(input('Give Second number :'))
        expo(fn,sn)
    elif ch == 6:
        print('----> 6. rem :')
        fn = int(input('Give First number:'))
        sn = int(input('Give Second number:'))
        rem(fn,sn)
    elif ch == 7:
        print('----> 7.flo:')
        fn = int(input('Give First number :'))
        sn = int(input('Give SEcond number :'))
        flo(fn,sn)
    elif ch == 8:
        break

    else :
        print('enter Correct option')




































        
