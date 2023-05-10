#ID 20803
lst=list(map(int,input().split(',')))
a=min(lst)
b=max(lst)
for i in range(b,(a*b)+1):
    if i%a==0 and i%b==0:
        print(i)
        break