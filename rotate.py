from matrix import transform_3d_vector
from math import cos, sin, radians

def rotate_along_z(point, angle):
    theta = radians(angle)

    rotation_matrix = [
        cos(theta), -sin(theta), 0,
        sin(theta), cos(theta),  0,
        0,          0,           1
    ]

    return transform_3d_vector(rotation_matrix, point)

def rotate_along_x(point, angle):
    theta = radians(angle)

    rotation_matrix = [
        1, 0,          0,
        0, cos(theta), -sin(theta),
        0, sin(theta), cos(theta)
    ]

    return transform_3d_vector(rotation_matrix, point)

def rotate_along_y(point, angle):
    theta = radians(angle)

    rotation_matrix = [
        cos(theta),  0, sin(theta),
        0,           1, 0,
        -sin(theta), 0, cos(theta)
    ]

    return transform_3d_vector(rotation_matrix, point)