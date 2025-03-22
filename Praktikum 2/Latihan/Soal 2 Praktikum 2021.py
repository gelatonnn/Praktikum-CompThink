for y in range(15, -15, -1):
    for x in range(-30, 31):
        fungsi = ((x/2)**2 + (5*y/4 - 2*(abs(x))**0.5)** 2)
        if fungsi <= 120:
            print("*", end="")
        else:
            print(" ", end="")
    print()