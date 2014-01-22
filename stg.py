# -*- coding:utf-8 -*-
import sys
import math
import random
import pygame
import pygame.locals

window_width = 640
window_height = 480

pygame.init()
screen = pygame.display.set_mode((window_width, window_height), 0, 32)
pygame.display.set_caption('STG')

clock = pygame.time.Clock()
time = 0
        
class PlayerBullet:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.die = False
    def move(self, passed):
        self.x += self.vx * passed
        self.y += self.vy * passed
        if self.x < 0 or self.x > window_width:
            self.die = True
        elif self.y < 0 or self.y > window_height:
            self.die = True
    def bound(self):
        return (self.x - 2, self.y - 2, self.x + 2, self.y + 2)
    def paint(self, screen):
        pygame.draw.circle(screen, [255, 255, 255], [int(self.x), int(self.y)], 5, 1)
        
player_bullet = []
        
class Player:
    def __init__(self):
        global window_width
        global window_height
        self.x = window_width / 2
        self.y = window_height / 2
        self.vx = 0
        self.vy = 0
        self.die = False
        self.life = 10
    def move(self, passed):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.locals.K_a]:
            self.vx -= 0.01 * passed
            if self.vx < -0.2:
                self.vx = -0.2
        elif pressed[pygame.locals.K_d]:
            self.vx += 0.01 * passed
            if self.vx > 0.2:
                self.vx = 0.2
        else:
            self.vx *= 0.4
        if pressed[pygame.locals.K_w]:
            self.vy -= 0.01 * passed
            if self.vy < -0.2:
                self.vy = -0.2
        elif pressed[pygame.locals.K_s]:
            self.vy += 0.01 * passed
            if self.vy > 0.2:
                self.vy = 0.2
        else:
            self.vy *= 0.4
        self.x += self.vx * passed
        self.y += self.vy * passed
        if self.x - 8 < 0:
            self.x = 8
        elif self.x + 8 > window_width:
            self.x = window_width - 8
        if self.y - 8 < 0:
            self.y = 8
        elif self.y + 8 > window_height:
            self.y = window_height - 8
        global player_bullet
        [x, y] = pygame.mouse.get_pos()
        angle = math.atan2(y - self.y, x - self.x)
        bullet = PlayerBullet()
        bullet.x = self.x
        bullet.y = self.y
        bullet.vx = random.uniform(0.7, 0.8) * math.cos(angle)
        bullet.vy = random.uniform(0.7, 0.8) * math.sin(angle)
        player_bullet.append(bullet)
    def bound(self):
        return (self.x - 4, self.y - 4, self.x + 4, self.y + 4)
    def paint(self, screen):
        pygame.draw.circle(screen, [255, 255, 255], [int(self.x), int(self.y)], 8, 2)

player = Player()

class EnemyBullet:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.die = False
    def move(self, passed):
        self.x += self.vx * passed
        self.y += self.vy * passed
        if self.x < 0 or self.x > window_width:
            self.die = True
        elif self.y < 0 or self.y > window_height:
            self.die = True
    def bound(self):
        return (self.x - 5, self.y - 5, self.x + 10, self.y + 10)
    def paint(self, screen):
        pygame.draw.rect(screen, [255, 255, 255], [int(self.x - 5), int(self.y - 5), 10, 10], 0)

enemy_bullet = []
        
class Enemy:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.die = False
        self.life = 30
    def move(self, passed):
        self.x += self.vx * passed
        self.y += self.vy * passed
        if self.x < 20:
            self.vx = math.fabs(self.vx)
        elif self.x > window_width - 20:
            self.vx = -math.fabs(self.vx)
        if self.y < 20:
            self.vy = math.fabs(self.vy)
        elif self.y > window_height - 20:
            self.vy = -math.fabs(self.vy)
        global player
        global enemy_bullet
        if random.randint(0, 300) == 0:
            angle = math.atan2(player.y - self.y, player.x - self.x)
            bullet = EnemyBullet()
            bullet.x = self.x
            bullet.y = self.y
            bullet.vx = 0.1 * math.cos(angle)
            bullet.vy = 0.1 * math.sin(angle)
            enemy_bullet.append(bullet)
    def bound(self):
        return (self.x - 20, self.y - 20, self.x + 20, self.y + 20)
    def paint(self, screen):
        pygame.draw.rect(screen, [255, 255, 255], [int(self.x - 20), int(self.y - 20), 40, 40], 2)
        
