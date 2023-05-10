#ID 10704
text=input()
d=0
x=0
for i in text:
    if i.islower():
        x+=1
    elif i.isupper():
        d+=1
print('{},{}'.format(d,x))