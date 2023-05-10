#ID 33012
text=input()
a=0
b=0
c=0
lst=[]
for i in text:
    if 'A'==i:
        a+=1
    elif 'B'==i:
        b+=1
    elif 'C'==i:
        c+=1
lst.extend([a,b,c])
lst.sort()
print(lst[0])
'''
text=input()
lst=[]
lst.append(text.count('A',0,len(text)+1))
lst.append(text.count('B',0,len(text)+1))
lst.append(text.count('C',0,len(text)+1))
print(min(lst))
'''