
def creartxt():
    archivo2 = open('2.txt', 'w')
    archivo2.close()

def grabartxt():
    archivo2 = open('2.txt', 'a')
    cadena = "programacion avanzada"
    cadenain = cadena.replace("programacion", "adaznava")
    cadenainv = cadenain.replace("avanzada", " noicamargorp")
    print(cadena)
    print(cadenain)
    print(cadenainv)
    archivo2.write('la cadena normal es = %s' % cadena)
    archivo2.write('\nla cadena invertida es = %s' % cadenainv)

    archivo2.close()


creartxt()
grabartxt()