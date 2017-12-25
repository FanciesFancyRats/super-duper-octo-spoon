x = 5

def blastoff(x):
    if (x == 0):
        print("Blastoff")
    else:
        print(x)
        x = x - 1
        blastoff(x)
blastoff(x)
