import pygame
from pygame.locals import *
import funciones
import recursos

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Leafy Pitfall")
clock = pygame.time.Clock()
turnos_de_unidades = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
muertos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fuente_de_texto = pygame.font.SysFont("Arial", 22)
fuente_de_texto_turno = pygame.font.SysFont("Arial", 50)
item_name_font = pygame.font.SysFont("Arial", 35)
item_name_desc = pygame.font.SysFont("Arial", 25)
bear_sfx = pygame.mixer.Sound("SFX/bear_sfx.mp3")
bow_sfx = pygame.mixer.Sound("SFX/bow_sfx.mp3")
crit_sfx = pygame.mixer.Sound("SFX/crit_sfx.mp3")
heal_sfx = pygame.mixer.Sound("SFX/heal_sfx.mp3")
shield_sfx = pygame.mixer.Sound("SFX/shield_sfx.mp3")
sword_sfx = pygame.mixer.Sound("SFX/sword_sfx.mp3")
button_sfx = pygame.mixer.Sound("SFX/button_sfx.mp3")
steps_sfx = pygame.mixer.Sound("SFX/steps_sfx.mp3")
bear_die_sfx = pygame.mixer.Sound("SFX/bear_die_sfx.mp3")
death_sfx = pygame.mixer.Sound("SFX/death_sfx.mp3")
healer_die_sfx = pygame.mixer.Sound("SFX/healer_die_sfx.mp3")
pygame.mixer.music.load("SFX/bg_song.wav")
pygame.mixer.music.set_volume(0.04)
pygame.mixer.music.play()
#tablero matriz vacia
def dibujar_tablero():
    #dibujar el tablero y las unidades

    if recursos.fase_de_juego == 0:
        recursos.pantalla.blit(recursos.menubg,recursos.menu_rect)
        recursos.pantalla.blit(recursos.back_img,recursos.back_rect)
    if recursos.fase_de_juego == 1:
        recursos.pantalla.blit(recursos.menubg,recursos.menu_rect)
        recursos.pantalla.blit(recursos.start_img,recursos.start_rect)
        recursos.pantalla.blit(recursos.exit_img,recursos.exit_rect)
    if recursos.fase_de_juego == 2:
        for fila in range(10):
            for columna in range(10):

                if recursos.turnos_unidades < 5:  #Subrayar en rojo los espacios prohibidos para el primer ejército
                    if (fila + columna) % 2 == 0 and columna > 3:
                        color = recursos.rojo_oscuro
                    elif (fila + columna) % 2 != 0 and columna > 3:
                        color = recursos.rojo_claro
                    elif (fila + columna) % 2 == 0:
                        color = recursos.verde
                    else:
                        color = recursos.agua
                else:  #Subrayar en rojo los espacios prohibidos para el segundo ejército
                    if (fila + columna) % 2 == 0 and columna < 6:
                        color = recursos.rojo_oscuro
                    elif (fila + columna) % 2 != 0 and columna < 6:
                        color = recursos.rojo_claro
                    elif (fila + columna) % 2 == 0:
                        color = recursos.verde
                    else:
                        color = recursos.agua
                pygame.draw.rect(recursos.pantalla, color,
                                 pygame.Rect(columna * recursos.tamaño_cuadrado, fila * recursos.tamaño_cuadrado,
                                             recursos.tamaño_cuadrado,
                                             recursos.tamaño_cuadrado))

    elif recursos.fase_de_juego == 3:
        for fila in range(10):
            for columna in range(10):
                if (fila + columna) % 2 == 0:
                    color = recursos.verde
                else:
                    color = recursos.agua
                pygame.draw.rect(recursos.pantalla, color,
                                 pygame.Rect(columna * recursos.tamaño_cuadrado, fila * recursos.tamaño_cuadrado,
                                             recursos.tamaño_cuadrado,
                                             recursos.tamaño_cuadrado))

    recursos.pantalla.blit(recursos.cazador1_surf, recursos.lista_de_unidades[0])
    recursos.pantalla.blit(recursos.escudero1_surf, recursos.lista_de_unidades[1])
    recursos.pantalla.blit(recursos.sanador1_surf, recursos.lista_de_unidades[2])
    recursos.pantalla.blit(recursos.oso1_surf, recursos.lista_de_unidades[3])
    recursos.pantalla.blit(recursos.caballero1_surf, recursos.lista_de_unidades[4])
    recursos.pantalla.blit(recursos.cazador2_surf, recursos.lista_de_unidades[5])
    recursos.pantalla.blit(recursos.escudero2_surf, recursos.lista_de_unidades[6])
    recursos.pantalla.blit(recursos.sanador2_surf, recursos.lista_de_unidades[7])
    recursos.pantalla.blit(recursos.oso2_surf, recursos.lista_de_unidades[8])
    recursos.pantalla.blit(recursos.caballero2_surf, recursos.lista_de_unidades[9])
    recursos.pantalla.blit(recursos.lapida1_surf, recursos.lista_de_lapidas[0])
    recursos.pantalla.blit(recursos.lapida2_surf, recursos.lista_de_lapidas[1])
    recursos.pantalla.blit(recursos.lapida3_surf, recursos.lista_de_lapidas[2])
    recursos.pantalla.blit(recursos.lapida4_surf, recursos.lista_de_lapidas[3])
    recursos.pantalla.blit(recursos.lapida5_surf, recursos.lista_de_lapidas[4])
    recursos.pantalla.blit(recursos.lapida6_surf, recursos.lista_de_lapidas[5])
    recursos.pantalla.blit(recursos.lapida7_surf, recursos.lista_de_lapidas[6])
    recursos.pantalla.blit(recursos.lapida8_surf, recursos.lista_de_lapidas[7])
    recursos.pantalla.blit(recursos.lapida9_surf, recursos.lista_de_lapidas[8])
    recursos.pantalla.blit(recursos.lapida10_surf, recursos.lista_de_lapidas[9])

    if recursos.fase_de_juego == 3:
        for b in range(len(recursos.lista_de_unidades)):
            if recursos.lista_de_unidades[b].collidepoint(mouse_pos):
                xtexto = recursos.lista_de_unidades[b].x
                ytexto = recursos.lista_de_unidades[b].y + 50
                for v in range(len(funciones.vida)):
                    if v == b:
                        for c in range(len(funciones.vida_maxima)):
                            texto = fuente_de_texto.render(str(funciones.vida[v]) + "/" + str(funciones.vida_maxima[v]),
                                                           1, (225, 0, 0))
                recursos.pantalla.blit(texto, (xtexto, ytexto))
        xturno = 100
        yturno = 100
        turno_texto = fuente_de_texto_turno.render("Turno jugador "+str(recursos.turno_jugador),1, (0, 0, 0))
        recursos.pantalla.blit(turno_texto, (xturno, yturno))
        if recursos.itemselect and recursos.inv_on:
            funciones.dibujar_inv(recursos.turno_jugador)

        if recursos.turno_jugador == 1 and recursos.inv_on and recursos.itemselect:
            if len(recursos.recitems1) > 0:
                if mouse_pos[0] <= 500:
                    xbg = mouse_pos[0] + 18
                    ybg = mouse_pos[1] - 15
                    xitem = mouse_pos[0] + 20
                    yitem = mouse_pos[1]
                    xname = mouse_pos[0] + 70
                    yname = mouse_pos[1]
                    xdesc = mouse_pos[0] + 70
                    ydesc = mouse_pos[1] + 40
                    xlongdesc1 = mouse_pos[0] + 70
                    ylongdesc1 = mouse_pos[1] + 70
                    xlongdesc2 = mouse_pos[0] + 70
                    ylongdesc2 = mouse_pos[1] + 90
                    xlongdesc3 = mouse_pos[0] + 70
                    ylongdesc3 = mouse_pos[1] + 110
                if mouse_pos[0] >= 500:
                    xbg = mouse_pos[0] - 355
                    ybg = mouse_pos[1] - 10
                    xitem = mouse_pos[0] - 350
                    yitem = mouse_pos[1]
                    xname = mouse_pos[0] - 300
                    yname = mouse_pos[1]
                    xdesc = mouse_pos[0] - 300
                    ydesc = mouse_pos[1] + 40
                    xlongdesc1 = mouse_pos[0] - 300
                    ylongdesc1 = mouse_pos[1] + 70
                    xlongdesc2 = mouse_pos[0] - 300
                    ylongdesc2 = mouse_pos[1] + 90
                    xlongdesc3 = mouse_pos[0] - 300
                    ylongdesc3 = mouse_pos[1] + 110
                for j in range(len(recursos.itemsEquipados1)):
                    for k in range(len(recursos.recitems1)):
                        if recursos.itemsEquipados1[j] == 1:
                            if k == j and recursos.recitems1[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(410,100))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                baya_surf = pygame.image.load('Sprites/items/berry.png').convert_alpha()
                                baya_surf = pygame.transform.scale(baya_surf,(50,50))
                                baya_rect = baya_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(baya_surf, baya_rect)
                                item_name = item_name_font.render("Baya Explosiva", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Realiza 100 de daño a un enemigo", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                        if recursos.itemsEquipados1[j] == 2:
                            if k == j and recursos.recitems1[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(330,140))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                ultal_surf = pygame.image.load('Sprites/items/lastbreath.png').convert_alpha()
                                ultal_surf = pygame.transform.scale(ultal_surf,(50,50))
                                ultal_rect = ultal_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(ultal_surf, ultal_rect)
                                item_name = item_name_font.render("Ultimo Aliento", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Revive 1 aliado con el 10%", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("de su vida máxima restaurada", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1, ylongdesc1))
                        if recursos.itemsEquipados1[j] == 3:
                            if k == j and recursos.recitems1[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(410,100))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                cust_surf = pygame.image.load('Sprites/items/custodia.png').convert_alpha()
                                cust_surf = pygame.transform.scale(cust_surf,(50,50))
                                cust_rect = cust_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(cust_surf, cust_rect)
                                item_name = item_name_font.render("Custodia", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Otorga un escudo a un aliado de 75HP", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                        if recursos.itemsEquipados1[j] == 4:
                            if k == j and recursos.recitems1[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(280,100))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                crist_surf = pygame.image.load('Sprites/items/cristal.png').convert_alpha()
                                crist_surf = pygame.transform.scale(crist_surf,(50,50))
                                crist_rect = crist_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(crist_surf, crist_rect)
                                item_name = item_name_font.render("Cristal", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Cura 100HP a un aliado", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                        if recursos.itemsEquipados1[j] == 5:
                            if k == j and recursos.recitems1[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(390,130))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                daga_surf = pygame.image.load('Sprites/items/daga.png').convert_alpha()
                                daga_surf = pygame.transform.scale(daga_surf,(50,50))
                                daga_rect = daga_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(daga_surf, daga_rect)
                                item_name = item_name_font.render("Daga", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Incrementa el daño realizado un 25%", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("durante dos turnos", 1,(0,0,0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1,ylongdesc1))
                        if recursos.itemsEquipados1[j] == 6:
                            if k == j and recursos.recitems1[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(330,140))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                colmvamp_surf = pygame.image.load('Sprites/items/fangs.png').convert_alpha()
                                colmvamp_surf = pygame.transform.scale(colmvamp_surf,(50,50))
                                colmvamp_rect = colmvamp_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(colmvamp_surf, colmvamp_rect)
                                item_name = item_name_font.render("Colmillos Vampiricos", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Cura un 30% el daño realizado", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("por el proximo ataque", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1, ylongdesc1))
                        if recursos.itemsEquipados1[j] == 7:
                            if k == j and recursos.recitems1[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(440,130))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                alpeste_surf = pygame.image.load('Sprites/items/alientodepeste.png').convert_alpha()
                                alpeste_surf = pygame.transform.scale(alpeste_surf,(50,50))
                                alpeste_rect = alpeste_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(alpeste_surf, alpeste_rect)
                                item_name = item_name_font.render("Aliento de Peste", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Reduce la curación que recibe un enemigo", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("durante 3 turnos un 90%", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1, ylongdesc1))
                        if recursos.itemsEquipados1[j] == 8:
                            if k == j and recursos.recitems1[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(430,100))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                botas_surf = pygame.image.load('Sprites/items/boots.png').convert_alpha()
                                botas_surf = pygame.transform.scale(botas_surf,(50,50))
                                botas_rect = botas_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(botas_surf, botas_rect)
                                item_name = item_name_font.render("Bota", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Otorga un movimiento extra a una tropa", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                        if recursos.itemsEquipados1[j] == 9:
                            if k == j and recursos.recitems1[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(380,100))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                frenesi_surf = pygame.image.load('Sprites/items/frenesi.png').convert_alpha()
                                frenesi_surf = pygame.transform.scale(frenesi_surf,(50,50))
                                frenesi_rect = frenesi_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(frenesi_surf, frenesi_rect)
                                item_name = item_name_font.render("Frenesí", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Otorga un ataque extra a un aliado", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                        if recursos.itemsEquipados1[j] == 10:
                            if k == j and recursos.recitems1[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(570,130))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                represion_surf = pygame.image.load('Sprites/items/represion.png').convert_alpha()
                                represion_surf = pygame.transform.scale(represion_surf,(50,50))
                                represion_rect = represion_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(represion_surf, represion_rect)
                                item_name = item_name_font.render("Represión", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Deshabilita la proxima acción (atacar, curar, defender)", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("de un enemigo el siguiente turno", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1, ylongdesc1))
                        if recursos.itemsEquipados1[j] == 11:
                            if k == j and recursos.recitems1[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(410,140))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                bendcel_surf = pygame.image.load('Sprites/items/bend.png').convert_alpha()
                                bendcel_surf = pygame.transform.scale(bendcel_surf,(50,50))
                                bendcel_rect = bendcel_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(bendcel_surf, bendcel_rect)
                                item_name = item_name_font.render("Bendición Celestial", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Solo se puede usar en: Sanador", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("Duplica la próxima curación realizada", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1, ylongdesc1))
                        if recursos.itemsEquipados1[j] == 12:
                            if k == j and recursos.recitems1[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(320,120))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                cargar_surf = pygame.image.load('Sprites/items/enrage.png').convert_alpha()
                                cargar_surf = pygame.transform.scale(cargar_surf,(50,50))
                                cargar_rect = cargar_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(cargar_surf, cargar_rect)
                                item_name = item_name_font.render("Enfurecer", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Solo se puede usar en: Oso", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("Otorga un escudo de 500HP", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1, ylongdesc1))
                        if recursos.itemsEquipados1[j] == 13:
                            if k == j and recursos.recitems1[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(350,130))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                punteria_surf = pygame.image.load('Sprites/items/aim.png').convert_alpha()
                                punteria_surf = pygame.transform.scale(punteria_surf,(50,50))
                                punteria_rect = punteria_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(punteria_surf, punteria_rect)
                                item_name = item_name_font.render("Apuntar", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Solo se puede usar en: Cazador", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc = item_name_desc.render("El próximo ataque será crítico", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc, (xlongdesc1, ylongdesc1))
                        if recursos.itemsEquipados1[j] == 14:
                            if k == j and recursos.recitems1[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(390,150))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                mandcel_surf = pygame.image.load('Sprites/items/mand.png').convert_alpha()
                                mandcel_surf = pygame.transform.scale(mandcel_surf,(50,50))
                                mandcel_rect = mandcel_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(mandcel_surf, mandcel_rect)
                                item_name = item_name_font.render("Mandato Celestial", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Solo se puede usar en: Escudero", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("Otorga un escudo de 200HP a todos", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1, ylongdesc1))
                                longer_desc2 = item_name_desc.render("los aliados en su rango", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc2, (xlongdesc2, ylongdesc2))
                        if recursos.itemsEquipados1[j] == 15:
                            if k == j and recursos.recitems1[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(440,180))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                gritdrac_surf = pygame.image.load('Sprites/items/steelwill.png').convert_alpha()
                                gritdrac_surf = pygame.transform.scale(gritdrac_surf,(50,50))
                                gritdrac_rect = gritdrac_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(gritdrac_surf, gritdrac_rect)
                                item_name = item_name_font.render("Voluntad de Acero", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Solo se puede usar en: Caballero", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("Otorga un escudo de 300HP e incrementa", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1, ylongdesc1))
                                longer_desc2 = item_name_desc.render("su daño en 200 además de sumar", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc2, (xlongdesc2, ylongdesc2))
                                longer_desc3 = item_name_desc.render("un escudo de 50HP cada turno", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc3, (xlongdesc3, ylongdesc3))

        if recursos.turno_jugador == 2 and recursos.inv_on and recursos.itemselect:
            if len(recursos.recitems2) > 0:
                if mouse_pos[0] <= 500:
                    xbg = mouse_pos[0] + 18
                    ybg = mouse_pos[1] - 15
                    xitem = mouse_pos[0] + 20
                    yitem = mouse_pos[1]
                    xname = mouse_pos[0] + 70
                    yname = mouse_pos[1]
                    xdesc = mouse_pos[0] + 70
                    ydesc = mouse_pos[1] + 40
                    xlongdesc1 = mouse_pos[0] + 70
                    ylongdesc1 = mouse_pos[1] + 70
                    xlongdesc2 = mouse_pos[0] + 70
                    ylongdesc2 = mouse_pos[1] + 90
                    xlongdesc3 = mouse_pos[0] + 70
                    ylongdesc3 = mouse_pos[1] + 110
                if mouse_pos[0] >= 500:
                    xbg = mouse_pos[0] - 355
                    ybg = mouse_pos[1] - 10
                    xitem = mouse_pos[0] - 350
                    yitem = mouse_pos[1]
                    xname = mouse_pos[0] - 300
                    yname = mouse_pos[1]
                    xdesc = mouse_pos[0] - 300
                    ydesc = mouse_pos[1] + 40
                    xlongdesc1 = mouse_pos[0] - 300
                    ylongdesc1 = mouse_pos[1] + 70
                    xlongdesc2 = mouse_pos[0] - 300
                    ylongdesc2 = mouse_pos[1] + 90
                    xlongdesc3 = mouse_pos[0] - 300
                    ylongdesc3 = mouse_pos[1] + 110
                for j in range(len(recursos.itemsEquipados2)):
                    for k in range(len(recursos.recitems2)):
                        if recursos.itemsEquipados2[j] == 1:
                            if k == j and recursos.recitems2[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(410,100))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                baya_surf = pygame.image.load('Sprites/items/berry.png').convert_alpha()
                                baya_surf = pygame.transform.scale(baya_surf,(50,50))
                                baya_rect = baya_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(baya_surf, baya_rect)
                                item_name = item_name_font.render("Baya Explosiva", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Realiza 100 de daño a un enemigo", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                        if recursos.itemsEquipados2[j] == 2:
                            if k == j and recursos.recitems2[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(330,140))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                ultal_surf = pygame.image.load('Sprites/items/lastbreath.png').convert_alpha()
                                ultal_surf = pygame.transform.scale(ultal_surf,(50,50))
                                ultal_rect = ultal_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(ultal_surf, ultal_rect)
                                item_name = item_name_font.render("Ultimo Aliento", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Revive 1 aliado con el 10%", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("de su vida máxima restaurada", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1, ylongdesc1))
                        if recursos.itemsEquipados2[j] == 3:
                            if k == j and recursos.recitems2[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(410,100))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                cust_surf = pygame.image.load('Sprites/items/custodia.png').convert_alpha()
                                cust_surf = pygame.transform.scale(cust_surf,(50,50))
                                cust_rect = cust_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(cust_surf, cust_rect)
                                item_name = item_name_font.render("Custodia", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Otorga un escudo a un aliado de 75HP", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                        if recursos.itemsEquipados2[j] == 4:
                            if k == j and recursos.recitems2[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(280,100))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                crist_surf = pygame.image.load('Sprites/items/cristal.png').convert_alpha()
                                crist_surf = pygame.transform.scale(crist_surf,(50,50))
                                crist_rect = crist_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(crist_surf, crist_rect)
                                item_name = item_name_font.render("Cristal", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Cura 100HP a un aliado", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                        if recursos.itemsEquipados2[j] == 5:
                            if k == j and recursos.recitems2[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(390,130))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                daga_surf = pygame.image.load('Sprites/items/daga.png').convert_alpha()
                                daga_surf = pygame.transform.scale(daga_surf,(50,50))
                                daga_rect = daga_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(daga_surf, daga_rect)
                                item_name = item_name_font.render("Daga", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Incrementa el daño realizado un 25%", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("durante dos turnos", 1,(0,0,0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1,ylongdesc1))
                        if recursos.itemsEquipados2[j] == 6:
                            if k == j and recursos.recitems2[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(330,140))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                colmvamp_surf = pygame.image.load('Sprites/items/fangs.png').convert_alpha()
                                colmvamp_surf = pygame.transform.scale(colmvamp_surf,(50,50))
                                colmvamp_rect = colmvamp_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(colmvamp_surf, colmvamp_rect)
                                item_name = item_name_font.render("Colmillos Vampiricos", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Cura un 30% el daño realizado", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("por el proximo ataque", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1, ylongdesc1))
                        if recursos.itemsEquipados2[j] == 7:
                            if k == j and recursos.recitems2[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(440,130))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                alpeste_surf = pygame.image.load('Sprites/items/alientodepeste.png').convert_alpha()
                                alpeste_surf = pygame.transform.scale(alpeste_surf,(50,50))
                                alpeste_rect = alpeste_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(alpeste_surf, alpeste_rect)
                                item_name = item_name_font.render("Aliento de Peste", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Reduce la curación que recibe un enemigo", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("durante 3 turnos un 90%", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1, ylongdesc1))
                        if recursos.itemsEquipados2[j] == 8:
                            if k == j and recursos.recitems2[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(430,100))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                botas_surf = pygame.image.load('Sprites/items/boots.png').convert_alpha()
                                botas_surf = pygame.transform.scale(botas_surf,(50,50))
                                botas_rect = botas_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(botas_surf, botas_rect)
                                item_name = item_name_font.render("Bota", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Otorga un movimiento extra a una tropa", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                        if recursos.itemsEquipados2[j] == 9:
                            if k == j and recursos.recitems2[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(380,100))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                frenesi_surf = pygame.image.load('Sprites/items/frenesi.png').convert_alpha()
                                frenesi_surf = pygame.transform.scale(frenesi_surf,(50,50))
                                frenesi_rect = frenesi_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(frenesi_surf, frenesi_rect)
                                item_name = item_name_font.render("Frenesí", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Otorga un ataque extra a un aliado", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                        if recursos.itemsEquipados2[j] == 10:
                            if k == j and recursos.recitems2[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(570,130))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                represion_surf = pygame.image.load('Sprites/items/represion.png').convert_alpha()
                                represion_surf = pygame.transform.scale(represion_surf,(50,50))
                                represion_rect = represion_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(represion_surf, represion_rect)
                                item_name = item_name_font.render("Represión", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Deshabilita la proxima acción (atacar, curar, defender)", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("de un enemigo el siguiente turno", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1, ylongdesc1))
                        if recursos.itemsEquipados2[j] == 11:
                            if k == j and recursos.recitems2[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(410,140))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                bendcel_surf = pygame.image.load('Sprites/items/bend.png').convert_alpha()
                                bendcel_surf = pygame.transform.scale(bendcel_surf,(50,50))
                                bendcel_rect = bendcel_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(bendcel_surf, bendcel_rect)
                                item_name = item_name_font.render("Bendición Celestial", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Solo se puede usar en: Sanador", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("Duplica la próxima curación realizada", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1, ylongdesc1))
                        if recursos.itemsEquipados2[j] == 12:
                            if k == j and recursos.recitems2[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(320,120))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                cargar_surf = pygame.image.load('Sprites/items/enrage.png').convert_alpha()
                                cargar_surf = pygame.transform.scale(cargar_surf,(50,50))
                                cargar_rect = cargar_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(cargar_surf, cargar_rect)
                                item_name = item_name_font.render("Enfurecer", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Solo se puede usar en: Oso", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("Otorga un escudo de 500HP", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1, ylongdesc1))
                        if recursos.itemsEquipados2[j] == 13:
                            if k == j and recursos.recitems2[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(350,130))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                punteria_surf = pygame.image.load('Sprites/items/aim.png').convert_alpha()
                                punteria_surf = pygame.transform.scale(punteria_surf,(50,50))
                                punteria_rect = punteria_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(punteria_surf, punteria_rect)
                                item_name = item_name_font.render("Apuntar", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Solo se puede usar en: Cazador", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc = item_name_desc.render("El próximo ataque será crítico", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc, (xlongdesc1, ylongdesc1))
                        if recursos.itemsEquipados2[j] == 14:
                            if k == j and recursos.recitems2[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(390,150))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                mandcel_surf = pygame.image.load('Sprites/items/mand.png').convert_alpha()
                                mandcel_surf = pygame.transform.scale(mandcel_surf,(50,50))
                                mandcel_rect = mandcel_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(mandcel_surf, mandcel_rect)
                                item_name = item_name_font.render("Mandato Celestial", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Solo se puede usar en: Escudero", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("Otorga un escudo de 200HP a todos", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1, ylongdesc1))
                                longer_desc2 = item_name_desc.render("los aliados en su rango", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc2, (xlongdesc2, ylongdesc2))
                        if recursos.itemsEquipados2[j] == 15:
                            if k == j and recursos.recitems2[k].collidepoint(mouse_pos):
                                tooltipbg = pygame.image.load('Sprites/items/tooltipbg.png').convert_alpha()
                                tooltipbg = pygame.transform.scale(tooltipbg,(440,180))
                                tooltipbg_rect = tooltipbg.get_rect(topleft=(xbg, ybg))
                                recursos.pantalla.blit(tooltipbg, tooltipbg_rect)
                                gritdrac_surf = pygame.image.load('Sprites/items/steelwill.png').convert_alpha()
                                gritdrac_surf = pygame.transform.scale(gritdrac_surf,(50,50))
                                gritdrac_rect = gritdrac_surf.get_rect(topleft=(xitem, yitem))
                                recursos.pantalla.blit(gritdrac_surf, gritdrac_rect)
                                item_name = item_name_font.render("Voluntad de Acero", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_name, (xname, yname))
                                item_desc = item_name_desc.render("Solo se puede usar en: Caballero", 1, (0, 0, 0))
                                recursos.pantalla.blit(item_desc, (xdesc, ydesc))
                                longer_desc1 = item_name_desc.render("Otorga un escudo de 300HP e incrementa", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc1, (xlongdesc1, ylongdesc1))
                                longer_desc2 = item_name_desc.render("su daño en 200 además de sumar", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc2, (xlongdesc2, ylongdesc2))
                                longer_desc3 = item_name_desc.render("un escudo de 50HP cada turno", 1, (0, 0, 0))
                                recursos.pantalla.blit(longer_desc3, (xlongdesc3, ylongdesc3))

def dibujar_posicionamiento(turnos, unidad):
    """
    Toma la lista de las unidades, según la unidad que sea mueve su rectángulo (El dibujo se actualiza en la función dibujar_tablero)
    """
    unidad[turnos].x = mouse_pos[0] - 50  #Toma la coordenada x del mouse y la reajusta 50 unidades
    unidad[turnos].y = mouse_pos[1] - 50  #Toma la coordenada y del mouse y la reajusta 50 unidades

def posicionamiento_inicial(turno, unidad):
    """
    Esta función recibe la posición del mouse y posiciona el rectángulo de la unidad en la casilla en la que se encuentra el mouse al momento del click
    Debe returnar true para que funcione en el bucle principal
    """

    casilla = (mouse_pos[0] // 100) * 100, (mouse_pos[1] // 100) * 100  #Se redonde al múltiplo de 100 más cercano

    if recursos.turnos_unidades < 5:  #posicionamiento primer ejército
        if mouse_pos[0] < 400:

            unidad[turno].x = casilla[0]
            unidad[turno].y = casilla[1]
            if funciones.calcular_colision_posicionamiento(unidad[turno],
                                                           turno):  #Retorna True si no posicionan dos unidades en el mismo lugar
                return True
    else:
        if mouse_pos[0] > 600:  #posicionamiento segundo ejército

            unidad[turno].x = casilla[0]
            unidad[turno].y = casilla[1]
            if funciones.calcular_colision_posicionamiento(unidad[turno], turno):
                return True

#Bucle principal del juego
corriendo = True
while corriendo:
    dibujar_tablero()
    mouse_pos = pygame.mouse.get_pos()  #Coordenadas actuales del mouse
    #Imprime los fps
    clock.tick(60)
    """
    fps = clock.get_fps()
    print(fps)
    """

    for event in pygame.event.get():
        #Para salir del juego
        if event.type == pygame.QUIT:
            corriendo = False
        if recursos.fase_de_juego == 1: #menu
            for rect in range(len(recursos.lista_de_botones)):
                if rect == 0 and recursos.lista_de_botones[0].collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    recursos.fase_de_juego += 1
                    button_sfx.play()
                if rect == 3 and recursos.lista_de_botones[3].collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    corriendo = False

        if recursos.fase_de_juego == 2:  #Posicionamiento
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if recursos.turnos_unidades == 9:  #Cuando las 10 piezas están colocadas se avanza a la fase de combate
                        recursos.fase_de_juego += 1

                    if posicionamiento_inicial(recursos.turnos_unidades,
                                               recursos.lista_de_unidades):  #Solo se pasa al siguiente turno si posicionan correctamente
                        recursos.turnos_unidades += 1

        if recursos.fase_de_juego == 3:  #Combate
            if (not recursos.moverse or not recursos.ataque) and not recursos.turno_activo and event.type == pygame.MOUSEBUTTONDOWN and not recursos.inv_on:
                if event.button == 1:
                    if recursos.turno_jugador == 1:
                        for rect in range(0, len(recursos.lista_de_unidades) - 5):
                            if recursos.lista_de_unidades[rect].collidepoint(mouse_pos):
                                if not turnos_de_unidades[rect] >= 1:
                                    i = rect
                                    unidad1 = recursos.lista_de_unidades[rect]
                                    recursos.moverse = True
                                    recursos.turno_activo = True
                                    coord_puntos = funciones.calcular_puntos(unidad1)

                    if recursos.turno_jugador == 2:
                        for rect in range(5, len(recursos.lista_de_unidades)):
                            if recursos.lista_de_unidades[rect].collidepoint(mouse_pos):
                                if not turnos_de_unidades[rect] >= 1:
                                    i = rect
                                    unidad1 = recursos.lista_de_unidades[rect]
                                    recursos.moverse = True
                                    recursos.turno_activo = True
                                    coord_puntos = funciones.calcular_puntos(unidad1)
                if event.button == 3:
                    if recursos.turno_jugador == 1:
                        for rect in range(0, len(recursos.lista_de_unidades) - 5):
                            if recursos.lista_de_unidades[rect].collidepoint(mouse_pos):
                                if not turnos_de_unidades[rect] == 2:
                                    a = rect
                                    unidad2 = recursos.lista_de_unidades[rect]
                                    recursos.ataque = True
                                    recursos.turno_activo = True
                                    coord_marcas = funciones.calcular_marcas(unidad2)
                                    if coord_marcas[0] == unidad2:
                                        recursos.en_rango = True

                    if recursos.turno_jugador == 2:
                        for rect in range(5, len(recursos.lista_de_unidades)):
                            if recursos.lista_de_unidades[rect].collidepoint(mouse_pos):
                                if not turnos_de_unidades[rect] == 2:
                                    a = rect
                                    unidad2 = recursos.lista_de_unidades[rect]
                                    recursos.ataque = True
                                    recursos.turno_activo = True
                                    coord_marcas = funciones.calcular_marcas(unidad2)

            for j in range(0, len(turnos_de_unidades) - 5):
                if all(j == 2 for j in turnos_de_unidades[0:5]):
                    funciones.checkStatus()
                    recursos.turno_jugador = 2
                    turnos_de_unidades = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    for i in range(10):
                        if funciones.statusCheck[i][5] != 0:
                            turnos_de_unidades[i] = 2
                            funciones.statusCheck[i][5] -= 1
                    recursos.pintarItems()
                    recursos.asignarItem1()
            for j in range(5, len(turnos_de_unidades)):
                if all(j == 2 for j in turnos_de_unidades[5:10]):
                    funciones.checkStatus()
                    recursos.turno_jugador = 1
                    turnos_de_unidades = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    for i in range(10):
                        if funciones.statusCheck[i][5] != 0:
                            turnos_de_unidades[i] = 2
                            funciones.statusCheck[i][5] -= 1
                    recursos.pintarItems()
                    recursos.asignarItem2()
                    recursos.ronda += 1
                    if recursos.ronda > 3:
                        recursos.ronda = 1

            if recursos.moverse and recursos.turno_activo:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for punto in coord_puntos:
                            if punto.collidepoint(mouse_pos) and not turnos_de_unidades[i] == 1:
                                unidad1.x = punto.x
                                unidad1.y = punto.y
                                recursos.moverse = False  # Se termina el movimiento
                                recursos.turno_activo = False
                                steps_sfx.play()
                                if funciones.statusCheck[i][3] == 1:
                                    funciones.statusCheck[i][3] = 0
                                else:
                                    turnos_de_unidades[i] = 1

            if recursos.ataque and recursos.turno_activo:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        for marca in coord_marcas[0]:
                            if marca.collidepoint(mouse_pos) and not turnos_de_unidades[a] == 2 and recursos.turno_jugador == 1:
                                if unidad2 != recursos.lista_de_unidades[2] and unidad2 != recursos.lista_de_unidades[1]:
                                    for unidads in range(5,len(recursos.lista_de_unidades)):
                                        if marca == recursos.lista_de_unidades[unidads]:
                                            funciones.ataque(unidad2, recursos.lista_de_unidades[unidads])
                                            recursos.ataque = False
                                            recursos.turno_activo = False
                                            if recursos.lista_de_unidades[0] == unidad2:
                                                bow_sfx.play()
                                            if recursos.lista_de_unidades[4] == unidad2:
                                                sword_sfx.play()
                                            if recursos.lista_de_unidades[3] == unidad2:
                                                bear_sfx.play()
                                            if funciones.statusCheck[a][4] == 1:
                                                funciones.statusCheck[a][4] = 0
                                            else:
                                                turnos_de_unidades[a] = 2
                                if unidad2 is recursos.lista_de_unidades[2]:
                                    for unidads in range(0,len(recursos.lista_de_unidades)-5):
                                        if marca == recursos.lista_de_unidades[unidads]:
                                            funciones.curar(unidad2, recursos.lista_de_unidades[unidads])
                                            recursos.ataque = False
                                            recursos.turno_activo = False
                                            heal_sfx.play()
                                            if funciones.statusCheck[a][4] == 1:
                                                funciones.statusCheck[a][4] = 0
                                            else:
                                                turnos_de_unidades[a] = 2
                                if unidad2 == recursos.lista_de_unidades[1]:
                                    for unidads in range(0,len(recursos.lista_de_unidades)-5):
                                        if marca == recursos.lista_de_unidades[unidads]:
                                            funciones.escudar(unidad2, recursos.lista_de_unidades[unidads])
                                            recursos.ataque = False
                                            recursos.turno_activo = False
                                            shield_sfx.play()
                                            if funciones.statusCheck[a][4] == 1:
                                                funciones.statusCheck[a][4] = 0
                                            else:
                                                turnos_de_unidades[a] = 2

                            if marca.collidepoint(mouse_pos) and not turnos_de_unidades[a] == 2 and recursos.turno_jugador == 2:
                                if unidad2 != recursos.lista_de_unidades[7] and unidad2 != recursos.lista_de_unidades[6]:
                                    for unidads in range(0,len(recursos.lista_de_unidades)-5):
                                        if marca == recursos.lista_de_unidades[unidads]:
                                            funciones.ataque(unidad2, recursos.lista_de_unidades[unidads])
                                            recursos.ataque = False
                                            recursos.turno_activo = False
                                            if recursos.lista_de_unidades[5] == unidad2:
                                                bow_sfx.play()
                                            if recursos.lista_de_unidades[9] == unidad2:
                                                sword_sfx.play()
                                            if recursos.lista_de_unidades[8] == unidad2:
                                                bear_sfx.play()
                                            if funciones.statusCheck[a][4] == 1:
                                                funciones.statusCheck[a][4] = 0
                                            else:
                                                turnos_de_unidades[a] = 2
                                if unidad2 is recursos.lista_de_unidades[7]:
                                    for unidads in range(5,len(recursos.lista_de_unidades)):
                                        if marca == recursos.lista_de_unidades[unidads]:
                                            funciones.curar(unidad2, recursos.lista_de_unidades[unidads])
                                            recursos.ataque = False
                                            recursos.turno_activo = False
                                            heal_sfx.play()
                                            if funciones.statusCheck[a][4] == 1:
                                                funciones.statusCheck[a][4] = 0
                                            else:
                                                turnos_de_unidades[a] = 2
                                if unidad2 == recursos.lista_de_unidades[6]:
                                    for unidads in range(5,len(recursos.lista_de_unidades)):
                                        if marca == recursos.lista_de_unidades[unidads]:
                                            funciones.escudar(unidad2, recursos.lista_de_unidades[unidads])
                                            recursos.ataque = False
                                            recursos.turno_activo = False
                                            shield_sfx.play()
                                            if funciones.statusCheck[a][4] == 1:
                                                funciones.statusCheck[a][4] = 0
                                            else:
                                                turnos_de_unidades[a] = 2

            for u in range(len(funciones.vida)):
                if funciones.vida[u] == 0:
                    for k in range(len(muertos)):
                        if k == u and muertos[k] == 0:
                            copiar_coordenadas = recursos.lista_de_unidades[k].copy
                            muertos[k] = 1
                            if funciones.vida[u] == funciones.vida[1] or funciones.vida[u] == funciones.vida[6] or funciones.vida[u] == funciones.vida[0] or funciones.vida[u] == funciones.vida[5] or funciones.vida[u] == funciones.vida[4] or funciones.vida[u] == funciones.vida[9]:
                                death_sfx.play()
                            elif funciones.vida[u] == funciones.vida[2] or funciones.vida[u] == funciones.vida[7]:
                                healer_die_sfx.play()
                            elif funciones.vida[u] == funciones.vida[3] or funciones.vida[u] == funciones.vida[8]:
                                bear_die_sfx.play()
                        for unidadm in range(len(recursos.lista_de_unidades)):
                            if unidadm == k and muertos[k] == 1:
                                recursos.lista_de_lapidas[k].x = recursos.lista_de_unidades[k].x
                                recursos.lista_de_lapidas[k].y = recursos.lista_de_unidades[k].y
                                muertos[k] = 2
                            if unidadm == k and muertos[k] == 2:
                                recursos.lista_de_unidades[k].x = -200
                                recursos.lista_de_unidades[k].y = 0
                            if all(h == 2 for h in muertos[0:5]) or all(h == 2 for h in muertos[5:10]):
                                muertos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                                for t in range(len(recursos.lista_de_lapidas)):
                                    recursos.lista_de_unidades[t].x = -200
                                    recursos.lista_de_unidades[t].y = 0
                                    recursos.lista_de_lapidas[t].x = -200
                                    recursos.lista_de_lapidas[t].y = 0
                                recursos.fase_de_juego = 1
                                recursos.turnos_unidades = 0
                                funciones.vida = [750, 1200, 800, 1050, 900, 750, 1200, 800, 1050, 900]

            if event.type == pygame.KEYDOWN:
                # eventeclas()
                # funcion switch para abrir el inventario
                if event.key == pygame.K_d: #abre y cierra el inventario
                    recursos.inv_on = not recursos.inv_on
                if event.key == pygame.K_q:  # Si oprime q puede escoger otra tropa para mover
                    recursos.ataque = False
                    recursos.moverse = False
                    recursos.turno_activo = False
                if event.key == pygame.K_w and recursos.turno_jugador == 1:
                    funciones.checkStatus()
                    recursos.turno_jugador = 2
                    turnos_de_unidades = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    for i in range(10):
                        if funciones.statusCheck[i][5] != 0:
                            turnos_de_unidades[i] = 2
                            funciones.statusCheck[i][5] -= 1
                    recursos.pintarItems()
                    recursos.asignarItem1()
                elif event.key == pygame.K_w and recursos.turno_jugador == 2:
                    funciones.checkStatus()
                    recursos.turno_jugador = 1
                    turnos_de_unidades = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    for i in range(10):
                        if funciones.statusCheck[i][5] != 0:
                            turnos_de_unidades[i] = 2
                            funciones.statusCheck[i][5] -= 1
                    recursos.pintarItems()
                    recursos.asignarItem2()
                    recursos.ronda += 1
                    if recursos.ronda > 3:
                        recursos.ronda = 1
                if recursos.inv_on:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e: # esta parte es para "equipar" los items
                        if recursos.itemselect: # en esta parte se diferencian los inventarios de los jugadores y sus items
                           if recursos.turno_jugador == 1:
                                for i in range(len(recursos.recitems1)):
                                    if recursos.recitems1[i].collidepoint(mouse_pos):
                                        z = recursos.itemsEquipados1[i] # esta variable se usa para identificar el item mas adelante
                                        recursos.itemselect = False
                                        print(
                                            f"la lista de items es: {recursos.itemsEquipados1} y el item equipado fue: {z}")
                                        break
                           if recursos.turno_jugador == 2:
                               for i in range(len(recursos.recitems2)):
                                   if recursos.recitems2[i].collidepoint(mouse_pos):
                                       z = recursos.itemsEquipados2[i]
                                       recursos.itemselect = False
                                       print(
                                           f"la lista de items es: {recursos.itemsEquipados2} y el item equipado fue: {z}")
                                       break
                        else:
                            for l in recursos.lista_de_lapidas: # las lapidas necesitan un for distinto al de las unidades
                                if l.collidepoint(mouse_pos):
                                    if z == 2:
                                        itemChk = funciones.ultimoAliento(l)
                                        funciones.useItem(recursos.turno_jugador, itemChk, z)
                                        recursos.inv_on = False
                                        recursos.itemselect = True
                                        print("no xdd")
                            for u in recursos.lista_de_unidades: #aca se usan las funciones de todos los diferentes items
                                if u.collidepoint(mouse_pos):
                                    if z == 1:
                                        itemChk = funciones.bayaExplosiva(u)
                                        funciones.useItem(recursos.turno_jugador, itemChk, z)
                                    elif z == 3:
                                        itemChk = funciones.custodia(u)
                                        funciones.useItem(recursos.turno_jugador, itemChk, z)
                                    elif z == 4:
                                        itemChk = funciones.cristal(u)
                                        funciones.useItem(recursos.turno_jugador, itemChk, z)
                                    elif z == 5:
                                        itemChk = funciones.daga(u)
                                        funciones.useItem(recursos.turno_jugador, itemChk, z)
                                    elif z == 6:
                                        itemChk = funciones.colmillosVampíricos(u)
                                        funciones.useItem(recursos.turno_jugador, itemChk, z)
                                    elif z == 7:
                                        itemChk = funciones.alientoPeste(u)
                                        funciones.useItem(recursos.turno_jugador, itemChk, z)
                                    elif z == 8:
                                        itemChk = funciones.botas(u)
                                        funciones.useItem(recursos.turno_jugador, itemChk, z)
                                    elif z == 9:
                                        itemChk = funciones.frenesi(u)
                                        funciones.useItem(recursos.turno_jugador, itemChk, z)
                                    elif z == 10:
                                        itemChk = funciones.represion(u)
                                        funciones.useItem(recursos.turno_jugador, itemChk, z)
                                    elif z == 11:
                                        itemChk = funciones.bendicionCelestial(u)
                                        funciones.useItem(recursos.turno_jugador, itemChk, z)
                                    elif z == 12:
                                        itemChk = funciones.cargar(u)
                                        funciones.useItem(recursos.turno_jugador, itemChk, z)
                                    elif z == 13:
                                        itemChk = funciones.punteria(u)
                                        funciones.useItem(recursos.turno_jugador, itemChk, z)
                                    elif z == 14:
                                        itemChk = funciones.mandatoCelestial(u)
                                        funciones.useItem(recursos.turno_jugador, itemChk, z)
                                    elif z == 15:
                                        itemChk = funciones.gritoDraconico(u)
                                        funciones.useItem(recursos.turno_jugador, itemChk, z)
                                    recursos.inv_on = False
                                    recursos.itemselect = True

    if recursos.fase_de_juego == 2:
        dibujar_posicionamiento(recursos.turnos_unidades, recursos.lista_de_unidades)

    if recursos.fase_de_juego == 3:
        if recursos.moverse and recursos.turno_activo:
            funciones.dibujar_puntos(coord_puntos)
        if recursos.ataque and recursos.turno_activo:
            funciones.dibujar_marcas(coord_marcas[0],coord_marcas[1])

    pygame.display.flip()

pygame.quit()
