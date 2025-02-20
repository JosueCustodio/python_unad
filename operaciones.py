print('Te pedire dos numeros y tu decidiras que operacion que realizaras con ellos')

num1 = input('Numero 1 > ')
num2 = input('Numero 2 > ')
operacion = input('Que operacion quieres hacer? +, -, /, * > ')

def operar():
    if (operacion == '+'):
        resultado = int(num1) + int(num2)
        print('El resultado de esa suma es', resultado)
        
    if (operacion == '-'):
        resultado = int(num1) - int(num2)
        print('El resultado de esa resta es', resultado)
        
    if (operacion == '/'):
        resultado = int(num1) / int(num2)
        print('El resultado de esa division es', resultado)
        
    if (operacion == '*'):
        resultado = int(num1) * int(num2)
        print('El resultado de esa multiplicacion es', resultado)
        
operar()