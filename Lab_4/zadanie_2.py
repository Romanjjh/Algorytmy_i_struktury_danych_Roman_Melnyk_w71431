def sprawdz_nawiasy(wyrazenie):
    stos = []

    for znak in wyrazenie:
        if znak == '(':
            stos.append(znak)
        elif znak == ')':
            if stos and stos[-1] == '(':
                stos.pop()
            else:

                return False
    return len(stos) == 0

wyrazenie = input("Podaj wyrażenie z nawiasami: ")
if sprawdz_nawiasy(wyrazenie):
    print("Nawiasy są prawidłowo zagnieżdżone.")
else:
    print("Nawiasy są nieprawidłowo zagnieżdżone.")