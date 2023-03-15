import csv

#objects of type stockdata with information about stock
#informations about stocks from csv files
#serialize informations from csv files in objects

class Stock:
    def __init__(self, name, wkn, krzl, history):
        self.name = name
        self.wkn = wkn
        self.krzl = krzl
        self.history = history

    def printHistory(self):
        for x in self.history:
            print(x)


def csvRead(f):
    #array with all the stock data
    stockdata = [31]

    # csv file name
    filename = 'data/' + f + '.csv'
    
    # initializing the titles and rows list
    fields = []
    rows = []
    
    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)
    
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
    
    stockdata.append(fields)

    for row in rows[-30:]:
        stockdata.append(row)

    return stockdata