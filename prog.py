text = open('INPUT.TXT').read()
result = 'YES'
letters=['A','B','C','D','E','F','G','H']
 
def check_size():
    if len(text) == 5:
        return True
    else:
        return False
 
def check_defis():
    if str(text[2]) == '-':
        return True
    else:
        return False
 
def check_alphabet (a):
    s = False
    for i in letters:
        if a == i:
            s += True
        else:
            s += False
    if s == True:
        return True
    else:
        return False
       
def check_numbers(n):
    if n >= 1 and n <= 8:
        return True
    else:
        return False
 
def diapazon_numbers(a, b):
    r = abs(a - b)
    if r >= 1 and r <= 2:
        return True
    else:
        return False
   
def numbers_1(a, b):
    if abs(a - b) == 1:
        return True
    else:
        return False
 
size = check_size()
defis = check_defis()
if size == True:
    letter1 = check_alphabet(text[0])
    letter2 = check_alphabet(text[3])
    n1 = check_numbers(int(text[1]))
    n2 = check_numbers(int(text[4]))
else:
    result = 'ERROR'
 
if letter1 == letter2 == defis == size == n1 == n2 == True:
    check = True
else:
    check = False
if check == True:
    dl = diapazon_numbers(int(letters.index(text[0])), int(letters.index(text[3])))
    dn = diapazon_numbers(int(text[1]), int(text[4]))
    if dl == dn == True:
        dl1 = numbers_1(int(letters.index(text[0])), int(letters.index(text[3])))
        dn1 = numbers_1(int(text[1]), int(text[4]))
        if dn1 != dl1:
            result = 'YES'
        else:
            result = 'NO'
    else:
        result = 'NO'
else:
    result = 'ERROR'
   
file = open('OUTPUT.TXT', 'w')
file.write(str(result))
file.close()