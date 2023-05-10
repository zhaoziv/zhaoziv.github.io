#ID 107001
n=input().split(',')
lst=[]
lst.append(int(min(n)))
n.remove(min(n))
lst.append(int(min(n)))
n.remove(min(n))
if lst[0]+lst[1]>=int(n[0]):
    if lst[0]*lst[0]+lst[1]*lst[1]==int(n[0])*int(n[0]):
        print('这是一个直角三角形')
    elif lst[0]==lst[1]==int(n[0]):
        print('这是一个等边三角形')
    elif lst[0]==lst[1] or lst[0]==int(n[0]) or lst[1]==int(n[0]):
        print('这是一个等腰三角形')
    else:
        print('这是一个普通三角形')
else:
    print('这三个数字不能组成三角形')