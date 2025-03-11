def druga_najwieksza(lista):

    unikalne_liczby = set(lista)

    posortowane_liczby = sorted(unikalne_liczby, reverse=True)

    return posortowane_liczby[1]



print(druga_najwieksza([5, 2, 9, 1, 9, 7, 5]))
print(druga_najwieksza([1, 2, 3, 4, 5]))
print(druga_najwieksza([10, 20, 30]))
print(druga_najwieksza([1, 2, 2, 2, 1]))
