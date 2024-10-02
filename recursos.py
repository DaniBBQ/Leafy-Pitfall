import pygame
import random
pygame.init()
pygame.mixer.init()
# Determina de quien es el turno
turno_jugador = 1
# Contador: Mantiene registro de las acciones realizadas por la unidad en este turno
# 0 = No ha realizado ninguna acción | 1 = Esta unidad ya se ha movido | 2 = Esta unidad ya ha atacado
accion_unidad = 0
# Determina el numero de rondas que han pasado, esto se toma de referencia para el reparto de items
ronda = 0

# Determina si se clickeo una unidad para moverse
moverse = False

# Determina si se clickeo una unidad para atacar
ataque = False

# Determina si una unidad ya está seleccionada
turno_activo = False

# Determina la fase del juego  0 = tuto, 1 = menu, 2 = posicionamiento, 3 = combate
fase_de_juego = 1
# Turnos de unidades
turnos_unidades = 0

# tamaño de la pantalla
tamaño_pantalla = 1000
pantalla = pygame.display.set_mode((tamaño_pantalla, tamaño_pantalla))

# Tamaño de cada cuadrado del tablero
tamaño_cuadrado = tamaño_pantalla // 10

# colores
verde, agua = (42, 195, 27), (59, 255, 172)
rojo_oscuro, rojo_claro = (172, 50, 50), (217, 87, 99)

# imagen y switch del inventario
inv_grid = pygame.transform.scale(pygame.image.load("Sprites/UI/inv_grid.png").convert_alpha(),
                                  (600,200))
inv_on = False
# aca se cargan las imagenes de los items y su "id" para poder usarse en las funciones
bayaExplosiva_ = (pygame.transform.scale(pygame.image.load("Sprites/items/berry.png").convert_alpha(),
                                         (tamaño_cuadrado * 2, tamaño_cuadrado * 2)), 1)
ultimoAliento_ = (pygame.transform.scale(pygame.image.load("Sprites/items/lastbreath.png").convert_alpha(),
                                         (tamaño_cuadrado * 2, tamaño_cuadrado * 2)), 2)
custodia_ = [pygame.transform.scale(pygame.image.load("Sprites/items/custodia.png").convert_alpha(),
                                    (tamaño_cuadrado * 2, tamaño_cuadrado * 2)), 3]
cristal_ = (pygame.transform.scale(pygame.image.load("Sprites/items/cristal.png").convert_alpha(),
                                   (tamaño_cuadrado * 2, tamaño_cuadrado * 2)), 4)
daga_ = (pygame.transform.scale(pygame.image.load("Sprites/items/daga.png").convert_alpha(),
                                   (tamaño_cuadrado * 2, tamaño_cuadrado * 2)), 5)
colmillosVampíricos_ = (pygame.transform.scale(pygame.image.load("Sprites/items/fangs.png").convert_alpha(),
                                   (tamaño_cuadrado * 2, tamaño_cuadrado * 2)), 6)
alientoPeste_ = (pygame.transform.scale(pygame.image.load("Sprites/items/alientodepeste.png").convert_alpha(),
                                   (tamaño_cuadrado * 2, tamaño_cuadrado * 2)), 7)
botas_ = (pygame.transform.scale(pygame.image.load("Sprites/items/boots.png").convert_alpha(),
                                   (tamaño_cuadrado * 2, tamaño_cuadrado * 2)), 8)
frenesi_ = (pygame.transform.scale(pygame.image.load("Sprites/items/frenesi.png").convert_alpha(),
                                   (tamaño_cuadrado * 2, tamaño_cuadrado * 2)), 9)
represion_ = (pygame.transform.scale(pygame.image.load("Sprites/items/represion.png").convert_alpha(),
                                   (tamaño_cuadrado * 2, tamaño_cuadrado * 2)), 10)
bendicionCelestial_ = (pygame.transform.scale(pygame.image.load("Sprites/items/bend.png").convert_alpha(),
                                   (tamaño_cuadrado * 2, tamaño_cuadrado * 2)), 11)
