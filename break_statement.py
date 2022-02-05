'''if we want 5 candy from the machine it will print 5 canndy
and if the machine has only 5 candy availabel then it will tell out of stock'''
av = 5
x = int(input("hoe much candy you want"))
i = 1
while i <= x:
    if i > av:
        print("Out Of Stock")
        break
    print('candy',i)
    i = i + 1