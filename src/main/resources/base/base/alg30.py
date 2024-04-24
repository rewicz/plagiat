def boyer_moore_algorithm(string, pattern):
    s_len = len(string)
    p_len = len(pattern)

    chars = [-1] * 200
    for p in range(p_len):
        chars[ord(pattern[p])] = p

    i = 0
    while i <= s_len - p_len:
        p = p_len - 1

        while p >= 0 and pattern[p] == string[i + p]:
            p -= 1

        if p < 0:
            if i + p_len < s_len:
                i += (p_len - chars[ord(string[i + p_len])])
            else:
                i += 1
        else:
            i += max(1, p - chars[ord(string[i + p])])
