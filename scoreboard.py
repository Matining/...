import pygame as p

WIDTH = 756
HEIGHT = 600

class Scoreboard:
    def __init__(self, x_position, initial_lives):
        self.score = 0
        self.lives = initial_lives
        self.font = p.font.Font("font.ttf", 16)
        self.x_position = x_position

    def increase_score(self, points):
        self.score += points
    
    def decrease_lives(self):
        self.lives -= 1

    def reset_score(self):
        self.score = 0
        self.lives = 3

    def display_score(self, screen):
        score_text = self.font.render("Score: {}".format(self.score), True, (255, 255, 255))
        lives_text = self.font.render("Lives: {}".format(self.lives), True, (255,255,255))
        screen.blit(score_text, (self.x_position, 10))
        screen.blit(lives_text, (self.x_position, 50))

    def display_game_over(self, screen):
        self.font = p.font.Font("font.ttf", 32)
        game_over_text = self.font.render("Game Over!", True, (255,25,0))
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 36))
