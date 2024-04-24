def cezar_algorithm(step, string):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    for s in string:
        idx = alphabet.find(s)

        if idx == -1:
            result += s
        else:
            new_index = (idx + step) % len(alphabet)
            result += alphabet[new_index]

    return result