cargar_ = (pygame.transform.scale(pygame.image.load("Sprites/items/enrage.png").convert_alpha(),
                                   (tamaño_cuadrado * 2, tamaño_cuadrado * 2)), 12)
punteria_ = (pygame.transform.scale(pygame.image.load("Sprites/items/aim.png").convert_alpha(),
                                   (tamaño_cuadrado * 2, tamaño_cuadrado * 2)), 13)
mandatoCelestial_ = (pygame.transform.scale(pygame.image.load("Sprites/items/mand.png").convert_alpha(),
                                   (tamaño_cuadrado * 2, tamaño_cuadrado * 2)), 14)
gritoDraconico_ = (pygame.transform.scale(pygame.image.load("Sprites/items/steelwill.png").convert_alpha(),
                                   (tamaño_cuadrado * 2, tamaño_cuadrado * 2)), 15)
items_lista = [ultimoAliento_, custodia_, bayaExplosiva_, cristal_, daga_,
               colmillosVampíricos_, alientoPeste_, botas_, frenesi_, represion_,
               bendicionCelestial_, cargar_, punteria_, mandatoCelestial_, gritoDraconico_]

accept_sfx = pygame.mixer.Sound("SFX/accept_sfx.mp3")
error_sfx = pygame.mixer.Sound("SFX/error_sfx.mp3")
# variables de los items
items1 = []
items2 = []
pitems1 = []
pitems2 = []
itemsEquipados1 = []
itemsEquipados2 = []
recitems1 = []
recitems2 = []
itemselect = True
probabilidad = [0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625,
                0.15, 0.15, 0.04, 0.04, 0.04, 0.04, 0.04] #los items tienen diferentes probabilidades de salir
itemsUsados1 = []# algunos items solo pueden salir 1 vez por jugador
itemsUsados2 = []
def asignarItem1():
    """
    funcion que asigna un item por uso (sin pasarse de 3) al jugador 1 siguiendo una serie de restricciones
    """
    x = True
    while x and len(items1) < 3:
        i = random.choices(items_lista, weights=probabilidad)[0]
        if i[1] in itemsEquipados1 or i[1] in itemsUsados1:
            continue
        if (i[1]>10 or i[1] == 2 or i[1] == 7) and i[1] not in itemsUsados1: # aca se restringen los items que solo se pueden usar 1 vez
            itemsUsados1.append(i[1])
        items1.append(i[0])
        itemsEquipados1.append(i[1])
        x = False
        print(itemsEquipados1, itemsEquipados2)
        print(itemsUsados2, itemsUsados1)
def asignarItem2():
    """
    funcion que asigna un item por uso (sin pasarse de 3) al jugador 2 siguiendo una serie de restricciones
    """
    x = True
    while x and len(items2) < 3:
        i = random.choices(items_lista, weights=probabilidad)[0]
        if i[1] in itemsEquipados2 or i[1] in itemsUsados2:
            continue
        if (i[1]>10 or i[1] == 2 or i[1] == 7) and i[1] not in itemsUsados2:
            itemsUsados2.append(i[1])
        items2.append(i[0])
        itemsEquipados2.append(i[1])
        x = False
        print(itemsEquipados1, itemsEquipados2)
        print(itemsUsados2, itemsUsados1)

def pintarItems():
    """
    esta funcion acomoda automaticamente los rectangulos de los items en el inventario
    """
    pitems1.clear()
    recitems1.clear()
    pitems2.clear()
    recitems2.clear()
    for it in range(len(items1)):
        pitems1.append([200 * (it + 1), 400])
        recitems1.append(items1[it].get_rect(topleft=(pitems1[it][0], pitems1[it][1])))
    for it in range(len(items2)):
        pitems2.append([200 * (it + 1), 400])
        recitems2.append(items2[it].get_rect(topleft=(pitems2[it][0], pitems2[it][1])))
