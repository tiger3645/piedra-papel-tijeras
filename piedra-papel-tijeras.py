import random

intro = '''
O=====================================O
|                                     |
|         ¡Escribe tu opción!         |
|      (Piedra, Papel, o Tijeras)     |
|                                     |
O=====================================O
'''
win = '''
O=====================================O
|                                     |
|              ¡Ganaste!              |
|                  :)                 |
|                                     |
O=====================================O
'''
lose = '''
O=====================================O
|                                     |
|              Perdiste...            |
|                 :(                  |
|                                     |
O=====================================O
'''
draw = '''
O=====================================O
|                                     |
|               ¡Empate!              |
|                                     |
O=====================================O
'''
opciones = ('piedra', 'papel', 'tijeras')

def jugar():
    usuario = input("opción: ")
    if usuario.lower() not in opciones:
        print("\"" + usuario + "\" no es una opción correcta. Intente nuevamente.")
        jugar()
    else:
        sistema = random.choice(opciones)
        print("PC: "+sistema+"!")
        if sistema == usuario:
            print(draw)
        else:
            if usuario.lower() == opciones[0]:
                if sistema == opciones[1]:
                    print(lose)
                elif sistema == opciones[2]:
                    print(win)
            elif usuario.lower() == opciones[1]:
                if sistema == opciones[0]:
                    print(win)
                elif sistema == opciones[2]:
                    print(lose)
            elif usuario.lower() == opciones[2]:
                if sistema == opciones[0]:
                    print(lose)
                elif sistema == opciones[1]:
                    print(win)
    ask_again()
    
def ask_again():
    again = input("¿Jugar de nuevo? (S/N): ")
    if again.lower() == "s":
        jugar()
    elif again.lower() == "n":
        exit()
    else:
        print("\""+again+"\" no es una opción correcta")
        ask_again()

if __name__ == "__main__":
    print(intro)
    jugar()