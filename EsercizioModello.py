shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]

class Modello(object):
    def fit(self,data):
        pass
    
    def predict(self):
        pass

class Variazione(Modello):
    def fit(self,data):
        if len(data) < 2:
            raise Exception('lista dati troppo piccola minimo 2 dati richiesti')
        
        for item in data:
            if not type(item)==int and not type(item)==float: 
                raise Exception ('lista dati non validi')

            media=[]
            
            i=0
            #mette in una lista la variazione da mese a mese 
            for item in data:
                if item != data[0]:
                    s=item-data[i-1]
                    media.append(s)
                i=i+1
            #fa una media della variazione 
            som=0
            for item in media:
                som=som+item
            
            x=len(media)
            som=som/x 
            self.ris_fit=som   
        return self.ris_fit  
                
          

    def predict(self,mesi_prec):
        if len(mesi_prec)<2:
            raise Exception('lista dati troppo piccola minimo 2 dati richiesti')
        for item in mesi_prec:
            if not type(item)==int and not type(item)==float: 
                raise Exception ('lista dati non validi')
            
                
            media=[]
            
            i=0
            #mette in una lista la variazione da mese a mese 
            for item in mesi_prec:
                if item != mesi_prec[0]:
                    s=item-mesi_prec[i-1]
                    media.append(s)
                i=i+1
            #fa una media della variazione 
            som=0
            x=len(media)
            for item in media:
                som=som+item
            
            som=som/x       
            #somma alle vendite attuali la teorica variazione 
            risprev=mesi_prec[-1]+((som+self.ris_fit)/2)
        return risprev              




        

obj=Variazione()
data=[8,19,31,41,50,52,60]
print('fit :{}'.format(obj.fit(data[:4])))
print('prev :{}'.format(obj.predict(data[4:7])))
