def karp_rabin_algorithm(string, pattern):

    string_len = len(string)
    pattern_len = len(pattern)

    p_hash = hash(pattern)
    s_hash = hash(string[0:pattern_len])

    counter = 0

    for i in range(string_len - pattern_len + 1):
        if s_hash != p_hash:
            s_hash = hash(string[i:i + pattern_len])
        else:
            counter += 1
            s_hash = hash(string[i:i + pattern_len])

    if counter == 0:
        print('No matching pattern in given string')
