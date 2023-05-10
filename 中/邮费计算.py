#ID 10708
lst=input().split()
n=int(lst[0])
yuan=8
if lst[1]=='y':
    yuan+=5
if n>1000:
    n=n-1000
    yuan+=(n//500)*4
    if n%500!=0:
        yuan+=4
print(yuan)