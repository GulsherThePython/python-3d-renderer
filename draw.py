from projection import project_points
from matrix import get_index_of_flat_matrix
import pygame

def draw_cube(screen, vertices, fov, window_width):
    projected_vertices = []
