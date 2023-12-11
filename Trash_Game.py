import pygame as p
from button_main import button
from Trashcans import Trashcan1, Trashcan2
from garbage import Garbage
from scoreboard import Scoreboard

GoodTrash = ['battery.png', 'glassbtl.png', 'plasticbag.png', 'plasticbtl.png'] 
BadTrash = ['apple.png', 'banana.png', 'pizza.png', 'vegetable.png']

p.init()

WIDTH = 756
HEIGHT = 600

background = p.image.load('garbagepic.jpg')
screen = p.display.set_mode((WIDTH, HEIGHT))

p.display.set_caption("Trash Game")
icon = p.image.load('catt.jpg')
p.display.set_icon(icon)

clock = p.time.Clock()

scoreboard1 = Scoreboard(10, 3)
scoreboard2 = Scoreboard(WIDTH - 150, 3)

trash1 = Trashcan1()
trash1_group = p.sprite.Group()
trash1_group.add(trash1)

trash2 = Trashcan2()
trash2_group = p.sprite.Group()
trash2_group.add(trash2)

garbage_group = p.sprite.Group()

all_sprites = p.sprite.Group()
good_images_group = p.sprite.Group()
bad_images_group = p.sprite.Group()

for _ in range(1):
    good_trash = Garbage(True, GoodTrash)
    good_images_group.add(good_trash)
    all_sprites.add(good_trash)

    bad_trash = Garbage(False, BadTrash)
    bad_images_group.add(bad_trash)
    all_sprites.add(bad_trash)

run = True
paused = False
game_over = False

while run:
    
    clock.tick(60)

    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
        elif event.type == p.KEYDOWN:
            if event.key == p.K_p:
                paused = not paused

    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    if not paused:

        trash1_group.draw(screen)
        trash1_group.update()

        trash2_group.draw(screen)
        trash2_group.update()

        garbage_group.draw(screen)
        garbage_group.update(trash1, trash2)

        all_sprites.update()

        good_trash_collisions1 = p.sprite.spritecollide(trash1, good_images_group, True)
        bad_trash_collisions1 = p.sprite.spritecollide(trash1, bad_images_group, True)

        good_trash_collisions2 = p.sprite.spritecollide(trash2, good_images_group, True)
        bad_trash_collisions2 = p.sprite.spritecollide(trash2, bad_images_group, True)

        if good_trash_collisions1:
            scoreboard1.increase_score(1)
        elif bad_trash_collisions1:
            scoreboard1.decrease_lives()

        if good_trash_collisions2:
            scoreboard2.decrease_lives()
        elif bad_trash_collisions2:
            scoreboard2.increase_score(1)
        
        scoreboard1.display_score(screen)
        scoreboard2.display_score(screen)

        if scoreboard1.lives == 0 or scoreboard2.lives == 0:
            scoreboard1.display_game_over(screen)
            game_over = True

        if len(good_images_group) < 1:
            new_good_trash = Garbage(True, GoodTrash)
            good_images_group.add(new_good_trash)
            all_sprites.add(new_good_trash)

        if len(bad_images_group) < 1:
            new_bad_trash = Garbage(False, BadTrash)
            bad_images_group.add(new_bad_trash)
            all_sprites.add(new_bad_trash)

        all_sprites.draw(screen)

    else:
        paused_font = p.font.Font("font.ttf", 52)
        paused_text = paused_font.render("Paused", True, (255,192,0))
        screen.blit(paused_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))

    p.display.update()
    
p.quit()