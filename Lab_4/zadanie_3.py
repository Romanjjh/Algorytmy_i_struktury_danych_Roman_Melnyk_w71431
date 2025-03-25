def main():
    stos = []

    while True:
        print("\nOpcje:")
        print("1. Dodaj tekst")
        print("2. Cofnij ostatnią operację (Undo)")
        print("3. Zakończ działanie (exit)")

        wybor = input("\nWybierz opcję (1/2/3): ")

        if wybor == '1':
            tekst = input("Wprowadź tekst do dodania: ")
            stos.append(tekst)
            print(f"Dodano tekst: '{tekst}'")

        elif wybor == '2':
            if stos:
                ostatni_tekst = stos.pop()
                print(f"Cofnięto ostatnią operację: '{ostatni_tekst}'")
            else:
                print("Brak tekstu do cofnięcia.")

        elif wybor == '3':
            print("Kończenie programu...")
            break

        else:
            print("Niepoprawny wybór. Wybierz 1, 2 lub 3.")

main()
