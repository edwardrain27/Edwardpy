#Lea un número (n) entero y positivo, de cualquier número de digitos, que calcule la suma de sus digitos y quela
#la imprima junto con el numero leido

def sumNumbers(num):
    
    integer = num//10
    d = num-integer*10

    if integer == 0:
        return d
    
    return d+sumNumbers(integer)



num = int(input('Digite un número: '))


print('la suma de los digitos es: {}'.format(sumNumbers(num)))