# posición inicial del cazador en la matriz del tablero e imagen del cazador 1

posicion_cazador1 = [12, 12]

cazador1_surf = pygame.image.load('Sprites/Tropas/hunter1.png').convert_alpha()
cazador1_surf = pygame.transform.scale(cazador1_surf, (tamaño_cuadrado, tamaño_cuadrado))
cazador1_rect = cazador1_surf.get_rect(
    topleft=(posicion_cazador1[1] * tamaño_cuadrado, posicion_cazador1[0] * tamaño_cuadrado))

# Estadisticas base del cazador
cazador1_estadisticas = [750, 225,
                         125]  # l[0] = Vida | l[1] = Ataque a larga distancia | l[2] = Ataque a corta distancia

# imagen del escudero y posición inicial
posicion_escudero1 = [12, 12]

escudero1_surf = pygame.image.load('Sprites/Tropas/squire1.png').convert_alpha()
escudero1_surf = pygame.transform.scale(escudero1_surf, (tamaño_cuadrado, tamaño_cuadrado))
escudero1_rect = escudero1_surf.get_rect(
    topleft=(posicion_escudero1[1] * tamaño_cuadrado, posicion_escudero1[0] * tamaño_cuadrado))

# Estadisticas base del escudero

escudero1_estadisticas = [1200, 150]  # l[0] = Vida | l[1] = Vida bonus del escudo que aplica a un aliado

# imagen del sanador y posición inicial

posicion_sanador1 = [12, 12]

sanador1_surf = pygame.image.load('Sprites/Tropas/healer1.png').convert_alpha()
sanador1_surf = pygame.transform.scale(sanador1_surf, (tamaño_cuadrado, tamaño_cuadrado))
sanador1_rect = sanador1_surf.get_rect(
    topleft=(posicion_sanador1[1] * tamaño_cuadrado, posicion_sanador1[0] * tamaño_cuadrado))

# Estadisticas base del sanador

sanador1_estadisticas = [800, 200]  # l[0] = Vida | l[1] = Cantidad de vida que cura a un aliado

# imagen del oso y posición inicial

posicion_oso1 = [12, 12]

oso1_surf = pygame.image.load('Sprites/Tropas/bear1.png').convert_alpha()
oso1_surf = pygame.transform.scale(oso1_surf, (tamaño_cuadrado, tamaño_cuadrado))
oso1_rect = oso1_surf.get_rect(
    topleft=(posicion_oso1[1] * tamaño_cuadrado, posicion_oso1[0] * tamaño_cuadrado))

# Estadisticas base del oso

oso1_estadisticas = [1050, 50]  # l[0] = Vida | l[1] = Ataque

# imagen del caballero y posición inicial
posicion_caballero1 = [12, 12]

caballero1_surf = pygame.image.load('Sprites/Tropas/knight1.png').convert_alpha()
caballero1_surf = pygame.transform.scale(caballero1_surf, (tamaño_cuadrado, tamaño_cuadrado))
caballero1_rect = caballero1_surf.get_rect(
    topleft=(posicion_caballero1[1] * tamaño_cuadrado, posicion_caballero1[0] * tamaño_cuadrado))

# Estadisticas base del caballero

caballero1_estadisticas = [900, 100]  # l[0] = Vida | l[1] = Ataque

# imagen del cazador y posición inicial
posicion_cazador2 = [12, 12]

cazador2_surf = pygame.image.load('Sprites/Tropas/hunter2.png').convert_alpha()
cazador2_surf = pygame.transform.scale(cazador2_surf, (tamaño_cuadrado, tamaño_cuadrado))
cazador2_rect = cazador2_surf.get_rect(
    topleft=(posicion_cazador2[1] * tamaño_cuadrado, posicion_cazador2[0] * tamaño_cuadrado))

# Estadisticas base del cazador

cazador2_estadisticas = [750, 225,
                         125]  # l[0] = Vida | l[1] = Ataque a larga distancia | l[2] = Ataque a corta distancia

