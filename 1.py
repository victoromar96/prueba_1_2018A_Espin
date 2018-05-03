def calculadora():
    print("calculadora de binario a decimales ")





def creartxt():
    archivo1 = open('1.txt', 'w')
    archivo1.close()

def grabartxt():
    archivo1 = open('1.txt', 'r+')
    archivo1.write('calculadora de binario a decimales')
    numero = int(input("Ingresa el numero a calcular, por favor: "))
    archivo1.write("\nnumero de entrada: ")
    #if numero == numero[0]:
       # print(numero*2**0)


    archivo1.write("\n%s" % numero)

    archivo1.close()


def leertxt():
    archivo1 = open('1.txt', 'r')
    lineas = archivo1.readlines()
    print(lineas)
    archivo1.close()


creartxt()
grabartxt()
leertxt()
#calculadora()