import math
from fractions import Fraction

def pitchDiff(n, q):
    log2_q = math.log2(q)
    frac_part = log2_q % 1
    rounded = round(n * frac_part)
    result = frac_part - (rounded / n)
    return (rounded, result)

tempnum = int(input("input EDO >> "))
target = list(range(3, 19))
targetSpecial = ['5/3', '7/3', '11/3', '11/5', '13/3', '13/5', '13/9', '17/3', '17/5', '17/9']

print("------------"+str(tempnum)+"EDO--------")
for trg in target:
    df = pitchDiff(tempnum, trg)
    print(str(df[0]) + " / " + str(trg) + " / " + str(df[1]))

for trg in targetSpecial:
    df = pitchDiff(tempnum, Fraction(trg))
    print(str(df[0]) + " / " + trg + " / " + str(df[1]))