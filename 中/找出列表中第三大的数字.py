#ID 21102
lst=list(map(int,input().split(',')))
lst.sort()
lst=set(lst)
lst=list(lst)
lst.remove(min(lst))
lst.remove(min(lst))
print(lst[0])