liste = [[1,"iPhone", 500],[2, "Bier", 5],[3, "MacBook", 2000],[4, "Sofa", 1000],[5, "Zigaretten", 7]]
bestellung = [[1,1], [1,1], [1,1], [1,1], [3,1], [3,1]]

def rabatt(bestellung):
    pass

def steuern(bestellung):
    pass

def bestellsumme(bestellung):
    sum = 0
    for [id, factor] in bestellung:
        sum += liste[id-1][2]*factor

    return sum

rabatt(bestellung)
steuern(bestellung)
bestellsumme(bestellung)