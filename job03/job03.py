def nombre():
    chiffre = range(101)
    for i in chiffre:
        if i ==26 or i == 37 or i == 88:
            print("-")
        else:
            print(i)
nombre()