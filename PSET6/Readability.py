from cs50 import get_string

letras = frases = palavras = 0
texto = get_string("Por favor, digite seu texto: ")


#tamanho do texto
length = len(texto)

for i in range(length):
    
    if texto[i].isalnum()==True:
        letras += 1
    elif texto[i].isspace()==True and texto[i+1].isalnum()==True:
        palavras += 1
    elif texto[i]=="?" or texto[i]=="!" or texto[i]==".":
        frases += 1

#Calculo
L = float(letras/palavras)*100
S = float(frases/palavras)*100
index = round((float)(0.0588 * L - 0.296 * S - 15.8))

#Grade

if (index >= 16):
    print('Grade 16+')
elif (index < 1):
    print('Before Grade 1')
else:
    print('Grade ', index)



