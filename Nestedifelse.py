'''
#Leap Year or Not
#for century Years leap year is after every 400 years e.g 2000 is leap but 1900 not a leap



year= int(input('Give a Year to check:\n'))

if year%4==0:
    if year%100==0 :
        if year%400 ==0 :
            print('leap year')
        else :
            print('Not a leap Year')
    else:
        print('Leap year')
else :
    print('Not a Leap year')

'''

# electricity bill NOT the noermal one
a= int(input('Give NO of Units: \n'))

if a>=100 :
    if a>=100 and a<=200:
        b= a - 100 
        print(b*5)
    elif a>=200 and a<=300:
        c= a-200 
        print((c*10)+500)
    elif a>=300 and a<=500 :
        d= a-300
        print((d*20)+1500)
            
    else :
        e= a - 500 
        print((e*30)+5500)
else:
    print(0)
