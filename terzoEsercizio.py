class CSVFile():
    def __init__(self,nome):
        self.nome=nome
        if(type(self.nome) != str):
            raise Exception ('non sono valide non stringhe come nome del file')
    
    def get_data(self, start=None, end=None):
        values =[]

        if (type(start) != int and start!=None):
                raise Exception ('non sono validi non int come valori di start')
        else:
            if (type(end) != int and end!=None):
                raise Exception ('non sono validi non int come valori di end')
            else:
                
                
                nome = self.nome
                nome = nome.strip()
                try:
                    file = open(nome,'r')                        
                except Exception as s:
                    print('file non esistente "{}"'.format(s))
                        
                i=0
                for line in file:
                    if start == end == None:
                        i=i+1
                        element=line.split(',')
                                
                        if element[0] != 'Date':
                            data = element[0]
                            value = element[1]

                            try:
                                values.append(float(value))
                            except Exception as s:
                                print('errore sconosciuto causato dalla conversione valore "{}"'.format(s))
                    elif i>=start and i<=end:
                        i=i+1
                        element=line.split(',')
                                    
                        if element[0] != 'Date':
                            data = element[0]
                            value = element[1]

                            try:
                                values.append(float(value))
                            except Exception as s:
                                print('errore sconosciuto causato dal valore "{}"'.format(s))
                    else:
                        i=i+1
                    
                file.close()
                return values

miofile = CSVFile("shampoo_sales.csv")


print('Nome del file: "{}"'.format(miofile.nome))
print('Dati contenuti nel file: "{}"'.format(miofile.get_data()))

 