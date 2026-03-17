## INÍCIO DO ENUNCIADO ## 

# Calcular IMC de uma pessoa e apresentar se está ou não em seu peso ideal

# IMC < 20: Abaixo do peso 
# 20 <= IMC < 25: Peso ideal 
# IMC >= 35: Acima do peso

## FIM DO ENUNCIADO ## 


print ("Vamos calcular seu IMC e verficar qual a categoria seu peso está.") #introdução

peso = float(input("Por favor, digite seu peso em kg: ")) #para saber o peso do indivíduo 

altura = float (input("Obrigado. Agora, precisamos saber sua altura em metros: ")) #para saber a altura do indivíduo

imc = peso / (altura ** 2) #calculo IMC

if imc < 20:

    print (f"Seu IMC é {imc:.1f}. Você está abaixo do peso.")

elif 20 <= imc < 25:

    print (f"Seu IMC é {imc:.1f}. Você está no peso ideal.")

else:

    print (f"Seu IMC é {imc:.1f}. Você está acima do peso.")