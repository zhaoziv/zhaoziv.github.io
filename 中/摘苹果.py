#ID 20901
h=int(input())
lst=list(map(int,input().split(',')))
count=0
for i in lst:
    if h+80>=i:
        count+=1
print(count)