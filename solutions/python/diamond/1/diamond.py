def rows(letter):
    length = ord(letter) - ord("A")
    result = []

    for i in range(length + 1):
        spaces_outside = " " * (length - i)
        if i == 0:
            result.append(spaces_outside + chr(i + ord("A")) + spaces_outside)
        else:
            spaces_inside = " " * (2 * i - 1)
            result.append(spaces_outside + chr(i + ord("A")) + spaces_inside + chr(i + ord("A")) + spaces_outside)

    return result + result[-2::-1]
