# Given three tuples of names, ages, and cities
# return a tuple of tuples where each tuple has specific name with its corresponding age and city.
# use tuple slicing to accomplish this
# for more info on this quiz, go to this url: http://www.programmr.com/slicing-tuples


def tuple_slice(names, ages, cities):
    empty = []
    for i in range(len(names)):
        k = names[i], ages[i], cities[i]
        empty.append(k)
    return tuple(empty)


if __name__ == "__main__":
    print(tuple_slice(('Gitau', 'Kanyoi', 'Ndegwa'), (13, 24, 5), ('Njogu-ini', 'Limuru', 'Kamae')))

