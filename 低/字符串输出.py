#ID 10702
st=input()
if len(st)>=20:
    print(st)
else:
    print(st+('='*20-len(st)))