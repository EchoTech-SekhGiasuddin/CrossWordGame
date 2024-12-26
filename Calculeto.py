while True:
    fst = input('Enter Your First Number (or q for Quit) : ')

    if fst.lower()=='q':
        break

    sec = input('Please Enter Your Secend Number : ')
    opp = input('Enter Your Oppretor Like (+ , - , * , / ) : ')

    match opp:
        case '+':
            fst=int(fst)
            sec=int(sec)
            tot=(fst+sec)
            print('---------------------------------------------')
            print(f"Your Result is = {tot}")
            print('---------------------------------------------')
        case '-':
            fst=int(fst)
            sec=int(sec)
            tot=(fst-sec)
            print('---------------------------------------------')
            print(f"Your Result is = {tot}")
            print('---------------------------------------------')
        case '*':
            fst=int(fst)
            sec=int(sec)
            tot=(fst*sec)
            print('---------------------------------------------')
            print(f"Your Result is = {tot}")
            print('---------------------------------------------')
        case '/':
            fst=int(fst)
            sec=int(sec)
            tot=(fst/sec)
            print('---------------------------------------------')
            print(f"Your Result is = {tot}")
            print('---------------------------------------------')
        case other:
            print('Invalid Opretor !')

