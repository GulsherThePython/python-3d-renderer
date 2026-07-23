import pygame
from draw import draw_wireframe
import draw
from rotate import rotate_along_z, rotate_along_x, rotate_along_y
from shapes import cube, cube_edges
from translate import translate_vertices
from matrix import get_index_of_flat_matrix

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

local_vertices = cube(10)
cube_position = [0, 0, 50]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    vertices = translate_vertices(local_vertices, cube_position)
    draw_wireframe(screen, vertices, 60, 400, cube_edges())

    for i in range(len(local_vertices) // 3):
        point = [
            local_vertices[get_index_of_flat_matrix(i, 0, 3)],
            local_vertices[get_index_of_flat_matrix(i, 1, 3)],
            local_vertices[get_index_of_flat_matrix(i, 2, 3)]
        ]

        rotated_point = rotate_along_x(point, 1)
        rotated_point = rotate_along_y(rotated_point, 1)
        rotated_point = rotate_along_z(rotated_point, 1)

        local_vertices[get_index_of_flat_matrix(i, 0, 3)] = rotated_point[0]
        local_vertices[get_index_of_flat_matrix(i, 1, 3)] = rotated_point[1]
        local_vertices[get_index_of_flat_matrix(i, 2, 3)] = rotated_point[2]

    pygame.display.flip()
    clock.tick(60)