
# guess the greater number
a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))

if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")




# nested while loop
a = 1
while a <= 7:
    print("ganesh", end="") # end= bring us on new line
    b = 1
    while b <= 24:
        print("bhadrike", end="")
        b = b+1
    a = a + 1
    print()
# o/p first it will print ganesh one time and bhadrike 24 times
#continue for 7 times









