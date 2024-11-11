# Projekterklärung

## Definition 
### Objekt
[id, Namen, Preis]

### Bestellung
[id, faktor]
[[1,1], [1,1], [1,1], [1,1], [3,1], [3,1]]

* Die Liste "liste" beinhaltet alle Objekte die man bestellen kann
* liste = [[1,"iPhone", 500],[2, "Bier", 5],[3, "MacBook", 2000],[4, "Sofa", 1000],[5, "Zigaretten", 7]]

### Funktionen

#### rabatt()

Mit einer Schrleife wird abgezählt, wie oft jedes Objekt in der Bestellung vorkommt und ab 5/10 Stück wird der jeweilige Rabatt dazugerechnet. Die Funktion bekommt als Parameter eine Bestelliste und bearbeitet die Faktor-Werte in dieser. 

#### steuern()

In einer Schleife wird bei jedem Wert über die ID der name des Bestellobjektes aufgerufen, der erste Buchstabe wird geprüft ob er in A-K fällt. Der Faktor wird daraufhin berechet.
