numero1 = input('escribe el primer numero > ')
numero2 = input('escribe el segundo numero > ')

def mayorOMenor (numero1, numero2):
    if (numero1 == numero2):
        print(numero1 + ' y ' + numero2 + ' son iguales')
    
    if (numero1 > numero2):
        print(numero1 + ' es mayor')
        
    if (numero2 > numero1):
        print(numero2 + ' es mayor')
        
mayorOMenor()