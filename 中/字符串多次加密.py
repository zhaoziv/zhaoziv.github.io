#ID 20806
text=input()
new1=''
new2=''
for i in text:
    if i==' ':
        new1=new1+' '
    else:
        new1=new1+str(ord(i)-96).zfill(2)
for j in new1:
    if j==' ':
        new2=new2+'00'
    else:  
        new2=new2+str(int(j)+27)
print(new2)