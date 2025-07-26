import math
count = {}
accuracy = int(input('factor > '))
templimit = int(input('temperament limit > '))
def pitchDiff(a, b):
    return min(abs(1200*math.log2(a/b)), abs(1200*math.log2(b/a)))
goods = {}
for w in [3, 5, 7, 11, 13, 17, 19]:
    goods[str(w)] = []
    for d in range(1, templimit):
        a = 1
        c = 2
        b = pow(w, d)
        while True:
            calculation = pitchDiff(b, c)
            if(c/2>=b):
                break
            if ((2*c>=b) or (c>=b)) and (calculation <= accuracy):
                goods[str(w)].append((d, a))
                print("2^"+str(a)+" , " +str(w)+"^"+str(d)+": "+ str(calculation) + "cents")
                if str(d) in count.keys():
                    count[str(d)] += 1
                else:
                    count[str(d)] = 1
            a += 1
            c *= 2
print(goods)
print(count)