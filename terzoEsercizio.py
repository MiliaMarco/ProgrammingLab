class CSVFile():
    def __init__(self,nome):
        self.nome=nome

    def get_data(self):
        values =[]
    
        file = open(self.nome,'r')
        for line in file:
            element=line.split(',')
            
            if element[0] != 'Date':
                data = element[0]
                value = element[1]

                values.append(float(value))
        return values

miofile = CSVFile('shampoo_sales.csv')
print(miofile.nome)
print(miofile.get_data())