class CSVFile():
    def __init__(self,nome):
        self.nome=nome

    def get_data(self):
        values =[]
<<<<<<< HEAD

        try:
            file = open(self.nome,'r')
        except Exception as s:
            print('file non esistente "{}"'.format(s))
            import sys
            sys.exit()

        
=======
    
        file = open(self.nome,'r')
>>>>>>> origin/main
        for line in file:
            element=line.split(',')
            
            if element[0] != 'Date':
                data = element[0]
                value = element[1]
<<<<<<< HEAD
                try:
                    values.append(float(value))
                except Exception as s:
                    print('errore sconosciuto causato dal valore "{}"'.format(s))
                    

        return values

miofile = CSVFile('sampoo_sales.csv')
=======

                values.append(float(value))
        return values

miofile = CSVFile('shampoo_sales.csv')
>>>>>>> origin/main
print(miofile.nome)
print(miofile.get_data())