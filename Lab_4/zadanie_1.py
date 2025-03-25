def odwroc_liczby():
    liczby = input("Podaj ciąg liczb całkowitych, oddzielonych spacją: ")

    liczby = list(map(int, liczby.split()))

    stos = []

    for liczba in liczby:
        stos.append(liczba)

    print("Liczby w odwrotnej kolejności:")
    while stos:
        print(stos.pop())


odwroc_liczby()
