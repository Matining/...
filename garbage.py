import pygame as p
import random

WIDTH = 756
HEIGHT = 600

paused = False
game_over = False

class Garbage(p.sprite.Sprite):
    def __init__(self, is_good, images):
        super().__init__()
        self.is_good = is_good
        self.images = [p.image.load(python)for python in images]
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-self.rect.height, -60)
        self.speed_y = random.randint(1, 3)
        self.appearance_interval = 3000
        self.appearance_time = 0
        self.trashcan1 = None
        self.trashcan2 = None

    def update(self):
        if not game_over and not paused:
            current_time = p.time.get_ticks()

            if current_time - self.appearance_time > self.appearance_interval:
                self.rect.y += self.speed_y

            if self.rect.y > HEIGHT:
                if self.is_good:
                    self.trashcan1.lives -= 1
                else:
                    self.trashcan2.lives -= 1
                    
                self.rect.y = random.randint(-self.rect.height, -60)
                self.rect.x = random.randint(0, WIDTH - self.rect.width)
                self.speed_y = random.randint(1, 1)
                self.appearance_time = p.time.get_ticks()
