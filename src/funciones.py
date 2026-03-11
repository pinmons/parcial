def maxima_nota(notas):
    if len(notas) == 0:
        return 0

    for nota in notas:
        if nota < 0 or nota > 5:
            raise ValueError("Las notas deben estar entre 0 y 5")

    return max(notas)



