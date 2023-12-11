import pygame as p

WIDTH = 756
HEIGHT = 600

class Trashcan1(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 328
        self.y = 430
        self.vel = 4
        self.width = 100
        self.height = 150
        #self.score = 0
        self.lives = 3

        self.trashbin_1 = p.image.load('trashbin3.png')
        self.trashbin_1 = p.transform.scale(self.trashbin_1, (self.width, self.height))
        self.image = self.trashbin_1
        self.rect = self.image.get_rect()
        self.direction = 0

    def update(self):
        self.movement()
        self.rect.center = (self.x, self.y)
        self.correction()

    def movement(self):
        keys = p.key.get_pressed()
        if keys[p.K_LEFT]:
            self.x -= self.vel

        elif keys[p.K_RIGHT]:
            self.x += self.vel

    def correction(self):
        if self.x - self.width / 2 < 0:
            self.x = self.width / 2

        elif self.x + self.width / 2 > WIDTH:
            self.x = WIDTH - self.width / 2

        if self.y - self.height / 2 < 0:
            self.y = self.height / 2

        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2

class Trashcan2(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 428
        self.y = 430
        self.vel = 4
        self.width = 100
        self.height = 150
        self.lives = 3

        self.trashbin_2 = p.image.load('trashbin1).png')
        self.trashbin_2 = p.transform.scale(self.trashbin_2, (self.width, self.height))
        self.image = self.trashbin_2
        self.rect = self.image.get_rect()
        self.direction = 0

    def update(self):
        self.movement()
        self.rect.center = (self.x, self.y)
        self.correction()

    def movement(self):
        keys = p.key.get_pressed()
        if keys [p.K_a]:
            self.x -= self.vel

        elif keys [p.K_d]:
            self.x += self.vel

    def correction(self):
        if self.x - self.width / 2 < 0:
            self.x = self.width / 2 

        elif self.x + self.width / 2 > WIDTH:
            self.x = WIDTH - self.width / 2

        if self.y - self.height / 2 < 0:
            self.y = self.height / 2

        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2
