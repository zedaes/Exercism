def translate_text(text):
    while not text[0] in 'aeiou':
        if text[0] in 'xy' and not text[1] in 'aeiou':
            break
        text = text[1:] + text[0]
        if text[-1] == 'q' and text[0] == 'u':
            text = text[1:] + 'u'
    return text + 'ay'

def translate(sentence):
    return ' '.join([translate_text(text) for text in sentence.split()])
