import math
from fractions import Fraction

k = int(input("Enter prime number >> "))
a = [k, 2]
n = []

for counter in range(1, 10):
    if a[-1] <= 1:
        break
    next_n = math.floor(math.log(a[-2]) / math.log(a[-1]))
    print(str(counter) + "th n: " + str(next_n))
    n.append(next_n)
    next_a = a[-2] / (a[-1] ** n[-1])
    print(str(counter) + "th a: " + str(next_a))
    a.append(next_a)

print("\n--- [해결] 차례대로 계산된 근사분수 수열 ---")
# n 리스트를 1개, 2개, 3개... 순서대로 늘려가며 각각 연분수를 복구합니다.
for limit in range(1, len(n) + 1):
    sub_n = n[:limit]  # 앞에서부터 해당 단계까지만 잘라내기
    
    # 잘라낸 부분 연분수를 복구
    recov = Fraction(sub_n[-1])
    for i in reversed(sub_n[:-1]):
        recov = i + (1 / recov)
        
    print(f"{limit}번째 근사분수: {recov}  (분모: {recov.denominator})")
