print("Type ‘exit’ to quit")

def main():
    number = str(input("Card Number: "));

    if number == ("exit"):
        exit("Goodbye!")
    for letter in number:
        if not letter.isdigit():
            print("INVALID")
            return 1
    if (12 > len(number) or 17 <= len(number) or len(number) ==14):
        print("INVALID")
        return 1

    first2 = int(number[:2])
    first1 = int(number[0])

    k = 0
    i = 0

    if (first2 == 34 or first2 == 37 or first2 == 51 or first2 == 52 or first2 == 53 or first2 == 54 or first2 == 55 or first1 == 4):
        for c in (number[::-1]):

            if (i % 2 != 0):
                k += int(((int(c) * 2) % 10)) + int(((int(c) * 2) / 10))
                i += 1
            else:
                k += int(c)
                i += 1

        if (k % 10 == 0):
            if(first2 == 34 or first2 == 37):
                print("AMEX")
            elif (first2 == 51 or first2 == 52 or first2 == 53 or first2 == 54 or first2 == 55 ):
            elif (first1 == 4):
                print("VISA")
        else:
            print("INVALID")
    else:
         print("INVALID")

while True:
    main()
