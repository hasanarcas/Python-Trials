def Isogram(str):
    chars = "abcdefghijklmnopqrstuvwxyz"
    for char in chars:
        count = str.count(char)
        if count > 1:
            return False , char , count
    return True
print(Isogram("moose"))