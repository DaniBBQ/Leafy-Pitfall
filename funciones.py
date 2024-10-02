import pygame
import recursos
import random

vida_maxima = recursos.vidas.copy()
vida = recursos.vidas
# en esta matriz se almacenan 6 por cada unidad que se utilizan para las funciones de los items
statusCheck = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]
## status indice : 0 == colmnillos vampiricos, 1 == aliento de peste,
#                  2 == daga, 3 == botas, 4 == frenesi, 5 == represion,
#                  6 == efecto de clase
cal = 0
daño = recursos.daños
a = 0
o = 0


def calcular_colisiones_movimiento(puntos):
    """
    Esta función calcula si un punto amarillo es igual a algún rectángulo de las unidades, si es así, elimina ese punto y no se puede mover ahí
    """

    for i in range(len(puntos) - 1, -1, -1):

        if puntos[i] in recursos.lista_de_unidades:
            puntos.pop(i)  # Elimina un rectángulo de la lista de los puntos, si comparte coordenadas con una unidad

    for m in range(len(puntos) - 1, -1, -1):
        if puntos[m] in recursos.lista_de_lapidas:
            puntos.pop(m)

    return puntos  # Devuelve la lista de los puntos depurada


def calcular_colisiones_ataque(marcas):
    """
    Esta función calcula si un punto amarillo es igual a algún rectángulo de las unidades, si es así, elimina ese punto y no se puede mover ahí
    """
    lista2 = []
    for i in range(len(marcas) - 1, -1, -1):

        if marcas[i] not in recursos.lista_de_unidades:
            lista2.append(
                marcas[i])  # Elimina un rectángulo de la lista de las marcas, si no comparte coordenadas con una unidad
            marcas.pop(i)
    return marcas, lista2  # Devuelve la lista de las marcas depurada


def calcular_puntos(unidad):
    """ Esta función calcula las posiciones en donde deben estar los cuadros amarillos según el movimiento de la unidad
        y devuelve una lista con esta información """
    global a
    copia_unidad = unidad.copy()
    puntos_p = []

    # ///////////////////////////
    rect = copia_unidad
    rect.y -= 100
    puntos_p.append(rect)
    copia_unidad = unidad.copy()

    rect = copia_unidad
    rect.y += 100
    puntos_p.append(rect)  # puntos compartidos por todos
    copia_unidad = unidad.copy()

    rect = copia_unidad
    rect.x += 100
    puntos_p.append(rect)
    copia_unidad = unidad.copy()

    rect = copia_unidad
    rect.x -= 100
    puntos_p.append(rect)
    copia_unidad = unidad.copy()
    # ////////////////////////////

    # ///////////////////////////////////////////////////////////////////////////////////

    if unidad is recursos.lista_de_unidades[1] or unidad is recursos.lista_de_unidades[6] or unidad is \
            recursos.lista_de_unidades[2] or unidad is \
            recursos.lista_de_unidades[7]:
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.y -= 100
        rect.x -= 100
        puntos_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.y -= 100
        rect.x += 100
        puntos_p.append(rect)  # Puntos compartidos por los escuderos y los sanadores
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.y += 100
        rect.x -= 100
        puntos_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.y += 100
        rect.x += 100
        puntos_p.append(rect)
        copia_unidad = unidad.copy()
    # ///////////////////////////////////////////////////////////////////////////////////

    # ///////////////////////////////////////////////////////////////////////////////////
    if unidad is recursos.lista_de_unidades[2] or unidad is recursos.lista_de_unidades[7] or unidad is \
            recursos.lista_de_unidades[4] or unidad is \
            recursos.lista_de_unidades[9]:
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.y -= 200
        puntos_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.y += 200
        puntos_p.append(rect)  # Puntos compartidos por los caballeros y los sanadores
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.x += 200
        puntos_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.x -= 200
        puntos_p.append(rect)
        copia_unidad = unidad.copy()
    # ///////////////////////////////////////////////////////////////////////////////////

    a = calcular_colisiones_movimiento(
        puntos_p)  # Acá se depura la lista con los puntos, los que presenten colisiones son eliminados

    return a


