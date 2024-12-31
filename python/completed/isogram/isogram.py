def is_isogram(string):
    chars = [char.lower() for char in string if char.isalpha()]
    return len(chars) == len(set(chars))
