import pygame
from scene import render_scene
from shapes import cube, cube_edges

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

cube1 = {
    "vertices": cube(10),
    "edges": cube_edges(),
    "position": [0, 0, 50],
    "angle": 0
}

scene = [cube1]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    cube1["angle"] += 1

    render_scene(scene, screen)

    pygame.display.flip()
    clock.tick(60)