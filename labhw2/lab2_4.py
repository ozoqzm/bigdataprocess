lengthA = 33 * 30
lengthB = 35 * 24
lengthC = 30 * 33

priceA = 13550 / lengthA
priceB = 15960 / lengthB
priceC = 11990 / lengthC

if priceA < priceB and priceA < priceC:
    print("A_market이 1m당 %.2f으로 최저가이다"%priceA)
elif priceB < priceA and priceB < priceC:
     print("B_market이 1m당 %.2f으로 최저가이다"%priceB)
else:
     print("C_market이 1m당 %.2f으로 최저가이다"%priceC)
     