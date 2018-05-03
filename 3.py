
def creartxt():
    archivo3 = open('3.txt','w')
    archivo3.close()

def grabartxt():
    archivo3 = open('3.txt','a')
    archivo3.write("Mensaje a codificar")

    #tabla de listas
    equivalencias = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    equivalenciasCorresp = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V',
                            'H', 'L', 'C', 'K', 'E']
    lista = [equivalencias, equivalenciasCorresp]
    print(lista)

    #mensaje a modificar
    mensaje = ['t', 'a', 'l', 'l', 'e', 'r']
    codificar = mensaje
    archivo3.write("\n%s " % codificar)
    archivo3.write("\n")
    #mensaje modificado
    archivo3.write("\nMensaje codificado")

    mensaje[0] = lista[0][0]
    mensaje[1] = lista[0][3]
    mensaje[2] = lista[0][19]
    mensaje[3] = lista[0][19]
    mensaje[4] = lista[0][22]
    mensaje[5] = lista[0][1]


    codificado = mensaje[0]
    codificado1 = mensaje[1]
    codificado2 = mensaje[2]
    codificado3 = mensaje[3]
    codificado4 = mensaje[4]
    codificado5 = mensaje[5]
    archivo3.write("\n%s " % codificado)
    archivo3.write("%s " % codificado1)
    archivo3.write("%s " % codificado2)
    archivo3.write("%s " % codificado3)
    archivo3.write("%s " % codificado4)
    archivo3.write("%s " % codificado5)
    archivo3.close()

creartxt()
grabartxt()



