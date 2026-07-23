import pygame
from draw import draw_wireframe
from rotate import rotate_points_along_axes
from shapes import cube, cube_edges
from translate import translate_vertices
from matrix import get_index_of_flat_matrix

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

local_vertices = cube(10)
cube_position = [0, 0, 50]

angle = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    angle += 1

    # Rotate the cube vertices
    vertices = rotate_points_along_axes(local_vertices, angle, 0, 0)

    # Translate the cube to its position
    vertices = translate_vertices(vertices, cube_position)

    # Draw the cube wireframe
    draw_wireframe(screen, vertices, fov=90, window_width=400, edges=cube_edges())

    pygame.display.flip()
    clock.tick(60)