import pygame
from pygame import mixer
import random
import math
import os

# Obtener la ruta del directorio actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Función para obtener la ruta completa de los archivos
def obtener_ruta(archivo):
    return os.path.join(directorio_actual, archivo)

# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título e icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load(obtener_ruta("ovni.png"))
pygame.display.set_icon(icono)

# Música de fondo
mixer.music.load(obtener_ruta('MusicaFondo.mp3'))
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Cargar imágenes
img_jugador1 = pygame.image.load(obtener_ruta("cohete.png"))
img_jugador2 = pygame.image.load(obtener_ruta("cohete_2.png"))
img_jugador3 = pygame.image.load(obtener_ruta("cohete_3.png"))
img_bala = pygame.image.load(obtener_ruta("bala.png"))
fondo = pygame.image.load(obtener_ruta("fondo.jpg"))
game_over_img = pygame.image.load(obtener_ruta("game_over.png"))
vida_img = pygame.image.load(obtener_ruta("energy_drink.png"))

# Enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8
for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load(obtener_ruta("enemigo.png")))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.6)
    enemigo_y_cambio.append(50)

# Jugador
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Balas
balas = []

# Puntaje
puntaje = 0
fuente = pygame.font.Font(None, 32)
texto_x = 10
texto_y = 10

# Vidas
vidas = 5

# Funciones de renderizado
def jugador(x, y, imagen):
    pantalla.blit(imagen, (x, y))

def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

def disparar_bala(x, y):
    pantalla.blit(img_bala, (x + 16, y + 10))

def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

def mostrar_vidas(x, y):
    for i in range(vidas):
        pantalla.blit(vida_img, (x + 32 * i, y))

def mostrar_game_over():
    pantalla.blit(game_over_img, (144, 44))

# Detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    return distancia < 27

# Bucle principal del juego
se_ejecuta = True
while se_ejecuta:
    pantalla.blit(fondo, (0, 0))  # Mostrar fondo

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound(obtener_ruta("disparo.mp3"))
                sonido_bala.play()
                nueva_bala = {"x": jugador_x + 16, "y": jugador_y, "velocidad": velocidad_bala}
                balas.append(nueva_bala)
        if evento.type == pygame.KEYUP:
            if evento.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                jugador_x_cambio = 0

    # Actualizar la posición del jugador
    jugador_x += jugador_x_cambio
    jugador_x = max(0, min(jugador_x, 736))  # Limitar dentro de los bordes

    # Actualizar posición de los enemigos
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]
        if enemigo_x[e] <= 0 or enemigo_x[e] >= 736:
            enemigo_x_cambio[e] *= -1
            enemigo_y[e] += enemigo_y_cambio[e]

        # Comprobar colisión con balas
        for bala in balas:
            if hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"]):
                sonido_colision = mixer.Sound(obtener_ruta("Golpe.mp3"))
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e], enemigo_y[e] = random.randint(0, 736), random.randint(20, 200)

        # Comprobar colisión con jugador
        if hay_colision(enemigo_x[e], enemigo_y[e], jugador_x, jugador_y):
            sonido_colision = mixer.Sound(obtener_ruta("Golpe.mp3"))
            sonido_colision.play()
            vidas -= 1
            enemigo_x[e], enemigo_y[e] = random.randint(0, 736), random.randint(20, 200)
            if vidas == 0:
                se_ejecuta = False
                pantalla.blit(fondo, (0, 0))  # Mostrar fondo final
                mostrar_game_over()
                pygame.display.update()
                pygame.time.wait(2000)  # Esperar 2 segundos antes de salir

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Controlar movimiento de las balas
    for bala in balas:
        bala["y"] += bala["velocidad"]
        if bala["y"] < 0:
            balas.remove(bala)  
        else:
            pantalla.blit(img_bala, (bala["x"], bala["y"]))

    # Cambiar la imagen del jugador según el puntaje
    if puntaje >= 150:
        imagen_actual = img_jugador3
        velocidad_bala = -2.5

    elif puntaje >= 50:
        imagen_actual = img_jugador2
        velocidad_bala = -1.5

    else:
        imagen_actual = img_jugador1
        velocidad_bala = -0.5

    # Mostrar elementos en pantalla
    jugador(jugador_x, jugador_y, imagen_actual)
    mostrar_puntaje(texto_x, texto_y)
    mostrar_vidas(600, 10)
    pygame.display.update()
