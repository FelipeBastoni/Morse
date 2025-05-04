
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


    txt =   {   ".-": "A",
                "-...": "B",
                "-.-.": "C",        
                "-..": "D",
                ".": "E", 
                "..-.": "F",
                "--.": "G",
                "....": "H",
                "..": "I",
                ".---": "J",
                "-.-": "K",
                ".-..": "L",
                "--": "M",
                "-.": "N",
                "---": "O",
                ".--.": "P",
                "--.-": "Q",
                ".-.": "R",
                "...": "S",
                "-": "T",
                "..-": "U",
                "...-": "V",
                ".--": "W",
                "-..-": "X",
                "-.--": "Y",
                "--..": "Z",
                "/": " ",

    }


    RES = []

    OPT = input("Voce deseja traduzir morse ou gerar uma frase em morse?\nTraduzir: T \nGerar: G\n").upper()
    
    if OPT == "G":
    
        LAP = input("Digite sua frase para transformar em Morse :D\n(PS: não funcionará com uso de acentos)\nFrase: ")
        REC = list(LAP.upper())  # Faz uma lista de caracteres
    
        rg = len(REC)


        for c in range(rg):

            RES.append(morse[REC[c]])
        
        resultado = ''.join(RES)
        print(f'\n{resultado} \n')

    if OPT == "T":

        TRA = input("Digite o Codigo morse")
        REC = list(TRA.split(' '))
        rg = len(REC)





        for c in range(rg):

            RES.append(txt[REC[c]])
        
        resultado = ''.join(RES)
        print(f'\n{resultado} \n')



