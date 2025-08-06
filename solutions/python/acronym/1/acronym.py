def abbreviate(words):
    return "".join([char for char in words.replace("'", "").title() if char.isupper()])
