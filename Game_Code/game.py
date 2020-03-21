import pygame, random
from car import Car
from bullets import bullet
from booster import boost
import random

pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 242, 0)

SCREENWIDTH = 800
SCREENHEIGHT = 800

player_score = 0
player_health = 100

OBSTACLE_DAMAGE = 10
BOOSTERS_POINT = 10
SURVIVAL_POINT = 1
BOOSTER_HEATH_GAIN = 5

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")

font = pygame.font.Font("freesansbold.ttf", 32)

all_sprites_list = pygame.sprite.Group()
obstacleles_list_above = pygame.sprite.Group()
obstacleles_list_side = pygame.sprite.Group()
boosters = pygame.sprite.Group()

playerCar = Car(RED, 40, 40, 300, 300)

all_sprites_list.add(playerCar)


carryOn = True
clock = pygame.time.Clock()


def send_player_game_data(
    player_health,
    player_score,
    obstacleles_list_above,
    obstacleles_list_side,
    playerCar,
    boosters,
):
    file = open("game_data.txt", "a")

    file.write(str(player_health) + " " + str(player_score) + "\n")

    for i in obstacleles_list_above:
        file.write(
            str(i.rect.x)
            + " "
            + str(i.rect.y)
            + " "
            + str(i.speed)
            + " "
            + str(i.angle)
            + " "
        )

    file.write("\n")

    for i in obstacleles_list_side:
        file.write(
            str(i.rect.x)
            + " "
            + str(i.rect.y)
            + " "
            + str(i.speed)
            + " "
            + str(i.angle)
            + " "
        )

    file.write("\n")

    for i in boosters:
        file.write(str(i.rect.x) + " " + str(i.rect.y) + " ")

    file.write("\n --end-- \n")
    file.close()


def check_collission(s1, s2):
    return pygame.sprite.collide_rect(s1, s2)


def game_manage(
    all_sprites_list, obstacleles_list_side, obstacleles_list_above, boosters_list
):
    global player_health, player_score

    booster_count = 0
    bullet_count = 0

    if len(obstacleles_list_side) < 5:
        obstacle = bullet(
            RED,
            15,
            15,
            random.choice([1, 799]),
            random.randrange(1, 800),
            random.randrange(0, 360),
            random.randrange(2, 5),
        )
        obstacleles_list_side.add(obstacle)
    if len(obstacleles_list_side) < 5:
        obstacle = bullet(
            RED,
            15,
            15,
            random.randrange(1, 800),
            random.choice([1, 799]),
            random.randrange(0, 360),
            random.randrange(2, 5),
        )
        obstacleles_list_above.add(obstacle)

    if len(boosters) < 2:
        boost_sprite = boost(YELLOW, 20, 20, 0, random.randrange(0, 799))
        boosters.add(boost_sprite)

    for i in boosters:
        if check_collission(playerCar, i):
            i.destroy()
            booster_count = booster_count + 1

    for i in obstacleles_list_above:
        if check_collission(playerCar, i):
            i.destroy()
            bullet_count = bullet_count + 1

    for i in obstacleles_list_side:
        if check_collission(playerCar, i):
            i.destroy()
            bullet_count = bullet_count + 1

    player_health = player_health - OBSTACLE_DAMAGE * bullet_count
    player_score = player_score - OBSTACLE_DAMAGE * bullet_count

    player_health = player_health + BOOSTER_HEATH_GAIN * booster_count
    player_score = player_score + BOOSTERS_POINT * booster_count
    player_score = player_score + SURVIVAL_POINT / 200


while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    keys = pygame.key.get_pressed()

    game_manage(
        all_sprites_list, obstacleles_list_side, obstacleles_list_above, boosters
    )
    all_sprites_list.update(keys)
    obstacleles_list_above.update()
    obstacleles_list_side.update()
    boosters.update()

    screen.fill(GREEN)

    all_sprites_list.draw(screen)
    obstacleles_list_above.draw(screen)
    obstacleles_list_side.draw(screen)
    boosters.draw(screen)

    send_player_game_data(
        player_health,
        player_score,
        obstacleles_list_above,
        obstacleles_list_side,
        playerCar,
        boosters,
    )

    pygame.display.flip()

    clock.tick(200)

pygame.quit()
