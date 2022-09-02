import pygame
import time
import random
import os
import math

import bind_change
from settings import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Pong")
clock = pygame.time.Clock()

right_gol = 0
left_gol = 0



def pause_menu():
    screen.fill(MAP_COLOR)
    font = pygame.font.Font(None, 72)
    text = font.render('Пауза', True, BALL_COLOR)
    place = text.get_rect(center=(WIDTH / 2, 50))
    screen.blit(text, place)

    font1 = pygame.font.Font(None, 50)

    mouse = pygame.mouse.get_pos()

    if WIDTH / 2 - 250 <= mouse[0] <= WIDTH / 2 + 250 and HEIGHT / 2 - 150 <= mouse[1] <= HEIGHT / 2 - 50:
        pygame.draw.rect(screen, LIGHT_COLOR, (WIDTH // 2 - 250, HEIGHT // 2 - 150, 500, 100))

    else:
        pygame.draw.rect(screen, BALL_COLOR, (WIDTH // 2 - 250, HEIGHT // 2 - 150, 500, 100))

    if WIDTH / 2 - 250 <= mouse[0] <= WIDTH / 2 + 250 and HEIGHT / 2 - 0 <= mouse[1] <= HEIGHT / 2 + 100:
        pygame.draw.rect(screen, LIGHT_COLOR, (WIDTH // 2 - 250, HEIGHT // 2 - 0, 500, 100))

    else:
        pygame.draw.rect(screen, BALL_COLOR, (WIDTH // 2 - 250, HEIGHT // 2 - 0, 500, 100))

    text1 = font1.render('Продолжить', True, MAP_COLOR)
    place1 = text1.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))
    screen.blit(text1, place1)

    text2 = font1.render('Вернуться в меню', True, MAP_COLOR)
    place2 = text2.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
    screen.blit(text2, place2)


def start_menu():
    screen.fill(MAP_COLOR)
    font = pygame.font.Font(None, 72)
    text = font.render('Game of Pong', True, BALL_COLOR)
    place = text.get_rect(center=(WIDTH / 2, 50))
    screen.blit(text, place)

    font1 = pygame.font.Font(None, 50)

    mouse = pygame.mouse.get_pos()

    if WIDTH / 2 - 250 <= mouse[0] <= WIDTH / 2 + 250 and HEIGHT / 2 - 150 <= mouse[1] <= HEIGHT / 2 - 50:
        pygame.draw.rect(screen, LIGHT_COLOR, (WIDTH // 2 - 250, HEIGHT // 2 - 150, 500, 100))

    else:
        pygame.draw.rect(screen, BALL_COLOR, (WIDTH // 2 - 250, HEIGHT // 2 - 150, 500, 100))


    if WIDTH / 2 - 250 <= mouse[0] <= WIDTH / 2 + 250 and HEIGHT / 2 - 0 <= mouse[1] <= HEIGHT / 2 + 100:
        pygame.draw.rect(screen, LIGHT_COLOR, (WIDTH // 2 - 250, HEIGHT // 2 - 0, 500, 100))

    else:
        pygame.draw.rect(screen, BALL_COLOR, (WIDTH // 2 - 250, HEIGHT // 2 - 0, 500, 100))


    text1 = font1.render('Играть', True, MAP_COLOR)
    place1 = text1.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))
    screen.blit(text1, place1)

    text2 = font1.render('Настройки', True, MAP_COLOR)
    place2 = text2.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
    screen.blit(text2, place2)


def settings_menu():
    print(bind_change.ula)


def player_win(side):

    global cheker
    screen.fill(MAP_COLOR)
    font = pygame.font.Font(None, 72)
    if side == 'left':
        text = font.render('Игрок 1 - выйграл!', True, BALL_COLOR)
    else:
        text = font.render('Игрок 2 - выйграл!', True, BALL_COLOR)
    place = text.get_rect(center=(WIDTH / 2, 50))
    screen.blit(text, place)

    font1 = pygame.font.Font(None, 50)

    mouse = pygame.mouse.get_pos()

    if WIDTH / 2 - 250 <= mouse[0] <= WIDTH / 2 + 250 and HEIGHT / 2 - 150 <= mouse[1] <= HEIGHT / 2 - 50:
        pygame.draw.rect(screen, LIGHT_COLOR, (WIDTH // 2 - 250, HEIGHT // 2 - 150, 500, 100))

    else:
        pygame.draw.rect(screen, BALL_COLOR, (WIDTH // 2 - 250, HEIGHT // 2 - 150, 500, 100))

    if WIDTH / 2 - 250 <= mouse[0] <= WIDTH / 2 + 250 and HEIGHT / 2 - 0 <= mouse[1] <= HEIGHT / 2 + 100:
        pygame.draw.rect(screen, LIGHT_COLOR, (WIDTH // 2 - 250, HEIGHT // 2 - 0, 500, 100))

    else:
        pygame.draw.rect(screen, BALL_COLOR, (WIDTH // 2 - 250, HEIGHT // 2 - 0, 500, 100))

    text1 = font1.render('Играть ещё', True, MAP_COLOR)
    place1 = text1.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))
    screen.blit(text1, place1)

    text2 = font1.render('Вернуться в меню', True, MAP_COLOR)
    place2 = text2.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
    screen.blit(text2, place2)




def check_goal(player):
    global right_gol, left_gol
    if player == 'left':
        print('Игрок 2 забил гол!!!')

        time.sleep(2)
        right_gol += 1

        ball = Ball()
        all_sprites.add(ball)
        ball_sprites.add(ball)

    if player == 'right':
        global left_gol
        print('Игрок 1 забил гол!!!')

        time.sleep(2)
        left_gol += 1

        ball = Ball()
        all_sprites.add(ball)
        ball_sprites.add(ball)

    if player == 'None':
        return [left_gol, right_gol]



class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([60, 60])
        self.image.set_colorkey(BLACK)
        pygame.draw.circle(self.image, BALL_COLOR, (30, 30), 30)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0
        self.MOVING = 'start'

    def update(self):
        global left_gol, right_gol
        if left_gol == 7 or right_gol == 7:
            self.kill()

        self.speedx = -10
        self.speedy = 0


        # находим координаты мяча
        self.ball_top = self.rect.top
        self.ball_bottom = self.rect.bottom
        self.ball_left = self.rect.left
        self.ball_right = self.rect.right

        # находим координаты игроков
        self.left_player_top = player.rect.top
        self.left_player_bottom = player.rect.bottom
        self.left_player_left = player.rect.left
        self.left_player_right = player.rect.right

        self.right_player_top = mob.rect.top
        self.right_player_bottom = mob.rect.bottom
        self.right_player_left = mob.rect.left
        self.right_player_right = mob.rect.right


        self.side_moving = 'stay'
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.side_moving = 'left'

        if keystate[pygame.K_RIGHT]:
            self.side_moving = 'right'



        self.mob_moving = 'stay'

        if keystate[pygame.K_a]:
            self.mob_moving = 'left'

        if keystate[pygame.K_d]:
            self.mob_moving = 'right'


        # Коснулся левой ракетки
        if (self.ball_left <= 75) and (self.ball_left >= 73):
            if (self.ball_top > self.left_player_top and self.ball_top < self.left_player_bottom) or (self.ball_bottom < self.left_player_bottom and self.ball_bottom > self.left_player_top):

                if self.side_moving == 'right':
                    self.MOVING = 'left+right'
                elif self.side_moving == 'left':
                    self.MOVING = 'left+left'
                else:
                    if self.MOVING == 'top+right' or self.MOVING == 'top+left':
                        self.MOVING = 'left+top'
                    if self.MOVING == 'bottom+right' or self.MOVING == 'bottom+left':
                        self.MOVING = 'left+bottom'
                    if self.MOVING == 'start':
                        self.MOVING = 'left'
                    if self.MOVING == 'right' or self.MOVING == 'right+bottom' or self.MOVING == 'right+top' or \
                            self.MOVING == 'right+right' or self.MOVING == 'right+left':
                        self.MOVING = 'left'



        # Коснулся правой ракетки
        elif (self.ball_right >= WIDTH - 75) and (self.ball_right <= WIDTH - 73):
            if (self.ball_top > self.right_player_top and self.ball_top < self.right_player_bottom) or (self.ball_bottom < self.right_player_bottom and self.ball_bottom > self.right_player_top):
                if self.mob_moving == 'right':
                    self.MOVING = 'right+right'
                elif self.mob_moving == 'left':
                    self.MOVING = 'right+left'
                else:
                    if self.MOVING == 'top+left' or self.MOVING == 'top+right':
                        self.MOVING = 'right+top'
                    if self.MOVING == 'bottom+left' or self.MOVING == 'bottom+right':
                        self.MOVING = 'right+bottom'
                    if self.MOVING == 'left' or self.MOVING == 'left+bottom' or self.MOVING == 'left+top' or \
                            self.MOVING == 'left+right' or self.MOVING == 'left+left':
                        self.MOVING = 'right'


        # Коснулся верха
        elif (self.ball_top <= 0 + 5) and (self.ball_top >= 0 + 3):
            if 'left' in self.MOVING:
                self.MOVING = 'top+left'
            else:
                self.MOVING = 'top+right'


        # Коснулся низа
        elif (self.ball_bottom >= HEIGHT - 5) and (self.ball_bottom <= HEIGHT - 3):
            if 'left' in self.MOVING and 'right+left' not in self.MOVING:
                self.MOVING = 'bottom+left'
            else:
                self.MOVING = 'bottom+right'

        elif self.ball_left < -10:
            self.kill()
            check_goal('left')

        elif self.ball_right > WIDTH + 10:
            self.kill()
            check_goal('right')


        # левая ракетка
        if self.MOVING == 'left':
            self.speedx = -self.speedx
            self.speedy = int(-self.speedy)

            self.rect.x += self.speedx
            self.rect.y += self.speedy

        elif self.MOVING == 'left+top':
            self.speedx = -self.speedx
            self.speedy = BALL_SPEED

            self.rect.x += self.speedx
            self.rect.y += self.speedy

        elif self.MOVING == 'left+bottom':
            self.speedx = -self.speedx
            self.speedy = BALL_SPEED

            self.rect.x += self.speedx
            self.rect.y += self.speedy

        elif self.MOVING == 'left+right':
            self.speedx = int(-self.speedx)
            self.speedy = BALL_SPEED

            self.rect.x += self.speedx
            self.rect.y += self.speedy

        elif self.MOVING == 'left+left':
            self.speedx = int(-self.speedx)
            self.speedy = -BALL_SPEED

            self.rect.x += self.speedx
            self.rect.y += self.speedy


        # Правая ракетка
        elif self.MOVING == 'right+top':
            self.speedx = self.speedx
            self.speedy = BALL_SPEED

            self.rect.x += self.speedx
            self.rect.y += self.speedy

        elif self.MOVING == 'right+bottom':
            self.speedx = self.speedx
            self.speedy = -BALL_SPEED

            self.rect.x += self.speedx
            self.rect.y += self.speedy

        elif self.MOVING == 'right+right':
            self.speedx = int(self.speedx)
            self.speedy = -BALL_SPEED

            self.rect.x += self.speedx
            self.rect.y += self.speedy

        elif self.MOVING == 'right+left':
            self.speedx = int(self.speedx)
            self.speedy = BALL_SPEED

            self.rect.x += self.speedx
            self.rect.y += self.speedy

        elif self.MOVING == 'right':
            self.speedx = self.speedx
            self.speedy = 0

            self.rect.x += self.speedx
            self.rect.y += self.speedy


        # Вверх
        elif self.MOVING == 'top+left':
            self.speedx = -self.speedx
            self.speedy = BALL_SPEED

            self.rect.x += self.speedx
            self.rect.y += self.speedy

        elif self.MOVING == 'top+right':
            self.speedx = self.speedx
            self.speedy = BALL_SPEED

            self.rect.x += self.speedx
            self.rect.y += self.speedy


        # Низ
        elif self.MOVING == 'bottom+left':
            self.speedx = -self.speedx
            self.speedy = -BALL_SPEED

            self.rect.x += self.speedx
            self.rect.y += self.speedy

        elif self.MOVING == 'bottom+right':
            self.speedx = self.speedx
            self.speedy = -BALL_SPEED

            self.rect.x += self.speedx
            self.rect.y += self.speedy

        # Просто летит
        else:
            self.rect.y += self.speedy
            self.rect.x += self.speedx






class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 200))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - 50, HEIGHT / 2)


    def update(self, number=None):
        self.speed = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        self.speed = 5

        if keystate[pygame.K_a]:
            self.speedy = self.speed
        if keystate[pygame.K_d]:
            self.speedy = -self.speed

        self.rect.y += self.speedy

        if self.rect.top < 5:
            self.rect.top = 5
        if self.rect.bottom > HEIGHT - 5:
            self.rect.bottom = HEIGHT - 5


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 200))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (0 + 50, HEIGHT / 2)

    def update(self):
        self.speed = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        self.speed = 5

        if keystate[pygame.K_LEFT]:
            self.speedy = -self.speed
        if keystate[pygame.K_RIGHT]:
            self.speedy = self.speed

        self.rect.y += self.speedy

        if self.rect.top < 5:
            self.rect.top = 5
        if self.rect.bottom > HEIGHT - 5:
            self.rect.bottom = HEIGHT - 5



all_sprites = pygame.sprite.Group()
ball_sprites = pygame.sprite.Group()
mob_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)


ball = Ball()
all_sprites.add(ball)
ball_sprites.add(ball)

mob = Mob()
all_sprites.add(mob)
mob_sprites.add(mob)

cheker = 0
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_ESCAPE]:
        cheker = 300

    if cheker == 200:

        if goal_table[0] == 7:
            side = 'left'
        else:
            side = 'right'

        player_win(side)
        right_gol = 0
        left_gol = 0
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if WIDTH / 2 - 250 <= mouse[0] <= WIDTH / 2 + 250 and HEIGHT / 2 - 150 <= mouse[1] <= HEIGHT / 2 - 50:
                cheker = 1
                time.sleep(1)

            if WIDTH / 2 - 250 <= mouse[0] <= WIDTH / 2 + 250 and HEIGHT / 2 - 0 <= mouse[1] <= HEIGHT / 2 + 100:
                cheker = 0
                time.sleep(1)
        else:
            pass

    elif cheker == 300:
        pause_menu()

        mouse = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if WIDTH / 2 - 250 <= mouse[0] <= WIDTH / 2 + 250 and HEIGHT / 2 - 150 <= mouse[1] <= HEIGHT / 2 - 50:
                cheker = 1
                time.sleep(1)

            if WIDTH / 2 - 250 <= mouse[0] <= WIDTH / 2 + 250 and HEIGHT / 2 - 0 <= mouse[1] <= HEIGHT / 2 + 100:
                cheker = 0
                time.sleep(1)
                right_gol = 0
                left_gol = 0

    elif cheker == 0:
        start_menu()

        mouse = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if WIDTH / 2 - 250 <= mouse[0] <= WIDTH / 2 + 250 and HEIGHT / 2 - 150 <= mouse[1] <= HEIGHT / 2 - 50:
                cheker = 1

            if WIDTH / 2 - 250 <= mouse[0] <= WIDTH / 2 + 250 and HEIGHT / 2 - 0 <= mouse[1] <= HEIGHT / 2 + 100:
                cheker = 2


    elif cheker == 2:
        settings_menu()
        print('tap to settings')
        time.sleep(1)
        cheker = 1


    elif cheker == 1:
        all_sprites.update()


        # map
        screen.fill(MAP_COLOR)
        pygame.draw.rect(screen, WHITE,
                        (0, 0, WIDTH, HEIGHT), 5)
        pygame.draw.line(screen, WHITE,
                        [WIDTH / 2, 0],
                        [WIDTH / 2, HEIGHT], 5)
        pygame.draw.circle(screen, WHITE,
                        (WIDTH / 2, HEIGHT / 2), 150, 5)

        goal_table = check_goal('None')
        if goal_table[0] == 7 or goal_table[1] == 7:
            cheker = 200

        left_number = pygame.font.Font(None, 72)
        number1 = left_number.render(str(goal_table[0]), True,
                          (0, 0, 0))

        right_number = pygame.font.Font(None, 72)
        number2 = right_number.render(str(goal_table[1]), True,
                                     (0, 0, 0))

        screen.blit(number1, (100, 50))
        screen.blit(number2, (WIDTH - 100, 50))

        all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()