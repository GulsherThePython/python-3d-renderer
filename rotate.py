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

def rotate_points_along_axes(vertices, angle_x, angle_y, angle_z):
    rotated_vertices = []
    for i in range(len(vertices) // 3):
        point = [
            vertices[i * 3],
            vertices[i * 3 + 1],
            vertices[i * 3 + 2]
        ]

        rotated_point = rotate_along_x(point, angle_x)
        rotated_point = rotate_along_y(rotated_point, angle_y)
        rotated_point = rotate_along_z(rotated_point, angle_z)

        for j in range(3):
            rotated_vertices.append(rotated_point[j])

    return rotated_vertices