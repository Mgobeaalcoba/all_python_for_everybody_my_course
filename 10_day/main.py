import pygame
from random import choice
from model.personajes import Player, Enemy


def run() -> None:
    set_name_and_icon()
    init_game()


def init_game() -> None:
    # Inicializo a pygame en nuestro programa
    pygame.init()

    ## Establezco el tamaño de nuestro pantalla
    pantalla : pygame.surface = pygame.display.set_mode((800, 600)) # 800 de ancho y 600 de ancho

    ## Programo que sucede frente al evento QUIT que es el presionar en la X de nuestra pantalla
    se_ejecuta = True

    ## Posiciones iniciales del jugador: 
    player_1 = Player(pantalla) 

    ## Posiciones iniciales del enemigo:
    enemy_1 = Enemy(pantalla)
    enemy_2 = Enemy(pantalla)
    enemy_3 = Enemy(pantalla)
    enemy_4 = Enemy(pantalla)
    enemy_5 = Enemy(pantalla)
    enemy_6 = Enemy(pantalla)
    enemy_7 = Enemy(pantalla)
    enemy_8 = Enemy(pantalla)
    enemy_9 = Enemy(pantalla)
    enemy_10 = Enemy(pantalla)
    

    # Loop central del juego
    ## Mostramos la pantalla para que la vea el usuario hasta que aprete en la X
    while se_ejecuta:
        ### Modifico el color de fondo de mi pantalla
        pantalla.fill((205, 144, 228)) # Escala RGB para setear color de fondo de mi pantalla 
        wall_image = pygame.image.load("./images/fondo_juego.jpg")
        wall_game = pygame.transform.scale(wall_image, (800, 600))
        pantalla.blit(wall_game, (0,0))
        ### Reviso cada uno de los eventos que existen en la nomenclatura de Pygame
        for evento in pygame.event.get():
            ### Si el evento es un evento QUIT entonces cambio el valor booleano de mi variable se_ejecuta
            if evento.type == pygame.QUIT:
                se_ejecuta = False

            ### Si el evento es un evento de KEYDOWN (Tecla presionada):
            if evento.type == pygame.KEYDOWN:
                #### Si la tecla es la de izquierda:
                if evento.key == pygame.K_LEFT:
                    player_1.move_left()
                    for enemy in Enemy.instancias:
                        choice([enemy.move_random_x(), enemy.move_random_y()])
                #### Si la tecla es la de derecha:
                elif evento.key == pygame.K_RIGHT:
                    player_1.move_right()
                    for enemy in Enemy.instancias:
                        choice([enemy.move_random_x(), enemy.move_random_y()])
                #### Si la tecla es la de arriba:
                elif evento.key == pygame.K_UP:
                    player_1.move_up()
                    for enemy in Enemy.instancias:
                        choice([enemy.move_random_x(), enemy.move_random_y()])
                #### Si la tecla es la de abajo:
                elif evento.key == pygame.K_DOWN:
                    player_1.move_down()
                    for enemy in Enemy.instancias:
                        choice([enemy.move_random_x(), enemy.move_random_y()])

        ### Pinto al jugador en la pantalla:
        make_player(pantalla, player_1)
        ### Pinto al enemigo en la pantalla: 
        for enemy in Enemy.instancias:
            make_enemy(pantalla, enemy)

        ### Actualizo la pantalla para que se vean nuestras novedades
        pygame.display.update()


def set_name_and_icon() -> None:
    # Personalizar la pantalla de pygame
    ## Titulo e icono:
    pygame.display.set_caption("Invasión Espacial")
    icono = pygame.image.load("./images/invasion-espacial.png")
    pygame.display.set_icon(icono)


def make_player(pantalla: pygame.surface, player: Player) -> None:
    img_jugador = pygame.image.load("./images/nave-player.png")
    pantalla.blit(img_jugador, (player.position_x, player.position_y))


def make_enemy(pantalla: pygame.surface, enemy: Enemy) -> None:
    img_enemy = pygame.image.load(enemy.select_enemy)
    pantalla.blit(img_enemy, (enemy.position_x, enemy.position_y))


if __name__ == '__main__':
    run()