#ID 10802
lst=(list(map(int,input().split(','))))
sum=0
for i in range(1,len(lst),2):
    sum+=lst[i]
print(sum)