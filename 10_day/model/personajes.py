from random import choice

class Personaje:

    position_x = 0 
    position_y = 0

    def __init__(self, screen) -> None:
        self.screen = screen


class Player(Personaje):
    
    position_x = 318 
    position_y = 516

    def __init__(self, screen) -> None:
        super().__init__(screen)

    def move_left(self) -> None:
        if self.position_x >= 0 and self.position_x <= 736:
            self.position_x -= 4
        elif self.position_x > 736:
            self.position_x = 736
        else:
            self.position_x = 0
    
    def move_right(self) -> None:
        if self.position_x >= 0 and self.position_x <= 736:
            self.position_x += 4
        elif self.position_x > 736:
            self.position_x = 736
        else:
            self.position_x = 0
    
    def move_up(self) -> None:
        if self.position_y >= 0 and self.position_y <= 536:
            self.position_y -= 2
        elif self.position_y > 536:
            self.position_y = 536
        else:
            self.position_y = 0

    def move_down(self) -> None:
        if self.position_y >= 0 and self.position_y <= 536:
            self.position_y += 2
        elif self.position_y > 536:
            self.position_y = 536
        else:
            self.position_y = 0


class Enemy(Personaje):
    # Variable de clase para almacenar las instancias
    instancias = []

    def __init__(self, screen) -> None:
        super().__init__(screen)
        self.position_x = choice([32, 128, 224, 320, 416, 512, 608, 704])
        self.position_y = choice([32, 128, 224])
        __enemies_list = ["./images/nave-espacial.png", "./images/nave-extraterrestre.png", "./images/enemigo.png", "./images/astronave.png"]
        self.select_enemy = choice(__enemies_list)
        Enemy.instancias.append(self)

    def move_random_x(self) -> None:
        if self.position_x >= 0 and self.position_x <= 736:
            self.position_x += choice([-2,2])
        elif self.position_x > 736:
            self.position_x = 736
        else:
            self.position_x = 0


    def move_random_y(self) -> None: 
        if self.position_y >= 0 and self.position_y <= 536:
            self.position_y += choice([-2,2])
        elif self.position_y > 536:
            self.position_y = 536
        else:
            self.position_y = 0

