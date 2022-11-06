dMuc = {
    "A": 100, "B": 500, "C": 200
}


class KH:
    NUM_KH = 0

    def __init__(self, name, feeInLevel, feeOutLevel, VAT, fee):
        self.fee = fee
        self.VAT = VAT
        self.feeOutLevel = feeOutLevel
        self.feeInLevel = feeInLevel
        KH.NUM_KH += 1
        self.id = "KH" + '{:02d}'.format(KH.NUM_KH)
        self.name = name
    def __str__(self):
        return self.id + " " + self.name + " " + self.feeInLevel + " " + self.feeOutLevel + " " + self.VAT + " " + str(self.fee)

l = list()
n = int(input())
for i in range(n):
    name = ' '.join(input().strip().lower().split()).title()
    muc, st, en = input().split()
    muc, st, en = dMuc[muc], int(st), int(en)
    feeInlevel = min(en - st, muc) * 450
    feeOutLevel = max(0, en - st - muc) * 1000
    VAT = feeOutLevel // 20
    fee = feeInlevel + feeOutLevel + VAT
    l.append(KH(name, str(feeInlevel), str(feeOutLevel), str(VAT), fee))
l = sorted(l, key=lambda x: -x.fee)
for i in l:
    print(i)
