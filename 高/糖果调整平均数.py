#ID 33013
lst=list(map(int,input().split(',')))
n=lst.pop(0)
r=lst.pop()
l=lst.pop()
lst.sort()
candy=lst
s=0
if sum(candy)<l*sum(candy) and sum(candy)>r*sum(candy):
    print(-1)
else:
    for i in range(len(candy)):
        if l<=candy[i] and candy[i]<=r and l<=candy[-1] and candy[-1]<=r:
            break
        else:
            s+=1
            candy[-1]-=1
            candy[i]+=1
    print(s)