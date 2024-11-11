liste = [[1,"iPhone", 500],[2, "Bier", 5],[3, "MacBook", 2000],[4, "Sofa", 1000],[5, "Zigaretten", 7]]
bestellung = [[1,1], [1,1], [1,1], [1,1], [3,1], [3,1]]

def rabatt(bestellung):
    for artikel_id, _ in bestellung:
        preis = next(item[2] for item in liste if item[0] == artikel_id)
    
        anzahl = bestellung.count([artikel_id, 1])
    
        rabatt = 0.10 if anzahl >= 10 else 0.05 if anzahl >= 5 else 0
        
        artikelpreis_nach_rabatt = preis * (1 - rabatt)

        print(f"Artikel ID {artikel_id}: {artikelpreis_nach_rabatt} €")

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