enemy_list = []
        
current_wave = 0
max_wave = 0

def next_wave():
    global enemy_list
    global current_wave
    global max_wave
    if len(enemy_list) == 0:
        current_wave += 1
        if current_wave > max_wave:
            max_wave = current_wave
        if current_wave == 1:
            enemy = Enemy()
            enemy.x = 0
            enemy.y = 0
            enemy.vx = 0.05
            enemy.vy = 0.05
            enemy_list.append(enemy)
            enemy = Enemy()
            enemy.x = window_width
            enemy.y = 0
            enemy.vx = -0.05
            enemy.vy = 0.05
            enemy_list.append(enemy)
            enemy = Enemy()
            enemy.x = 0
            enemy.y = window_height
            enemy.vx = 0.05
            enemy.vy = -0.05
            enemy_list.append(enemy)
            enemy = Enemy()
            enemy.x = window_width
            enemy.y = window_height
            enemy.vx = -0.05
            enemy.vy = -0.05
            enemy_list.append(enemy)
        else:
            current_wave -= 1
            
def inside(point, rect):
    return point[0] > rect[0] and point[0] < rect[2] and point[1] > rect[1] and point[1] < rect[3]
            
def intersect(rect1, rect2):
    return inside([rect1[0], rect1[1]], rect2) or inside([rect1[2], rect1[1]], rect2) or inside([rect1[0], rect1[3]], rect2) or inside([rect1[2], rect1[3]], rect2) or inside([rect2[0], rect2[1]], rect1) or inside([rect2[2], rect2[1]], rect1) or inside([rect2[0], rect2[3]], rect1) or inside([rect2[2], rect2[3]], rect1)
        
while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            sys.exit()
        elif event.type == pygame.locals.KEYUP:
             if player.die:
                player.die = False
                player.x = window_width / 2
                player.y = window_height / 2
                player.vx = 0
                player.vy = 0
                current_wave = 0
                enemy_list = []
                player_bullet = []
                enemy_bullet = []
    passed = clock.tick(30)
    time += passed
    if not player.die:
        for bullet in player_bullet:
            bullet.move(passed)
            if bullet.die:
                player_bullet.remove(bullet)
        for bullet in enemy_bullet:
            bullet.move(passed)
            if bullet.die:
                enemy_bullet.remove(bullet)
        for enemy in enemy_list:
            enemy.move(passed)
        for enemy in enemy_list:
            for bullet in player_bullet:
                if intersect(enemy.bound(), bullet.bound()):
                    player_bullet.remove(bullet)
                    enemy.life -= 1
                    if enemy.life <= 0:
                        enemy.die = True
            if enemy.die:
                enemy_list.remove(enemy)
        player.move(passed)
        for bullet in enemy_bullet:
            if intersect(player.bound(), bullet.bound()):
                enemy_bullet.remove(bullet)
                player.life -= 1
                if player.life <= 0:
                    player.die = True
        pygame.draw.rect(screen, [0, 0, 0], [0, 0, window_width, window_height], 0)
        for bullet in player_bullet:
            bullet.paint(screen)
        for bullet in enemy_bullet:
            bullet.paint(screen)
        for enemy in enemy_list:
            enemy.paint(screen)
        player.paint(screen)
        font = pygame.font.SysFont("Consolas", 16)
        current_wave_text = font.render("Current Wave: " + str(current_wave), 1, (255, 255, 255))
        max_wave_text = font.render("Max Wave: " + str(max_wave), 1, (255, 255, 255))
        player_life_text = font.render("Life: " + str(player.life), 1, (255, 255, 255))
        time_text = font.render("Time: " + str(time), 1, (255, 255, 255))
        screen.blit(current_wave_text, (10, 10))
        screen.blit(max_wave_text, (10, 30))
        screen.blit(player_life_text, (10, 50))
        screen.blit(time_text, (10, 70))
        next_wave()
    pygame.display.update()