def calcular_marcas(unidad):
    """ Esta función calcula las posiciones en donde deben estar las marcas rojas según el ataque de la unidad
        y devuelve una lista con esta información """
    global marcas_p, b
    copia_unidad = unidad.copy()
    marcas_p = []
    if unidad in recursos.lista_de_unidades[1:5] or unidad in recursos.lista_de_unidades[6:10]:
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.y -= 100
        rect.x -= 100
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.y -= 100
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.y -= 100
        rect.x += 100
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.x -= 100
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.x += 100
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.y += 100
        rect.x -= 100
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.y += 100
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.y += 100
        rect.x += 100
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

    else:
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.x -= 300
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.x -= 200
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.x -= 200
        rect.y -= 200
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.x -= 100
        rect.y -= 100
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.y -= 300
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.y -= 200
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.x += 100
        rect.y -= 100
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.x += 200
        rect.y -= 200
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.x += 200
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.x += 300
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.x += 100
        rect.y += 100
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.x += 200
        rect.y += 200
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.y += 200
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.y += 300
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.x -= 200
        rect.y += 200
        marcas_p.append(rect)
        copia_unidad = unidad.copy()

        rect = copia_unidad
        rect.x -= 100
        rect.y += 100
        marcas_p.append(rect)
        copia_unidad = unidad.copy()
    a = calcular_colisiones_ataque(marcas_p)
    return a


def ataque(atacante, objetivo):
    """
    la funcion de ataque de las unidades
    """
    global vida, daño, a, o
    x = objetivo.x
    y = objetivo.y
    for i in range(len(recursos.lista_de_unidades)):
        if atacante == recursos.lista_de_unidades[i]:
            a = i
            if statusCheck[a][0] == 1:
                colmillosVampíricos(atacante)
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            o = i
    if atacante in recursos.lista_de_unidades and atacante != recursos.lista_de_unidades[3] and atacante != \
            recursos.lista_de_unidades[8] and atacante != recursos.lista_de_unidades[0] and atacante != \
            recursos.lista_de_unidades[5]:
        vida[o] = vida[o] - daño[a]
        if vida[o] <= 0:
            vida[o] = 0
    elif atacante is recursos.lista_de_unidades[0] or atacante is recursos.lista_de_unidades[5]:
        if random.randint(0, 99) < 20 or statusCheck[a][6] == 1:
            vida[o] = vida[o] - int(daño[a] * 1.5)
            statusCheck[a][6] = 0
            print('critico!!')
        else:
            vida[o] = vida[o] - daño[a]
        if vida[o] <= 0:
            vida[o] = 0

    elif atacante is recursos.lista_de_unidades[3]:
        for i in range(len(recursos.lista_de_unidades)):
            if objetivo == recursos.lista_de_unidades[i]:
                o = i
        vida[o] = vida[o] - daño[3]
        if vida[o] <= 0:
            vida[o] = 0
        if 0 < objetivo.x < 900 or 0 < objetivo.y < 900:
            if atacante.x > objetivo.x and atacante.y == objetivo.y:
                objetivo.x -= 100
            if atacante.x > objetivo.x and atacante.y > objetivo.y:
                objetivo.x -= 100
                objetivo.y -= 100
            if atacante.x == objetivo.x and atacante.y > objetivo.y:
                objetivo.y -= 100
            if atacante.x < objetivo.x and atacante.y > objetivo.y:
                objetivo.x += 100
                objetivo.y -= 100
            if atacante.x < objetivo.x and atacante.y == objetivo.y:
                objetivo.x += 100
            if atacante.x < objetivo.x and atacante.y < objetivo.y:
                objetivo.x += 100
                objetivo.y += 100
            if atacante.x == objetivo.x and atacante.y < objetivo.y:
                objetivo.y += 100
            if atacante.x > objetivo.x and atacante.y < objetivo.y:
                objetivo.x -= 100
                objetivo.y += 100
        for k in recursos.lista_de_unidades:
            if objetivo != k:
                if objetivo.collidepoint((k.x, k.y)):
                    objetivo.x = x
                    objetivo.y = y

    elif atacante is recursos.lista_de_unidades[8]:
        for i in range(len(recursos.lista_de_unidades)):
            if objetivo == recursos.lista_de_unidades[i]:
                o = i
        vida[o] = vida[o] - daño[8]
        if 0 < objetivo.x < 900 or 0 < objetivo.y < 900:
            if atacante.x > objetivo.x and atacante.y == objetivo.y:
                objetivo.x -= 100
            if atacante.x > objetivo.x and atacante.y > objetivo.y:
                objetivo.x -= 100
                objetivo.y -= 100
            if atacante.x == objetivo.x and atacante.y > objetivo.y:
                objetivo.y -= 100
            if atacante.x < objetivo.x and atacante.y > objetivo.y:
                objetivo.x += 100
                objetivo.y -= 100
            if atacante.x < objetivo.x and atacante.y == objetivo.y:
                objetivo.x += 100
            if atacante.x < objetivo.x and atacante.y < objetivo.y:
                objetivo.x += 100
                objetivo.y += 100
            if atacante.x == objetivo.x and atacante.y < objetivo.y:
                objetivo.y += 100
            if atacante.x > objetivo.x and atacante.y < objetivo.y:
                objetivo.x -= 100
                objetivo.y += 100
        for k in range(len(recursos.lista_de_unidades)):
            a = 1

    print(x, y)
    print(vida[o])
    return vida[o]


