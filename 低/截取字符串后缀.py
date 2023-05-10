#ID 10806
text=input()
if 'er'in text:
    print(text[0:len(text)-2])
elif 'ly'in text:
    print(text[0:len(text)-2])
elif 'ing'in text:
    print(text[0:len(text)-3])
else:
    print(text)