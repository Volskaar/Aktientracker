import dataHandler as dh
import hashing as hash

while True:
    userinput = input("ADD | DEL | IMPORT | SEARCH | PLOT | SAVE | LOAD | QUIT --> ")
    
    if userinput == "ADD":
        print("add stock")

    elif userinput == "DEL":
        print("delete stock")

    elif userinput == "IMPORT":
        print("import stock")

    elif userinput == "SEARCH":
        print("search for stock")

    elif userinput == "PLOT":
        print("plot stock")

    elif userinput == "SAVE":
        print("save hashtable")
        getFilename = input("filename: ")

    elif userinput == "LOAD":
        print("load hashtable")
        getFilename = input("filename: ")

    elif userinput == "QUIT":
        break