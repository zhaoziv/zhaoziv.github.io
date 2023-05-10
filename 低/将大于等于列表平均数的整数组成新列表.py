#ID 10811
lst=eval(input())
num=sum(lst)/len(lst)
lst2=[]
for i in lst:
    if i>=num:
        lst2.append(i)
print(lst2)  