def curar(sanador, objetivo):
    """
    la funcion del sanador para curar
    """
    global vida, daño, a, o
    if sanador is recursos.lista_de_unidades[2]:
        a = daño[2]
        if statusCheck[2][6] == 1:
            a = a*2
            statusCheck[2][6] = 0
    elif sanador is recursos.lista_de_unidades[7]:
        a = daño[7]
        if statusCheck[7][6] == 1:
            a = a*2
            statusCheck[7][6] = 0
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            o = i
    if vida[o] > 0:
        if vida[o] < vida_maxima[o]:
            if statusCheck[o][1] > 0:
                vida[o] = vida[o] + int(a * 0.1)
            else:
                vida[o] = vida[o] + a
            if vida[o] > vida_maxima[o]:
                vida[o] = vida_maxima[o]
        print(vida[o])
        return vida[o]


def escudar(escudero, objetivo):
    """
    la funcion del escudero para escudar
    """
    global vida, daño, a, o
    if escudero is recursos.lista_de_unidades[1]:
        a = daño[1]
    elif escudero is recursos.lista_de_unidades[6]:
        a = daño[6]
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            o = i
    if vida[o] > 0:
        vida[o] = vida[o] + a
        print(vida[o])
        return vida[o]


def dibujar_puntos(lista_puntos):
    """
    Esta función recibe la lista con los rectángulos de los puntos y los dibuja
    """
    for rect in lista_puntos:
        recursos.pantalla.blit(recursos.punto_surf, rect)


def dibujar_marcas(lista_marcas, lista2):
    """
    Esta función recibe la lista con los rectángulos de las marcas y las dibuja
    """
    for rect in lista_marcas:
        recursos.pantalla.blit(recursos.marca_surf, rect)
    for l in lista2:
        recursos.pantalla.blit(recursos.dot_surf, l)


def calcular_colision_posicionamiento(unidad, turno):
    """
    Esta función retorna False si la unidad comparte posición con alguna otra unidad
    """

    for i in range(len(recursos.lista_de_unidades)):

        if i == turno:  # Se salta la posición de su unidad propia
            continue
        elif recursos.lista_de_unidades[i] == unidad:
            return False

    return True


## Funciones de items
## las funciones restringen el uso del item y retorna True si se uso correctamente, de lo contrario retorna False
## varias de las funciones solamente cambian el estado de la unidad en la matriz statuscheck
## posteriormente este estado se revisa en las otras funciones y se hacen los cambios correspondientes
def cristal(objetivo):
    """
    la funcion del item "cristal"
    """
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            if ((recursos.turno_jugador == 1 and i < 5) or (recursos.turno_jugador == 2 and i > 4)):
                if vida[i] > 0:
                    if vida[i] < vida_maxima[i]:
                        if statusCheck[i][1] > 0:
                            vida[i] = vida[i] + 10
                        else:
                            vida[i] = vida[i] + 100
                        if vida[i] > vida_maxima[i]:
                            vida[i] = vida_maxima[i]
                    return True
            return False


