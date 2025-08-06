def classify(number):
    """Classify a number as perfect, abundant, or deficient.

    :param number: int - the number to classify.
    :return: str - 'perfect', 'abundant', or 'deficient'.
    :raises ValueError: if the number is not a positive integer.
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    aliquot_sum = sum(i for i in range(1, number // 2 + 1) if number % i == 0)
    
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"