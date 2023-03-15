import dataHandler as dh
import csv
import pickle

class hashTable:
    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size

    #calculates and returns hashed index of key
    def get_hash_code(self, key):
        hash = 0

        for char in key:
            hash = hash + ord(char)

        return hash % self.size

    
    #create stock object with data
    #calculate index of object in hashtable with name
    #collision detection
    def add(self, name, wkn, short):
        stock = dh.Stock(name, wkn, short, list())
        
        index = self.get_hash_code(name)

        #collision detection and handling
        if self.table[index] is None:
            self.table[index] = list([stock])
        else:
            self.table[index].append([stock])

    
    #calculates index based on name
    #add array with stock data to history-list
    def importData(self, name):
        index = self.get_hash_code(name)
        
        if self.table[index] is not None:
            for stock in self.table[index]:
                if stock.name == name:
                    stock.history = dh.csvRead(stock.krzl)

    
    #calculates index based on name
    #prints last entry in stock-data array
    def search(self, name):
        index = self.get_hash_code(name)

        if self.table[index] is not None:
            for stock in self.table[index]:
                if stock.name == name:
                    print(stock.krzl + " | Date, Open, High, Low, Close, Volume, Adj, Close")
                    for entry in stock.history[-1:]:
                        print(entry)


    #calculates index based on name
    #deletes element from hashtable
    def remove(self, name):
        index = self.get_hash_code(name)
        
        for stock in self.table[index]:
                if stock.name == name:
                    del self.table[index]


    #pickles hashtable and stores into csv file
    def saveToCSV(self, filename):
        csv = open(filename, 'wb')
        pickle.dump(self.table, csv)
        csv.close()


    #depickles and loads hashtable from csv file then stores in hashtable
    def loadFromCSV(self, filename):
        with open(filename, 'rb') as pickleFile:
            hashtable = pickle.load(pickleFile)
        
        self.table = hashtable
        
        for elem in hashtable:
            if elem is not None:
                print(elem)

    #prints price chart
    def plot(self, name):
        ausgabe = str()
        n = 29

        index = self.get_hash_code(name)
  
        for i in range(0, n):
            if self.table[index] is not None:
                for stock in self.table[index]:
                    if stock.name == name:
                         if i < 29:
                            day1 = stock.history[-30 + i][4]
                            day2 = stock.history[-29 + i][4]
                            day1 = float(day1)
                            day2 = float(day2)
                
                            if day1 - day2 <= 2 and day1 - day2 >= -2:
                                ausgabe = ausgabe + '- '
                            elif day1 - day2 > 2:
                                ausgabe = ausgabe + '\\ '
                            else:
                                ausgabe = ausgabe + '/ '

        print(ausgabe),