def bayaExplosiva(objetivo):
    """
    funcion de el item "baya explosiva"
    """
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            if ((recursos.turno_jugador == 2 and i < 5) or (recursos.turno_jugador == 1 and i > 4)):
                if vida[i] > 0:
                    vida[i] = vida[i] - 100
                    if vida[i] < 0:
                        vida[i] = 0
                    return True
            return False


def custodia(objetivo):
    """
    funcion de el item "custodia"
    """
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            if ((recursos.turno_jugador == 1 and i < 5) or (recursos.turno_jugador == 2 and i > 4)):
                if vida[i] != 0:
                    vida[i] = vida[i] + 75
                return True
            return False


def ultimoAliento(objetivo):
    """
    funcion de el item "ultimo aliento"
    """
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_lapidas[i]:
            print(1, i, recursos.turno_jugador)
            if (recursos.turno_jugador == 1 and i < 5) or (recursos.turno_jugador == 2 and i > 4):
                recursos.lista_de_unidades[i].x = recursos.lista_de_lapidas[i].x
                recursos.lista_de_unidades[i].y = recursos.lista_de_lapidas[i].y
                vida[i] = vida_maxima[i] // 10
                recursos.lista_de_lapidas[i].x = -200
                recursos.lista_de_lapidas[i].y = 0
                print(recursos.lista_de_unidades[i].x, recursos.lista_de_unidades[i].y, vida[i])
                return True
        return False

def daga(objetivo):
    """
    funcion de el item "daga"
    """
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            if ((recursos.turno_jugador == 1 and i < 5) or (recursos.turno_jugador == 2 and i > 4)):
                daño[i] += int(daño[i] * 0.25)
                statusCheck[i][2] = 4
                return True
            return False


def colmillosVampíricos(objetivo):
    """
    funcion de el item "colmillos vampiricos"
    esta funcion verifica si el estado de la funcion es 1 para usarse, si es 0, lo pone en 1 (statuscheck)
    """
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            if ((recursos.turno_jugador == 1 and i < 5) or (recursos.turno_jugador == 2 and i > 4)):
                if statusCheck[i][0] == 0:
                    statusCheck[i][0] = 1
                elif statusCheck[i][0] == 1:
                    if statusCheck[i][1] > 0:
                        vida[i] += int(daño[i] * 0.3 * 0.1)
                    else:
                        vida[i] += int(daño[i] * 0.3)
                    if vida[i] > vida_maxima[i]:
                        vida[i] = vida_maxima[i]
                    statusCheck[i][0] = 0
                return True
            return False


def alientoPeste(objetivo):
    """
    funcion del item "aliento de peste"
    """
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            if ((recursos.turno_jugador == 2 and i < 5) or (recursos.turno_jugador == 1 and i > 4)):
                statusCheck[i][1] = 6
                return True
            return False


def botas(objetivo):
    """
    funcion del item "botas"
    """
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            if ((recursos.turno_jugador == 1 and i < 5) or (recursos.turno_jugador == 2 and i > 4)):
                if statusCheck[i][3] == 0:
                    statusCheck[i][3] = 1
                return True
            return False


def frenesi(objetivo):
    """
    funcion del item "frenesi"
    """
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            if ((recursos.turno_jugador == 1 and i < 5) or (recursos.turno_jugador == 2 and i > 4)):
                if statusCheck[i][4] == 0:
                    statusCheck[i][4] = 1
                return True
            return False


def represion(objetivo):
    """
    funcion del item "represion"
    """
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            if ((recursos.turno_jugador == 2 and i < 5) or (recursos.turno_jugador == 1 and i > 4)):
                if statusCheck[i][5] == 0:
                    statusCheck[i][5] = 2
                return True
            return False

def bendicionCelestial(objetivo):
    """
    funcion del item "bendicion celestial"
    """
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            if ((recursos.turno_jugador == 1 and i == 2) or (recursos.turno_jugador == 2 and i == 7)):
                if statusCheck[i][6] == 0:
                    statusCheck[i][6] = 1
                return True
            return False

