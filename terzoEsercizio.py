class CSVFile():
    def __init__(self,nome):
        self.nome=nome

    def get_data(self):
        values =[]

        try:
            file = open(self.nome,'r')
        except Exception as s:
            print('file non esistente "{}"'.format(s))
            import sys
            sys.exit()

        
        for line in file:
            element=line.split(',')
            
            if element[0] != 'Date':
                data = element[0]
                value = element[1]
                try:
                    values.append(float(value))
                except Exception as s:
                    print('errore sconosciuto causato dal valore "{}"'.format(s))
                    

        return values

miofile = CSVFile('sampoo_sales.csv')
print(miofile.nome)
print(miofile.get_data())