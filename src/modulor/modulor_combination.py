'''
Created on 19.10.2013

@author: chris
'''
# redLineCm = [95280.7,
# 58886.7,
# 36394.0,
# 22492.7,
# 13901.3,
# 8591.4,
# 5309.8,
# 3281.6,
# 2028.2,
# 1253.5,
# 774.7,
# 478.8,
# 295.9,
# 182.9,
# 113.0,
# 69.8,
# 43.2,
# 26.7,
# 16.5,
# 10.2,
# 6.3,
# 3.9,
# 2.4,
# 1.5,
# 0.9,
# 0.6]
# 
# blueLineCm = [117773.5,
# 72788.0,
# 44985.5,
# 27802.5,
# 17182.9,
# 10619.6,
# 6563.3,
# 4056.3,
# 2506.9,
# 1549.4,
# 957.6,
# 591.8,
# 365.8,
# 226.0,
# 139.7,
# 86.3,
# 53.4,
# 33.0,
# 20.4,
# 12.6,
# 7.8,
# 4.8,
# 3.0,
# 1.8,
# 1.1]

redLineCm = [5, 11, 16, 27, 43, 70, 113, 183, 296, 479, 775]

blueLineCm = [10, 22, 32, 54, 86, 140, 226, 366, 592, 958, 1550]


allLines = list(map(lambda x: [x, 'r'], redLineCm.copy()))
allLines.extend(list(map(lambda x: [x, 'b'], blueLineCm)))
allLines.sort()

LIST_LENGTH = len(allLines)

def approx(a, b, margin):
    if (a > b):
        return a - b <= margin
    else:
        return b - a <= margin    

def indexInc(list, pos):
    if (pos < len(list)):
        list[pos] += 1
        if list[pos] == LIST_LENGTH:
            list[pos] = 0
            indexInc(list, pos + 1)

def computePossibilities(indizes):
    result = []
    for val in range(LIST_LENGTH ** len(indizes)):
        lengthSum = 0.0
        for index in indizes:
            lengthSum += allLines[index][0]
        
        for mainVal in allLines:
            if approx(mainVal[0], lengthSum, 0.0):
                resultTuple = []
                for index in indizes:
                    resultTuple.append(allLines[index])
                
                result.append([mainVal, lengthSum, resultTuple])
                
        indexInc(indizes, 0)
    return result

indizes = [0, 0, 0, 0, 0]
with open("/tmp/modulor.txt", "a") as outfile:
    result = computePossibilities(indizes)
    result.sort()
    for row in result:
        outfile.write("{0} (computed: {1:.2f}); values: {2}\n".format(row[0], row[1], row[2]))
#        outfile.write("Computed value: {0:.2f}; true value: {}; line: {}\n".format(row[0], row[1][0], row[1][1]))
#     print("{}".format(result))
