#pattern matching
'''
match 2:
    case 1:
        print('case1 executed')
    case 2:
        print('case2 executed')
    case 3:
        print('case3 executed')


#ex2

ch=int(input('give any number from 1 to7:'))

match ch:
    case 1:
        print('its monday')
    case 2:
        print('its tuesday')
    case 3:
        print('its wednesday')
    case 4:
        print('its thursday')
    case 5:
        print('its friday')
    case 6:
        print('its saturday')
    case 7:
        print('its sunday')
    case _:
        print('enter correct value')

'''
# ex3


def add(a,s):
    print(a+s)
def sub(a,s):
    print(a-s)
def mul(a,s):
    print(a*s)
def div(a,s):
    print(a/s)
def floor(a,s):
    print(a//s)
def mod(a,s):
    print(a%s)
def exp(a,s):
    print(a**s)


ch= int(input('chose the operation \n 1.add \t 2.sub \n 3.mul \t 4.div \n 5.flo\t6.mod \n 7.exp'))

match ch:
    case 1:
        fn=int(input('give first number:'))
        sn=int(input('give second number:'))
        print('addition is=',fn+sn)
    case 2:
        fn=int(input('give first number:'))
        sn=int(input('give second number:'))
        print('substraction is=',fn-sn)
    case 3:
        fn=int(input('give first number:'))
        sn=int(input('give second number:'))
        print('multiplication is=',fn*sn)
    case 4:
        fn=int(input('give first number:'))
        sn=int(input('give second number:'))
        print('division is=',fn/sn)
    case 5:
        fn=int(input('give first number:'))
        sn=int(input('give second number:'))
        print('floor is=',fn//sn)
    case 6:
        fn=int(input('give first number:'))
        sn=int(input('give second number:'))
        print('mod is=',fn%sn)
    case 7:
        fn=int(input('give first number:'))
        sn=int(input('give second number:'))
        print('expo is=',fn**sn)

    
































