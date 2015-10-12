import math
redLineCm = [95280.7,
58886.7,
36394.0,
22492.7,
13901.3,
8591.4,
5309.8,
3281.6,
2028.2,
1253.5,
774.7,
478.8,
295.9,
182.9,
113.0,
69.8,
43.2,
26.7,
16.5,
10.2,
6.3,
3.9,
2.4,
1.5,
0.9,
0.6]

blueLineCm = [117773.5,
72788.0,
44985.5,
27802.5,
17182.9,
10619.6,
6563.3,
4056.3,
2506.9,
1549.4,
957.6,
591.8,
365.8,
226.0,
139.7,
86.3,
53.4,
33.0,
20.4,
12.6,
7.8,
4.8,
3.0,
1.8,
1.1]

def modulor(start):
    val = start
    for i in range(12):
        val = val * 0.618
        roundedVal = val % 1
        if (val % 1 > 0.6):
            val2 = math.ceil(val) / 10
        else:
            val2 = math.floor(val) / 10
        print("{} {} and {}".format(val, val2, roundedVal))

print("red line")
modulor(1829)

print("\nblue line")
modulor(2660)
