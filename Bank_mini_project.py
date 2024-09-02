'''

# Bank prjt mini without minimum bank balance

balance=0

def check_balance():
    print('Your Balance is :',balance)

def deposit_amt(amt):
    global balance
    balance = balance + amt
    print(amt,'RS.Deposited')
    
def withdraw_amt(w_amt):
    global balance
    if w_amt <= balance :
        balance = balance - w_amt
        print(w_amt,'RS. Withdrawn')
    else:
        print('Insufficient Balance')
while True :
    ch= int(input('\n\n Enter choice :\n1.Deposit cash\t2.Withdraw Cash\n3.Check balance\t4.Exit\n'))
    if ch==1:
        print('----> 1.Deposit Cash')
        mamt= int(input("Enter Amount to Deposit :"))
        deposit_amt(mamt)
    elif ch==2:
        print('---->2.Deposit Amount:')
        w_amt=int(input('Withdraw Amount:'))
        withdraw_amt(w_amt)
    elif ch==3:
        print('---->3.Check Balance :')
        check_balance()
    elif ch==4:
        print('---->Exit')
        break
    else:
        print('Enter corrrect choice')
'''    
# Bank prjt mini with minimum bank balance


balance= 10000
  
def check_balance () :
    
    print('Your Balance is :',balance)
    
def deposit_balace(amt):
    global balance
    balance = balance + amt
    print(amt,'Rs.Deposited')
    
def withdraw_Amount(w_amt):
    global balance
    if (balance - w_amt)>= 10000:
        balance = balance - w_amt
        print(w_amt,"RS.Withdrawn:")
    else :
        print('Minimum bank balance reached :')
        
while True :
    
    ch= int(input('\n\n Enter choice :\n1.Deposit cash\t2.Withdraw Cash\n3.Check balance\t4.Exit\n'))
    if ch==1:
        print('----> 1.Deposit Cash')
        mamt= int(input("Enter Amount to Deposit :"))
        deposit_balace(mamt)
    elif ch==2:
        print('---->2.Deposit Amount:')
        wq_amt=int(input('Withdraw Amount:'))
        withdraw_Amount(wq_amt)
    elif ch==3:
        print('---->3.Check Balance :')
        check_balance()
    elif ch==4:
        print('---->Exit')
        break
    else:
        print('Enter corrrect choice')
    
    










    











































        
    