# imagen del escudero y posición inicial

posicion_escudero2 = [12, 12]

escudero2_surf = pygame.image.load('Sprites/Tropas/squire2.png').convert_alpha()
escudero2_surf = pygame.transform.scale(escudero2_surf, (tamaño_cuadrado, tamaño_cuadrado))
escudero2_rect = escudero2_surf.get_rect(
    topleft=(posicion_escudero2[1] * tamaño_cuadrado, posicion_escudero2[0] * tamaño_cuadrado))

# Estadisticas base del escudero

escudero2_estadisticas = [1200, 150]  # l[0] = Vida | l[1] = Vida bonus del escudo que aplica a un aliado

# imagen del sanador y posición inicial
posicion_sanador2 = [12, 12]

sanador2_surf = pygame.image.load('Sprites/Tropas/healer2.png').convert_alpha()
sanador2_surf = pygame.transform.scale(sanador2_surf, (tamaño_cuadrado, tamaño_cuadrado))
sanador2_rect = sanador2_surf.get_rect(
    topleft=(posicion_sanador2[1] * tamaño_cuadrado, posicion_sanador2[0] * tamaño_cuadrado))

# Estadisticas base del sanador

sanador2_estadisticas = [800, 200]  # l[0] = Vida | l[1] = Cantidad de vida que cura a un aliado

# imagen del oso y posición inicial
posicion_oso2 = [12, 12]

oso2_surf = pygame.image.load('Sprites/Tropas/bear2.png').convert_alpha()
oso2_surf = pygame.transform.scale(oso2_surf, (tamaño_cuadrado, tamaño_cuadrado))
oso2_rect = oso2_surf.get_rect(
    topleft=(posicion_oso2[1] * tamaño_cuadrado, posicion_oso2[0] * tamaño_cuadrado))

# Estadisticas base del oso

oso2_estadisticas = [1050, 50]  # l[0] = Vida | l[1] = Ataque

# imagen del caballero y posición inicial
posicion_caballero2 = [12, 12]

caballero2_surf = pygame.image.load('Sprites/Tropas/knight2.png').convert_alpha()
caballero2_surf = pygame.transform.scale(caballero2_surf, (tamaño_cuadrado, tamaño_cuadrado))
caballero2_rect = caballero2_surf.get_rect(
    topleft=(posicion_caballero2[1] * tamaño_cuadrado, posicion_caballero2[0] * tamaño_cuadrado))

# Estadisticas base del caballero

caballero2_estadisticas = [900, 100]  # l[0] = Vida | l[1] = Ataque

# lista con el rectángulo de las unidades
lista_de_unidades = [cazador1_rect, escudero1_rect, sanador1_rect, oso1_rect, caballero1_rect, cazador2_rect,
                     escudero2_rect, sanador2_rect, oso2_rect, caballero2_rect]

equipo1_rect = []  # Rectangulos del equipo 1 (se toman de la lista_de_unidades, van desde l[0] hasta l[4] incluyendo este ultimo)
equipo2_rect = []  # Rectangulos del equipo 2 (se toman de la lista_de_unidades, van desde l[5] hasta l[9] incluyendo este ultimo)

# Separa los rectangulos de las unidades por equipos para referenciarlos más especificamente
for i in range(len(lista_de_unidades) - 5):
    equipo1_rect.append(lista_de_unidades[i])
for i in range(5, len(lista_de_unidades)):
    equipo2_rect.append(lista_de_unidades[i])

# Lista con las estadisticas de cada unidad
lista_estadisticas_de_unidades = [cazador1_estadisticas, escudero1_estadisticas, sanador1_estadisticas,
                                  oso1_estadisticas, caballero1_estadisticas, cazador2_estadisticas,
                                  escudero2_estadisticas, sanador2_estadisticas, oso2_estadisticas,
                                  caballero2_estadisticas]

