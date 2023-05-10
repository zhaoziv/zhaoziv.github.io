#ID 22010
num = input()
def sum(index):
    if index >= 0:
        return int(num[index]) + sum(index-1)
    else:
        return 0
print(sum(len(num)-1))
'''
return 返回后面的值
return int(num[index]) + sum(index-1)
sum(index-1)这里又调用了函数
除非index等于-1然后返回0(之后不会再调用函数)
例如:输入 123
sum(len(num)-1)
    index=2
然后if index >= 0:
    返回num的索引为2的字符(也就是3,int是因为字符不能数字运算,所以强制类型转换),再次调用函数(函数调用值为index-1,然后一直调用到index=-1,返回0)
        3+      第一次sum(3-1)
        3+2       第二次 sum(2-1)
        3+2+1       第三次 sum(1-1)
        3+2+1+0       第四次 sum(0-1) 
        3+2+1+0+0       第五次 因为-1<0,所以返回0
最后打印(3+2+1+0+0)
'''