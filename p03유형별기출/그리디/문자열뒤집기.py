s = input()
a = 0
b = 0

if s[0] == '1':
    a += 1
else:
    b += 1

for i in range(len(s)-1):
    if s[i+1] != s[i]:
        if s[i+1] == '1':
            a+=1
        else:
            b+=1

print(min(a,b))