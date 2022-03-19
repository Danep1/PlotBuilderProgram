def text_to_function(text):
    x = 2
    text = text[text.index('=') + 1:].replace('^', '**').strip()
    return eval(text), text


a = text_to_function('y = x^2')
print(a)
