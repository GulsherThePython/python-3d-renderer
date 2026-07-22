from projection import project_points
from matrix import get_index_of_flat_matrix
from shapes import cube_edges
import pygame

def draw_wireframe(screen, vertices, fov, window_width, edges):
    projected_vertices = []
    for i in range(len(vertices) // 3):
        projected_vertices.append(
            project_points(
                [
                    vertices[get_index_of_flat_matrix(i, 0, 3)],
                    vertices[get_index_of_flat_matrix(i, 1, 3)],
                    vertices[get_index_of_flat_matrix(i, 2, 3)]
                ], fov, window_width
            )
        )

    for i in range(0, len(edges), 2):
        start_vertex = projected_vertices[edges[i]]
        end_vertex = projected_vertices[edges[i + 1]]

        if None not in start_vertex and None not in end_vertex:
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (start_vertex[0] + window_width / 2, start_vertex[1] + window_width / 2),
                (end_vertex[0] + window_width / 2, end_vertex[1] + window_width / 2)
            )