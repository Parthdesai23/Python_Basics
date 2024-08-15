import importfile1 as calc

ch=int(input('enter choice:\n 1.add \t 2.sub \n 3.mul \t 4.div \n 5.flo \t 6.mod \n 7.exp :\n'))

match ch :
    case 1:
        fn=int(input('give first number:'))
        sn=int(input('give second number:'))
        calc.add(fn,sn)
    case 2:
        fn=int(input('give first number'))
        sn=int(input('give second number'))
        calc.sub(fn,sn)
    case 3:
        fn=int(input('give first number:'))
        sn=int(input('give second number:'))
        calc.mul(fn,sn)
    case 4:
        fn=int(input('give first number:'))
        sn=int(input('give second number:'))
        calc.div(fn,sn)
    case 5:
        fn=int(input('give first number:'))
        sn=int(input('give second number:'))
        calc.flo(fn,sn)
    case 6:
        fn=int(input('give first number:'))
        sn=int(input('give first number:'))
        calc.mod(fn,sn)
    case 7:
        fn=int(input('give first number:'))
        sn=int(input('give second number:'))
        calc.exp(fn,sn)
    case _:
        print('give valit input')
