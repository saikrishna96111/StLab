flag=0
locks=int(input("entre locks"))
if(locks<1 or locks >70):
    flag=1
bar=int(input("enter barrels"))
if(bar<1 or bar >80):
    flag=1
stock=int(input("enter stock"))
if(stock<1 or stock >80):
    flag=1

if(flag==1):
    print("invlaid inpits ")
    exit (0)

tsals=locks*40 + bar*35 + stock*25

if(tsals<=1000):
    commission=0.1*tsals
elif(tsals>1000 and tsals <=1800):
    commission=0.1*1000
    commission=commission + (0.15 * (tsals - 1000))
elif(tsals>1800):
    commission=0.1*1000
    commission=commission+0.15*800
    commission=commission+0.20*(tsals-1800)

print("total sales is ",tsals)
print("total commission is ",commission)
