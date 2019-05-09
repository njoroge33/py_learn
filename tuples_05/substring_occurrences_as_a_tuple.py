# Given a source string and a key string, return the occurrences of key string in the source string as a Tuple
# Example given string 'tattattata' and key_string 'tt', return (2, 5)
# for more info on this quiz, go to this url: http://www.programmr.com/substring-occrrences-tuple


def occurrences(source_str, key_str):
    list(source_str)
    list(key_str)
    occur = []
    for i in range(len(source_str) - 1):
        if source_str[i] == key_str[0] and source_str[i + 1] == key_str[1]:
            occur.append(i)
    if occur:
        return tuple(occur)
    else:
        return None


if __name__ == "__main__":
    print(occurrences('sesasesu', 'sb'))
