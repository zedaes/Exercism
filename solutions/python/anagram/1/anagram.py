def find_anagrams(word, candidates):
    a = []
    for i in candidates:
        sorted_candidate = sorted(i.lower())
        sorted_word = sorted(word.lower())
        if sorted_candidate == sorted_word and i.lower() != word.lower():
            a.append(i)
            
    return a
