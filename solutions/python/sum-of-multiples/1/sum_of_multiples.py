def sum_of_multiples(limit, multiples):
    multiples_set = set()
    for multiple in multiples:
        if multiple == 0:
            continue
        current_multiple = multiple
        while current_multiple < limit:
            multiples_set.add(current_multiple)
            current_multiple += multiple
    return sum(multiples_set)
