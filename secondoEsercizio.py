def somma(lista):
    tot=0
    for item in lista:
        tot = tot + item
    return tot


values =[]
data= 0

file = open('shampoo_sales.csv','r')
for line in file:
    element=line.split(',')
    
    if element[0] != 'Date':
        data = element[0]
        value = element[1]

        values.append(float(value))


tot=somma(values)     
print(tot)