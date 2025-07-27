# Method of finding temperament from https://note.com/hojo_minori/n/n6a9c39b67327
# Classes 3, 5, 7, 11, 13, 17, 19
import math
import matplotlib.pyplot as plt
import numpy as np
count = {}
accuracy = int(input('accuracy > ')) # Pitch difference filter
templimit = int(input('temperament limit > ')) # Numbers of temperaments checking

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
print(goods) # temperaments and the exponents of 2 when it showed accuracy for each classes
sortablelist = []
for aqp in count.items():
    sortablelist.append(int(aqp[0]))
sorted_temperaments = sorted(sortablelist)
sorted_count = {}
good_count = {}
for aqp in sorted_temperaments:
    if count[str(aqp)] >= 4:
        good_count[str(aqp)] = count[str(aqp)]
    sorted_count[str(aqp)] = count[str(aqp)]

print(sorted_count) # counts how many times which temperament was decided accurate

# Graphs of all temperaments which got any count
tmp = []
freq = []
for key, value in sorted_count.items():
    tmp.append(key)
    freq.append(value)
x = np.arange(len(tmp))
plt.title("Accuracy: "+str(accuracy))
plt.bar(x, freq)
plt.xticks(x, tmp, fontsize=5)
plt.show()

# Graphs of ones which past 4 counts
tmp = []
freq = []
for key, value in good_count.items():
    tmp.append(key)
    freq.append(value)
x = np.arange(len(tmp))
plt.title("4+ / Accuracy: "+str(accuracy))
plt.bar(x, freq)
plt.xticks(x, tmp, fontsize=7)
plt.show()