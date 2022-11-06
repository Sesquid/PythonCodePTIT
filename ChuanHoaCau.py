import re

while True:
    try:
        tmp = input().lower().strip()
        x = tmp[-1]
        if x != '.' and x != '!' and x != '?':
            x = '.'
        l = re.findall("[\w,:]+", tmp)
        res = ""
        for i in l:
            res += i + " "
        res = res.strip() + x
        res = res[0].title() + res[1:]
        print(res)
    except:
        break