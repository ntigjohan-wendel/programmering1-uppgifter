def _1():
    i_valueCount = int(input("Antal värden: "))
    values = str.split(input("Värden: "), ",", i_valueCount)
    if len(values) > i_valueCount:
        values.pop(len(values)-1)
    
    print(values)
    print("-----")
    
    def getLargest(sortedList):
        return sortedList[len(sortedList)-1]
    
    def getSmallest(sortedList):
        return sortedList[0]
    
    def getMean(sortedList):
        sum = 0
        for n in sortedList:
            sum = sum + n
        return sum/len(sortedList)
    
    def getOddCount(sortedList):
        count = 0
        for n in sortedList:
            if n % 2 == 1:
                count += 1
        return count
    def getEvenCount(sortedList):
        count = 0
        for n in sortedList:
            if n % 2 == 0:
                count += 1
        return count
    
    values_sorted = list(map(int, values))
    values_sorted.sort()
    
    print(f"Largest: {getLargest(values_sorted)}")
    print(f"Smallest: {getSmallest(values_sorted)}")
    print(f"Mean: {getMean(values_sorted)}")
    print(f"Amount of odd numbers: {getOddCount(values_sorted)}")
    print(f"Amount of even numbers: {getEvenCount(values_sorted)}")
    print()

_1()

def _2():
    pass