def resistor_label(colors):
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
        "white": 9,
        "gold": 0.05,
        "silver": 0.1
    }
    
    tolerance_map = {
        "grey": 0.05,
        "violet": 0.1,
        "blue": 0.25,
        "green": 0.5,
        "brown": 1,
        "red": 2,
        "gold": 5,
        "silver": 10
    }
    
    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"
    
    if len(colors) == 4:
        first_digit = color_map[colors[0]]
        second_digit = color_map[colors[1]]
        multiplier = color_map[colors[2]]
        tolerance = tolerance_map[colors[3]]
        base_value = int(f"{first_digit}{second_digit}") * (10 ** multiplier)
        
    elif len(colors) == 5:
        first_digit = color_map[colors[0]]
        second_digit = color_map[colors[1]]
        third_digit = color_map[colors[2]]
        multiplier = color_map[colors[3]]
        tolerance = tolerance_map[colors[4]]
        base_value = int(f"{first_digit}{second_digit}{third_digit}") * (10 ** multiplier)
        
    else:
        first_digit = color_map[colors[0]]
        second_digit = color_map[colors[1]]
        multiplier = color_map[colors[2]]
        base_value = int(f"{first_digit}{second_digit}") * (10 ** multiplier)
        tolerance = 0 
    
    if base_value >= 1_000_000_000:
        result_value = round(base_value / 1_000_000_000, 2)
        unit = "gigaohms"
    elif base_value >= 1_000_000:
        result_value = round(base_value / 1_000_000, 2)
        unit = "megaohms"
    elif base_value >= 1_000:
        result_value = round(base_value / 1_000, 2)
        unit = "kiloohms"
    else:
        result_value = base_value
        unit = "ohms"
    
    if isinstance(result_value, float) and result_value.is_integer():
        result_value = int(result_value)

    return f"{result_value} {unit} ±{round(tolerance, 2)}%"
