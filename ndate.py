day=int(input("enter day"))
mon=int(input("enter month"))
year=int(input("enter year"))
nextday=day
nextmon=mon;
invalid=False
def checkmonth(mon,day):
    if(mon==4 or mon== 6 or mon==9 or mon==11)and (day==31) :
        return True;
    else:
        return False;
def isleap(year):
    if(year% 4 ==0 and year %100 ==0) or( year % 400==0):
        return True
    else:
        return false
if(day<1 or day >31):
    invalid = True
    print("day is not correct")
elif(mon<1 or mon >12):
    invalid = True
    print("month is not correct")
elif(checkmonth(day,mon)):
    invalid=True
    print("invalid date")
elif(year <1813 or year >2013):
    invalid=True
    print("year not correct")
elif mon==2 and day>29:
    invalid=True
    print("not valid")

if(invalid== False):
    if(mon==1 or mon==3 or mon == 5 or mon== 8 or mon==10):
        if(day<31):
            nextday =day+1
        else:
            nextday=1
            nextmon=mon+1
    elif(mon == 2 or mon == 4 or mon == 6 or mon==9):
        if(day<30):
            nextday=day+1
        else:
            nextday=1
            nextmon=mon+1
    elif(mon==2):
        if(date<28):
            nextday=day+1
        elif(isleap(year) and day==28):
            nextday=1
            nextmon=3
        elif(day==28 or day==29):
            nextday=1
            nextmon=3
        elif(day>29):
            print("feb cannot have day mpre than 29")
    elif(mon==12):
        if(day<31):
            nextday=day+1
        elif(day==31):
            nextday=1
            nextmon=1
        elif(year==2013):
            
            print("year is out of bound")
        else:
            year=year+1
if(invalid == False):
    print("next date is :"+str(nextday)+"/"+str(nextmon)+"/"+str(year))
