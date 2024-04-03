class atm:
    def __init__(s):
        s.b=0
        s.m=[]
        s.c={500:16,200:50,100:50}
    def cash(s,a):
        if a%100!=0:
            return 0,0,0
        k=0.9
        if a<10000:
            k=.5
        if s.c[500]<9:
            k=.7
        amount=int(a*k)
        amountr=a-amount
        n5=amount//500
        if n5>s.c[500]:
            n5=s.c[500]
        amount-=n5*500
        total_amount=amountr+amount
        n2=total_amount//200
        if n2>s.c[200]:
            n2=s.c[200]
        total_amount-=n2*200
        n1=total_amount//100
        if n1>s.c[100]:
            n1=s.c[100]
        return n5,n2,n1
    def cashout(s,a):
        n5=a//500
        if s.c[500]<n5:
            n5=s.c[500]
        a-=n5*500
        n2=a//200
        if s.c[200]<n2:
            n2=s.c[200]
        a-=n2*200
        n1=a//100
        if s.c[100]<n1:
            n1=s.c[100]
        return n5,n2,n1
    def deposit(s):
        a=int(input("Enter the amount: "))
        n5=int(input("Enter no.of 500 notes: "))
        n2=int(input("Enter no.of 200 notes: "))
        n1=int(input("Enter no.of 100 notes: "))
        t=(n5*500)+(n2*200)+(n1*100)
        if a==t:
            s.m.append(f"deposit:{a}")
            s.b+=a
            s.c[500]+=n5
            s.c[200]+=n2
            s.c[100]+=n1
            print("Deposit successful")
        else:
            print("amount and cash doesn't match")
    def withdraw(s):
        a=int(input("Enter the amount: "))
        if a<=s.b:
            if a>9999:
                if len(input("Enter OTP:"))!=4:
                   print("Invalid OTP")
                   return
            c5,c2,c1=s.cash(a)
            t=(c5*500)+(c2*200)+(c1*100)
            if t==a:
                s.c[500]-=c5
                s.c[200]-=c2
                s.c[100]-=c1
                print(f"500 notes count:{c5}\n200 notes count:{c2}\n100 notes count:{c1}")
                s.b-=a
                s.m.append(f"withdraw:{a}")
                print("Withdraw successful")
            else:
                c5,c2,c1=s.cashout(a)
                t=(c5*500)+(c2*200)+(c1*100)
                if t==a:
                    s.c[500]-=c5
                    s.c[200]-=c2
                    s.c[100]-=c1
                    print(f"500 notes count:{c5}\n200 notes count:{c2}\n100 notes count:{c1}")
                    s.b-=a
                    s.m.append(f"withdraw:{a}")
                    print("Withdraw successful")
                    return
                print("cash not avil")
        else:
            print("unsufficient amount")
    def mini(s):
        for i in s.m[-5:]:
            print(i)
        print(f"Balence:{a.b}")
a=atm()
while True:
    print("1.deposit\n2.withdrw\n3.ministatement\n4.exit")
    c=input("Enter your choice: ")
    if c=="1":
        a.deposit()
    elif c=="2":
        a.withdraw()
    elif c=="3":
        a.mini()
    elif c=="4":
        break
    else:
        print("Invalid Input")
            
        
