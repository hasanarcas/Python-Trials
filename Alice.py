file = open("alice.txt","r")
d={}
for line in file:
    for word in line.split():
        word = word.lower()
        if word in d:
            d[word] +=1
        else:
            d[word] = 1

print(d)