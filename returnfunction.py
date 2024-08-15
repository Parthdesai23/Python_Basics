#1
'''
def luckynumber():
    print('lucky number fun starts')
    print('lucky number fun ends')
    return None
luckynumber()

#2
def luckynumber():
    print('lucky number fun starts')
    print('lucky number fun ends')
    #return None
ln=luckynumber()
print('ln=',ln)


#3
def luckyNumber():
    print('lucky Number fun starts')
    print('lucky number fun ends')
    return 25

#i
ln=luckyNumber()
print('ln=',ln)

#ii

print(luckyNumber())
#iii
luckyNumber()



#4
def calculate_bill(p,o):
    tot_bill = p+o
    return tot_bill

def disconted_bill(tot_bill):
    dis_bill= tot_bill /2
    return dis_bill
disc_bill= disconted_bill(calculate_bill(70,30))
print('disc_bill=',disc_bill)
'''

#addition of nubers using return statements

def addition(o,p):
    add = o+p
    return add
a=int(input("give no1:"))
b=int(input("give no2:"))
print(addition(a,b))
    










































