# author: Branden Kim
# assignment: HW1
# description: Reverse a 2-digit number

while True:
    try:
        str_number = input('Enter a 2-digit integer: ')
        int(str_number)
    except ValueError:
        print("Value must be a number")
    except KeyboardInterrupt:
        print()
        break
    else:
        if len(str_number) == 2:
            print(str_number[::-1])
            break
        print('Must be a 2-digit number')


