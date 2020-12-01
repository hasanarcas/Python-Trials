def count(p, letter):
    upper = ""
    for i in range(65, 91):
        upper += chr(i)
    lower = ""
    for i in range(97, 123):
        lower += chr(i)

    upper_count = 0
    lower_count = 0

    for char in p:
        if upper.find(char) > -1:
            upper_count += 1
        elif lower.find(char) > -1:
            lower_count += 1

    letter_count = 0
    for i in p:
        if i == letter:
            letter_count += 1

    print("Your paragraph contains", upper_count, "upper case letters and", lower_count, "lower count letters and",letter
          , "is written ",letter_count," times.")


count("Asjdfaskdfjsd ALKJsdflksadjf asdlkfjlaks asdjkld ASKJdhnkjas asdlkfhn ASasLKFDNjakdf", "a")