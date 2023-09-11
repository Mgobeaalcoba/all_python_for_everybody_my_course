import pygame


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
    position_x_player = 368
    position_y_player = 516

    # Loop central del juego
    ## Mostramos la pantalla para que la vea el usuario hasta que aprete en la X
    while se_ejecuta:
        ### Modifico el color de fondo de mi pantalla
        pantalla.fill((205, 144, 228)) # Escala RGB para setear color de fondo de mi pantalla 
        ### Reviso cada uno de los eventos que existen en la nomenclatura de Pygame
        for evento in pygame.event.get():
            ### Si el evento es un evento QUIT entonces cambio el valor booleano de mi variable se_ejecuta
            if evento.type == pygame.QUIT:
                se_ejecuta = False

            ### Si el evento es un evento de KEYDOWN (Tecla presionada):
            if evento.type == pygame.KEYDOWN:
                #### Si la tecla es la de izquierda:
                if evento.key == pygame.K_LEFT:
                    position_x_player -= 4
                #### Si la tecla es la de derecha:
                elif evento.key == pygame.K_RIGHT:
                    position_x_player += 4
                #### Si la tecla es la de arriba:
                elif evento.key == pygame.K_UP:
                    position_y_player -= 4
                #### Si la tecla es la de abajo:
                elif evento.key == pygame.K_DOWN:
                    position_y_player += 4

        ### Pinto al jugador en la pantalla:
        make_player(pantalla, position_x_player, position_y_player)
        ### Actualizo la pantalla para que se vean nuestras novedades
        pygame.display.update()


def set_name_and_icon() -> None:
    # Personalizar la pantalla de pygame
    ## Titulo e icono:
    pygame.display.set_caption("Invasión Espacial")
    icono = pygame.image.load("./invasion-espacial.png")
    pygame.display.set_icon(icono)


def make_player(pantalla: pygame.surface, player_x_position : int = 368, player_y_position : int = 516) -> None:
    img_jugador = pygame.image.load("./cohete.png")
    pantalla.blit(img_jugador, (player_x_position, player_y_position))


if __name__ == '__main__':
    run()