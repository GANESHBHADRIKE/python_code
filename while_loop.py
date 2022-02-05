''' in the given string
if we dont want the character a and t  '''
i = 0
str1 = 'javatpoint'

while i < len(str1):
    if str1[i] == 'a' or str1[i] == 't':
        i += 1

    print('Current Letter :', str1[i])
    i+=1

