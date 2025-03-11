def znajdz_min_max(macierz):
    min_val, max_val = float('inf'), float('-inf')
    min_idx, max_idx = None, None

    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] < min_val:
                min_val, min_idx = macierz[i][j], (i, j)
            if macierz[i][j] > max_val:
                max_val, max_idx = macierz[i][j], (i, j)

    macierz_zmodyfikowana = [row[:] for row in macierz]
    macierz_zmodyfikowana[min_idx[0]][min_idx[1]] = "MIN"
    macierz_zmodyfikowana[max_idx[0]][max_idx[1]] = "MAX"

    print(f"Najmniejsza wartość: {min_val} na pozycji {min_idx}")
    print(f"Największa wartość: {max_val} na pozycji {max_idx}")

    for row in macierz_zmodyfikowana:
        print(row)

macierz = [
    [5, 2, 9, 8],
    [1, 7, 3, 4],
    [6, 0, 2, 5]
]
znajdz_min_max(macierz)
