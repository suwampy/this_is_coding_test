s = input()
alpa =[]
num = 0
for x in s:
    if x.isalpha():
        alpa.append(x)
    else:
        num+=int(x)

alpa.sort()

if num !=0 :
    alpa.append(str(num))

print(''.join(alpa))