equipo1_estadisticas = []  # Estadisticas del equipo 1 (se toman de la lista_estadisticas_de_unidades, van desde l[0] hasta l[4] incluyendo este ultimo)
equipo2_estadisticas = []  # Estadisticas del equipo 2 (se toman de la lista_estadisticas_de_unidades, van desde l[5] hasta l[9] incluyendo este ultimo)

# Separa las estadisticas de las unidades por equipos para referenciarlos más especificamente
for i in range(len(lista_estadisticas_de_unidades) - 5):
    equipo1_estadisticas.append(lista_estadisticas_de_unidades[i])
for i in range(5, len(lista_estadisticas_de_unidades)):
    equipo2_estadisticas.append(lista_estadisticas_de_unidades[i])

# Vida de cada unidad
vidas = []

for i in range(len(equipo1_estadisticas)):
    vidas.append(equipo1_estadisticas[i][0])
for i in range(len(equipo2_estadisticas)):
    vidas.append(equipo2_estadisticas[i][0])

# Daño de cada unidad
daños = []

for i in range(len(equipo1_estadisticas)):
    daños.append(equipo1_estadisticas[i][1])
for i in range(len(equipo2_estadisticas)):
    daños.append(equipo2_estadisticas[i][1])

# Imagen de los puntos a los que se puede mover la unidad
punto_surf = pygame.image.load('Sprites/UI/punto.png').convert_alpha()
punto_surf = pygame.transform.scale(punto_surf, (tamaño_cuadrado, tamaño_cuadrado))

# Imagen de los puntos a los que no puede atacar la unidad
dot_surf = pygame.image.load('Sprites/UI/dot.png').convert_alpha()
dot_surf = pygame.transform.scale(dot_surf, (tamaño_cuadrado, tamaño_cuadrado))

# Imagen de las marcas a las que la unidad puede atacar
marca_surf = pygame.image.load("Sprites/UI/marca.png").convert_alpha()
marca_surf = pygame.transform.scale(marca_surf, (tamaño_cuadrado, tamaño_cuadrado))

# Imagen de calavera
skull_surf = pygame.image.load("Sprites/UI/skull.png").convert_alpha()
skull_surf = pygame.transform.scale(skull_surf, (tamaño_cuadrado, tamaño_cuadrado))
menubg = pygame.image.load("Sprites/UI/menuscreen.png").convert_alpha()
menubg = pygame.transform.scale(menubg, (1000, 1000))
menu_rect = menubg.get_rect(topleft=(0,0))
# Imagen del botón start
start_img = pygame.image.load("Sprites/UI/start_button.png").convert_alpha()
start_img = pygame.transform.scale(start_img, (200, 100))
start_rect = start_img.get_rect(topleft=(400, 300))
# Imagen del botón exit
exit_img = pygame.image.load("Sprites/UI/exit_button.png").convert_alpha()
exit_img = pygame.transform.scale(exit_img, (200, 100))
exit_rect = exit_img.get_rect(topleft=(400, 500))
# Se activa temporalmente mientras se mueve un personaje
moviendose = False

lapida1_surf = pygame.image.load('Sprites/Tropas/rip.png').convert_alpha()
lapida1_surf = pygame.transform.scale(lapida1_surf, (tamaño_cuadrado, tamaño_cuadrado))
lapida1_rect = lapida1_surf.get_rect(
    topleft=(posicion_sanador1[1] * tamaño_cuadrado, posicion_sanador1[0] * tamaño_cuadrado))

lapida2_surf = pygame.image.load('Sprites/Tropas/rip.png').convert_alpha()
lapida2_surf = pygame.transform.scale(lapida2_surf, (tamaño_cuadrado, tamaño_cuadrado))
lapida2_rect = lapida2_surf.get_rect(
    topleft=(posicion_sanador1[1] * tamaño_cuadrado, posicion_sanador1[0] * tamaño_cuadrado))

