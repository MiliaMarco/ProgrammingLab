class ExamException(Exception):
    pass

def hourly_trend_changes(data):
    i=0
    listacamb=[]
    epoch=[]
    temp=[]
    epochConsiderata=0
    tempConsiderata=0
    cont=0
    lung=len(data)
    prob=[] #variabile utiliazzata se il trend iniziale non e' facilmente riconoscibile        
    for item in data:
        if lung==1:
            listacamb.append(cont)
        if lung==2 and i==1:
            listacamb.append(cont)    
        if i<2:
            epoch.append(item[0])
            temp.append(item[1])
            i=i+1
        else:
            epochConsiderata=item[0]
            tempConsiderata=item[1]
            if i>2:
                ep=epochConsiderata/3600
                ep=int(ep)
                e1=epoch[1]/3600
                e1=int(e1)
                if not (ep)==(e1): 
                    listacamb.append(cont)
                    cont=0
            if i==2: 
                if temp[0]==temp[1]:
                    prob.append(temp[0])
                    prob.append(temp[1])
                    for x in data[2:]:
                        if prob[0]==prob[1]:
                            prob[0]=prob[1]
                            prob[1]=x[1]
                        if prob[0]<prob[1]:
                            salita=True
                            break
                        elif prob[0]>prob[1]:
                            salita=False
                            break

                elif temp[0]<temp[1]:
                    salita= True
                else:
                    salita= False

            
            if temp[1]==tempConsiderata:
                if salita==True:
                    salita=True
                else:
                    salita=False
            
            elif temp[1]<tempConsiderata:
                if salita == True:
                    salita =True
                else:
                    cont=cont+1
                    salita = True
            
            else:
                if salita == True:
                    cont=cont+1
                    salita=False
                else:
                    salita=False
            
           
            epoch[0]=epoch[1]
            epoch[1]=epochConsiderata
            temp[0]=temp[1]
            temp[1]=tempConsiderata    
            
            i=i+1
            if i == lung:
                listacamb.append(cont)
                cont=0    
    return listacamb


class CSVTimeSeriesFile():
    def __init__(self,name):
        self.name=name

    def get_data(self):
        i=0
        lista=[]
        sublist=[]
        ordinamento=[]
        name=self.name.strip() 
        try: 
            file = open(name,'r')
        except:
            raise ExamException('Errore, file non esistente')
        for line in file:
            element=line.split(',')
            try: 
                x=float(element[0])
                y=float(element[1])
            except:
                continue
            x=float(element[0])
            round(x)
            x=int(element[0])
            y=float(element[1])
            ordinamento.append(x)
            if i>0:
                if x<ordinamento[0]:
                    raise ExamException('Errore, ordinamento dati incorretto, epoch {}'.format(x))
                if x==ordinamento[0]:
                    raise ExamException('Errore, epoch duplicato, epoch {}'.format(x))    
                ordinamento[0]=x
            sublist.append(x)
            sublist.append(y)
            lista.append(sublist)
            sublist=[]
            i=i+1
        return lista

#test-----------------------------------------------------        
time_series_file= CSVTimeSeriesFile(name="data.csv")
time_series=time_series_file.get_data()
print(time_series)
test=hourly_trend_changes(time_series)
print(test)
#test------------------------------------------------------




