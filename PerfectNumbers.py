def isPerfect(n):
    c = 0
    for i in range(1,n):
        if n % i == 0:
            c +=i
    if c == n:
        return True
    else:
        return False
print(isPerfect(28))
def listOfPerfect():
    array = []
    for i in range(1,1000):
        if isPerfect(i):
            array.append(i)
    return array
print(listOfPerfect())