d=int(input("enter the numbre of the days: ")) #d=day
ins=float(input("enter the value of the insurance: "))#ins=insurance
km=float(input("enter the numbre of the kilometres: "))#km=kilometres
a=input("Is this the end of year offer? ")
if a=="no":
    t1=float(input("enter the value of the rate 1: "))
    t2=float(input("enter the value of the rate 2: "))
    t3=float(input("enter the value of the rate 3: "))
    if km<= 100:
        c=t1*km+d*ins
    elif km>1000:
        c=t3*km+d*ins
    else :
        c=t2*km+d*ins
    print("pricing cost is :",c)
elif a=="yes":
    t4=float(input("enter the value of the rate 4: "))
    print("pricing cost is: ", t4*km+d*ins)
    
