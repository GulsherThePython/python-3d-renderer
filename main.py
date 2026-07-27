import pygame
from camera import handle_camera_movement, handle_camera_rotation
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

cube2 = {
    "vertices": cube(5),
    "edges": cube_edges(),
    "position": [10, 0, 50],
    "angle": 0
}

scene = [cube1, cube2]

camera = {
    "position": [0, 0, 0],
    "rotation": [0, 0, 0]
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    handle_camera_movement(camera)

    handle_camera_rotation(camera)

    render_scene(scene, screen, camera)

    pygame.display.flip()
    clock.tick(60)