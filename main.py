from pygame import *
from random import randint

FPS = 60
PLAYER_SPEED = 5
PLAYER_SIZE = 50
OBSTACLE_SIZE = 50

obstacle_speed = 3
is_game_over = False

window_size = 800, 600
window = display.set_mode(window_size)
clock = time.Clock()


def spawn_obstacle(count, obstacles):
    for _ in range(count):
        obstacles.append(
            Rect(randint(0, window_size[0] - OBSTACLE_SIZE),
                 randint(-600, -100),
                 OBSTACLE_SIZE, OBSTACLE_SIZE))
    return obstacles


player = Rect(0, window_size[1]-PLAYER_SIZE, 50, 50)
obstacles = spawn_obstacle(5, [])

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
    keys = key.get_pressed()
    if not is_game_over:
        window.fill('light green')

        if keys[K_d]: player.x += PLAYER_SPEED
        if keys[K_a]: player.x -= PLAYER_SPEED

        draw.rect(window, 'sky blue', player)

        for obstacle in obstacles[:]:
            obstacle.y += obstacle_speed
            draw.rect(window, 'red', obstacle)
            if obstacle.colliderect(player):
                is_game_over = True
            if obstacle.y >= window_size[1]:
                obstacles.remove(obstacle)
        if not obstacles: obstacles = spawn_obstacle(randint(4, 8), obstacles)

    if is_game_over:
        window.fill('red')
        if keys[K_r]:
            is_game_over = False
            obstacles = spawn_obstacle(5, [])
            player.x = 0


    display.update()
    clock.tick(FPS)
