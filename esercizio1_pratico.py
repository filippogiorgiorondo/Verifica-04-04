"""
TRACCIA -

"""
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n','o','p','q','r','s','t','u','v','w','x','y','z']
numeri = ["1"...]
def divisore_dati():
    #creazione liste
    num = []
    bool = []
    char = []
    quanteVolte = int(input("Inserisci il numero di volte che vuoi ripetere l'operazione"))
    for i in range(quanteVolte): #quante volte ripetere il ciclo
        valoreInserito = input("Inserisci il tuo valore").lowe()
        if valoreInserito in alfabeto: #verifica se il valore è nell'alfabeto per verificare che sia un char
            char.append(valoreInserito)
        elif valoreInserito in numeri: #verifica se è nella lista numeri da uno a nove (non completata)
            num.append(valoreInserito)
        elif valoreInserito =='true' or valoreInserito=='false': #verifica bool
            bool.append(valoreInserito) 
#codice incompleto
