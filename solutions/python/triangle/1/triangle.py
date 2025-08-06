def valid_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c  # Triangle inequality check

def equilateral(sides):
    if valid_triangle(sides):
        return len(set(sides)) == 1  # All sides are equal
    return False

def isosceles(sides):
    if valid_triangle(sides):
        return len(set(sides)) <= 2  # At least two sides are equal
    return False

def scalene(sides):
    if valid_triangle(sides):
        return len(set(sides)) == 3  # All sides are different
    return False
