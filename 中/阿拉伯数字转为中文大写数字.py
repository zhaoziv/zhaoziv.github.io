#ID 10701
text='零壹贰叁肆伍陆柒捌玖'
text2=''
s=input()
for i in s:
    if i.isdigit():
        text2=text2+text[int(i)]
    else:
        text2=text2+i
print(str(text2))