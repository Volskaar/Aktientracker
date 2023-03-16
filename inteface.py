import dataHandler as dh
import hashing as hash

hashtable = hash.hashTable()

while True:
    userinput = input("ADD | DEL | IMPORT | SEARCH | PLOT | SAVE | LOAD | QUIT --> ")
    
    #liest name, wkn und kürzel ein und erstellt ein neues objekt, welches in die hashtable gespeichert wird
    if userinput == "ADD":
        stockname = input("Atkienname: ")
        wkn = input("WKN: ")
        short = input("Kürzel: ")
        hashtable.add(stockname, wkn, short)

    #löscht objekt per errechnetem index aus der hashtable
    elif userinput == "DEL":
        stockname = input("Atkienname: ")
        hashtable.remove(stockname)

    #kurswerte der letzten 30 tage werden aus csv zu objekt hinzugefügt
    elif userinput == "IMPORT":
        stockname = input("Atkienname: ")
        hashtable.importData(stockname)

    #gibt letzten Kurswert aus
    elif userinput == "SEARCH":
        stockname = input("Atkienname: ")
        hashtable.search(stockname)

    #plots ascii graph of last 30 days of graph
    elif userinput == "PLOT":
        stockname = input("Atkienname: ")
        hashtable.plot(stockname)

    #stores current hashtable in csv file
    elif userinput == "SAVE":
        filename = input("Filename: ")
        hashtable.saveToCSV(filename)

    #loads hashtable from csv file
    elif userinput == "LOAD":
        filename = input("filename: ")
        hashtable.loadFromCSV(filename)

    elif userinput == "QUIT":
        break