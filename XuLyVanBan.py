import re
s = ""
while True:
    try:
        tmp = input()
        s += tmp
    except:
        break
# print(s)
st = re.findall('[\w\s,:]+', s)
for i in st:
    tmpS = i.lower().split()
    tmpS[0] = tmpS[0].title()
    print(' '.join(tmpS))