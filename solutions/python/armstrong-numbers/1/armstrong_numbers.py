def is_armstrong_number(number):
    digits = [int(digit) for digit in str(number)]
    power = len(digits)
    
    return number == sum(digit ** power for digit in digits)
