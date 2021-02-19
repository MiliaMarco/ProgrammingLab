def SommoElementiLista(lisata):
    ris =0
    for item in lisata:
        ris=ris+item
    return ris



print("Sommma = {}".format(SommoElementiLista([1,5,7])))
