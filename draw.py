from projection import project_points
from matrix import get_index_of_flat_matrix
from shapes import cube_edges
import pygame

def draw_cube(screen, vertices, fov, window_width):
    projected_vertices = []
    for vertex in vertices:
        projected_vertices.append(project_points((vertex[0], vertex[1], vertex[2]), fov, window_width))

    edges = cube_edges()
    