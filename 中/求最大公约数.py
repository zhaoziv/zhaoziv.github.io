#ID 20802
lst=list(map(int,input().split(',')))
a=min(lst)
b=max(lst)
for i in range(a,0,-1):
    if a%i==0 and b%i==0:
        print(i)
        break