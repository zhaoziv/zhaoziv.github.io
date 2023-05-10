#ID 10803
text=input()
num=0
char=0
for i in text:
    if i.isdigit():     #.isdigit()是否为数字
        num+=1
    elif i.isalpha():     #.isalpha()是否为字母
        char+=1
print('{},{}'.format(num,char))