def cargar(objetivo):
    """
    funcion del item "cargar"
    """
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            if ((recursos.turno_jugador == 1 and i == 3) or (recursos.turno_jugador == 2 and i == 8)):
                if vida[i] != 0:
                    vida[i] = vida[i] + 500
                return True
            return False

def punteria(objetivo):
    """
    funcion del item "punteria"
    """
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            if ((recursos.turno_jugador == 1 and i == 0) or (recursos.turno_jugador == 2 and i == 5)):
                if statusCheck[i][6] == 0:
                    statusCheck[i][6] = 1
                return True
            return False
def mandatoCelestial(objetivo):
    """
    funcion del item "mandato celestial"
    esta funcion verifica las posiciones de las unidades aliadas cercanas al objetivo y les da escudo
    """
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            if recursos.turno_jugador == 1 and i == 1:
                for j in range(5):
                    if ((abs(recursos.lista_de_unidades[j].x - recursos.lista_de_unidades[i].x) <= 100)
                            and (abs(recursos.lista_de_unidades[j].y - recursos.lista_de_unidades[i].y) <= 100)):
                        if vida[j] > 0:
                            vida[j] += 200
                return True
            elif recursos.turno_jugador == 2 and i == 6:
                for j in range(5, 10):
                    if ((abs(recursos.lista_de_unidades[j].x - recursos.lista_de_unidades[i].x) <= 100)
                            and (abs(recursos.lista_de_unidades[j].y - recursos.lista_de_unidades[i].y) <= 100)):
                        if vida[j] > 0:
                            vida[j] += 200
                return True
            return False

def gritoDraconico(objetivo):
    """
    funcion del item "grito dragonico"
    """
    for i in range(len(recursos.lista_de_unidades)):
        if objetivo == recursos.lista_de_unidades[i]:
            if ((recursos.turno_jugador == 1 and i == 4) or (recursos.turno_jugador == 2 and i == 9)):
                if statusCheck[i][6] == 0:
                    statusCheck[i][6] = 6
                    daño[i] += 200
                    vida[i] += 300
                return True
            return False

def checkStatus():
    """
    esta funcion revisa el estado de varias de las otras funciones de items (de la matriz statuscheck)
    y hace diferentes ajustes a la unidad y al estado, se usa al final de cada turno
    """
    global statusCheck
    for i in range(10):
        if statusCheck[i][1] > 0:
            statusCheck[i][1] -= 1
        if statusCheck[i][2] > 0:
            statusCheck[i][2] -= 1
            if statusCheck[i][2] == 0:
                daño[i] -= int(daño[i] * 25 / 125)
    x = [4, 9]
    for i in x:
        if statusCheck[i][6] > 0:
            statusCheck[i][6] -= 1
            vida[i] += 50
            if statusCheck[i][6] == 0:
                daño[i] -= 200
                if vida[i] >= vida_maxima[i]:
                    vida[i] = vida_maxima[i]

def useItem(turno, tf, z):
    """
    esta funcion verifica si el item se uso correctamente (segun si la funcion del item retorno True o False)
    si se utilizo correctamente lo elimina de la lista de items del jugador
    """
    if tf:
        if turno == 1:
            n = recursos.itemsEquipados1.index(z)
            recursos.itemsEquipados1.pop(n)
            recursos.items1.pop(n)
            recursos.accept_sfx.play()
        elif turno == 2:
            n = recursos.itemsEquipados2.index(z)
            recursos.itemsEquipados2.pop(n)
            recursos.items2.pop(n)
            recursos.accept_sfx.play()
    else:
        recursos.error_sfx.play()

def dibujar_inv(turno):
    """
    dibuja el inventario en pantalla
    """
    recursos.pantalla.blit(recursos.inv_grid, (200, 400))
    if turno == 1:
        for i, j in zip(recursos.items1, recursos.pitems1):
            recursos.pantalla.blit(i, (j[0], j[1]))
    if turno == 2:
        for i, j in zip(recursos.items2, recursos.pitems2):
            recursos.pantalla.blit(i, (j[0], j[1]))
