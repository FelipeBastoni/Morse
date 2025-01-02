while (1>0):

    morse = {   "A": ".- ",
                "B": "-... ",
                "C": "-.-. ",        
                "D": "-.. ",
                "E": ". ", 
                "F": "..-. ",
                "G": "--. ",
                "H": ".... ",
                "I": ".. ",
                "J": ".--- ",
                "K": "-.- ",
                "L": ".-.. ",
                "M": "-- ",
                "N": "-. ",
                "O": "--- ",
                "P": ".--. ",
                "Q": "--.- ",
                "R": ".-. ",
                "S": "... ",
                "T": "- ",
                "U": "..- ",
                "V": "...- ",
                "W": ".-- ",
                "X": "-..- ",
                "Y": "-.-- ",
                "Z": "--.. ",
                " ": "/ ",
            
    }



    LAP = []
    RES = []


    LAP = input("Digite sua frase para transformar em Morse :D : ")
    REC = list(LAP)  # Separa em uma lista de caracteres


    rg= len(REC)


    for c in range (rg):

        x= REC[c]

        RES.append(morse[x])


    resultado = ''.join(RES)
    print(resultado)
