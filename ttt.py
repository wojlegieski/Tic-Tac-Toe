import pygame
import sys
import random
from pygame.locals import *
pygame.init()
width = 850
window = pygame.display.set_mode((width, width), 0, 32)
pygame.display.set_caption("trywialne.exe")
FPS = 60
fpsClock = pygame.time.Clock()
rows = 10
wincondition = 5
if rows < wincondition:
    sys.exit()
game = []
for somethink in range(rows ** 2):
    game.append(0)
move = random.randint(1, 2)  # 1- gracz 2 - komputer
score = 0  # 0 - gra trwa  1 - wygrał geazcz 3 - remis
end = False
bacckground_color = (5, 5, 5)
player_1_color = (0, 255, 0)
player_11_color = (255, 255, 0)
player_2_color = (255, 0, 0)
player_22_color = (0, 0, 255)
mesage_color = (25, 255, 25)
cyrcle_color = (200, 200, 100)
index_list = []
inedexs = []
for x in range(rows - (wincondition - 1)):
    for y in range(rows):
        indexs = []
        for index in range(wincondition):
            indexs.append(index + x + rows * y)
        index_list.append(indexs)
for x in range(rows):
    for y in range(rows - (wincondition - 1)):
        indexs = []
        for index in range(wincondition):
            indexs.append(index * rows + x + rows * y)
        index_list.append(indexs)
for x in range(rows - (wincondition - 1)):
    for y in range(rows - (wincondition - 1)):
        indexs = []
        for index in range(wincondition):
            indexs.append(index * (1 + rows) + x + rows * y)
        index_list.append(indexs)
for x in range(rows - (wincondition - 1)):
    for y in range(rows - (wincondition - 1)):
        indexs = []
        for index in range(wincondition):
            indexs.append(wincondition - 1 - index + rows * index + x + rows * y)
        index_list.append(indexs)
z1 = 0
z2 = 0
z3 = 0
c1 = 1
c2 = 1
c3 = 1

scall = int(rows / 25)


def print_line():
    for i in range(1, rows):
        position = width / rows * i
        pygame.draw.line(window, line_color, (0, position), (width, position), 5 - scall)
    for i in range(1, rows):
        position = width / rows * i
        pygame.draw.line(window, line_color2, (position, 0), (position, width), 5 - scall)
    for i1 in range(1, rows):
        for i2 in range(1, rows):
            position = width / rows * i1
            position2 = width / rows * i2
            pygame.draw.circle(window, cyrcle_color, (position, position2), 6 - scall)


rows_2 = 2 * rows
cyrcle_R = int(width / (rows * 2) - 1 - (5 - scall))


def print_marks():
    for y in range(0, rows):
        for x in range(0, rows):
            cell = y * rows + x
            cell_x = x * (width / rows) + (width / rows_2)
            cell_y = y * (width / rows) + (width / rows_2)
            if game[cell] == 1:
                for cyrcle in range(cyrcle_R):
                    pygame.draw.circle(window, player_1_color if cyrcle % 2 == 0 else player_11_color, (cell_y, cell_x),
                                       cyrcle_R - cyrcle)
            if game[cell] == 2:
                for cyrcle in range(cyrcle_R):
                    pygame.draw.circle(window, player_2_color if cyrcle % 2 == 0 else player_22_color, (cell_y, cell_x),
                                       cyrcle_R - cyrcle)


def ai_move(move):
    if 0 in game:
        while True:
            cell = random.randrange(0, 100)
            if game[cell] == 0:
                return mark(cell, move)


def mark(cell, move):
    if game[cell] == 0:
        if move == 1:
            game[cell] = 1
            return 2
        elif move == 2:
            game[cell] = 2
            return 1
    return move


def who_win(index):
    score = check(index)
    if score == 0 and 0 not in game:
        score = 3

    return score


def print_score(score):
    mesage = pygame.font.Font("OpenSans-Bold.ttf", 50)
    if score == 1:
        text = "wygrał 1"
    elif score == 2:
        text = "wygrał 2"
    elif score == 3:
        text = "remis"
    text_mesage = mesage.render(text, True, mesage_color)
    text_mesage_rect = text_mesage.get_rect()
    text_mesage_rect.center = (width / 2, width / 2)
    window.blit(text_mesage, text_mesage_rect)


def check(index):
    for num in range(wincondition):
        if not game[index[0]] == game[index[num]]:
            return 0
    return game[index[0]]


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if end is False:
            if move == 1:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouseX, mouseY = event.pos
                        y = int(mouseY / (width / rows))
                        x = int(mouseX / (width / rows))
                        cell = (x * rows + y)
                        move = mark(cell, move)
            elif move == 2:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouseX, mouseY = event.pos
                        y = int(mouseY / (width / rows))
                        x = int(mouseX / (width / rows))
                        cell = (x * rows + y)
                        move = mark(cell, move)
        for k in index_list:
            score = who_win(k)
            if score != 0:
                break
        if score != 0:
            end = True
    line_color = (z1, z2, z3)
    line_color2 = (255 - z1, 255 - z2, 255 - z3)
    if z1 == 255:
        c1 = 2
    if z1 == 0:
        c1 = 1
    if c1 == 1:
        z1 += 1
    if c1 == 2:
        z1 -= 1
    if z2 == 255:
        c2 = 2
    if z2 == 0:
        c2 = 1
    if z1 % 2 == 0 and c2 == 1:
        z2 += 1
    if z1 % 2 == 0 and c2 == 2:
        z2 -= 1
    if z3 == 255:
        c3 = 2
    if z3 == 0:
        c3 = 1
    if z1 % 3 == 0 and c3 == 1:
        z3 -= - 1
    if z1 % 3 == 0 and c3 == 2:
        z3 -= 1
    for gradiend in range(width):
        gradiend_c = (gradiend / width) * 255
        gradiend_color = (gradiend_c, z3, 255 - gradiend_c)

        pygame.draw.line(window, gradiend_color, (gradiend, width), (gradiend, 0), 1)
    print_line()
    print_marks()

    if end:
        print_score(score)
    fpsClock.tick(FPS)
    pygame.display.update()
