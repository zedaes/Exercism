class Luhn:
    def __init__(self, card_num):
        self.number = card_num.replace(' ', '')

    def valid(self):
        number = self.number
        
        if len(number) <= 1:
            return False
        
        if not number.isnumeric():
            return False
        
        total = sum(int(digit) for digit in number[-1::-2])
        
        for digit in number[-2::-2]:
            digit = 2 * int(digit)
            total += digit if digit < 10 else digit - 9
        
        return total % 10 == 0
            
