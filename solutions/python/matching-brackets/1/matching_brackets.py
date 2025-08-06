def is_paired(input_string):
    allowed = "([{}])"
    
    filtered_characters = []
    for character in input_string:
        if character in allowed:
            filtered_characters.append(character)
    input_string = "".join(filtered_characters)
    
    stack = []
    for character in input_string:
        if character in "({[":
            stack.append(character)
        elif character in ")}]":
            if not stack: 
                return False
            top = stack.pop() 
            if character == ")" and top != "(":
                return False
            elif character == "]" and top != "[":
                return False
            elif character == "}" and top != "{":
                return False
    
    if stack:
        return False
    
    return True
