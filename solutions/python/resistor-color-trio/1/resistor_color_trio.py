def label(colors):
    color_map = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }
    
    first_digit = color_map[colors[0]]
    second_digit = color_map[colors[1]]
    
    zeros = color_map[colors[2]]
    
    resistance = str(first_digit) + str(second_digit) + '0' * zeros
    
    resistance_value = int(resistance)
    
    if resistance_value >= 1_000_000_000:
        return f"{resistance_value // 1_000_000_000} gigaohms"
    elif resistance_value >= 1_000_000:
        return f"{resistance_value // 1_000_000} megaohms"
    elif resistance_value >= 1_000:
        return f"{resistance_value // 1_000} kiloohms"
    else:
        return f"{resistance_value} ohms"
