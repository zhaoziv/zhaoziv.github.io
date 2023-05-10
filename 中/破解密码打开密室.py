#ID 20801
n=int(input())
count=0
sum=0
for i in range(1,n):
    if i%7==0:
        count+=1
        sum+=i
print(str(count)+str(sum))