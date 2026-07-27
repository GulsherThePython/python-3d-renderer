import pygame
from math import cos, radians, sin

def handle_camera_movement(camera):
    camera_position = camera["position"]
    yaw = radians(camera["rotation"][1])
    move_step = 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        camera_position[0] += sin(yaw) * move_step
        camera_position[2] -= cos(yaw) * move_step
    if keys[pygame.K_s]:
        camera_position[0] -= sin(yaw) * move_step
        camera_position[2] += cos(yaw) * move_step
    if keys[pygame.K_a]:
        camera_position[0] += cos(yaw) * move_step
        camera_position[2] += sin(yaw) * move_step
    if keys[pygame.K_d]:
        camera_position[0] -= cos(yaw) * move_step
        camera_position[2] -= sin(yaw) * move_step
    if keys[pygame.K_q]:
        camera_position[1] -= 1
    elif keys[pygame.K_e]:
        camera_position[1] += 1

def handle_camera_rotation(camera):
    camera_rotation = camera["rotation"]

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        camera_rotation[0] += 1
    if keys[pygame.K_DOWN]:
        camera_rotation[0] += -1
    if keys[pygame.K_LEFT]:
        camera_rotation[1] += 1
    if keys[pygame.K_RIGHT]:
        camera_rotation[1] += -1

