import math
from fractions import Fraction

def PEC(n, q):
    """
    PEC: Percentage Error Calculation(대충만듬)
    """

    log2_q = math.log2(q)
    frac_part = log2_q % 1
    rounded = round(n * frac_part)
    result = abs((rounded / n) - frac_part)
    return result

results = open("./results.txt", "w")
allResults = open("./allResults.txt", "w")
target = list(range(3, 19))
targetSpecial = ['5/3', '7/3', '11/3', '11/5', '13/3', '13/5', '13/9', '17/3', '17/5', '17/9']
targetTemp = [12, 41, 53, 306, 665, 28, 59, 146, 643, 4004, 8651, 12655, 26, 109, 571, 2393, 2964, 88349, 11, 13, 24, 37, 949, 986, 1935, 10, 227, 5231, 5458, 54353, 23, 80, 263, 343, 4036, 32631, 36667]
minavgTemp = []
minavg = 123412341234

for tmp in targetTemp:
    sum = 0
    for trg in target:
        errr = PEC(tmp, trg)*1000
        sum += errr
        print(str(tmp) + " temperament / " + str(trg) + " / " + str(errr) + " per mil")
        allResults.write(str(tmp) + " temperament / " + str(trg) + " / " + str(errr) + " per mil\n")
    for trg in targetSpecial:
        floatTrg = Fraction(trg)
        errr = PEC(tmp, floatTrg)*1000
        sum += errr
        print(str(tmp) + " temperament / " + trg + " / " + str(errr) + " per mil")
        allResults.write(str(tmp) + " temperament / " + trg + " / " + str(errr) + " per mil\n")
    avg = sum / len(target)
    print()
    print(str(tmp) + " temperament avg: " + str(avg) + "per mil")
    results.write(str(tmp) + " temperament avg: " + str(avg) + "per mil\n")
    allResults.write("\n"+ str(tmp) + " temperament avg: " + str(avg) + "per mil\n\n")
    print()
    if avg < minavg:
        minavg = avg
        minavgTemp = [tmp]
    elif avg == minavg:
        minavgTemp.append(tmp)

print(minavgTemp)
print(minavg)