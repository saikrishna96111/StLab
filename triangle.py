print("enter three sides of a Triangle in the range (0 to 10)")
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
c=int(input("Enter the value of c "))
if a>10 or b>10 or c>10:
    printf("invalid input values are exceeding the range")
if (a<(b+c))and(b<(a+c))and(c<(a+b)):
    if a==b==c:
        print("Equilateral Triangle")
    elif (a==b)or(b==c)or(a==c):
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a Triangle")
