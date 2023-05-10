#ID 21101
a=[3,6,9]
sum=0
mode=0
lst=[]
b=input()
b=b[1:len(b)-1]
b=list(map(int,b.split(',')))
if len(a)>len(b):
    mode=len(a)
else:
    mode=len(b)
for i in range(mode):
    sum+=a[i]*b[i]  
print(sum)