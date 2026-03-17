## INÍCIO DO ENUNCIADO ##

# Exercício para calculo de peso

# Escreva um programa que leia a altura e o sexo de uma pessoa (M ou F) e
# apresente o seu peso ideal, utilizando as seguintes fórmulas:

# Homens: (72.7 * altura) – 58.0

# Mulheres: (62.1 * altura) – 44.7

## FIM DO ENUNCIADO ##

print ("Descubra o seu peso ideal")

altura = float(input ("Digite sua altura em metros: "))

peso_mulher = (62.1 * altura) - 44.7 

peso_homem = (72.7* altura) - 58.0
   
sexo = str(input("Muito obrigado. Agora, precisamos saber seu sexo: "))

if sexo == "Mulher" or sexo == "mulher":

    print (f"Muito obrigado pelas informações, seu peso ideal é: {peso_mulher:.2f} kg")

else:

    print (f"Muito obrigado pelas informações, seu peso ideal é: {peso_homem:.2f} kg")




