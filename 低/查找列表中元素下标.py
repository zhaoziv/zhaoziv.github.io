#ID 10810
lst1=eval(input())
itme=lst1[-1]
text=lst1[0]
x=False
for i in range(len(text)):
    if itme==text[i]:
        x=True
        print(i)
        break
if x==False:   
    print('不存在')  