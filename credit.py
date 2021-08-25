print("Type ‘exit’ to quit")

def main():
    number = str(input("Card Number: "));

    if number == ("exit"):
        exit("Goodbye!")
    for letter in number:
        # reject as invalid if input contains non-numeric characters
        if not letter.isdigit():
            print("INVALID")
            return 1
    # reject as invalid if input does not match specific     
    if (12 > len(number) or 17 <= len(number) or len(number) == 14):
        print("INVALID")
        return 1

    first2 = int(number[:2])
    first1 = int(number[0])

    k = 0
    i = 0

    # run algorithim if digit specifications are met
    if (first2 == 34 or first2 == 37 or first2 == 51 or first2 == 52 or first2 == 53 or first2 == 54 or first2 == 55 or first1 == 4):
        for c in (number[::-1]):
            
            # multiplies every other digit by 2, starting with the number’s 2nd last digit then add those products’ digits together
            if (i % 2 != 0):
                k += int(((int(c) * 2) % 10)) + int(((int(c) * 2) / 10))
                i += 1
            else:
                # add new some of digits not multiplied by 2, to previous sum
                k += int(c)
                i += 1
        # number read as valid if (mod 10 of sum) = 0
        if (k % 10 == 0):
            
            # prints card type if digit specifications are made 
            if(first2 == 34 or first2 == 37):
                print("AMEX")
            elif (first2 == 51 or first2 == 52 or first2 == 53 or first2 == 54 or first2 == 55 ):
                print("MASTERCARD")
            elif (first1 == 4):
                print("VISA")
        else:
            print("INVALID")
    else:
         print("INVALID")

while True:
    main()