lapida3_surf = pygame.image.load('Sprites/Tropas/rip.png').convert_alpha()
lapida3_surf = pygame.transform.scale(lapida3_surf, (tamaño_cuadrado, tamaño_cuadrado))
lapida3_rect = lapida3_surf.get_rect(
    topleft=(posicion_sanador1[1] * tamaño_cuadrado, posicion_sanador1[0] * tamaño_cuadrado))

lapida4_surf = pygame.image.load('Sprites/Tropas/rip.png').convert_alpha()
lapida4_surf = pygame.transform.scale(lapida4_surf, (tamaño_cuadrado, tamaño_cuadrado))
lapida4_rect = lapida4_surf.get_rect(
    topleft=(posicion_sanador1[1] * tamaño_cuadrado, posicion_sanador1[0] * tamaño_cuadrado))

lapida5_surf = pygame.image.load('Sprites/Tropas/rip.png').convert_alpha()
lapida5_surf = pygame.transform.scale(lapida5_surf, (tamaño_cuadrado, tamaño_cuadrado))
lapida5_rect = lapida5_surf.get_rect(
    topleft=(posicion_sanador1[1] * tamaño_cuadrado, posicion_sanador1[0] * tamaño_cuadrado))

lapida6_surf = pygame.image.load('Sprites/Tropas/rip.png').convert_alpha()
lapida6_surf = pygame.transform.scale(lapida6_surf, (tamaño_cuadrado, tamaño_cuadrado))
lapida6_rect = lapida6_surf.get_rect(
    topleft=(posicion_sanador1[1] * tamaño_cuadrado, posicion_sanador1[0] * tamaño_cuadrado))

lapida7_surf = pygame.image.load('Sprites/Tropas/rip.png').convert_alpha()
lapida7_surf = pygame.transform.scale(lapida7_surf, (tamaño_cuadrado, tamaño_cuadrado))
lapida7_rect = lapida7_surf.get_rect(
    topleft=(posicion_sanador1[1] * tamaño_cuadrado, posicion_sanador1[0] * tamaño_cuadrado))

lapida8_surf = pygame.image.load('Sprites/Tropas/rip.png').convert_alpha()
lapida8_surf = pygame.transform.scale(lapida8_surf, (tamaño_cuadrado, tamaño_cuadrado))
lapida8_rect = lapida8_surf.get_rect(
    topleft=(posicion_sanador1[1] * tamaño_cuadrado, posicion_sanador1[0] * tamaño_cuadrado))

lapida9_surf = pygame.image.load('Sprites/Tropas/rip.png').convert_alpha()
lapida9_surf = pygame.transform.scale(lapida9_surf, (tamaño_cuadrado, tamaño_cuadrado))
lapida9_rect = lapida9_surf.get_rect(
    topleft=(posicion_sanador1[1] * tamaño_cuadrado, posicion_sanador1[0] * tamaño_cuadrado))

lapida10_surf = pygame.image.load('Sprites/Tropas/rip.png').convert_alpha()
lapida10_surf = pygame.transform.scale(lapida10_surf, (tamaño_cuadrado, tamaño_cuadrado))
lapida10_rect = lapida10_surf.get_rect(
    topleft=(posicion_sanador1[1] * tamaño_cuadrado, posicion_sanador1[0] * tamaño_cuadrado))

lista_de_lapidas = [lapida1_rect, lapida2_rect, lapida3_rect, lapida4_rect, lapida5_rect, lapida6_rect, lapida7_rect,
                    lapida8_rect, lapida9_rect, lapida10_rect]

tuto_img = pygame.image.load("Sprites/UI/tuto_button.png").convert_alpha()
tuto_img = pygame.transform.scale(tuto_img, (200, 100))
tuto_rect = tuto_img.get_rect(topleft=(400, 400))
back_img = pygame.image.load("Sprites/UI/back_button.png").convert_alpha()
back_img = pygame.transform.scale(back_img, (200, 100))
back_rect = back_img.get_rect(topleft=(30, 870))

lista_de_botones = [start_rect, 1, 2, exit_rect]
